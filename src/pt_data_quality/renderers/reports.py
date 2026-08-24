from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from ..model import Issue, Repository
from ..profile import constraint_enabled, enabled_target, resolve_profile
from ..projection import implementation_bindings
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
            location = issue.sheet + (f":{issue.row_number}" if issue.row_number else "")
        lines.append("| " + " | ".join(markdown_cell(x) for x in [issue.severity.upper(), issue.code, location, issue.artifact_id, issue.message]) + " |")
    return "\n".join(lines)


def coverage(repository: Repository, profile_id: str) -> dict[str, Any]:
    profile = resolve_profile(repository, profile_id)
    domains: defaultdict[str, dict[str, int]] = defaultdict(lambda: {"targets": 0, "constraints": 0, "reviewRequired": 0, "governanceMapped": 0})
    target_domains = {str(r.get("validation_target_id")): str(r.get("domain_id")) for r in repository.validation_targets}
    active_targets = {tid for tid in profile.target_settings if enabled_target(profile, tid)}
    for tid in active_targets:
        domains[target_domains.get(tid, "UNKNOWN")]["targets"] += 1

    active_constraints = [
        r for r in repository.constraints
        if str(r.get("validation_target_id")) in active_targets
        and constraint_enabled(profile, str(r.get("constraint_id")))
        and str(r.get("status") or "").upper() not in {"RETIRED", "ARCHIVED", "DEPRECATED"}
    ]
    mapping_status: defaultdict[str, list[str]] = defaultdict(list)
    for r in repository.governance_mappings:
        if str(r.get("profile_id") or "*") in {"*", profile_id}:
            mapping_status[str(r.get("constraint_id"))].append(str(r.get("mapping_status") or ""))
    mapped = 0
    for row in active_constraints:
        d = str(row.get("domain_id"))
        domains[d]["constraints"] += 1
        if row.get("review_required") is True:
            domains[d]["reviewRequired"] += 1
        statuses = mapping_status.get(str(row.get("constraint_id")), [])
        if any(s != "UNMAPPED" for s in statuses):
            mapped += 1
            domains[d]["governanceMapped"] += 1

    target_bindings = implementation_bindings(repository, profile_id, "VALIDATION_TARGET")
    bound_runtime_targets = [
        str(target_bindings[tid].get("runtime_target") or "")
        for tid in active_targets if tid in target_bindings and target_bindings[tid].get("runtime_target")
    ]
    return {
        "profileId": profile_id,
        "validationTargets": len(active_targets),
        "constraints": len(active_constraints),
        "governanceMappedConstraints": mapped,
        "governanceConstraintCoveragePercent": round(mapped / len(active_constraints) * 100, 2) if active_constraints else 100.0,
        "ptMasterBoundTargets": len(bound_runtime_targets),
        "ptMasterUniqueRuntimeTargets": len(set(bound_runtime_targets)),
        "ptMasterRuntimeTargetCollisions": len(bound_runtime_targets) - len(set(bound_runtime_targets)),
        "ptMasterBindingCoveragePercent": round(len(bound_runtime_targets) / len(active_targets) * 100, 2) if active_targets else 100.0,
        "domains": dict(sorted(domains.items())),
    }


def governance_traceability(repository: Repository, profile_id: str) -> str:
    profile = resolve_profile(repository, profile_id)
    active_targets = {tid for tid in profile.target_settings if enabled_target(profile, tid)}
    mappings: defaultdict[str, list[Any]] = defaultdict(list)
    for row in repository.governance_mappings:
        if str(row.get("profile_id") or "*") in {"*", profile_id}:
            mappings[str(row.get("constraint_id"))].append(row)
    lines = [
        f"# Governance traceability — {profile_id}", "",
        "| Domain | Constraint | Validation target | Dimension | Metric | Requirement | Status |",
        "|---|---|---|---|---|---|---|",
    ]
    for c in sorted(repository.constraints, key=lambda r: (str(r.get("domain_id")), str(r.get("constraint_id")))):
        tid = str(c.get("validation_target_id")); cid = str(c.get("constraint_id"))
        if tid not in active_targets or not constraint_enabled(profile, cid):
            continue
        for m in mappings.get(cid, []):
            lines.append("| " + " | ".join(markdown_cell(x) for x in [c.get("domain_id"), cid, tid, m.get("dimension_id"), m.get("metric_id"), m.get("requirement_id"), m.get("mapping_status")]) + " |")
    return "\n".join(lines)


def runtime_compatibility_markdown(legacy: dict[str, Any], current: dict[str, Any], profile_id: str) -> str:
    """Compare the new PT Master projection with the deployed legacy fixture.

    Messages/translations are intentionally excluded from equality because the
    RSR v2 migration deliberately consolidates and generalizes them.
    """
    old = legacy.get("dataQualityRemarks", {})
    new = current.get("dataQualityRemarks", {})
    old_keys, new_keys = set(old), set(new)
    common = sorted(old_keys & new_keys)
    statuses: list[tuple[str, str, str]] = []
    compare_fields = ["target", "severity", "dimension", "blocking", "points", "usedForFairCompliance", "constraints"]
    for key in common:
        changed = [f for f in compare_fields if old[key].get(f) != new[key].get(f)]
        statuses.append((key, "PRESERVED" if not changed else "CHANGED", ", ".join(changed)))
    statuses.extend((k, "REMOVED", "") for k in sorted(old_keys - new_keys))
    statuses.extend((k, "ADDED", "") for k in sorted(new_keys - old_keys))
    counts = Counter(s for _, s, _ in statuses)

    lines = [
        f"# PT Master runtime compatibility — {profile_id}", "",
        "This report compares the generated runtime projection with the deployed legacy JSON fixture.",
        "Message/title text is intentionally excluded because RSR v2 consolidates and localizes messages differently.", "",
        f"- Legacy remarks: **{len(old)}**",
        f"- Generated remarks: **{len(new)}**",
        f"- Preserved keys with unchanged runtime semantics: **{counts.get('PRESERVED', 0)}**",
        f"- Preserved keys with changed runtime semantics: **{counts.get('CHANGED', 0)}**",
        f"- Removed legacy keys: **{counts.get('REMOVED', 0)}**",
        f"- Added keys: **{counts.get('ADDED', 0)}**", "",
        "| Runtime key | Status | Changed fields |", "|---|---|---|",
    ]
    for key, status, changed in statuses:
        lines.append("| " + " | ".join(markdown_cell(x) for x in [key, status, changed]) + " |")
    return "\n".join(lines)
