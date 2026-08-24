from __future__ import annotations

from collections import defaultdict
from typing import Any

from ..model import Repository
from ..profile import constraint_enabled, enabled_target, resolve_profile
from ..projection import english_messages, runtime_parameter_map


def _iri(value: str) -> str:
    value = str(value).strip()
    if value.startswith("<") or ":" in value:
        return value
    return f"<{value}>"


def _quote(value: Any) -> str:
    text = str(value).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{text}"'


def _bindings(repository: Repository, profile_id: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in repository.implementation_bindings:
        if row.get("representation") != "RDF_SHACL" or str(row.get("artifact_type") or "").upper() != "VALIDATION_TARGET":
            continue
        scope = str(row.get("profile_scope") or "*")
        if scope not in {"*", profile_id}:
            continue
        result[str(row.get("artifact_id"))] = dict(row.data)
    return result


def render_shacl(repository: Repository, profile_id: str) -> tuple[str, dict[str, Any]]:
    profile = resolve_profile(repository, profile_id)
    params = runtime_parameter_map(repository)
    messages = english_messages(repository)
    bindings = _bindings(repository, profile_id)
    vocab_terms: defaultdict[str, list[str]] = defaultdict(list)
    for row in repository.vocabulary_terms:
        vocab_terms[str(row.get("vocabulary_id"))].append(str(row.get("term_code")))

    coverage = {"profileId": profile_id, "boundTargets": 0, "emittedConstraints": 0, "unsupportedConstraints": [], "unboundTargets": []}
    lines = [
        "@prefix sh: <http://www.w3.org/ns/shacl#> .",
        "@prefix ptq: <https://example.org/ptcris/data-quality/> .",
        "",
    ]

    constraints_by_target: defaultdict[str, list[Any]] = defaultdict(list)
    for row in repository.constraints:
        cid = str(row.get("constraint_id")); tid = str(row.get("validation_target_id"))
        if enabled_target(profile, tid) and constraint_enabled(profile, cid):
            constraints_by_target[tid].append(row)

    for tid in sorted(profile.target_settings):
        if not enabled_target(profile, tid):
            continue
        binding = bindings.get(tid)
        if not binding:
            coverage["unboundTargets"].append(tid)
            continue
        entity = str(binding.get("entity_selector") or "").strip()
        path = str(binding.get("value_selector") or "").strip()
        if not entity or not path:
            coverage["unboundTargets"].append(tid)
            continue
        coverage["boundTargets"] += 1
        shape_name = tid.replace(".", "_").replace("-", "_")
        lines.extend([f"ptq:{shape_name} a sh:NodeShape ;", f"    sh:targetClass {_iri(entity)} ;", "    sh:property [", f"        sh:path {_iri(path)} ;"])
        emitted = 0
        for row in constraints_by_target.get(tid, []):
            c = dict(row.data); cid = str(c.get("constraint_id")); ctype = str(c.get("constraint_type")); p = params.get(cid, {})
            statement = None
            if ctype == "PRESENCE": statement = "sh:minCount 1"
            elif ctype == "MIN_LENGTH" and p.get("minLength") is not None: statement = f"sh:minLength {int(float(p['minLength']))}"
            elif ctype == "MAX_LENGTH" and p.get("maxLength") is not None: statement = f"sh:maxLength {int(float(p['maxLength']))}"
            elif ctype == "MIN_CARDINALITY" and p.get("minCardinality") is not None: statement = f"sh:minCount {int(float(p['minCardinality']))}"
            elif ctype == "MAX_CARDINALITY" and p.get("maxCardinality") is not None: statement = f"sh:maxCount {int(float(p['maxCardinality']))}"
            elif ctype == "REGEX" and p.get("pattern") is not None: statement = f"sh:pattern {_quote(p['pattern'])}"
            elif ctype == "MIN_VALUE" and isinstance(p.get("minValue"), (int, float)): statement = f"sh:minInclusive {p['minValue']}"
            elif ctype == "MAX_VALUE" and isinstance(p.get("maxValue"), (int, float)): statement = f"sh:maxInclusive {p['maxValue']}"
            elif ctype == "VOCABULARY" and c.get("vocabulary_id") and vocab_terms.get(str(c.get("vocabulary_id"))):
                statement = "sh:in ( " + " ".join(_quote(v) for v in vocab_terms[str(c.get("vocabulary_id"))]) + " )"
            if not statement:
                coverage["unsupportedConstraints"].append(cid)
                continue
            if emitted:
                lines[-1] += " ;"
            lines.append(f"        {statement}")
            if messages.get(cid):
                lines[-1] += " ;"
                lines.append(f"        sh:message {_quote(messages[cid])}@en")
            emitted += 1; coverage["emittedConstraints"] += 1
        if emitted == 0:
            lines.append("        # No SHACL Core-compatible constraints are currently available for this target.")
        lines.extend(["    ] .", ""])

    if coverage["boundTargets"] == 0:
        lines.extend(["# No RDF_SHACL target bindings are currently defined in the XLSX source.", ""])
    coverage["unsupportedConstraints"] = sorted(set(coverage["unsupportedConstraints"]))
    coverage["unboundTargets"] = sorted(set(coverage["unboundTargets"]))
    return "\n".join(lines), coverage
