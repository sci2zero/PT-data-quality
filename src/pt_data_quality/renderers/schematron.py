from __future__ import annotations

import html
from collections import defaultdict
from typing import Any

from ..model import Repository
from ..profile import constraint_enabled, enabled_target, resolve_profile
from ..projection import english_messages, runtime_parameter_map


def _bindings(repository: Repository, profile_id: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in repository.implementation_bindings:
        if row.get("representation") != "XML_SCHEMATRON" or str(row.get("artifact_type") or "").upper() != "VALIDATION_TARGET":
            continue
        scope = str(row.get("profile_scope") or "*")
        if scope not in {"*", profile_id}:
            continue
        result[str(row.get("artifact_id"))] = dict(row.data)
    return result


def _xpath_literal(value: Any) -> str:
    text = str(value)
    if "'" not in text: return f"'{text}'"
    if '"' not in text: return f'"{text}"'
    parts = text.split("'")
    return "concat(" + ", \"'\", ".join(f"'{p}'" for p in parts) + ")"


def render_schematron(repository: Repository, profile_id: str) -> tuple[str, dict[str, Any]]:
    profile = resolve_profile(repository, profile_id)
    params = runtime_parameter_map(repository)
    messages = english_messages(repository)
    bindings = _bindings(repository, profile_id)
    terms: defaultdict[str, list[str]] = defaultdict(list)
    for row in repository.vocabulary_terms:
        terms[str(row.get("vocabulary_id"))].append(str(row.get("term_code")))

    coverage = {"profileId": profile_id, "boundTargets": 0, "emittedConstraints": 0, "unsupportedConstraints": [], "unboundTargets": []}
    constraints_by_target: defaultdict[str, list[Any]] = defaultdict(list)
    for row in repository.constraints:
        cid = str(row.get("constraint_id")); tid = str(row.get("validation_target_id"))
        if enabled_target(profile, tid) and constraint_enabled(profile, cid):
            constraints_by_target[tid].append(row)

    rules_xml: list[str] = []
    for tid in sorted(profile.target_settings):
        if not enabled_target(profile, tid): continue
        binding = bindings.get(tid)
        if not binding:
            coverage["unboundTargets"].append(tid); continue
        context = str(binding.get("entity_selector") or "").strip(); value = str(binding.get("value_selector") or "").strip()
        if not context or not value:
            coverage["unboundTargets"].append(tid); continue
        coverage["boundTargets"] += 1
        asserts = []
        for row in constraints_by_target.get(tid, []):
            c = dict(row.data); cid = str(c.get("constraint_id")); p = params.get(cid, {}); ctype = str(c.get("constraint_type")); test = None
            if ctype == "PRESENCE": test = f"exists({value})"
            elif ctype == "MIN_LENGTH" and p.get("minLength") is not None: test = f"string-length(normalize-space(string({value}))) &gt;= {int(float(p['minLength']))}"
            elif ctype == "MAX_LENGTH" and p.get("maxLength") is not None: test = f"string-length(string({value})) &lt;= {int(float(p['maxLength']))}"
            elif ctype == "REGEX" and p.get("pattern") is not None: test = f"matches(string({value}), {_xpath_literal(p['pattern'])})"
            elif ctype == "MIN_CARDINALITY" and p.get("minCardinality") is not None: test = f"count({value}) &gt;= {int(float(p['minCardinality']))}"
            elif ctype == "MAX_CARDINALITY" and p.get("maxCardinality") is not None: test = f"count({value}) &lt;= {int(float(p['maxCardinality']))}"
            elif ctype == "MIN_VALUE" and isinstance(p.get("minValue"), (int,float)): test = f"number({value}) &gt;= {p['minValue']}"
            elif ctype == "MAX_VALUE" and isinstance(p.get("maxValue"), (int,float)): test = f"number({value}) &lt;= {p['maxValue']}"
            elif ctype == "VOCABULARY" and c.get("vocabulary_id") and terms.get(str(c.get("vocabulary_id"))):
                test = f"string({value}) = ({', '.join(_xpath_literal(x) for x in terms[str(c.get('vocabulary_id'))])})"
            if not test:
                coverage["unsupportedConstraints"].append(cid); continue
            asserts.append(f'      <sch:assert id="{html.escape(cid)}" test="{test}">{html.escape(messages.get(cid, cid))}</sch:assert>')
            coverage["emittedConstraints"] += 1
        if asserts:
            rules_xml.append(f'    <sch:rule context="{html.escape(context)}">'); rules_xml.extend(asserts); rules_xml.append("    </sch:rule>")

    body = "\n".join(rules_xml) or "    <!-- No XML_SCHEMATRON bindings are currently defined, or no bound constraints are auto-convertible. -->"
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
  <sch:title>PTCRIS Data Quality - {html.escape(profile_id)}</sch:title>
  <sch:pattern id="ptcris-data-quality">
{body}
  </sch:pattern>
</sch:schema>
'''
    coverage["unsupportedConstraints"] = sorted(set(coverage["unsupportedConstraints"]))
    coverage["unboundTargets"] = sorted(set(coverage["unboundTargets"]))
    return xml, coverage
