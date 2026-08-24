from __future__ import annotations

import re
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
from ..projection import (
    assessment_dimension_definitions,
    governance_by_constraint,
    implementation_bindings,
    message_map,
    runtime_parameter_map,
)
from ..util import lower_camel


_SUFFIX = {
    "PRESENCE": "missing",
    "MIN_LENGTH": "tooShort",
    "MAX_LENGTH": "tooLong",
    "MIN_VALUE": "belowMinimum",
    "MAX_VALUE": "aboveMaximum",
    "MIN_CARDINALITY": "tooFewValues",
    "MAX_CARDINALITY": "tooManyValues",
    "MIN_DATE": "beforeMinimumDate",
    "MAX_DATE": "afterMaximumDate",
    "MIN_VALUE_OR_LENGTH": "belowMinimum",
    "MAX_VALUE_OR_LENGTH": "aboveMaximum",
    "REGEX": "invalidFormat",
    "UNIQUENESS": "duplicate",
    "VOCABULARY": "invalidVocabulary",
    "RESOLVABLE": "notResolvable",
    "CUSTOM": "customValidation",
}


def _auto_runtime_key(repository: Repository, constraint: dict[str, Any]) -> str:
    tid = str(constraint.get("validation_target_id") or "")
    target = repository.targets_by_id.get(tid)
    domain = str(constraint.get("domain_id") or "")
    if target:
        object_name = str(target.get("object_name") or "")
        field_name = str(target.get("field_name") or target.get("canonical_path") or "")
    else:
        object_name = ""
        field_name = tid
    suffix = _SUFFIX.get(str(constraint.get("constraint_type") or ""), "validation")
    return lower_camel([domain, object_name, field_name, suffix])


def _unique_runtime_key(preferred: str, fallback: str, cid: str, used: set[str]) -> str:
    if preferred and preferred not in used:
        return preferred
    if fallback not in used:
        return fallback
    return lower_camel([fallback, re.sub(r"[^A-Za-z0-9]", "", cid)])


def render_pt_master(repository: Repository, profile_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    profile = resolve_profile(repository, profile_id)
    target_bindings = implementation_bindings(repository, profile_id, "VALIDATION_TARGET")
    constraint_bindings = implementation_bindings(repository, profile_id, "CONSTRAINT")
    params = runtime_parameter_map(repository)
    messages = message_map(repository)
    governance = governance_by_constraint(repository, profile_id)

    target_weights: dict[str, Any] = {}
    target_meta: dict[str, Any] = {}
    for tid in sorted(profile.target_settings):
        if not enabled_target(profile, tid):
            continue
        binding = target_bindings.get(tid)
        if not binding:
            continue
        runtime_target = str(binding.get("runtime_target") or "")
        if not runtime_target:
            continue
        setting = target_setting(profile, tid) or {}
        importance = setting.get("importance")
        if runtime_target in target_weights:
            try:
                current = float(target_weights[runtime_target])
                candidate = float(importance)
                value: Any = max(current, candidate)
                target_weights[runtime_target] = int(value) if value.is_integer() else value
            except (TypeError, ValueError, AttributeError):
                target_weights[runtime_target] = importance
            existing = target_meta[runtime_target]
            ids = existing.setdefault("validationTargetIds", [])
            if existing.get("validationTargetId") and existing["validationTargetId"] not in ids:
                ids.append(existing.pop("validationTargetId"))
            ids.append(tid)
        else:
            target_weights[runtime_target] = importance
            target_meta[runtime_target] = {
                "validationTargetId": tid,
                "requirementLevel": setting.get("requirement_level"),
                "defaultValue": setting.get("default_value"),
            }

    remarks: dict[str, Any] = {}
    enriched_remarks: dict[str, Any] = {}
    used_keys: set[str] = set()

    for row in repository.constraints:
        constraint = dict(row.data)
        cid = str(constraint.get("constraint_id"))
        tid = str(constraint.get("validation_target_id"))
        if not enabled_target(profile, tid) or not constraint_enabled(profile, cid):
            continue
        if str(constraint.get("status") or "").upper() in {"RETIRED", "ARCHIVED", "DEPRECATED"}:
            continue

        target_binding = target_bindings.get(tid) or {}
        constraint_binding = constraint_bindings.get(cid) or {}
        runtime_target = str(constraint_binding.get("runtime_target") or target_binding.get("runtime_target") or "")
        if not runtime_target:
            continue

        explicit_key = str(constraint_binding.get("runtime_key") or "")
        auto_key = _auto_runtime_key(repository, constraint)
        key = _unique_runtime_key(explicit_key, auto_key, cid, used_keys)
        used_keys.add(key)

        localized = messages.get(cid, {})
        titles = {lang: item["title"] for lang, item in localized.items()}
        texts = {lang: item["message"] for lang, item in localized.items()}
        setting = target_setting(profile, tid) or {}
        severity, blocking = constraint_severity_and_blocking(profile, constraint, setting)
        points, include_in_score = constraint_weight(profile, constraint)
        if isinstance(points, float) and points.is_integer():
            points = int(points)

        mapping_rows = governance.get(cid, [])
        requirement_ids = sorted({str(m.get("requirement_id")) for m in mapping_rows if m.get("requirement_id")})
        metric_ids = sorted({str(m.get("metric_id")) for m in mapping_rows if m.get("metric_id")})
        dimension_ids = sorted({str(m.get("dimension_id")) for m in mapping_rows if m.get("dimension_id")})

        constraint_payload = dict(params.get(cid, {}))
        if constraint.get("resolver_id"):
            constraint_payload.setdefault("resolverId", constraint.get("resolver_id"))
        if constraint.get("vocabulary_id"):
            constraint_payload.setdefault("vocabularyId", constraint.get("vocabulary_id"))

        item: dict[str, Any] = {
            "title": titles,
            "message": texts,
            "target": runtime_target,
            "severity": severity,
            "dimension": constraint.get("assessment_dimension"),
            "blocking": blocking,
            "points": points if include_in_score else 0,
            "usedForFairCompliance": bool(constraint.get("used_for_fair_compliance")),
        }
        if constraint_payload:
            item["constraints"] = constraint_payload
        remarks[key] = item

        enriched_remarks[key] = {
            **item,
            "constraintId": cid,
            "validationTargetId": tid,
            "constraintType": constraint.get("constraint_type"),
            "weightKey": constraint.get("weight_key"),
            "includedInScore": include_in_score,
            "governanceDimensionIds": dimension_ids,
            "governanceMetricIds": metric_ids,
            "governanceRequirementIds": requirement_ids,
            "resolverId": constraint.get("resolver_id"),
            "vocabularyId": constraint.get("vocabulary_id"),
            "runtimeKeySource": "EXPLICIT" if explicit_key and key == explicit_key else "GENERATED",
            "reviewRequired": bool(constraint.get("review_required")),
        }

    legacy = {
        "minimumRequiredScore": profile.profile.get("minimum_required_score"),
        "dimensionDefinitions": assessment_dimension_definitions(repository),
        "targetWeights": target_weights,
        "dataQualityRemarks": remarks,
    }
    enriched = {
        "profileId": profile_id,
        "profileVersion": profile.profile.get("version"),
        "minimumRequiredScore": profile.profile.get("minimum_required_score"),
        "scoringMethod": profile.profile.get("scoring_method"),
        "dimensionDefinitions": assessment_dimension_definitions(repository),
        "targetWeights": target_weights,
        "targets": target_meta,
        "dataQualityRemarks": enriched_remarks,
    }
    return legacy, enriched
