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
