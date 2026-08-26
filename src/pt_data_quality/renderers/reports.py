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
    """Check that the refreshed 1.0.0 remains consumable by the current Java code.

    The new 1.0.0 is intentionally *not* content-identical to the Java-branch
    baseline: messages, Portuguese localisation, DQP scoring/behaviour and
    compatible parameter values may change. Compatibility means the current
    Java DTO/runtime keys/targets and hard-coded constraint parameter names and
    JSON types still work unchanged.
    """
    old = legacy.get("dataQualityRemarks", {})
    new = current.get("dataQualityRemarks", {})
    old_keys, new_keys = set(old), set(new)
    allowed_top = {"minimumRequiredScore", "dimensionDefinitions", "targetWeights", "dataQualityRemarks"}
    allowed_rule = {"title", "message", "target", "severity", "dimension", "blocking", "points", "usedForFairCompliance", "constraints"}

    missing_keys = sorted(old_keys - new_keys)
    added_keys = sorted(new_keys - old_keys)
    target_changes = []
    contract_parameter_issues = []
    unexpected_rule_fields = []
    message_changes = 0
    scoring_changes = 0

    for key in sorted(old_keys & new_keys):
        old_rule, new_rule = old[key], new[key]
        if old_rule.get("target") != new_rule.get("target"):
            target_changes.append(key)
        extras = sorted(set(new_rule) - allowed_rule)
        if extras:
            unexpected_rule_fields.append((key, extras))
        old_constraints = old_rule.get("constraints") or {}
        new_constraints = new_rule.get("constraints") or {}
        for pname, old_value in old_constraints.items():
            if pname not in new_constraints:
                contract_parameter_issues.append((key, pname, "missing"))
                continue
            new_value = new_constraints[pname]
            # Current Java reads numeric constraints through Number.intValue()/doubleValue(),
            # so integer <-> decimal JSON-number changes remain contract compatible.
            old_is_number = isinstance(old_value, (int, float)) and not isinstance(old_value, bool)
            new_is_number = isinstance(new_value, (int, float)) and not isinstance(new_value, bool)
            if not (old_is_number and new_is_number) and type(new_value) is not type(old_value):
                contract_parameter_issues.append((key, pname, f"type {type(old_value).__name__} -> {type(new_value).__name__}"))
        if old_rule.get("title") != new_rule.get("title") or old_rule.get("message") != new_rule.get("message"):
            message_changes += 1
        if any(old_rule.get(f) != new_rule.get(f) for f in ("severity", "dimension", "blocking", "points", "usedForFairCompliance")):
            scoring_changes += 1

    contract_compatible = (
        set(current) == allowed_top
        and not missing_keys
        and not added_keys
        and not target_changes
        and not contract_parameter_issues
        and not unexpected_rule_fields
    )
    pt_messages = sum(1 for rule in new.values() if "pt" in (rule.get("message") or {}))
    pt_titles = sum(1 for rule in new.values() if "pt" in (rule.get("title") or {}))

    lines = [
        f"# PT Master current-Java compatibility — {profile_id}", "",
        "This report compares the refreshed RSR-driven `1.0.0.json` with the current Java-branch runtime contract.",
        "Content differences are expected; the check below is about **runtime/API compatibility**, not byte-for-byte equality.", "",
        f"- Current Java runtime contract compatible: **{'YES' if contract_compatible else 'NO'}**",
        f"- Baseline runtime keys: **{len(old)}**",
        f"- Generated runtime keys: **{len(new)}**",
        f"- Missing baseline keys: **{len(missing_keys)}**",
        f"- Added unsupported 1.x keys: **{len(added_keys)}**",
        f"- Runtime target changes: **{len(target_changes)}**",
        f"- Java parameter contract issues: **{len(contract_parameter_issues)}**",
        f"- Rules with refreshed title/message content: **{message_changes}**",
        f"- Rules with refreshed severity/dimension/blocking/points/FAIR behaviour: **{scoring_changes}**",
        f"- Portuguese titles: **{pt_titles}/{len(new)}**",
        f"- Portuguese messages: **{pt_messages}/{len(new)}**",
        f"- targetWeights: **{len(legacy.get('targetWeights', {}))} -> {len(current.get('targetWeights', {}))}**", "",
    ]
    if missing_keys:
        lines += ["## Missing runtime keys", "", *[f"- `{k}`" for k in missing_keys], ""]
    if added_keys:
        lines += ["## Added 1.x runtime keys", "", *[f"- `{k}`" for k in added_keys], ""]
    if target_changes:
        lines += ["## Runtime target changes", "", *[f"- `{k}`: `{old[k].get('target')}` -> `{new[k].get('target')}`" for k in target_changes], ""]
    if contract_parameter_issues:
        lines += ["## Java parameter contract issues", "", "| Runtime key | Parameter | Issue |", "|---|---|---|"]
        for key, pname, issue in contract_parameter_issues:
            lines.append("| " + " | ".join(markdown_cell(x) for x in [key, pname, issue]) + " |")
    return "\n".join(lines)


def next_runtime_support_markdown(next_runtime: dict[str, Any], profile_id: str) -> str:
    """Summarize the future 2.0.0 configuration and Java migration backlog."""
    remarks = next_runtime.get("dataQualityRemarks", {})
    counts = Counter((item.get("javaSupport") or {}).get("status", "UNKNOWN") for item in remarks.values())
    lines = [
        f"# PT Master 2.0.0-preview support — {profile_id}", "",
        "`2.0.0-preview.json` is the future configuration contract. It keeps the familiar PT Master rule fields but adds all active RSR Constraints, typed canonical parameter definitions, resolver/vocabulary registries, governance traceability and explicit Java migration notes.",
        "The current Java code continues to consume `1.0.0.json`. As generic evaluators are implemented, rules can move from `NOT_SUPPORTED`/`LEGACY_*` to native 2.0.0 execution without redesigning the RSR.", "",
        f"- Runtime model version: **{next_runtime.get('runtimeModelVersion')}**",
        f"- Runtime remarks: **{len(remarks)}**",
        f"- Resolver definitions: **{len(next_runtime.get('resolverDefinitions', {}))}**",
        f"- Vocabulary definitions: **{len(next_runtime.get('vocabularyDefinitions', {}))}**",
        f"- LEGACY_SUPPORTED: **{counts.get('LEGACY_SUPPORTED', 0)}**",
        f"- LEGACY_CONFIG_ONLY: **{counts.get('LEGACY_CONFIG_ONLY', 0)}**",
        f"- NOT_SUPPORTED: **{counts.get('NOT_SUPPORTED', 0)}**", "",
        "## Rules not yet natively supported by current Java", "",
        "| Runtime key | Target | Constraint | Type | Status | Comment |",
        "|---|---|---|---|---|---|",
    ]
    for key, item in remarks.items():
        support = item.get("javaSupport") or {}
        if support.get("status") == "LEGACY_SUPPORTED":
            continue
        lines.append("| " + " | ".join(markdown_cell(x) for x in [
            key, item.get("target"), item.get("constraintId"), item.get("constraintType"),
            support.get("status"), support.get("comment"),
        ]) + " |")
    return "\n".join(lines)
