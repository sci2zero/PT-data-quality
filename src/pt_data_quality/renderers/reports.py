from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from ..model import Issue, Repository
from ..profile import constraint_enabled, constraint_weight, enabled_target, resolve_profile, rule_enabled, target_setting
from ..util import markdown_cell


def validation_markdown(issues: list[Issue]) -> str:
    counts = Counter(i.severity for i in issues)
    lines = [
        "# Validation report",
        "",
        f"- Errors: **{counts.get('error', 0)}**",
        f"- Warnings: **{counts.get('warning', 0)}**",
        f"- Info: **{counts.get('info', 0)}**",
        "",
    ]
    if not issues:
        lines.append("No validation issues were found.")
        return "\n".join(lines)
    lines.extend(["| Severity | Code | Location | Artifact | Message |", "|---|---|---|---|---|"])
    for issue in issues:
        location = ""
        if issue.sheet:
            location = issue.sheet
            if issue.row_number:
                location += f":{issue.row_number}"
        lines.append(
            "| " + " | ".join(
                markdown_cell(x)
                for x in [issue.severity.upper(), issue.code, location, issue.artifact_id, issue.message]
            ) + " |"
        )
    return "\n".join(lines)


def coverage(repository: Repository, profile_id: str) -> dict[str, Any]:
    profile = resolve_profile(repository, profile_id)
    domains: defaultdict[str, dict[str, int]] = defaultdict(lambda: {"targets": 0, "constraints": 0, "reviewRequired": 0})
    target_domains = {str(r.get("validation_target_id")): str(r.get("domain_id")) for r in repository.validation_targets}
    active_targets = {tid for tid in profile.target_settings if enabled_target(profile, tid)}
    for tid in active_targets:
        domains[target_domains.get(tid, "UNKNOWN")]["targets"] += 1
    active_rules = {
        str(r.get("rule_id"))
        for r in repository.rules
        if str(r.get("validation_target_id")) in active_targets and rule_enabled(profile, str(r.get("rule_id")))
    }
    active_constraints = [
        r for r in repository.constraints
        if str(r.get("rule_id")) in active_rules and constraint_enabled(profile, str(r.get("constraint_id")))
    ]
    for row in active_constraints:
        d = str(row.get("domain_id"))
        domains[d]["constraints"] += 1
        if row.get("review_required") is True:
            domains[d]["reviewRequired"] += 1

    gov_mapped_rules = {str(r.get("artifact_id")) for r in repository.governance_mappings if str(r.get("artifact_type")).upper() == "RULE" and str(r.get("profile_id") or "*") in {"*", profile_id}}
    active_rule_rows = [r for r in repository.rules if str(r.get("rule_id")) in active_rules]
    mapped_active_rules = sum(1 for r in active_rule_rows if str(r.get("rule_id")) in gov_mapped_rules)

    pt_bindings = {
        str(r.get("artifact_id")): str(r.get("runtime_target") or "")
        for r in repository.implementation_bindings
        if r.get("implementation_id") == "PT_MASTER" and r.get("representation") == "RUNTIME_JSON" and r.get("artifact_type") == "VALIDATION_TARGET"
    }
    bound_runtime_targets = [pt_bindings[tid] for tid in active_targets if tid in pt_bindings and pt_bindings[tid]]
    runtime_target_collisions = len(bound_runtime_targets) - len(set(bound_runtime_targets))
    return {
        "profileId": profile_id,
        "validationTargets": len(active_targets),
        "rules": len(active_rules),
        "constraints": len(active_constraints),
        "governanceMappedRules": mapped_active_rules,
        "governanceRuleCoveragePercent": round((mapped_active_rules / len(active_rules) * 100), 2) if active_rules else 100.0,
        "ptMasterBoundTargets": sum(1 for tid in active_targets if tid in pt_bindings and pt_bindings[tid]),
        "ptMasterUniqueRuntimeTargets": len(set(bound_runtime_targets)),
        "ptMasterRuntimeTargetCollisions": runtime_target_collisions,
        "ptMasterBindingCoveragePercent": round((sum(1 for tid in active_targets if tid in pt_bindings and pt_bindings[tid]) / len(active_targets) * 100), 2) if active_targets else 100.0,
        "domains": dict(sorted(domains.items())),
    }


def governance_traceability(repository: Repository, profile_id: str) -> str:
    profile = resolve_profile(repository, profile_id)
    active_targets = {tid for tid in profile.target_settings if enabled_target(profile, tid)}
    active_rules = {str(r.get("rule_id")) for r in repository.rules if str(r.get("validation_target_id")) in active_targets}
    mappings_by_artifact: defaultdict[str, list[str]] = defaultdict(list)
    for row in repository.governance_mappings:
        scope = str(row.get("profile_id") or "*")
        if scope in {"*", profile_id}:
            mappings_by_artifact[str(row.get("artifact_id"))].append(str(row.get("requirement_id")))
    lines = [
        f"# Governance traceability — {profile_id}",
        "",
        "| Domain | Rule | Validation target | Governance requirements |",
        "|---|---|---|---|",
    ]
    for rule in sorted((r for r in repository.rules if str(r.get("rule_id")) in active_rules), key=lambda r: (str(r.get("domain_id")), str(r.get("rule_id")))):
        rid = str(rule.get("rule_id"))
        reqs = sorted(set(mappings_by_artifact.get(rid, [])))
        lines.append("| " + " | ".join(markdown_cell(x) for x in [rule.get("domain_id"), rid, rule.get("validation_target_id"), ", ".join(reqs)]) + " |")
    return "\n".join(lines)
