from __future__ import annotations

import re
from collections import defaultdict
from typing import Any

from ..model import Repository, Row
from ..profile import (
    coerce_value,
    constraint_severity_and_blocking,
    constraint_weight,
    enabled_target,
    resolve_profile,
    target_setting,
)
from ..projection import (
    assessment_dimension_definitions,
    constraint_parameter_rows,
    message_map,
    runtime_parameter_map,
    typed_parameter_value,
)


_INACTIVE = {"RETIRED", "ARCHIVED", "DEPRECATED"}
_SEVERITY_RANK = {"INFO": 0, "WARNING": 1, "ERROR": 2}

# Portuguese fallback text is needed only for legacy-only or N:M runtime rules
# for which there is no single canonical RSR Message that can be reused safely.
# Canonically bound 1:1 rules take all four languages directly from Messages.
_LEGACY_PT: dict[str, tuple[str, str]] = {
    "invalidDocumentDateFormat": ("Formato de data de publicação inválido", 'A data de publicação "{0}" no registo de resultado não está num formato válido.'),
    "defenceTooFarInFuture": ("Data de defesa demasiado distante no futuro", "A data de defesa da tese ({0}) pode estar, no máximo, {1} anos no futuro."),
    "dateRequestedInvalid": ("Formato inválido da data do pedido", "O campo da data do pedido está num formato inválido. Embora este campo não seja obrigatório, o seu preenchimento é recomendado."),
    "dateFilingPriorityInvalid": ("Formato inválido da data de prioridade", "O campo da data de prioridade está num formato inválido. Embora este campo não seja obrigatório, o seu preenchimento é recomendado."),
    "dateEndTermInvalid": ("Formato inválido da data de fim de vigência", "O campo da data de fim de vigência está num formato inválido. Embora este campo não seja obrigatório, o seu preenchimento é recomendado."),
    "numberOfPagesBelowMinimum": ("Número de páginas abaixo do mínimo", "O número de páginas ({0}) no registo de tese deve ser superior ou igual a {1}."),
    "numberOfPagesAboveMaximum": ("Número de páginas acima do máximo", "O número de páginas ({0}) no registo de tese deve ser inferior ou igual a {1}."),
    "firstNameMissing": ("Nome próprio em falta", "O nome próprio está em falta no registo da pessoa."),
    "birthDateInFuture": ("Data de nascimento no futuro", "A data de nascimento ({0}) no registo da pessoa não pode estar no futuro."),
    "documentBeforePersonBirth": ("Data do documento anterior ao nascimento da pessoa", "A data do documento associado à contribuição ({1} - {2}) não pode ser anterior à data de nascimento da pessoa associada."),
    "activityStartDateMissing": ("Data de início da atividade em falta", "A data de início da atividade ({1} - {2}) não foi indicada. Embora o campo não seja obrigatório, o seu preenchimento é recomendado."),
    "activityStartDateBefore": ("Data de início da atividade anterior ao ano configurado", "A data de início da atividade ({0}) na atividade ({2} - {3}) não pode ser anterior ao ano {1}."),
    "activityStartDateBeforeMinAge": ("Data de início da atividade anterior à idade mínima da pessoa", "A data de início da atividade ({0}) na atividade ({3} - {4}) não pode ser anterior ao momento em que a pessoa associada completou {2} anos (data de nascimento: {1})."),
    "activityStartDateTooFarInFuture": ("Data de início da atividade demasiado distante no futuro", "A data de início da atividade ({0}) na atividade ({2} - {3}) pode estar, no máximo, {1} anos no futuro."),
    "activityEndDateMissing": ("Data de fim da atividade em falta", "A data de fim da atividade ({1} - {2}) não foi indicada. Embora o campo não seja obrigatório, o seu preenchimento é recomendado."),
    "activityEndDateBeforeStartDate": ("Data de fim da atividade anterior à data de início", "A data de fim da atividade ({0}) na atividade ({2} - {3}) não pode ser anterior à data de início da atividade ({1})."),
    "activityResearchAreasMissing": ("Áreas de investigação da atividade em falta", "Nenhuma área de investigação está associada ao registo da atividade ({1} - {2}). Embora o campo não seja obrigatório, o seu preenchimento é recomendado."),
    "identifierValueMissing": ("Valor do identificador em falta", "O campo do valor do identificador está em falta. O campo é obrigatório."),
    "identifierValueTooLong": ("Valor do identificador demasiado longo", 'O valor do identificador "{0}" excede o comprimento máximo permitido de {1} caracteres.'),
    "identifierTypeMissing": ("Tipo de identificador em falta", "O campo do tipo de identificador está em falta. O campo é obrigatório."),
    "identifierTypeTooLong": ("Tipo de identificador demasiado longo", 'O tipo de identificador "{0}" excede o comprimento máximo permitido de {1} caracteres.'),
    "identifierUriTooLong": ("URI do identificador demasiado longo", 'O URI do identificador "{0}" excede o comprimento máximo permitido de {1} caracteres.'),
    "invalidIdentifierUriFormat": ("Formato do URI do identificador inválido", 'O URI do identificador "{0}" não está num formato válido.'),
    "latitudeOutOfRange": ("Latitude fora do intervalo", "A latitude ({0}) deve estar entre {1} e {2}."),
    "longitudeOutOfRange": ("Longitude fora do intervalo", "A longitude ({0}) deve estar entre {1} e {2}."),
    "addressTooLong": ("Endereço demasiado longo", 'O endereço "{0}" excede o comprimento máximo permitido de {1} caracteres.'),
    "invalidAddressFormat": ("Formato de endereço inválido", 'O endereço "{0}" não está num formato válido.'),
    "contactWebsiteTooLong": ("URL do sítio Web demasiado longo", 'O URL do sítio Web "{0}" excede o comprimento máximo permitido de {1} caracteres.'),
    "invalidContactWebsiteFormat": ("Formato do URL do sítio Web inválido", 'O URL do sítio Web "{0}" não está num formato válido.'),
    "invalidResearchAreaNameFormat": ("Formato do nome da área de investigação inválido", 'O nome da área de investigação "{0}" não está num formato válido.'),
    "researchAreaUriTooLong": ("URI da área de investigação demasiado longo", 'O URI da área de investigação "{0}" excede o comprimento máximo permitido de {1} caracteres.'),
    "invalidResearchAreaUriFormat": ("Formato do URI da área de investigação inválido", 'O URI da área de investigação "{0}" não está num formato válido.'),
    "duplicateResearchAreaUri": ("URI da área de investigação duplicado", 'O URI da área de investigação "{0}" deve ser único.'),
    "countryCodeInvalidLength": ("Comprimento inválido do código do país", 'O código do país "{0}" deve conter exatamente {1} caracteres.'),
    "invalidCountryCodeFormat": ("Formato do código do país inválido", 'O código do país "{0}" não está num formato válido. É esperado um código de país ISO 3166-1 alfa-2 em minúsculas.'),
    "countryNameMissing": ("Nome do país em falta", "O campo do nome do país está em falta. O campo é obrigatório."),
    "countryNameTooLong": ("Nome do país demasiado longo", 'O nome do país "{0}" excede o comprimento máximo permitido de {1} caracteres.'),
    "invalidCountryNameFormat": ("Formato do nome do país inválido", 'O nome do país "{0}" não está num formato válido.'),
}


def _active(row: Row | dict[str, Any]) -> bool:
    return str(row.get("status") or "ACTIVE").upper() not in _INACTIVE


def _implementation_profile(repository: Repository, profile_id: str) -> Row | None:
    candidates: list[tuple[int, int, Row]] = []
    for row in repository.implementation_profiles:
        if not _active(row) or str(row.get("implementation_id") or "") != "PT_MASTER":
            continue
        scope = str(row.get("profile_scope") or "*")
        if scope not in {"*", profile_id}:
            continue
        candidates.append((1 if scope == profile_id else 0, -row.row_number, row))
    return max(candidates, key=lambda item: (item[0], item[1]))[2] if candidates else None


def _runtime_rows(repository: Repository, implementation_profile_id: str, rows: list[Row]) -> list[Row]:
    selected = [
        row for row in rows
        if _active(row) and str(row.get("implementation_profile_id") or "") == implementation_profile_id
    ]
    selected.sort(key=lambda r: (int(r.get("sequence") or 0), r.row_number))
    return selected


def _bindings_by_runtime_key(repository: Repository, profile_id: str, artifact_type: str) -> defaultdict[str, list[dict[str, Any]]]:
    result: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in repository.implementation_bindings:
        if not _active(row) or str(row.get("implementation_id") or "") != "PT_MASTER":
            continue
        if str(row.get("artifact_type") or "").upper() != artifact_type.upper():
            continue
        if str(row.get("representation") or "") != "RUNTIME_JSON":
            continue
        scope = str(row.get("profile_scope") or "*")
        if scope not in {"*", profile_id}:
            continue
        key = str(row.get("runtime_key") or "")
        if key:
            result[key].append(dict(row.data))
    for rows in result.values():
        rows.sort(key=lambda r: (str(r.get("artifact_id") or ""), str(r.get("binding_id") or "")))
    return result


def _target_bindings(repository: Repository, profile_id: str) -> dict[str, dict[str, Any]]:
    generic: dict[str, dict[str, Any]] = {}
    specific: dict[str, dict[str, Any]] = {}
    for row in repository.implementation_bindings:
        if not _active(row) or str(row.get("implementation_id") or "") != "PT_MASTER":
            continue
        if str(row.get("artifact_type") or "").upper() != "VALIDATION_TARGET":
            continue
        if str(row.get("representation") or "") != "RUNTIME_JSON":
            continue
        scope = str(row.get("profile_scope") or "*")
        if scope not in {"*", profile_id}:
            continue
        target = specific if scope == profile_id else generic
        target[str(row.get("artifact_id") or "")] = dict(row.data)
    return {**generic, **specific}


def _canonical_target_weights(repository: Repository, profile_id: str) -> dict[str, Any]:
    profile = resolve_profile(repository, profile_id)
    bindings = _target_bindings(repository, profile_id)
    result: dict[str, Any] = {}
    for tid in sorted(profile.target_settings):
        if not enabled_target(profile, tid):
            continue
        binding = bindings.get(tid) or {}
        runtime_target = str(binding.get("runtime_target") or "")
        if not runtime_target:
            continue
        importance = (target_setting(profile, tid) or {}).get("importance")
        if runtime_target not in result:
            result[runtime_target] = importance
            continue
        try:
            value = max(float(result[runtime_target]), float(importance))
            result[runtime_target] = int(value) if value.is_integer() else value
        except (TypeError, ValueError, AttributeError):
            result[runtime_target] = importance
    return result


def _fallback_localized(runtime_row: Row, key: str) -> tuple[dict[str, str], dict[str, str]]:
    pt_title, pt_message = _LEGACY_PT.get(key, (str(runtime_row.get("title_en") or ""), str(runtime_row.get("message_en") or "")))
    return (
        {
            "sr": str(runtime_row.get("title_sr") or ""),
            "sr-cyr": str(runtime_row.get("title_sr_cyr") or ""),
            "en": str(runtime_row.get("title_en") or ""),
            "pt": pt_title,
        },
        {
            "sr": str(runtime_row.get("message_sr") or ""),
            "sr-cyr": str(runtime_row.get("message_sr_cyr") or ""),
            "en": str(runtime_row.get("message_en") or ""),
            "pt": pt_message,
        },
    )


def _bound_constraint_ids(repository: Repository, bindings: list[dict[str, Any]]) -> list[str]:
    result: list[str] = []
    for binding in bindings:
        cid = str(binding.get("artifact_id") or "")
        if cid and cid in repository.constraints_by_id and cid not in result:
            result.append(cid)
    return result


def _canonical_semantics(repository: Repository, profile_id: str, cids: list[str], runtime_row: Row) -> tuple[str, str, bool, Any, bool]:
    if not cids:
        return (
            str(runtime_row.get("severity") or "WARNING"),
            str(runtime_row.get("assessment_dimension") or "VALIDITY"),
            bool(runtime_row.get("blocking")),
            runtime_row.get("points"),
            bool(runtime_row.get("used_for_fair_compliance")),
        )

    profile = resolve_profile(repository, profile_id)
    severities: list[str] = []
    dimensions: list[str] = []
    blockings: list[bool] = []
    points: list[float] = []
    fair: list[bool] = []
    for cid in cids:
        row = repository.constraints_by_id[cid]
        constraint = dict(row.data)
        tid = str(constraint.get("validation_target_id") or "")
        setting = target_setting(profile, tid) or {}
        severity, blocking = constraint_severity_and_blocking(profile, constraint, setting)
        weight, included = constraint_weight(profile, constraint)
        severities.append(severity)
        dimensions.append(str(constraint.get("assessment_dimension") or runtime_row.get("assessment_dimension") or "VALIDITY"))
        blockings.append(blocking)
        points.append(float(weight) if included else 0.0)
        fair.append(bool(constraint.get("used_for_fair_compliance")))

    severity = max(severities, key=lambda s: _SEVERITY_RANK.get(str(s).upper(), -1))
    dimension = dimensions[0] if len(set(dimensions)) == 1 else str(runtime_row.get("assessment_dimension") or dimensions[0])
    score = max(points) if points else 0.0
    score_value: Any = int(score) if float(score).is_integer() else score
    return severity, dimension, any(blockings), score_value, any(fair)


def _compact_canonical_parameters(repository: Repository) -> dict[str, dict[str, Any]]:
    return runtime_parameter_map(repository)


def _raw_parameter_rows(repository: Repository) -> dict[str, list[dict[str, Any]]]:
    return constraint_parameter_rows(repository)


def _parse_year_offset(value: Any) -> int | None:
    match = re.search(r"\+\s*(\d+)\s*years?", str(value), flags=re.IGNORECASE)
    return int(match.group(1)) if match else None


def _parse_year(value: Any) -> int | None:
    match = re.search(r"\b(18|19|20|21)\d{2}\b", str(value))
    return int(match.group(0)) if match else None


def _transform_parameter(
    repository: Repository,
    compact: dict[str, dict[str, Any]],
    raw: dict[str, list[dict[str, Any]]],
    binding: dict[str, Any],
) -> Any:
    cid = str(binding.get("artifact_id") or "")
    canonical_name = str(binding.get("parameter_name") or "")
    transform = str(binding.get("runtime_value_transform") or "IDENTITY").upper()
    if transform == "RESOLVER_IDENTITY":
        return None  # 2.0.0-only concept

    value = (compact.get(cid) or {}).get(canonical_name)
    rows = [r for r in raw.get(cid, []) if str(r.get("parameter_name") or "") == canonical_name]

    if transform in {"", "IDENTITY", "FIXED_LENGTH_FROM_BOUNDS"}:
        return value
    if transform in {"DATE_OR_EXPRESSION_TO_YEAR", "SELECT_DATE_LITERAL_YEAR"}:
        for row in rows:
            if str(row.get("value_type") or "").upper() == "DATE":
                year = _parse_year(typed_parameter_value(row))
                if year is not None:
                    return year
        return _parse_year(value)
    if transform == "CURRENT_DATE_OFFSET_TO_YEARS":
        return _parse_year_offset(value)
    if transform == "SELECT_REFERENCE_OFFSET_YEARS":
        for row in rows:
            if str(row.get("value_type") or "").upper() == "EXPRESSION":
                offset = _parse_year_offset(typed_parameter_value(row))
                if offset is not None:
                    return offset
        return _parse_year_offset(value)
    if transform == "EXPLICIT_RUNTIME_BASELINE":
        return None
    return value


def _coerce_java_contract(value: Any, contract_type: str | None) -> Any:
    if value is None:
        return None
    kind = str(contract_type or "").upper()
    try:
        if kind == "INTEGER":
            return int(value)
        if kind == "DECIMAL":
            return float(value)
        if kind == "BOOLEAN":
            if isinstance(value, bool):
                return value
            return str(value).strip().lower() in {"true", "1", "yes"}
        if kind == "STRING":
            return str(value)
    except (TypeError, ValueError):
        return value
    return value


def _current_java_parameters(repository: Repository, profile_id: str, implementation_profile_id: str) -> dict[str, dict[str, Any]]:
    # Start from the current Java parameter contract so every hard-coded lookup
    # remains present and type-compatible. Canonical RSR values then replace the
    # baseline values where an explicit parameter binding/transform exists.
    result: defaultdict[str, dict[str, Any]] = defaultdict(dict)
    contract_type: dict[tuple[str, str], str | None] = {}
    for row in _runtime_rows(repository, implementation_profile_id, repository.implementation_runtime_parameters):
        if bool(row.get("additive_metadata")):
            continue
        key = str(row.get("runtime_key") or "")
        name = str(row.get("parameter_name") or "")
        if not key or not name:
            continue
        result[key][name] = coerce_value(row.get("parameter_value"), str(row.get("value_type") or ""))
        contract_type[(key, name)] = row.get("java_contract_type") or row.get("value_type")

    compact = _compact_canonical_parameters(repository)
    raw = _raw_parameter_rows(repository)
    parameter_bindings = _bindings_by_runtime_key(repository, profile_id, "PARAMETER")
    for key, bindings in parameter_bindings.items():
        for binding in bindings:
            if str(binding.get("compatibility_role") or "") == "ADDITIVE_METADATA":
                continue
            runtime_name = str(binding.get("runtime_parameter_name") or "")
            if not runtime_name:
                continue
            value = _transform_parameter(repository, compact, raw, binding)
            if value is None:
                continue
            result[key][runtime_name] = _coerce_java_contract(value, contract_type.get((key, runtime_name)))
    return dict(result)


def _render_current_java_pt_master(repository: Repository, profile_id: str, implementation_profile: Row) -> tuple[dict[str, Any], dict[str, Any]]:
    """Generate the improved 1.0.0 runtime for the *current* Java code.

    Compatibility means the current Java DTO, hard-coded runtime keys, targets,
    and expected constraint parameter names/types continue to work. Content is
    intentionally refreshed from the RSR: four-language messages, DQP
    severity/blocking/scoring and canonical values are used wherever a stable
    canonical binding exists. Future-only concepts such as generic resolvers and
    vocabularies are not emitted here.
    """
    profile = resolve_profile(repository, profile_id)
    impl_id = str(implementation_profile.get("implementation_profile_id") or "")
    messages = message_map(repository)
    constraint_bindings = _bindings_by_runtime_key(repository, profile_id, "CONSTRAINT")
    parameters = _current_java_parameters(repository, profile_id, impl_id)

    remarks: dict[str, Any] = {}
    trace: dict[str, Any] = {}
    for runtime_row in _runtime_rows(repository, impl_id, repository.implementation_runtime_rules):
        if runtime_row.get("include_in_runtime") is False:
            continue
        key = str(runtime_row.get("runtime_key") or "")
        if not key:
            continue
        cids = _bound_constraint_ids(repository, constraint_bindings.get(key, []))

        # A 1:1 canonical mapping can safely use the new canonical messages. For
        # N:M and legacy-only rules the old runtime wording remains the semantic
        # contract, with a Portuguese fallback added for UI completeness.
        if len(cids) == 1 and cids[0] in messages:
            localized = messages[cids[0]]
            title = {lang: localized[lang]["title"] for lang in ("sr", "sr-cyr", "en", "pt") if lang in localized}
            message = {lang: localized[lang]["message"] for lang in ("sr", "sr-cyr", "en", "pt") if lang in localized}
            message_source = "CANONICAL_RSR"
        else:
            title, message = _fallback_localized(runtime_row, key)
            message_source = "LEGACY_RUNTIME_FALLBACK"

        severity, dimension, blocking, points, fair = _canonical_semantics(
            repository, profile_id, cids, runtime_row
        )
        item: dict[str, Any] = {
            "title": title,
            "message": message,
            "target": runtime_row.get("runtime_target"),
            "severity": severity,
            "dimension": dimension,
            "blocking": blocking,
            "points": points,
            "usedForFairCompliance": fair,
        }
        if parameters.get(key):
            item["constraints"] = dict(parameters[key])
        remarks[key] = item
        trace[key] = {
            "runtimeKey": key,
            "requiredByCurrentJava": bool(runtime_row.get("required_by_current_java")),
            "canonicalConstraintIds": cids,
            "messageSource": message_source,
        }

    current = {
        "minimumRequiredScore": profile.profile.get("minimum_required_score"),
        "dimensionDefinitions": assessment_dimension_definitions(repository),
        "targetWeights": _canonical_target_weights(repository, profile_id),
        "dataQualityRemarks": remarks,
    }
    enriched = {
        "profileId": profile_id,
        "profileVersion": profile.profile.get("version"),
        "implementationProfileId": impl_id,
        "compatibilityMode": "CURRENT_JAVA_RSR_COMPATIBLE",
        "minimumRequiredScore": profile.profile.get("minimum_required_score"),
        "dimensionDefinitions": assessment_dimension_definitions(repository),
        "targetWeights": current["targetWeights"],
        "dataQualityRemarks": trace,
    }
    return current, enriched


def render_pt_master(repository: Repository, profile_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    implementation_profile = _implementation_profile(repository, profile_id)
    if implementation_profile is None:
        raise ValueError(
            "PT Master 1.0.0 generation requires an explicit Implementation Profile so current Java runtime keys/parameters are known."
        )
    return _render_current_java_pt_master(repository, profile_id, implementation_profile)
