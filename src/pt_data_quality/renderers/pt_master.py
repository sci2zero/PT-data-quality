from __future__ import annotations

import re
from collections import defaultdict
from typing import Any

from ..model import Repository
from ..profile import (
    constraint_enabled,
    constraint_weight,
    enabled_target,
    presence_severity,
    resolve_profile,
    rule_enabled,
    target_setting,
)
from ..util import lower_camel


def _binding_index(repository: Repository, profile_id: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in repository.implementation_bindings:
        if row.get("implementation_id") != "PT_MASTER":
            continue
        if row.get("artifact_type") != "VALIDATION_TARGET":
            continue
        if row.get("representation") != "RUNTIME_JSON":
            continue
        scope = str(row.get("profile_scope") or "*")
        if scope not in {"*", profile_id}:
            continue
        if str(row.get("status")).upper() in {"RETIRED", "ARCHIVED", "DEPRECATED"}:
            continue
        result[str(row.get("artifact_id"))] = dict(row.data)
    return result


def _constraint_runtime_key(constraint: dict[str, Any]) -> str:
    suffix = {
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
    }.get(str(constraint.get("constraint_type")), "validation")
    parts = [str(constraint.get("domain_id")), str(constraint.get("object_name")), str(constraint.get("field_name")), suffix]
    return lower_camel(parts)


def _parameter_map(repository: Repository) -> dict[str, dict[str, Any]]:
    result: defaultdict[str, dict[str, Any]] = defaultdict(dict)
    for row in repository.constraint_parameters:
        result[str(row.get("constraint_id"))][str(row.get("parameter_name"))] = row.get("parameter_value")
    return result


def _message_map(repository: Repository) -> dict[str, dict[str, dict[str, str]]]:
    result: defaultdict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for row in repository.messages:
        cid = str(row.get("constraint_id"))
        lang = str(row.get("language") or "en")
        result[cid][lang] = {
            "title": str(row.get("title") or ""),
            "message": str(row.get("message_text") or ""),
        }
    return result


def _governance_map(repository: Repository, profile_id: str) -> dict[str, list[str]]:
    by_artifact: defaultdict[str, list[str]] = defaultdict(list)
    for row in repository.governance_mappings:
        scope = str(row.get("profile_id") or "*")
        if scope not in {"*", profile_id}:
            continue
        by_artifact[str(row.get("artifact_id"))].append(str(row.get("requirement_id")))
    return by_artifact


def _is_fair_requirement(repository: Repository, requirement_id: str) -> bool:
    row = repository.requirements_by_id.get(requirement_id)
    if row is None:
        return False
    text = " ".join(
        str(row.get(k) or "")
        for k in ["requirement_id", "metric_id", "title", "description", "notes", "source_kind"]
    ).lower()
    return "fair" in text or "fsf-" in text


def _severity_and_blocking(profile, constraint: dict[str, Any], setting: dict[str, Any]) -> tuple[str, bool]:
    cid = str(constraint.get("constraint_id"))
    override = profile.override_for("CONSTRAINT", cid)
    if constraint.get("constraint_type") == "PRESENCE":
        severity = str(override.get("severity") or presence_severity(setting.get("requirement_level")))
        default_block = bool(setting.get("blocking_on_failure"))
    else:
        severity = str(override.get("severity") or "ERROR")
        default_block = True
    blocking = override.get("blocking", default_block)
    if isinstance(blocking, str):
        blocking = blocking.lower() in {"true", "1", "yes"}
    return severity, bool(blocking)


def render_pt_master(repository: Repository, profile_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    profile = resolve_profile(repository, profile_id)
    bindings = _binding_index(repository, profile_id)
    params = _parameter_map(repository)
    messages = _message_map(repository)
    governance = _governance_map(repository, profile_id)

    target_weights: dict[str, Any] = {}
    target_meta: dict[str, Any] = {}
    for tid in sorted(profile.target_settings):
        if not enabled_target(profile, tid):
            continue
        binding = bindings.get(tid)
        if not binding:
            continue
        setting = target_setting(profile, tid) or {}
        runtime_target = str(binding.get("runtime_target") or "")
        if not runtime_target:
            continue
        importance = setting.get("importance")
        if runtime_target in target_weights:
            try:
                target_weights[runtime_target] = max(float(target_weights[runtime_target]), float(importance))
                if target_weights[runtime_target].is_integer():
                    target_weights[runtime_target] = int(target_weights[runtime_target])
            except (TypeError, ValueError, AttributeError):
                target_weights[runtime_target] = importance
            existing = target_meta[runtime_target]
            existing.setdefault("validationTargetIds", [existing.pop("validationTargetId")])
            existing["validationTargetIds"].append(tid)
        else:
            target_weights[runtime_target] = importance
            target_meta[runtime_target] = {
                "validationTargetId": tid,
                "requirementLevel": setting.get("requirement_level"),
                "blockingOnPresenceFailure": setting.get("blocking_on_failure"),
                "defaultValue": setting.get("default_value"),
            }

    remarks: dict[str, Any] = {}
    enriched_remarks: dict[str, Any] = {}
    used_keys: set[str] = set()
    active_rule_ids = {
        str(r.get("rule_id"))
        for r in repository.rules
        if enabled_target(profile, str(r.get("validation_target_id")))
        and rule_enabled(profile, str(r.get("rule_id")))
    }

    for row in repository.constraints:
        constraint = dict(row.data)
        cid = str(constraint.get("constraint_id"))
        if str(constraint.get("rule_id")) not in active_rule_ids or not constraint_enabled(profile, cid):
            continue
        tid = str(constraint.get("validation_target_id"))
        binding = bindings.get(tid)
        if not binding:
            continue
        runtime_target = str(binding.get("runtime_target") or "")
        if not runtime_target:
            continue
        setting = target_setting(profile, tid) or {}
        key = _constraint_runtime_key(constraint)
        if key in used_keys:
            key = lower_camel([key, re.sub(r"[^A-Za-z0-9]", "", cid)])
        used_keys.add(key)

        localized = messages.get(cid, {})
        titles = {lang: item["title"] for lang, item in localized.items()}
        texts = {lang: item["message"] for lang, item in localized.items()}
        severity, blocking = _severity_and_blocking(profile, constraint, setting)
        points, include_in_score = constraint_weight(profile, constraint)
        if isinstance(points, float) and points.is_integer():
            points = int(points)
        requirement_ids = sorted(set(governance.get(str(constraint.get("rule_id")), []) + governance.get(cid, []) + governance.get(tid, [])))
        used_for_fair = any(_is_fair_requirement(repository, req) for req in requirement_ids)
        constraint_payload = dict(params.get(cid, {}))
        if constraint.get("resolver_id"):
            constraint_payload.setdefault("resolverId", constraint.get("resolver_id"))
        if constraint.get("vocabulary_id"):
            constraint_payload.setdefault("vocabularyId", constraint.get("vocabulary_id"))

        legacy_item: dict[str, Any] = {
            "title": titles,
            "message": texts,
            "target": runtime_target,
            "severity": severity,
            "dimension": constraint.get("assessment_dimension"),
            "blocking": blocking,
            "points": points if include_in_score else 0,
            "usedForFairCompliance": used_for_fair,
        }
        if constraint_payload:
            legacy_item["constraints"] = constraint_payload
        remarks[key] = legacy_item

        enriched_remarks[key] = {
            **legacy_item,
            "constraintId": cid,
            "ruleId": constraint.get("rule_id"),
            "validationTargetId": tid,
            "constraintType": constraint.get("constraint_type"),
            "weightKey": constraint.get("weight_key"),
            "includedInScore": include_in_score,
            "governanceRequirementIds": requirement_ids,
            "resolverId": constraint.get("resolver_id"),
            "vocabularyId": constraint.get("vocabulary_id"),
            "reviewRequired": bool(constraint.get("review_required")),
        }

    legacy = {
        "minimumRequiredScore": profile.profile.get("minimum_required_score"),
        "targetWeights": target_weights,
        "dataQualityRemarks": remarks,
    }
    enriched = {
        "profileId": profile_id,
        "profileVersion": profile.profile.get("version"),
        "minimumRequiredScore": profile.profile.get("minimum_required_score"),
        "scoringMethod": profile.profile.get("scoring_method"),
        "targetWeights": target_weights,
        "targets": target_meta,
        "dataQualityRemarks": enriched_remarks,
    }
    return legacy, enriched
