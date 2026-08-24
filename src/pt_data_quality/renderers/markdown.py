from __future__ import annotations

from collections import defaultdict
from typing import Any

from ..model import Repository
from ..profile import (
    constraint_enabled,
    constraint_severity_and_blocking,
    constraint_weight,
    enabled_target,
    resolve_profile,
    target_setting,
)
from ..projection import english_messages, governance_by_constraint
from ..util import markdown_cell, slug


def index_markdown(repository: Repository, profile_ids: list[str]) -> str:
    lines = [
        "# PT Data Quality Repository", "",
        "This site is generated from the authoritative XLSX Rule Specification Repository (RSR).", "",
        "## Available Data Quality Profiles", "",
        "| Profile | Version | Status | Description |", "|---|---:|---|---|",
    ]
    for pid in profile_ids:
        row = repository.profiles_by_id[pid]
        lines.append("| " + " | ".join([
            f"[{markdown_cell(pid)}](profiles/{slug(pid)}/index.md)",
            markdown_cell(row.get("version")), markdown_cell(row.get("status")), markdown_cell(row.get("description")),
        ]) + " |")
    lines.extend(["", "## Repository principle", "", "Validation Targets define what is assessed. Constraints define executable validation conditions. The former one-to-one Rule layer is not part of RSR schema 2.0."])
    return "\n".join(lines)


def profile_index(repository: Repository, profile_id: str, coverage: dict[str, Any]) -> str:
    p = resolve_profile(repository, profile_id).profile
    return "\n".join([
        f"# {p.get('name') or profile_id}", "",
        f"**Profile ID:** `{profile_id}`  ",
        f"**Version:** `{p.get('version')}`  ",
        f"**Status:** `{p.get('status')}`  ",
        f"**Minimum required score:** `{p.get('minimum_required_score')}`", "",
        str(p.get("description") or ""), "",
        "## Effective configuration", "",
        f"- Validation Targets: **{coverage['validationTargets']}**",
        f"- Constraints: **{coverage['constraints']}**",
        f"- Governance-mapped Constraints: **{coverage['governanceMappedConstraints']}** ({coverage['governanceConstraintCoveragePercent']}%)",
        f"- PT Master target binding coverage: **{coverage['ptMasterBindingCoveragePercent']}%**", "",
        "See the domain pages, scoring page, governance traceability and implementation coverage for details.",
    ])


def scoring_markdown(repository: Repository, profile_id: str) -> str:
    profile = resolve_profile(repository, profile_id)
    lines = [
        f"# Scoring — {profile_id}", "",
        f"Minimum required score: **{profile.profile.get('minimum_required_score')}**", "",
        "Effective Constraint weight is resolved from the active profile. Presence constraints may be excluded from score while still affecting validity.", "",
        "## Constraint defaults", "",
        "| Weight key | Weight | Included in score | Behaviour basis | Default severity | Default blocking |",
        "|---|---:|---|---|---|---|",
    ]
    for key, row in sorted(profile.constraint_defaults.items()):
        lines.append("| " + " | ".join(markdown_cell(x) for x in [key, row.get("weight"), row.get("include_in_score"), row.get("behavior_basis"), row.get("default_severity"), row.get("default_blocking")]) + " |")
    lines.extend(["", "## Validation Target settings", "", "| Domain | Validation Target | Importance | Requirement level |", "|---|---|---:|---|"])
    for tid, setting in sorted(profile.target_settings.items()):
        if enabled_target(profile, tid):
            lines.append("| " + " | ".join(markdown_cell(x) for x in [setting.get("domain_id"), tid, setting.get("importance"), setting.get("requirement_level")]) + " |")
    return "\n".join(lines)


def governance_markdown(repository: Repository, profile_id: str) -> str:
    gov = governance_by_constraint(repository, profile_id)
    profile = resolve_profile(repository, profile_id)
    lines = [f"# Governance mapping — {profile_id}", "", "| Constraint | Dimension | Metric | Requirement | Status |", "|---|---|---|---|---|"]
    for c in repository.constraints:
        cid = str(c.get("constraint_id")); tid = str(c.get("validation_target_id"))
        if not enabled_target(profile, tid) or not constraint_enabled(profile, cid):
            continue
        for m in gov.get(cid, []):
            lines.append("| " + " | ".join(markdown_cell(x) for x in [cid, m.get("dimension_id"), m.get("metric_id"), m.get("requirement_id"), m.get("mapping_status")]) + " |")
    return "\n".join(lines)


def implementation_markdown(profile_id: str, shacl_cov: dict[str, Any], schematron_cov: dict[str, Any]) -> str:
    return "\n".join([
        f"# Implementation projections — {profile_id}", "",
        "The PT Master JSON is the runtime projection for the current Java implementation. SHACL and Schematron are optional projections and only emit constraints with explicit compatible bindings.", "",
        "| Projection | Bound targets | Emitted constraints | Unsupported constraints |",
        "|---|---:|---:|---:|",
        f"| SHACL | {shacl_cov.get('boundTargets', 0)} | {shacl_cov.get('emittedConstraints', 0)} | {len(shacl_cov.get('unsupportedConstraints', []))} |",
        f"| Schematron | {schematron_cov.get('boundTargets', 0)} | {schematron_cov.get('emittedConstraints', 0)} | {len(schematron_cov.get('unsupportedConstraints', []))} |",
    ])


def review_required_markdown(repository: Repository, profile_id: str) -> str:
    profile = resolve_profile(repository, profile_id)
    lines = [f"# Review required — {profile_id}", "", "| Type | Artifact | Notes |", "|---|---|---|"]
    groups = [
        ("Validation Target", repository.validation_targets, "validation_target_id"),
        ("Constraint", repository.constraints, "constraint_id"),
        ("Constraint Parameter", repository.constraint_parameters, "parameter_id"),
        ("Message", repository.messages, "message_id"),
        ("Governance Mapping", repository.governance_mappings, "mapping_id"),
        ("Implementation Binding", repository.implementation_bindings, "binding_id"),
    ]
    active_targets = {tid for tid in profile.target_settings if enabled_target(profile, tid)}
    active_constraints = {str(c.get("constraint_id")) for c in repository.constraints if str(c.get("validation_target_id")) in active_targets}
    for label, rows, key in groups:
        for row in rows:
            if row.get("review_required") is not True:
                continue
            if label == "Constraint" and str(row.get("constraint_id")) not in active_constraints:
                continue
            if label == "Governance Mapping" and str(row.get("constraint_id")) not in active_constraints:
                continue
            lines.append("| " + " | ".join(markdown_cell(x) for x in [label, row.get(key), row.get("notes")]) + " |")
    return "\n".join(lines)


def domain_markdown(repository: Repository, profile_id: str, domain_id: str) -> str:
    profile = resolve_profile(repository, profile_id)
    messages = english_messages(repository)
    gov = governance_by_constraint(repository, profile_id)
    targets = [t for t in repository.validation_targets if str(t.get("domain_id")) == domain_id and enabled_target(profile, str(t.get("validation_target_id")))]
    constraints_by_target: defaultdict[str, list[Any]] = defaultdict(list)
    for c in repository.constraints:
        cid = str(c.get("constraint_id")); tid = str(c.get("validation_target_id"))
        if constraint_enabled(profile, cid):
            constraints_by_target[tid].append(c)
    lines = [f"# {domain_id}", ""]
    for t in targets:
        tid = str(t.get("validation_target_id")); setting = target_setting(profile, tid) or {}
        lines.extend([f"## `{t.get('canonical_path')}`", "", f"Validation Target: `{tid}`  ", f"Importance: `{setting.get('importance')}`  ", f"Requirement level: `{setting.get('requirement_level')}`", "", "| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |", "|---|---|---|---|---|---:|---|---|"])
        for c in constraints_by_target.get(tid, []):
            cid = str(c.get("constraint_id"))
            severity, blocking = constraint_severity_and_blocking(profile, dict(c.data), setting)
            weight, include = constraint_weight(profile, dict(c.data))
            g = gov.get(cid, [])
            gtxt = "; ".join(str(x.get("requirement_id") or x.get("metric_id") or x.get("dimension_id") or "UNMAPPED") for x in g)
            lines.append("| " + " | ".join(markdown_cell(x) for x in [cid, c.get("constraint_type"), c.get("assessment_dimension"), severity, blocking, weight if include else 0, messages.get(cid), gtxt]) + " |")
        lines.append("")
    return "\n".join(lines)
