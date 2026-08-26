from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Any, Iterable

from .model import Issue, Repository
from .profile import coerce_value, enabled_target, resolve_profile
from .projection import implementation_bindings


INACTIVE = {"RETIRED", "ARCHIVED", "DEPRECATED"}
PLACEHOLDER_RE = re.compile(r"\{(?:value\d*|recordId\d*|startDateValue|endDateValue|\d+)\}")


def _duplicates(rows: Iterable, key: str) -> set[str]:
    counts = Counter(str(r.get(key)) for r in rows if r.get(key) not in (None, ""))
    return {k for k, n in counts.items() if n > 1}


def _issue(severity: str, code: str, message: str, row=None, artifact_id: str | None = None) -> Issue:
    return Issue(severity, code, message, getattr(row, "sheet", None), getattr(row, "row_number", None), artifact_id)


def _status_active(row) -> bool:
    return str(row.get("status") or "ACTIVE").upper() not in INACTIVE


def _as_int(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def validate_repository(repository: Repository, schema: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    enums = schema.get("enums", {})

    unique_specs = [
        (repository.domains, "domain_id"),
        (repository.governance_sources, "governance_source_id"),
        (repository.governance_dimensions, "dimension_id"),
        (repository.governance_metrics, "metric_id"),
        (repository.governance_requirements, "requirement_id"),
        (repository.assessment_dimensions, "assessment_dimension_id"),
        (repository.validation_targets, "validation_target_id"),
        (repository.constraints, "constraint_id"),
        (repository.constraint_parameters, "parameter_id"),
        (repository.messages, "message_id"),
        (repository.governance_mappings, "mapping_id"),
        (repository.resolvers, "resolver_id"),
        (repository.vocabularies, "vocabulary_id"),
        (repository.profiles, "profile_id"),
        (repository.profile_overrides, "override_id"),
        (repository.implementation_bindings, "binding_id"),
        (repository.implementation_profiles, "implementation_profile_id"),
        (repository.implementation_runtime_rules, "runtime_rule_id"),
        (repository.implementation_runtime_parameters, "runtime_parameter_id"),
    ]
    for rows, key in unique_specs:
        for duplicate in sorted(_duplicates(rows, key)):
            issues.append(_issue("error", "DUPLICATE_ID", f"Duplicate {key}: {duplicate}", artifact_id=duplicate))

    # Composite uniqueness for profile configuration.
    for rows, fields, code in [
        (repository.profile_target_settings, ("profile_id", "validation_target_id"), "DUPLICATE_PROFILE_TARGET"),
        (repository.profile_constraint_defaults, ("profile_id", "weight_key"), "DUPLICATE_PROFILE_DEFAULT"),
    ]:
        seen: set[tuple[str, ...]] = set()
        for row in rows:
            key = tuple(str(row.get(f)) for f in fields)
            if key in seen:
                issues.append(_issue("error", code, f"Duplicate configuration row: {key}", row, key[-1]))
            seen.add(key)

    domains = repository.domains_by_id
    targets = repository.targets_by_id
    constraints = repository.constraints_by_id
    dimensions = repository.governance_dimensions_by_id
    metrics = repository.governance_metrics_by_id
    requirements = repository.requirements_by_id
    assessment_dimensions = repository.assessment_dimensions_by_id
    profiles = repository.profiles_by_id
    resolvers = repository.resolvers_by_id
    vocabularies = repository.vocabularies_by_id

    if str(repository.metadata.get("schema_version")) != str(schema.get("repository_schema_version")):
        issues.append(_issue("warning", "SCHEMA_VERSION_MISMATCH", f"Workbook schema_version={repository.metadata.get('schema_version')} but repository schema is {schema.get('repository_schema_version')}"))

    for row in repository.validation_targets:
        tid = str(row.get("validation_target_id"))
        if str(row.get("domain_id")) not in domains:
            issues.append(_issue("error", "UNKNOWN_DOMAIN", f"Target {tid} references unknown domain {row.get('domain_id')}", row, tid))
        if row.get("target_category") not in enums.get("target_category", []):
            issues.append(_issue("error", "INVALID_TARGET_CATEGORY", f"Target {tid} has invalid category {row.get('target_category')}", row, tid))
        if row.get("review_required") is True:
            issues.append(_issue("warning", "REVIEW_REQUIRED", f"Validation target {tid} requires review", row, tid))

    expected_parameter = {
        "MIN_LENGTH": "minLength", "MAX_LENGTH": "maxLength",
        "MIN_VALUE": "minValue", "MAX_VALUE": "maxValue",
        "MIN_CARDINALITY": "minCardinality", "MAX_CARDINALITY": "maxCardinality",
        "MIN_DATE": "minDate", "MAX_DATE": "maxDate",
        "REGEX": "pattern",
    }
    params_by_constraint: defaultdict[str, list[Any]] = defaultdict(list)
    param_triplets: set[tuple[str, str, int]] = set()
    for row in repository.constraint_parameters:
        cid = str(row.get("constraint_id"))
        params_by_constraint[cid].append(row)
        if cid not in constraints:
            issues.append(_issue("error", "UNKNOWN_CONSTRAINT", f"Parameter references unknown Constraint {cid}", row, cid))
        value_type = str(row.get("value_type") or "")
        if value_type not in enums.get("parameter_value_type", []):
            issues.append(_issue("error", "INVALID_PARAMETER_TYPE", f"Parameter {row.get('parameter_id')} has invalid value_type {value_type}", row, cid))
        op = str(row.get("combine_operator") or "")
        if op and op not in enums.get("combine_operator", []):
            issues.append(_issue("error", "INVALID_COMBINE_OPERATOR", f"Parameter {row.get('parameter_id')} has invalid combine_operator {op}", row, cid))
        seq = _as_int(row.get("sequence"))
        if seq is None:
            issues.append(_issue("error", "INVALID_PARAMETER_SEQUENCE", f"Parameter {row.get('parameter_id')} has invalid sequence", row, cid))
        else:
            triplet = (cid, str(row.get("parameter_name")), seq)
            if triplet in param_triplets:
                issues.append(_issue("error", "DUPLICATE_PARAMETER_SEQUENCE", f"Duplicate parameter sequence {triplet}", row, cid))
            param_triplets.add(triplet)
        coerced = coerce_value(row.get("parameter_value"), value_type)
        if value_type == "INTEGER" and not isinstance(coerced, int):
            issues.append(_issue("error", "PARAMETER_TYPE_MISMATCH", f"{row.get('parameter_id')} is declared INTEGER but value is {row.get('parameter_value')!r}", row, cid))
        if row.get("review_required") is True:
            issues.append(_issue("warning", "REVIEW_REQUIRED", f"Constraint parameter {row.get('parameter_id')} requires review", row, cid))

    for row in repository.constraints:
        cid = str(row.get("constraint_id"))
        tid = str(row.get("validation_target_id"))
        ctype = str(row.get("constraint_type") or "")
        if tid not in targets:
            issues.append(_issue("error", "UNKNOWN_TARGET", f"Constraint {cid} references unknown target {tid}", row, cid))
        if ctype not in enums.get("constraint_type", []):
            issues.append(_issue("error", "INVALID_CONSTRAINT_TYPE", f"Constraint {cid} has invalid type {ctype}", row, cid))
        if row.get("weight_key") not in enums.get("weight_key", []):
            issues.append(_issue("error", "INVALID_WEIGHT_KEY", f"Constraint {cid} has invalid weight_key {row.get('weight_key')}", row, cid))
        if str(row.get("assessment_dimension")) not in assessment_dimensions:
            issues.append(_issue("error", "UNKNOWN_ASSESSMENT_DIMENSION", f"Constraint {cid} references unknown assessment dimension {row.get('assessment_dimension')}", row, cid))
        if row.get("resolver_id") and str(row.get("resolver_id")) not in resolvers:
            issues.append(_issue("error", "UNKNOWN_RESOLVER", f"Constraint {cid} references unknown resolver {row.get('resolver_id')}", row, cid))
        if row.get("vocabulary_id") and str(row.get("vocabulary_id")) not in vocabularies:
            issues.append(_issue("error", "UNKNOWN_VOCABULARY", f"Constraint {cid} references unknown vocabulary {row.get('vocabulary_id')}", row, cid))
        pname = expected_parameter.get(ctype)
        if pname and not any(str(p.get("parameter_name")) == pname for p in params_by_constraint.get(cid, [])):
            issues.append(_issue("error", "MISSING_EXPECTED_PARAMETER", f"Constraint {cid} ({ctype}) requires parameter {pname}", row, cid))
        if row.get("review_required") is True:
            issues.append(_issue("warning", "REVIEW_REQUIRED", f"Constraint {cid} requires review", row, cid))

    # Exactly one logical message per Constraint; localized columns live on that row.
    messages_by_constraint: defaultdict[str, list[Any]] = defaultdict(list)
    for row in repository.messages:
        cid = str(row.get("constraint_id"))
        messages_by_constraint[cid].append(row)
        if cid not in constraints:
            issues.append(_issue("error", "UNKNOWN_CONSTRAINT", f"Message references unknown Constraint {cid}", row, cid))
        for suffix in ("en", "sr", "sr_cyr", "pt"):
            if not row.get(f"title_{suffix}") or not row.get(f"message_{suffix}"):
                issues.append(_issue("warning", "MISSING_MESSAGE_TRANSLATION", f"Message {row.get('message_id')} is missing {suffix} title/text", row, cid))
            text = str(row.get(f"message_{suffix}") or "")
            if PLACEHOLDER_RE.search(text):
                issues.append(_issue("error", "RUNTIME_PLACEHOLDER_IN_MESSAGE", f"Message {row.get('message_id')} contains runtime placeholder in {suffix}", row, cid))
        if row.get("review_required") is True:
            issues.append(_issue("warning", "REVIEW_REQUIRED", f"Message {row.get('message_id')} requires review", row, cid))
    for cid, row in constraints.items():
        count = len(messages_by_constraint.get(cid, []))
        if count != 1:
            issues.append(_issue("error", "MESSAGE_CARDINALITY", f"Constraint {cid} must have exactly one logical Messages row; found {count}", row, cid))

    # Governance hierarchy and constraint-centric coverage.
    for row in repository.governance_metrics:
        mid = str(row.get("metric_id"))
        did = str(row.get("dimension_id") or "")
        if did and did not in dimensions:
            issues.append(_issue("error", "UNKNOWN_GOVERNANCE_DIMENSION", f"Metric {mid} references unknown dimension {did}", row, mid))
    for row in repository.governance_requirements:
        rid = str(row.get("requirement_id"))
        mid = str(row.get("metric_id") or "")
        if mid and mid not in metrics:
            issues.append(_issue("error", "UNKNOWN_GOVERNANCE_METRIC", f"Requirement {rid} references unknown metric {mid}", row, rid))

    mappings_by_constraint: defaultdict[str, list[Any]] = defaultdict(list)
    for row in repository.governance_mappings:
        cid = str(row.get("constraint_id"))
        mappings_by_constraint[cid].append(row)
        if cid not in constraints:
            issues.append(_issue("error", "UNKNOWN_CONSTRAINT", f"Governance mapping references unknown Constraint {cid}", row, cid))
            continue
        did = str(row.get("dimension_id") or "")
        mid = str(row.get("metric_id") or "")
        rid = str(row.get("requirement_id") or "")
        status = str(row.get("mapping_status") or "")
        if status not in enums.get("mapping_status", []):
            issues.append(_issue("error", "INVALID_MAPPING_STATUS", f"Mapping {row.get('mapping_id')} has invalid status {status}", row, cid))
        if did and did not in dimensions:
            issues.append(_issue("error", "UNKNOWN_GOVERNANCE_DIMENSION", f"Mapping {row.get('mapping_id')} references unknown dimension {did}", row, cid))
        if mid and mid not in metrics:
            issues.append(_issue("error", "UNKNOWN_GOVERNANCE_METRIC", f"Mapping {row.get('mapping_id')} references unknown metric {mid}", row, cid))
        if rid and rid not in requirements:
            issues.append(_issue("error", "UNKNOWN_GOVERNANCE_REQUIREMENT", f"Mapping {row.get('mapping_id')} references unknown requirement {rid}", row, cid))
        if rid and not mid:
            issues.append(_issue("error", "REQUIREMENT_WITHOUT_METRIC", f"Mapping {row.get('mapping_id')} has requirement but no metric", row, cid))
        if rid and rid in requirements and mid and str(requirements[rid].get("metric_id") or "") != mid:
            issues.append(_issue("error", "REQUIREMENT_METRIC_MISMATCH", f"Requirement {rid} belongs to {requirements[rid].get('metric_id')}, not {mid}", row, cid))
        if mid and mid in metrics and did and metrics[mid].get("dimension_id") and str(metrics[mid].get("dimension_id")) != did:
            issues.append(_issue("error", "METRIC_DIMENSION_MISMATCH", f"Metric {mid} belongs to {metrics[mid].get('dimension_id')}, not {did}", row, cid))
        if status == "UNMAPPED":
            issues.append(_issue("warning", "UNMAPPED_GOVERNANCE", f"Constraint {cid} has no authoritative governance mapping yet", row, cid))
        elif row.get("review_required") is True:
            issues.append(_issue("warning", "REVIEW_REQUIRED", f"Governance mapping {row.get('mapping_id')} requires review", row, cid))
    for cid, row in constraints.items():
        if _status_active(row) and not mappings_by_constraint.get(cid):
            issues.append(_issue("error", "MISSING_GOVERNANCE_COVERAGE_ROW", f"Active Constraint {cid} must appear in Governance Mappings, even if UNMAPPED", row, cid))

    # Profile references and effective configuration.
    for row in repository.profile_target_settings:
        pid = str(row.get("profile_id")); tid = str(row.get("validation_target_id"))
        if pid not in profiles:
            issues.append(_issue("error", "UNKNOWN_PROFILE", f"Profile target setting references unknown profile {pid}", row, tid))
        if tid not in targets:
            issues.append(_issue("error", "UNKNOWN_TARGET", f"Profile target setting references unknown target {tid}", row, tid))
        if row.get("requirement_level") not in enums.get("requirement_level", []):
            issues.append(_issue("error", "INVALID_REQUIREMENT_LEVEL", f"Target setting {tid} has invalid requirement level {row.get('requirement_level')}", row, tid))
    for row in repository.profile_constraint_defaults:
        if str(row.get("profile_id")) not in profiles:
            issues.append(_issue("error", "UNKNOWN_PROFILE", f"Constraint default references unknown profile {row.get('profile_id')}", row, str(row.get("weight_key"))))
        if row.get("weight_key") not in enums.get("weight_key", []):
            issues.append(_issue("error", "INVALID_WEIGHT_KEY", f"Constraint default has invalid weight_key {row.get('weight_key')}", row, str(row.get("weight_key"))))
    for row in repository.profile_overrides:
        cid = str(row.get("constraint_id"))
        if cid not in constraints:
            issues.append(_issue("error", "UNKNOWN_CONSTRAINT", f"Profile override references unknown Constraint {cid}", row, cid))

    # Explicit implementation compatibility overlay.
    implementation_profiles = repository.implementation_profiles_by_id
    runtime_rules = repository.implementation_runtime_rules_by_id

    seen_weights: set[tuple[str, str]] = set()
    for row in repository.implementation_profiles:
        ipid = str(row.get("implementation_profile_id") or "")
        scope = str(row.get("profile_scope") or "*")
        if scope != "*" and scope not in profiles:
            issues.append(_issue("error", "UNKNOWN_IMPLEMENTATION_PROFILE_SCOPE", f"Implementation profile {ipid} references unknown Data Quality Profile {scope}", row, ipid))
        mode = str(row.get("compatibility_mode") or "")
        if mode not in enums.get("compatibility_mode", []):
            issues.append(_issue("error", "INVALID_COMPATIBILITY_MODE", f"Implementation profile {ipid} has invalid compatibility_mode {mode}", row, ipid))

    seen_runtime_keys: set[tuple[str, str]] = set()
    for row in repository.implementation_target_weights:
        ipid = str(row.get("implementation_profile_id") or "")
        target = str(row.get("runtime_target") or "")
        if ipid not in implementation_profiles:
            issues.append(_issue("error", "UNKNOWN_IMPLEMENTATION_PROFILE", f"Target weight references unknown implementation profile {ipid}", row, target))
        key = (ipid, target)
        if key in seen_weights:
            issues.append(_issue("error", "DUPLICATE_IMPLEMENTATION_TARGET_WEIGHT", f"Duplicate implementation target weight {key}", row, target))
        seen_weights.add(key)

    for row in repository.implementation_runtime_rules:
        ipid = str(row.get("implementation_profile_id") or "")
        rid = str(row.get("runtime_rule_id") or "")
        key = str(row.get("runtime_key") or "")
        if ipid not in implementation_profiles:
            issues.append(_issue("error", "UNKNOWN_IMPLEMENTATION_PROFILE", f"Runtime rule {rid} references unknown implementation profile {ipid}", row, rid))
        dim = str(row.get("assessment_dimension") or "")
        if dim not in assessment_dimensions:
            issues.append(_issue("error", "UNKNOWN_ASSESSMENT_DIMENSION", f"Runtime rule {rid} references unknown assessment dimension {dim}", row, rid))
        pair = (ipid, key)
        if pair in seen_runtime_keys:
            issues.append(_issue("error", "DUPLICATE_IMPLEMENTATION_RUNTIME_KEY", f"Duplicate runtime key {key} in implementation profile {ipid}", row, key))
        seen_runtime_keys.add(pair)

    for row in repository.implementation_runtime_parameters:
        ipid = str(row.get("implementation_profile_id") or "")
        rid = str(row.get("runtime_rule_id") or "")
        pid = str(row.get("runtime_parameter_id") or "")
        if ipid not in implementation_profiles:
            issues.append(_issue("error", "UNKNOWN_IMPLEMENTATION_PROFILE", f"Runtime parameter {pid} references unknown implementation profile {ipid}", row, pid))
        rule = runtime_rules.get(rid)
        if rule is None:
            issues.append(_issue("error", "UNKNOWN_IMPLEMENTATION_RUNTIME_RULE", f"Runtime parameter {pid} references unknown runtime rule {rid}", row, pid))
        elif str(rule.get("implementation_profile_id") or "") != ipid:
            issues.append(_issue("error", "IMPLEMENTATION_PROFILE_MISMATCH", f"Runtime parameter {pid} and runtime rule {rid} belong to different implementation profiles", row, pid))
        value_type = str(row.get("value_type") or "")
        if value_type not in enums.get("parameter_value_type", []):
            issues.append(_issue("error", "INVALID_PARAMETER_TYPE", f"Runtime parameter {pid} has invalid value_type {value_type}", row, pid))
        coerced = coerce_value(row.get("parameter_value"), value_type)
        if value_type == "INTEGER" and not isinstance(coerced, int):
            issues.append(_issue("error", "PARAMETER_TYPE_MISMATCH", f"Runtime parameter {pid} is declared INTEGER but value is {row.get('parameter_value')!r}", row, pid))
        if bool(row.get("required_by_current_java")) and bool(row.get("additive_metadata")):
            issues.append(_issue("error", "ADDITIVE_PARAMETER_MARKED_REQUIRED", f"Runtime parameter {pid} cannot be both additive metadata and required by current Java", row, pid))

    # Validate extended implementation-binding metadata without requiring every
    # legacy runtime rule to have a canonical Constraint mapping.
    for row in repository.implementation_bindings:
        role = str(row.get("compatibility_role") or "")
        if role and role not in enums.get("implementation_compatibility_role", []):
            issues.append(_issue("error", "INVALID_IMPLEMENTATION_COMPATIBILITY_ROLE", f"Binding {row.get('binding_id')} has invalid compatibility_role {role}", row, str(row.get("binding_id"))))
        mode = str(row.get("binding_mode") or "")
        if mode and mode not in enums.get("implementation_binding_mode", []):
            issues.append(_issue("error", "INVALID_IMPLEMENTATION_BINDING_MODE", f"Binding {row.get('binding_id')} has invalid binding_mode {mode}", row, str(row.get("binding_id"))))
        runtime_rule_id = str(row.get("runtime_rule_id") or "")
        if runtime_rule_id and runtime_rule_id not in runtime_rules:
            issues.append(_issue("error", "UNKNOWN_IMPLEMENTATION_RUNTIME_RULE", f"Binding {row.get('binding_id')} references unknown runtime rule {runtime_rule_id}", row, str(row.get("binding_id"))))

    # PT Master bindings and runtime compatibility hazards.
    for pid in profiles:
        try:
            effective = resolve_profile(repository, pid)
        except (KeyError, ValueError) as exc:
            issues.append(_issue("error", "PROFILE_RESOLUTION_FAILED", str(exc), artifact_id=pid))
            continue
        target_bindings = implementation_bindings(repository, pid, "VALIDATION_TARGET")
        constraint_bindings = implementation_bindings(repository, pid, "CONSTRAINT")
        runtime_targets: defaultdict[str, list[tuple[str, Any]]] = defaultdict(list)
        for tid, setting in effective.target_settings.items():
            if not enabled_target(effective, tid):
                continue
            binding = target_bindings.get(tid)
            if not binding:
                issues.append(_issue("error", "MISSING_PT_MASTER_BINDING", f"Enabled target {tid} has no PT_MASTER/RUNTIME_JSON binding for profile {pid}", artifact_id=tid))
                continue
            runtime_target = str(binding.get("runtime_target") or "")
            if not runtime_target:
                issues.append(_issue("error", "EMPTY_PT_MASTER_RUNTIME_TARGET", f"Target {tid} has PT Master binding without runtime_target", artifact_id=tid))
                continue
            if "???" in runtime_target:
                issues.append(_issue("error", "UNRESOLVED_RUNTIME_BINDING", f"Target {tid} has unresolved runtime_target {runtime_target}", artifact_id=tid))
            runtime_targets[runtime_target].append((tid, setting.get("importance")))
        for runtime_target, entries in sorted(runtime_targets.items()):
            if len(entries) > 1:
                importances = {str(x[1]) for x in entries}
                code = "PT_MASTER_RUNTIME_TARGET_WEIGHT_CONFLICT" if len(importances) > 1 else "PT_MASTER_RUNTIME_TARGET_REUSED"
                details = ", ".join(f"{tid} (importance={importance})" for tid, importance in entries)
                issues.append(_issue("warning", code, f"Runtime target {runtime_target} is used by multiple validation targets in profile {pid}: {details}", artifact_id=runtime_target))
        runtime_keys: defaultdict[str, list[str]] = defaultdict(list)
        for cid, binding in constraint_bindings.items():
            key = str(binding.get("runtime_key") or "")
            if key:
                runtime_keys[key].append(cid)
            if "???" in str(binding.get("runtime_target") or "") or "???" in key:
                issues.append(_issue("error", "UNRESOLVED_RUNTIME_BINDING", f"Constraint {cid} has unresolved PT Master binding", artifact_id=cid))
        for key, cids in runtime_keys.items():
            if len(cids) > 1:
                issues.append(_issue("warning", "SHARED_EXPLICIT_RUNTIME_KEY", f"Explicit runtime key {key} is shared by Constraints: {', '.join(cids)}. This is valid for the RSR 2.0.1 N:M compatibility layer; canonical fallback projection may still collapse it.", artifact_id=key))

    return issues
