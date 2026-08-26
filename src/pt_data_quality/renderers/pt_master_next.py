from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Any

from ..model import Repository, Row
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
    constraint_parameter_rows,
    governance_by_constraint,
    message_map,
    runtime_parameter_map,
    typed_parameter_value,
)
from ..util import lower_camel
from .pt_master import _canonical_target_weights


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
_INACTIVE = {"RETIRED", "ARCHIVED", "DEPRECATED"}


def _active(row: Row | dict[str, Any]) -> bool:
    return str(row.get("status") or "ACTIVE").upper() not in _INACTIVE


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


def _bindings(repository: Repository, profile_id: str, artifact_type: str) -> defaultdict[str, list[dict[str, Any]]]:
    result: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in repository.implementation_bindings:
        if not _active(row):
            continue
        if str(row.get("implementation_id") or "") != "PT_MASTER":
            continue
        if str(row.get("representation") or "") != "RUNTIME_JSON":
            continue
        if str(row.get("artifact_type") or "").upper() != artifact_type.upper():
            continue
        scope = str(row.get("profile_scope") or "*")
        if scope not in {"*", profile_id}:
            continue
        result[str(row.get("artifact_id") or "")].append(dict(row.data))
    for rows in result.values():
        rows.sort(key=lambda r: (0 if str(r.get("profile_scope") or "*") == profile_id else 1, str(r.get("binding_id") or "")))
    return result


def _preferred_binding(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        return {}
    return sorted(
        rows,
        key=lambda r: (
            0 if str(r.get("compatibility_role") or "") == "BASELINE" else 1,
            0 if str(r.get("binding_mode") or "") == "EXPLICIT" else 1,
            str(r.get("binding_id") or ""),
        ),
    )[0]


def _implementation_runtime_rules(repository: Repository) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in repository.implementation_runtime_rules:
        if not _active(row):
            continue
        key = str(row.get("runtime_key") or "")
        if key:
            result[key] = dict(row.data)
    return result


def _implementation_runtime_parameters(repository: Repository) -> defaultdict[str, list[dict[str, Any]]]:
    result: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in repository.implementation_runtime_parameters:
        if not _active(row):
            continue
        key = str(row.get("runtime_key") or "")
        if key:
            result[key].append(dict(row.data))
    for rows in result.values():
        rows.sort(key=lambda r: (int(r.get("sequence") or 0), str(r.get("parameter_name") or "")))
    return result


def _java_support(
    constraint_bindings: list[dict[str, Any]],
    runtime_rules: dict[str, dict[str, Any]],
    runtime_parameters: dict[str, list[dict[str, Any]]],
    preview_key: str,
) -> dict[str, Any]:
    legacy_keys: list[str] = []
    required: list[str] = []
    config_only: list[str] = []
    contracts: dict[str, list[dict[str, Any]]] = {}
    for binding in constraint_bindings:
        key = str(binding.get("runtime_key") or "")
        if not key or key not in runtime_rules or key in legacy_keys:
            continue
        legacy_keys.append(key)
        if bool(runtime_rules[key].get("required_by_current_java")):
            required.append(key)
        else:
            config_only.append(key)
        contracts[key] = [
            {
                "name": p.get("parameter_name"),
                "type": p.get("java_contract_type") or p.get("value_type"),
            }
            for p in runtime_parameters.get(key, [])
            if not bool(p.get("additive_metadata"))
        ]

    if required:
        status = "LEGACY_SUPPORTED"
        comment = (
            "Current Java executes equivalent validation through the listed legacy runtime key(s). "
            "It does not yet execute the canonical 2.0.0 constraint model generically."
        )
    elif config_only:
        status = "LEGACY_CONFIG_ONLY"
        comment = (
            "Equivalent configuration exists in the current 1.x runtime, but DataQualityCalculator does not actively report it."
        )
    else:
        status = "NOT_SUPPORTED"
        comment = (
            "This canonical RSR constraint is not executed by the current Java data-quality engine. "
            "Java must be extended before this 2.0.0 rule becomes operational."
        )

    return {
        "status": status,
        "supportedByCurrentJava": bool(required),
        "legacyRuntimeKeys": legacy_keys,
        "legacyParameterContract": contracts,
        "previewRuntimeKey": preview_key,
        "comment": comment,
    }


def _resolver_definitions(repository: Repository) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in repository.resolvers:
        if not _active(row):
            continue
        rid = str(row.get("resolver_id") or "")
        if not rid:
            continue
        statuses: list[int] = []
        raw_statuses = str(row.get("accepted_status_codes") or "")
        for part in re.split(r"[;,\s]+", raw_statuses):
            if part.isdigit():
                statuses.append(int(part))
        item: dict[str, Any] = {
            "name": row.get("name"),
            "type": row.get("resolver_type"),
            "uriTemplate": row.get("uri_template"),
            "httpMethod": row.get("http_method"),
            "acceptedStatusCodes": statuses,
            "timeoutSeconds": row.get("timeout_seconds"),
        }
        if row.get("accept_header"):
            item["acceptHeader"] = row.get("accept_header")
        if row.get("review_required"):
            item["reviewRequired"] = True
        result[rid] = item
    return result


def _vocabulary_definitions(repository: Repository) -> dict[str, dict[str, Any]]:
    terms: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in repository.vocabulary_terms:
        if not _active(row):
            continue
        vid = str(row.get("vocabulary_id") or "")
        if not vid:
            continue
        terms[vid].append({
            "code": row.get("term_code"),
            "label": row.get("term_label"),
            "language": row.get("language"),
        })
    for rows in terms.values():
        rows.sort(key=lambda r: (str(r.get("code") or ""), str(r.get("language") or "")))

    result: dict[str, dict[str, Any]] = {}
    for row in repository.vocabularies:
        if not _active(row):
            continue
        vid = str(row.get("vocabulary_id") or "")
        if not vid:
            continue
        item: dict[str, Any] = {
            "name": row.get("name"),
            "description": row.get("description"),
            "type": row.get("vocabulary_type"),
        }
        if row.get("source_uri"):
            item["sourceUri"] = row.get("source_uri")
        if row.get("version_or_standard"):
            item["versionOrStandard"] = row.get("version_or_standard")
        if terms.get(vid):
            item["terms"] = terms[vid]
        if row.get("review_required"):
            item["reviewRequired"] = True
        result[vid] = item
    return result


def _parameter_definitions(repository: Repository) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    for cid, rows in constraint_parameter_rows(repository).items():
        defs: list[dict[str, Any]] = []
        for row in rows:
            item: dict[str, Any] = {
                "name": row.get("parameter_name"),
                "value": typed_parameter_value(row),
                "valueType": row.get("value_type"),
                "sequence": row.get("sequence"),
            }
            if row.get("combine_operator"):
                item["combineOperator"] = row.get("combine_operator")
            defs.append(item)
        result[cid] = defs
    return result


def render_pt_master_next(repository: Repository, profile_id: str) -> dict[str, Any]:
    """Render the future 2.0.0 PT Master configuration contract.

    It preserves the familiar 1.x fields while adding canonical RSR concepts
    needed for a future generic Java engine: all Constraints, typed parameter
    definitions, resolver/vocabulary registries, governance traceability and an
    explicit per-rule Java migration comment/status.
    """
    profile = resolve_profile(repository, profile_id)
    target_bindings = _bindings(repository, profile_id, "VALIDATION_TARGET")
    constraint_bindings = _bindings(repository, profile_id, "CONSTRAINT")
    compact_params = runtime_parameter_map(repository)
    parameter_defs = _parameter_definitions(repository)
    messages = message_map(repository)
    governance = governance_by_constraint(repository, profile_id)
    runtime_rules = _implementation_runtime_rules(repository)
    runtime_parameters = _implementation_runtime_parameters(repository)

    remarks: dict[str, Any] = {}
    used_keys: set[str] = set()
    support_counts: Counter[str] = Counter()

    for row in repository.constraints:
        constraint = dict(row.data)
        cid = str(constraint.get("constraint_id") or "")
        tid = str(constraint.get("validation_target_id") or "")
        if not cid or not tid or not _active(row):
            continue
        if not enabled_target(profile, tid) or not constraint_enabled(profile, cid):
            continue

        tb = _preferred_binding(target_bindings.get(tid, []))
        cbs = constraint_bindings.get(cid, [])
        cb = _preferred_binding(cbs)
        runtime_target = str(cb.get("runtime_target") or tb.get("runtime_target") or "")
        if not runtime_target:
            continue

        explicit_key = str(cb.get("runtime_key") or "")
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

        payload = dict(compact_params.get(cid, {}))
        if parameter_defs.get(cid):
            payload["parameterDefinitions"] = parameter_defs[cid]
        if constraint.get("resolver_id"):
            payload["resolverId"] = constraint.get("resolver_id")
        if constraint.get("vocabulary_id"):
            payload["vocabularyId"] = constraint.get("vocabulary_id")

        mapping_rows = governance.get(cid, [])
        java_support = _java_support(cbs, runtime_rules, runtime_parameters, key)
        support_counts[java_support["status"]] += 1

        item: dict[str, Any] = {
            "title": titles,
            "message": texts,
            "target": runtime_target,
            "severity": severity,
            "dimension": constraint.get("assessment_dimension"),
            "blocking": blocking,
            "points": points if include_in_score else 0,
            "usedForFairCompliance": bool(constraint.get("used_for_fair_compliance")),
            "constraintId": cid,
            "validationTargetId": tid,
            "constraintType": constraint.get("constraint_type"),
            "includedInScore": include_in_score,
            "javaSupport": java_support,
        }
        if payload:
            item["constraints"] = payload
        if mapping_rows:
            item["governance"] = {
                "dimensionIds": sorted({str(m.get("dimension_id")) for m in mapping_rows if m.get("dimension_id")}),
                "metricIds": sorted({str(m.get("metric_id")) for m in mapping_rows if m.get("metric_id")}),
                "requirementIds": sorted({str(m.get("requirement_id")) for m in mapping_rows if m.get("requirement_id")}),
                "mappingStatuses": sorted({str(m.get("mapping_status")) for m in mapping_rows if m.get("mapping_status")}),
            }
        remarks[key] = item

    return {
        "runtimeModelVersion": "2.0.0-preview",
        "minimumRequiredScore": profile.profile.get("minimum_required_score"),
        "dimensionDefinitions": assessment_dimension_definitions(repository),
        "targetWeights": _canonical_target_weights(repository, profile_id),
        "resolverDefinitions": _resolver_definitions(repository),
        "vocabularyDefinitions": _vocabulary_definitions(repository),
        "javaMigration": {
            "currentContract": "1.0.0",
            "statusCounts": dict(sorted(support_counts.items())),
            "comment": (
                "Rules marked LEGACY_SUPPORTED are already implemented through the 1.x hard-coded Java contract. "
                "LEGACY_CONFIG_ONLY entries exist in 1.x configuration but are not reported by the current calculator. "
                "NOT_SUPPORTED rules require Java implementation before they become operational."
            ),
        },
        "dataQualityRemarks": remarks,
    }
