from __future__ import annotations

from collections import defaultdict
from typing import Any

from ..model import Repository
from ..profile import constraint_enabled, constraint_weight, enabled_target, resolve_profile, rule_enabled, target_setting
from ..util import markdown_cell, slug


def _gov_by_artifact(repository: Repository, profile_id: str) -> dict[str, list[str]]:
    result: defaultdict[str, list[str]] = defaultdict(list)
    for row in repository.governance_mappings:
        scope = str(row.get("profile_id") or "*")
        if scope in {"*", profile_id}:
            result[str(row.get("artifact_id"))].append(str(row.get("requirement_id")))
    return result


def index_markdown(repository: Repository, profile_ids: list[str]) -> str:
    lines = [
        "# PT Data Quality Repository",
        "",
        "This site is generated from the authoritative XLSX Rule Specification Repository.",
        "",
        "## Available Data Quality Profiles",
        "",
        "| Profile | Version | Status | Description |",
        "|---|---:|---|---|",
    ]
    profiles = repository.profiles_by_id
    for pid in profile_ids:
        row = profiles[pid]
        lines.append(
            "| " + " | ".join(
                [f"[{markdown_cell(pid)}](profiles/{slug(pid)}/index.md)", markdown_cell(row.get("version")), markdown_cell(row.get("status")), markdown_cell(row.get("description"))]
            ) + " |"
        )
    lines.extend([
        "",
        "## Repository principle",
        "",
        "The XLSX source is maintained by governance/domain experts. JSON, implementation configuration, documentation, validation reports, SHACL and Schematron artefacts are derived outputs and must not be edited manually.",
    ])
    return "\n".join(lines)


def profile_index(repository: Repository, profile_id: str, coverage: dict[str, Any]) -> str:
    effective = resolve_profile(repository, profile_id)
    p = effective.profile
    lines = [
        f"# {p.get('name') or profile_id}",
        "",
        f"**Profile ID:** `{profile_id}`  ",
        f"**Version:** `{p.get('version')}`  ",
        f"**Status:** `{p.get('status')}`  ",
        f"**Base profile:** `{p.get('base_profile_id') or '—'}`  ",
        f"**Minimum required score:** `{p.get('minimum_required_score')}`",
        "",
        str(p.get("description") or ""),
        "",
        "## Effective configuration",
        "",
        f"- Validation targets: **{coverage['validationTargets']}**",
        f"- Rules: **{coverage['rules']}**",
        f"- Constraints: **{coverage['constraints']}**",
        f"- Governance-mapped rules: **{coverage['governanceMappedRules']}** ({coverage['governanceRuleCoveragePercent']}%)",
        f"- PT Master runtime target binding coverage: **{coverage['ptMasterBoundTargets']}** ({coverage['ptMasterBindingCoveragePercent']}%)",
        "",
        "## Domains",
        "",
    ]
    for domain, counts in coverage["domains"].items():
        lines.append(f"- [{domain}](domains/{slug(domain)}.md) — {counts['targets']} targets, {counts['constraints']} constraints")
    lines.extend([
        "",
        "## Profile documentation",
        "",
        "- [Scoring policy](scoring.md)",
        "- [Governance alignment](governance.md)",
        "- [Implementation outputs](implementation.md)",
        "- [Review-required items](review-required.md)",
    ])
    return "\n".join(lines)


def scoring_markdown(repository: Repository, profile_id: str) -> str:
    effective = resolve_profile(repository, profile_id)
    lines = [
        f"# Scoring policy — {profile_id}",
        "",
        f"Minimum required score: **{effective.profile.get('minimum_required_score')}**",
        "",
        "## Constraint-type defaults",
        "",
        "| Weight key | Weight | Included in score | Description |",
        "|---|---:|---|---|",
    ]
    for key, row in effective.constraint_defaults.items():
        lines.append("| " + " | ".join(markdown_cell(x) for x in [key, row.get("weight"), row.get("include_in_score"), row.get("description")]) + " |")
    lines.extend([
        "",
        "## Target importance",
        "",
        "| Domain | Validation target | Importance | Requirement level | Blocking on presence failure |",
        "|---|---|---:|---|---|",
    ])
    targets = repository.targets_by_id
    for tid, setting in sorted(effective.target_settings.items(), key=lambda x: (str(x[1].get("domain_id")), x[0])):
        if not enabled_target(effective, tid):
            continue
        lines.append("| " + " | ".join(markdown_cell(x) for x in [setting.get("domain_id"), tid, setting.get("importance"), setting.get("requirement_level"), setting.get("blocking_on_failure")]) + " |")
    return "\n".join(lines)


def governance_markdown(repository: Repository, profile_id: str) -> str:
    gov = _gov_by_artifact(repository, profile_id)
    lines = [
        f"# Governance alignment — {profile_id}",
        "",
        "## PTCRIS Data Governance dimensions",
        "",
        "| Dimension | Metric | Description |",
        "|---|---|---|",
    ]
    for row in repository.governance_dimensions:
        lines.append("| " + " | ".join(markdown_cell(x) for x in [row.get("name"), row.get("metric_id"), row.get("description")]) + " |")
    lines.extend([
        "",
        "## Governance requirements and implemented rules",
        "",
        "| Requirement | Metric | Dimension | Implementing artefacts | Review required |",
        "|---|---|---|---|---|",
    ])
    reverse: defaultdict[str, list[str]] = defaultdict(list)
    for artifact, reqs in gov.items():
        for req in reqs:
            reverse[req].append(artifact)
    for row in repository.governance_requirements:
        rid = str(row.get("requirement_id"))
        lines.append("| " + " | ".join(markdown_cell(x) for x in [rid, row.get("metric_id"), row.get("dimension_id"), ", ".join(sorted(reverse.get(rid, []))), row.get("review_required")]) + " |")
    return "\n".join(lines)


def domain_markdown(repository: Repository, profile_id: str, domain_id: str) -> str:
    effective = resolve_profile(repository, profile_id)
    targets = repository.targets_by_id
    gov = _gov_by_artifact(repository, profile_id)
    active_rule_ids = {
        str(r.get("rule_id"))
        for r in repository.rules
        if enabled_target(effective, str(r.get("validation_target_id"))) and rule_enabled(effective, str(r.get("rule_id")))
    }
    constraints_by_target: defaultdict[str, list] = defaultdict(list)
    for row in repository.constraints:
        if str(row.get("rule_id")) in active_rule_ids and constraint_enabled(effective, str(row.get("constraint_id"))):
            constraints_by_target[str(row.get("validation_target_id"))].append(row)
    params: defaultdict[str, list[str]] = defaultdict(list)
    for row in repository.constraint_parameters:
        params[str(row.get("constraint_id"))].append(f"{row.get('parameter_name')}={row.get('parameter_value')}")
    messages = {str(r.get("constraint_id")): str(r.get("message_text") or "") for r in repository.messages if str(r.get("language") or "en") == "en"}

    lines = [
        f"# {domain_id} — {profile_id}",
        "",
        "| Validation target | Importance | Requirement | Constraint | Type | Dimension | Weight | Blocking | Parameters | Governance | Message | Review |",
        "|---|---:|---|---|---|---|---:|---|---|---|---|---|",
    ]
    for tid, setting in sorted(effective.target_settings.items()):
        if str(setting.get("domain_id")) != domain_id or not enabled_target(effective, tid):
            continue
        for c in constraints_by_target.get(tid, []):
            cid = str(c.get("constraint_id"))
            weight, included = constraint_weight(effective, c.data)
            blocking = setting.get("blocking_on_failure") if c.get("constraint_type") == "PRESENCE" else True
            reqs = sorted(set(gov.get(str(c.get("rule_id")), []) + gov.get(cid, []) + gov.get(tid, [])))
            lines.append(
                "| " + " | ".join(markdown_cell(x) for x in [
                    tid,
                    setting.get("importance"),
                    setting.get("requirement_level"),
                    cid,
                    c.get("constraint_type"),
                    c.get("assessment_dimension"),
                    weight if included else "—",
                    blocking,
                    ", ".join(params.get(cid, [])),
                    ", ".join(reqs),
                    messages.get(cid, ""),
                    c.get("review_required"),
                ]) + " |"
            )
    return "\n".join(lines)


def implementation_markdown(profile_id: str, shacl_coverage: dict[str, Any], schematron_coverage: dict[str, Any]) -> str:
    return "\n".join([
        f"# Implementation outputs — {profile_id}",
        "",
        "## PT Master runtime JSON",
        "",
        f"The generator creates `generated/implementation/pt-master/{profile_id}/{profile_id.split('-')[-1]}.json` in the legacy-compatible format and `runtime-config.json` with explicit traceability metadata.",
        "",
        "## SHACL",
        "",
        f"- Bound validation targets: **{shacl_coverage.get('boundTargets', 0)}**",
        f"- Emitted SHACL Core constraints: **{shacl_coverage.get('emittedConstraints', 0)}**",
        f"- Unbound active targets: **{len(shacl_coverage.get('unboundTargets', []))}**",
        "",
        "SHACL is emitted only when the XLSX contains `RDF_SHACL` bindings in the `Implementation Bindings` sheet. This avoids inventing RDF classes or properties.",
        "",
        "## Schematron",
        "",
        f"- Bound validation targets: **{schematron_coverage.get('boundTargets', 0)}**",
        f"- Emitted Schematron assertions: **{schematron_coverage.get('emittedConstraints', 0)}**",
        f"- Unbound active targets: **{len(schematron_coverage.get('unboundTargets', []))}**",
        "",
        "Schematron is emitted only when the XLSX contains `XML_SCHEMATRON` bindings with an XML context and value selector.",
    ])


def review_required_markdown(repository: Repository, profile_id: str) -> str:
    effective = resolve_profile(repository, profile_id)
    lines = [
        f"# Review-required items — {profile_id}",
        "",
        "| Type | Domain | ID | Reason / notes |",
        "|---|---|---|---|",
    ]
    for row in repository.validation_targets:
        if row.get("review_required") is True and enabled_target(effective, str(row.get("validation_target_id"))):
            lines.append("| " + " | ".join(markdown_cell(x) for x in ["Validation target", row.get("domain_id"), row.get("validation_target_id"), row.get("notes")]) + " |")
    for row in repository.constraints:
        if row.get("review_required") is True and enabled_target(effective, str(row.get("validation_target_id"))):
            lines.append("| " + " | ".join(markdown_cell(x) for x in ["Constraint", row.get("domain_id"), row.get("constraint_id"), row.get("migration_notes") or row.get("description")]) + " |")
    for row in repository.governance_requirements:
        if row.get("review_required") is True:
            lines.append("| " + " | ".join(markdown_cell(x) for x in ["Governance requirement", "—", row.get("requirement_id"), row.get("notes")]) + " |")
    for row in repository.implementation_bindings:
        scope = str(row.get("profile_scope") or "*")
        if scope in {"*", profile_id} and row.get("review_required") is True:
            lines.append("| " + " | ".join(markdown_cell(x) for x in ["Implementation binding", row.get("domain_id"), row.get("binding_id"), row.get("notes")]) + " |")
    return "\n".join(lines)
