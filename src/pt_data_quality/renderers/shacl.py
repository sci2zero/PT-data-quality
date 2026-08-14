from __future__ import annotations

from collections import defaultdict
from typing import Any

from ..model import Repository
from ..profile import constraint_enabled, enabled_target, resolve_profile, rule_enabled, target_setting


SUPPORTED = {
    "PRESENCE",
    "MIN_LENGTH",
    "MAX_LENGTH",
    "MIN_VALUE",
    "MAX_VALUE",
    "MIN_CARDINALITY",
    "MAX_CARDINALITY",
    "REGEX",
    "VOCABULARY",
}


def _iri(value: str) -> str:
    value = value.strip()
    if value.startswith("<") or ":" in value and not value.startswith("http"):
        return value
    return f"<{value}>"


def _quote(value: Any) -> str:
    text = str(value).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{text}"'


def _param_map(repository: Repository) -> dict[str, dict[str, Any]]:
    result: defaultdict[str, dict[str, Any]] = defaultdict(dict)
    for row in repository.constraint_parameters:
        result[str(row.get("constraint_id"))][str(row.get("parameter_name"))] = row.get("parameter_value")
    return result


def _messages(repository: Repository) -> dict[str, dict[str, str]]:
    result: defaultdict[str, dict[str, str]] = defaultdict(dict)
    for row in repository.messages:
        result[str(row.get("constraint_id"))][str(row.get("language") or "en")] = str(row.get("message_text") or "")
    return result


def _bindings(repository: Repository, profile_id: str) -> dict[str, dict[str, Any]]:
    result = {}
    for row in repository.implementation_bindings:
        if row.get("representation") != "RDF_SHACL" or row.get("artifact_type") != "VALIDATION_TARGET":
            continue
        scope = str(row.get("profile_scope") or "*")
        if scope not in {"*", profile_id}:
            continue
        result[str(row.get("artifact_id"))] = dict(row.data)
    return result


def render_shacl(repository: Repository, profile_id: str) -> tuple[str, dict[str, Any]]:
    profile = resolve_profile(repository, profile_id)
    bindings = _bindings(repository, profile_id)
    params = _param_map(repository)
    messages = _messages(repository)
    vocab_terms: defaultdict[str, list[str]] = defaultdict(list)
    for row in repository.vocabulary_terms:
        if str(row.get("status")).upper() in {"RETIRED", "ARCHIVED", "DEPRECATED"}:
            continue
        vocab_terms[str(row.get("vocabulary_id"))].append(str(row.get("term_code")))

    lines = [
        "@prefix sh: <http://www.w3.org/ns/shacl#> .",
        "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .",
        "@prefix ptq: <urn:ptcris:data-quality:> .",
        "",
        f"# Generated from profile {profile_id}.",
        "# Only targets with RDF_SHACL bindings are emitted.",
        "",
    ]
    coverage = {"profileId": profile_id, "boundTargets": 0, "emittedConstraints": 0, "unsupportedConstraints": [], "unboundTargets": []}

    active_rules = {
        str(r.get("rule_id"))
        for r in repository.rules
        if enabled_target(profile, str(r.get("validation_target_id"))) and rule_enabled(profile, str(r.get("rule_id")))
    }
    constraints_by_target: defaultdict[str, list] = defaultdict(list)
    for row in repository.constraints:
        cid = str(row.get("constraint_id"))
        if str(row.get("rule_id")) in active_rules and constraint_enabled(profile, cid):
            constraints_by_target[str(row.get("validation_target_id"))].append(row)

    for tid, setting in sorted(profile.target_settings.items()):
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
        lines.append(f"ptq:{shape_name} a sh:NodeShape ;")
        lines.append(f"    sh:targetClass {_iri(entity)} ;")
        lines.append("    sh:property [")
        lines.append(f"        sh:path {_iri(path)} ;")
        emitted = 0
        for row in constraints_by_target.get(tid, []):
            c = dict(row.data)
            cid = str(c.get("constraint_id"))
            ctype = str(c.get("constraint_type"))
            p = params.get(cid, {})
            supported = True
            statement = None
            if ctype == "PRESENCE":
                statement = "sh:minCount 1"
            elif ctype == "MIN_LENGTH" and p.get("minLength") is not None:
                statement = f"sh:minLength {int(float(p['minLength']))}"
            elif ctype == "MAX_LENGTH" and p.get("maxLength") is not None:
                statement = f"sh:maxLength {int(float(p['maxLength']))}"
            elif ctype == "MIN_CARDINALITY" and p.get("minCardinality") is not None:
                statement = f"sh:minCount {int(float(p['minCardinality']))}"
            elif ctype == "MAX_CARDINALITY" and p.get("maxCardinality") is not None:
                statement = f"sh:maxCount {int(float(p['maxCardinality']))}"
            elif ctype == "REGEX" and p.get("pattern") is not None:
                statement = f"sh:pattern {_quote(p['pattern'])}"
            elif ctype in {"MIN_VALUE", "MIN_VALUE_OR_LENGTH"} and p.get("minValue") is not None:
                statement = f"sh:minInclusive {p['minValue']}"
            elif ctype in {"MAX_VALUE", "MAX_VALUE_OR_LENGTH"} and p.get("maxValue") is not None:
                statement = f"sh:maxInclusive {p['maxValue']}"
            elif ctype == "VOCABULARY" and c.get("vocabulary_id") and vocab_terms.get(str(c.get("vocabulary_id"))):
                values = " ".join(_quote(v) for v in vocab_terms[str(c.get("vocabulary_id"))])
                statement = f"sh:in ( {values} )"
            else:
                supported = False

            if not supported or statement is None:
                coverage["unsupportedConstraints"].append(cid)
                continue
            if emitted:
                lines[-1] += " ;"
            lines.append(f"        {statement}")
            msg = messages.get(cid, {}).get("en")
            if msg:
                lines[-1] += " ;"
                lines.append(f"        sh:message {_quote(msg)}@en")
            emitted += 1
            coverage["emittedConstraints"] += 1
        if emitted == 0:
            lines.append("        # No SHACL Core-compatible constraints are currently available for this target.")
        lines.append("    ] .")
        lines.append("")

    if coverage["boundTargets"] == 0:
        lines.extend([
            "# No RDF_SHACL target bindings are currently defined in the XLSX source.",
            "# Add rows to Implementation Bindings with representation=RDF_SHACL,",
            "# entity_selector=<RDF class> and value_selector=<RDF property/path>.",
            "",
        ])
    coverage["unsupportedConstraints"] = sorted(set(coverage["unsupportedConstraints"]))
    coverage["unboundTargets"] = sorted(set(coverage["unboundTargets"]))
    return "\n".join(lines), coverage
