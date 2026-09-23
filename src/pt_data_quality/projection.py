from __future__ import annotations

from collections import defaultdict
from typing import Any

from .model import Repository
from .profile import coerce_value


LANGUAGES = ("en", "sr", "sr-cyr", "pt")


def constraint_parameter_rows(repository: Repository) -> dict[str, list[dict[str, Any]]]:
    result: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in repository.constraint_parameters:
        result[str(row.get("constraint_id"))].append(dict(row.data))
    for rows in result.values():
        rows.sort(key=lambda r: (str(r.get("parameter_name")), int(r.get("sequence") or 0)))
    return result


def typed_parameter_value(row: dict[str, Any]) -> Any:
    return coerce_value(row.get("parameter_value"), str(row.get("value_type") or ""))


def runtime_parameter_map(repository: Repository) -> dict[str, dict[str, Any]]:
    """Resolve typed parameter rows into the compact PT Master runtime shape.

    Multiple rows for the same parameter are preserved through an explicit
    combine_operator. This function remains canonical: implementation-specific
    parameter aliases and transformations are represented separately in the
    PT Master compatibility sheets and are not folded back into the RSR model.
    """
    grouped: defaultdict[str, defaultdict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for row in repository.constraint_parameters:
        grouped[str(row.get("constraint_id"))][str(row.get("parameter_name"))].append(dict(row.data))

    result: dict[str, dict[str, Any]] = {}
    for cid, by_name in grouped.items():
        resolved: dict[str, Any] = {}
        for pname, rows in by_name.items():
            rows.sort(key=lambda r: int(r.get("sequence") or 0))
            values = [typed_parameter_value(r) for r in rows]
            ops = {str(r.get("combine_operator") or "").upper() for r in rows if r.get("combine_operator")}
            runtime_name = pname
            if len(values) == 1:
                resolved[runtime_name] = values[0]
            elif len(ops) == 1 and next(iter(ops)) in {"MIN", "MAX"}:
                op = next(iter(ops)).lower()
                resolved[runtime_name] = f"{op}({', '.join(str(v) for v in values)})"
            elif len(ops) == 1 and next(iter(ops)) in {"ALL", "ANY"}:
                op = next(iter(ops)).lower()
                resolved[runtime_name] = f"{op}({', '.join(str(v) for v in values)})"
            else:
                # Keep all values visible rather than silently overwriting data.
                resolved[runtime_name] = values
        result[cid] = resolved
    return result


def message_map(repository: Repository) -> dict[str, dict[str, dict[str, str]]]:
    result: dict[str, dict[str, dict[str, str]]] = {}
    for row in repository.messages:
        cid = str(row.get("constraint_id"))
        localized: dict[str, dict[str, str]] = {}
        for lang in LANGUAGES:
            suffix = lang.replace("-", "_")
            title = row.get(f"title_{suffix}")
            message = row.get(f"message_{suffix}")
            if title not in (None, "") or message not in (None, ""):
                localized[lang] = {"title": str(title or ""), "message": str(message or "")}
        result[cid] = localized
    return result


def english_messages(repository: Repository) -> dict[str, str]:
    return {cid: loc.get("en", {}).get("message", "") for cid, loc in message_map(repository).items()}


def governance_by_constraint(repository: Repository, profile_id: str) -> dict[str, list[dict[str, Any]]]:
    result: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in repository.governance_mappings:
        scope = str(row.get("profile_id") or "*")
        if scope not in {"*", profile_id}:
            continue
        result[str(row.get("constraint_id"))].append(dict(row.data))
    return result


def implementation_bindings(
    repository: Repository,
    profile_id: str,
    artifact_type: str,
    representation: str = "RUNTIME_JSON",
    implementation_id: str = "PT_MASTER",
) -> dict[str, dict[str, Any]]:
    generic: dict[str, dict[str, Any]] = {}
    specific: dict[str, dict[str, Any]] = {}
    artifact_type = artifact_type.upper()
    for row in repository.implementation_bindings:
        if row.get("implementation_id") != implementation_id:
            continue
        if str(row.get("artifact_type") or "").upper() != artifact_type:
            continue
        if row.get("representation") != representation:
            continue
        if str(row.get("status") or "").upper() in {"RETIRED", "ARCHIVED", "DEPRECATED"}:
            continue
        scope = str(row.get("profile_scope") or "*")
        if scope not in {"*", profile_id}:
            continue
        target = specific if scope == profile_id else generic
        target[str(row.get("artifact_id"))] = dict(row.data)
    return {**generic, **specific}


def assessment_dimension_definitions(repository: Repository) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for row in repository.assessment_dimensions:
        did = str(row.get("assessment_dimension_id"))
        if str(row.get("status") or "").upper() in {"RETIRED", "ARCHIVED", "DEPRECATED"}:
            continue
        result[did] = {
            "sr": str(row.get("description_sr") or ""),
            "sr-cyr": str(row.get("description_sr_cyr") or ""),
            "en": str(row.get("description_en") or ""),
            "pt": str(row.get("description_pt") or ""),
        }
    return result


def governance_dimension_key(dimension_id: str | None) -> str:
    """Convert canonical PTCRIS governance dimension IDs to runtime enum keys.

    Example: ``PTCRIS.STRUCTURAL_CONSISTENCY`` -> ``STRUCTURAL_CONSISTENCY``.
    """
    value = str(dimension_id or "").strip()
    return value.split(".", 1)[1] if value.startswith("PTCRIS.") else value


def governance_dimension_definitions(
    repository: Repository,
    runtime_contract: dict[str, Any] | None = None,
) -> dict[str, dict[str, str]]:
    """Render the seven PTCRIS Data Governance dimensions for runtime JSON.

    The RSR Governance Dimensions sheet is authoritative for the dimension set and
    English semantics. The current Java contract is used as a localization source
    for Serbian, Serbian Cyrillic and Portuguese descriptions when available.
    """
    contract_defs = (runtime_contract or {}).get("dimensionDefinitions", {})
    result: dict[str, dict[str, str]] = {}
    for row in repository.governance_dimensions:
        if str(row.get("status") or "").upper() in {"RETIRED", "ARCHIVED", "DEPRECATED"}:
            continue
        key = governance_dimension_key(str(row.get("dimension_id") or ""))
        if not key:
            continue
        fallback = str(row.get("description") or "")
        localized = contract_defs.get(key, {}) if isinstance(contract_defs, dict) else {}
        result[key] = {
            "sr": str(localized.get("sr") or fallback),
            "sr-cyr": str(localized.get("sr-cyr") or fallback),
            "en": str(localized.get("en") or fallback),
            "pt": str(localized.get("pt") or fallback),
        }
    return result


def primary_governance_mapping(
    repository: Repository,
    profile_id: str,
    constraint_id: str,
    preferred_runtime_dimension: str | None = None,
) -> dict[str, Any] | None:
    """Select one deterministic primary governance mapping for runtime scoring.

    All mappings remain available in the future runtime ``governance`` block. The
    primary mapping is only needed because the existing Java rule DTO exposes one
    ``dimension`` value. If the current Java contract dimension is one of the
    canonical mappings, it is preferred to minimize unnecessary runtime churn.
    Otherwise we prefer authoritative, complete and non-review mappings.
    """
    rows: list[dict[str, Any]] = []
    for row in repository.governance_mappings:
        if str(row.get("constraint_id") or "") != constraint_id:
            continue
        if str(row.get("profile_id") or "*") not in {"*", profile_id}:
            continue
        item = dict(row.data)
        if not item.get("dimension_id") and item.get("metric_id"):
            metric = repository.governance_metrics_by_id.get(str(item.get("metric_id")))
            if metric and metric.get("dimension_id"):
                item["dimension_id"] = metric.get("dimension_id")
        if item.get("dimension_id"):
            rows.append(item)
    if not rows:
        return None

    preferred = str(preferred_runtime_dimension or "").upper()
    if preferred:
        preferred_rows = [
            row for row in rows
            if governance_dimension_key(row.get("dimension_id")).upper() == preferred
        ]
        if preferred_rows:
            rows = preferred_rows

    status_rank = {
        "FULL": 0,
        "DIMENSION_AND_METRIC": 1,
        "DIMENSION_ONLY": 2,
        "METRIC_ONLY": 3,
        "UNMAPPED": 4,
    }

    def rank(row: dict[str, Any]) -> tuple[Any, ...]:
        basis = str(row.get("mapping_basis") or "")
        authoritative = 0 if basis.startswith("AUTHORITATIVE_GOVERNANCE") else 1
        review = 1 if bool(row.get("review_required")) else 0
        return (
            authoritative,
            review,
            status_rank.get(str(row.get("mapping_status") or "").upper(), 9),
            str(row.get("mapping_id") or ""),
        )

    return sorted(rows, key=rank)[0]


def governance_runtime_dimension(
    repository: Repository,
    profile_id: str,
    constraint_ids: list[str],
    preferred_runtime_dimension: str | None = None,
) -> str | None:
    """Resolve the single PTCRIS governance dimension expected by Java."""
    preferred = str(preferred_runtime_dimension or "").upper()
    mappings: list[dict[str, Any]] = []
    for cid in constraint_ids:
        mapping = primary_governance_mapping(
            repository, profile_id, cid, preferred_runtime_dimension=preferred or None
        )
        if mapping:
            mappings.append(mapping)

    if preferred and any(
        governance_dimension_key(m.get("dimension_id")).upper() == preferred for m in mappings
    ):
        return preferred
    if mappings:
        return governance_dimension_key(mappings[0].get("dimension_id"))
    return preferred or None
