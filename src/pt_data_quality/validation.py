from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, Iterable

from .model import Issue, Repository
from .profile import resolve_profile


def _duplicates(rows: Iterable, key: str) -> set[str]:
    counts = Counter(str(r.get(key)) for r in rows if r.get(key) not in (None, ""))
    return {k for k, n in counts.items() if n > 1}


def _issue(severity: str, code: str, message: str, row=None, artifact_id: str | None = None) -> Issue:
    return Issue(
        severity=severity,
        code=code,
        message=message,
        sheet=getattr(row, "sheet", None),
        row_number=getattr(row, "row_number", None),
        artifact_id=artifact_id,
    )


def validate_repository(repository: Repository, schema: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    enums = schema.get("enums", {})

    unique_specs = [
        (repository.domains, "domain_id"),
        (repository.governance_sources, "governance_source_id"),
        (repository.governance_dimensions, "dimension_id"),
        (repository.governance_requirements, "requirement_id"),
        (repository.validation_targets, "validation_target_id"),
        (repository.rules, "rule_id"),
        (repository.constraints, "constraint_id"),
        (repository.resolvers, "resolver_id"),
        (repository.vocabularies, "vocabulary_id"),
        (repository.profiles, "profile_id"),
        (repository.implementation_bindings, "binding_id"),
    ]
    for rows, key in unique_specs:
        for duplicate in sorted(_duplicates(rows, key)):
            issues.append(_issue("error", "DUPLICATE_ID", f"Duplicate {key}: {duplicate}", artifact_id=duplicate))

    # Composite uniqueness.
    seen_pairs: dict[tuple[str, str], Any] = {}
    for row in repository.profile_target_settings:
        pair = (str(row.get("profile_id")), str(row.get("validation_target_id")))
        if pair in seen_pairs:
            issues.append(_issue("error", "DUPLICATE_PROFILE_TARGET", f"Duplicate profile target setting: {pair}", row, pair[1]))
        seen_pairs[pair] = row
    seen_defaults: set[tuple[str, str]] = set()
    for row in repository.profile_constraint_defaults:
        pair = (str(row.get("profile_id")), str(row.get("weight_key")))
        if pair in seen_defaults:
            issues.append(_issue("error", "DUPLICATE_PROFILE_DEFAULT", f"Duplicate profile constraint default: {pair}", row, pair[1]))
        seen_defaults.add(pair)

    domains = repository.domains_by_id
    targets = repository.targets_by_id
    rules = repository.rules_by_id
    constraints = repository.constraints_by_id
    requirements = repository.requirements_by_id
    profiles = repository.profiles_by_id
    resolvers = repository.resolvers_by_id
    vocabularies = repository.vocabularies_by_id

    for row in repository.validation_targets:
        tid = str(row.get("validation_target_id"))
        if str(row.get("domain_id")) not in domains:
            issues.append(_issue("error", "UNKNOWN_DOMAIN", f"Target {tid} references unknown domain {row.get('domain_id')}", row, tid))
        if row.get("target_category") not in enums.get("target_category", []):
            issues.append(_issue("error", "INVALID_TARGET_CATEGORY", f"Target {tid} has invalid category {row.get('target_category')}", row, tid))
        if row.get("review_required") is True:
            issues.append(_issue("warning", "REVIEW_REQUIRED", f"Validation target {tid} requires review", row, tid))

    for row in repository.rules:
        rid = str(row.get("rule_id"))
        target = str(row.get("validation_target_id"))
        if target not in targets:
            issues.append(_issue("error", "UNKNOWN_TARGET", f"Rule {rid} references unknown target {target}", row, rid))
        elif row.get("domain_id") != targets[target].get("domain_id"):
            issues.append(_issue("error", "DOMAIN_MISMATCH", f"Rule {rid} domain differs from target {target}", row, rid))
        if row.get("review_required") is True:
            issues.append(_issue("warning", "REVIEW_REQUIRED", f"Rule {rid} requires review", row, rid))

    messages_by_constraint: defaultdict[str, int] = defaultdict(int)
    for msg in repository.messages:
        cid = str(msg.get("constraint_id"))
        if cid not in constraints:
            issues.append(_issue("error", "UNKNOWN_CONSTRAINT", f"Message {msg.get('message_id')} references unknown constraint {cid}", msg, cid))
        messages_by_constraint[cid] += 1

    params_by_constraint: defaultdict[str, list] = defaultdict(list)
    for param in repository.constraint_parameters:
        cid = str(param.get("constraint_id"))
        if cid not in constraints:
            issues.append(_issue("error", "UNKNOWN_CONSTRAINT", f"Parameter references unknown constraint {cid}", param, cid))
        params_by_constraint[cid].append(param)

    for row in repository.constraints:
        cid = str(row.get("constraint_id"))
        rid = str(row.get("rule_id"))
        tid = str(row.get("validation_target_id"))
        if rid not in rules:
            issues.append(_issue("error", "UNKNOWN_RULE", f"Constraint {cid} references unknown rule {rid}", row, cid))
        if tid not in targets:
            issues.append(_issue("error", "UNKNOWN_TARGET", f"Constraint {cid} references unknown target {tid}", row, cid))
        if rid in rules and rules[rid].get("validation_target_id") != tid:
            issues.append(_issue("error", "RULE_TARGET_MISMATCH", f"Constraint {cid} target differs from rule {rid}", row, cid))
        if row.get("constraint_type") not in enums.get("constraint_type", []):
            issues.append(_issue("error", "INVALID_CONSTRAINT_TYPE", f"Constraint {cid} has invalid type {row.get('constraint_type')}", row, cid))
        if row.get("weight_key") not in enums.get("weight_key", []):
            issues.append(_issue("error", "INVALID_WEIGHT_KEY", f"Constraint {cid} has invalid weight key {row.get('weight_key')}", row, cid))
        if row.get("assessment_dimension") not in enums.get("assessment_dimension", []):
            issues.append(_issue("error", "INVALID_ASSESSMENT_DIMENSION", f"Constraint {cid} has invalid assessment dimension {row.get('assessment_dimension')}", row, cid))
        if row.get("constraint_type") == "RESOLVABLE" and not row.get("resolver_id"):
            issues.append(_issue("error", "MISSING_RESOLVER", f"Resolvable constraint {cid} has no resolver_id", row, cid))
        if row.get("resolver_id") and str(row.get("resolver_id")) not in resolvers:
            issues.append(_issue("error", "UNKNOWN_RESOLVER", f"Constraint {cid} references unknown resolver {row.get('resolver_id')}", row, cid))
        if row.get("constraint_type") == "VOCABULARY" and not row.get("vocabulary_id"):
            issues.append(_issue("error", "MISSING_VOCABULARY", f"Vocabulary constraint {cid} has no vocabulary_id", row, cid))
        if row.get("vocabulary_id") and str(row.get("vocabulary_id")) not in vocabularies:
            issues.append(_issue("error", "UNKNOWN_VOCABULARY", f"Constraint {cid} references unknown vocabulary {row.get('vocabulary_id')}", row, cid))
        if not messages_by_constraint[cid]:
            issues.append(_issue("warning", "MISSING_MESSAGE", f"Constraint {cid} has no message template", row, cid))
        if row.get("review_required") is True:
            issues.append(_issue("warning", "REVIEW_REQUIRED", f"Constraint {cid} requires review", row, cid))

    for row in repository.governance_dimensions:
        gid = str(row.get("dimension_id"))
        if str(row.get("governance_source_id")) not in repository.index(repository.governance_sources, "governance_source_id"):
            issues.append(_issue("error", "UNKNOWN_GOVERNANCE_SOURCE", f"Dimension {gid} references unknown governance source", row, gid))

    governance_dimensions = repository.index(repository.governance_dimensions, "dimension_id")
    for row in repository.governance_requirements:
        req = str(row.get("requirement_id"))
        dim = str(row.get("dimension_id") or "")
        if dim not in governance_dimensions:
            severity = "warning" if (row.get("review_required") is True or not dim) else "error"
            issues.append(_issue(severity, "UNKNOWN_GOVERNANCE_DIMENSION", f"Requirement {req} references unknown governance dimension {row.get('dimension_id')}", row, req))
        if row.get("review_required") is True:
            issues.append(_issue("warning", "REVIEW_REQUIRED", f"Governance requirement {req} requires review", row, req))

    valid_artifact_indexes = {
        "VALIDATION_TARGET": targets,
        "TARGET": targets,
        "RULE": rules,
        "CONSTRAINT": constraints,
        "PROFILE": profiles,
    }
    for row in repository.governance_mappings:
        req = str(row.get("requirement_id"))
        art_type = str(row.get("artifact_type") or "").upper()
        art = str(row.get("artifact_id"))
        if req not in requirements:
            issues.append(_issue("error", "UNKNOWN_GOVERNANCE_REQUIREMENT", f"Mapping references unknown requirement {req}", row, art))
        index = valid_artifact_indexes.get(art_type)
        if index is None:
            issues.append(_issue("error", "INVALID_ARTIFACT_TYPE", f"Governance mapping uses unsupported artifact type {art_type}", row, art))
        elif art not in index:
            issues.append(_issue("error", "UNKNOWN_ARTIFACT", f"Governance mapping references unknown {art_type} {art}", row, art))
        pid = str(row.get("profile_id") or "")
        if pid and pid != "*" and pid not in profiles:
            issues.append(_issue("error", "UNKNOWN_PROFILE", f"Governance mapping references unknown profile {pid}", row, art))

    for row in repository.profile_target_settings:
        pid = str(row.get("profile_id"))
        tid = str(row.get("validation_target_id"))
        if pid not in profiles:
            issues.append(_issue("error", "UNKNOWN_PROFILE", f"Target setting references unknown profile {pid}", row, tid))
        if tid not in targets:
            issues.append(_issue("error", "UNKNOWN_TARGET", f"Target setting references unknown target {tid}", row, tid))
        if row.get("requirement_level") not in enums.get("requirement_level", []):
            issues.append(_issue("error", "INVALID_REQUIREMENT_LEVEL", f"Target setting {tid} has invalid requirement level {row.get('requirement_level')}", row, tid))
        try:
            importance = float(row.get("importance"))
            if importance < 0:
                raise ValueError
        except (TypeError, ValueError):
            issues.append(_issue("error", "INVALID_IMPORTANCE", f"Target setting {tid} has invalid importance {row.get('importance')}", row, tid))

    for row in repository.profile_constraint_defaults:
        pid = str(row.get("profile_id"))
        if pid not in profiles:
            issues.append(_issue("error", "UNKNOWN_PROFILE", f"Constraint default references unknown profile {pid}", row, str(row.get("weight_key"))))
        if row.get("weight_key") not in enums.get("weight_key", []):
            issues.append(_issue("error", "INVALID_WEIGHT_KEY", f"Profile default has invalid weight key {row.get('weight_key')}", row, str(row.get("weight_key"))))
        if row.get("include_in_score") is True and row.get("weight") in (None, ""):
            issues.append(_issue("error", "MISSING_WEIGHT", f"Scored weight key {row.get('weight_key')} has no weight", row, str(row.get("weight_key"))))

    for row in repository.profile_overrides:
        pid = str(row.get("profile_id"))
        art_type = str(row.get("artifact_type") or "").upper()
        art = str(row.get("artifact_id") or "")
        if pid not in profiles:
            issues.append(_issue("error", "UNKNOWN_PROFILE", f"Override references unknown profile {pid}", row, art))
        index = valid_artifact_indexes.get(art_type)
        if index is None or art not in index:
            issues.append(_issue("error", "UNKNOWN_ARTIFACT", f"Override references unknown {art_type} {art}", row, art))

    for row in repository.implementation_bindings:
        art_type = str(row.get("artifact_type") or "").upper()
        art = str(row.get("artifact_id") or "")
        index = valid_artifact_indexes.get(art_type)
        if index is None or art not in index:
            issues.append(_issue("error", "UNKNOWN_ARTIFACT", f"Binding {row.get('binding_id')} references unknown {art_type} {art}", row, art))
        pid = str(row.get("profile_scope") or "")
        if pid not in {"", "*"} and pid not in profiles:
            issues.append(_issue("error", "UNKNOWN_PROFILE", f"Binding {row.get('binding_id')} references unknown profile {pid}", row, art))
        if row.get("review_required") is True:
            issues.append(_issue("warning", "REVIEW_REQUIRED", f"Implementation binding {row.get('binding_id')} requires review", row, art))

    # Profile inheritance and runtime weight coverage.
    for pid in profiles:
        try:
            effective = resolve_profile(repository, pid)
        except (KeyError, ValueError) as exc:
            issues.append(_issue("error", "PROFILE_INHERITANCE", str(exc), profiles[pid], pid))
            continue
        used_weight_keys = {str(c.get("weight_key")) for c in repository.constraints}
        for key in sorted(used_weight_keys):
            if key not in effective.constraint_defaults:
                issues.append(_issue("warning", "MISSING_PROFILE_WEIGHT_DEFAULT", f"Profile {pid} has no default for weight key {key}", profiles[pid], pid))

    # PT Master binding coverage for enabled targets.
    runtime_bindings = {
        str(b.get("artifact_id")): b
        for b in repository.implementation_bindings
        if b.get("implementation_id") == "PT_MASTER"
        and b.get("artifact_type") == "VALIDATION_TARGET"
        and b.get("representation") == "RUNTIME_JSON"
        and str(b.get("status")).upper() not in {"RETIRED", "ARCHIVED", "DEPRECATED"}
    }
    for pid in profiles:
        try:
            effective = resolve_profile(repository, pid)
        except Exception:
            continue
        runtime_targets: defaultdict[str, list[tuple[str, Any]]] = defaultdict(list)
        for tid, setting in effective.target_settings.items():
            enabled = setting.get("enabled") is True or str(setting.get("enabled")).lower() == "true"
            if not enabled:
                continue
            if tid not in runtime_bindings:
                issues.append(_issue("error", "MISSING_PT_MASTER_BINDING", f"Enabled target {tid} has no PT_MASTER/RUNTIME_JSON binding for profile {pid}", artifact_id=tid))
                continue
            runtime_target = str(runtime_bindings[tid].get("runtime_target") or "")
            if not runtime_target:
                issues.append(_issue("warning", "EMPTY_PT_MASTER_RUNTIME_TARGET", f"Target {tid} has a PT Master binding without runtime_target", runtime_bindings[tid], tid))
                continue
            runtime_targets[runtime_target].append((tid, setting.get("importance")))
        for runtime_target, entries in sorted(runtime_targets.items()):
            if len(entries) <= 1:
                continue
            importances = {str(x[1]) for x in entries}
            code = "PT_MASTER_RUNTIME_TARGET_WEIGHT_CONFLICT" if len(importances) > 1 else "PT_MASTER_RUNTIME_TARGET_REUSED"
            details = ", ".join(f"{tid} (importance={importance})" for tid, importance in entries)
            issues.append(_issue("warning", code, f"Runtime target {runtime_target} is used by multiple validation targets in profile {pid}: {details}. Legacy targetWeights cannot distinguish these contexts.", artifact_id=runtime_target))

    return issues
