from __future__ import annotations

from typing import Any

from .model import EffectiveProfile, Repository


def as_bool(value: Any, default: bool = False) -> bool:
    if value is None or value == "":
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def coerce_value(value: Any, value_type: str | None = None) -> Any:
    if value is None:
        return None
    kind = str(value_type or "").upper()
    if kind in {"INTEGER", "INT"}:
        try:
            return int(value)
        except (TypeError, ValueError):
            return value
    if kind in {"NUMBER", "FLOAT", "DECIMAL"}:
        try:
            return float(value)
        except (TypeError, ValueError):
            return value
    if kind in {"BOOLEAN", "BOOL"}:
        return as_bool(value)
    if kind == "NULL":
        return None
    return value


def resolve_profile(repository: Repository, profile_id: str) -> EffectiveProfile:
    profiles = repository.profiles_by_id
    if profile_id not in profiles:
        raise KeyError(f"Unknown profile: {profile_id}")

    chain: list[str] = []
    seen: set[str] = set()
    current = profile_id
    while current:
        if current in seen:
            raise ValueError(f"Profile inheritance cycle detected at {current}")
        seen.add(current)
        chain.append(current)
        row = profiles.get(current)
        if row is None:
            raise KeyError(f"Unknown base profile: {current}")
        current = str(row.get("base_profile_id") or "").strip()
    chain.reverse()

    profile_data: dict[str, Any] = {}
    target_settings: dict[str, dict[str, Any]] = {}
    constraint_defaults: dict[str, dict[str, Any]] = {}
    overrides: dict[str, dict[str, Any]] = {}

    for pid in chain:
        profile_data.update(profiles[pid].data)
        for row in repository.profile_target_settings:
            if row.get("profile_id") == pid:
                target_settings[str(row.get("validation_target_id"))] = dict(row.data)
        for row in repository.profile_constraint_defaults:
            if row.get("profile_id") == pid:
                constraint_defaults[str(row.get("weight_key"))] = dict(row.data)
        for row in repository.profile_overrides:
            if row.get("profile_id") != pid:
                continue
            cid = str(row.get("constraint_id") or "")
            if not cid:
                continue
            overrides.setdefault(cid, {})[str(row.get("property_name"))] = coerce_value(
                row.get("property_value"), row.get("value_type")
            )

    return EffectiveProfile(
        profile_id=profile_id,
        profile=profile_data,
        target_settings=target_settings,
        constraint_defaults=constraint_defaults,
        overrides=overrides,
    )


def enabled_target(profile: EffectiveProfile, target_id: str) -> bool:
    setting = profile.target_settings.get(target_id)
    return bool(setting) and as_bool(setting.get("enabled"), True)


def target_setting(profile: EffectiveProfile, target_id: str) -> dict[str, Any] | None:
    setting = profile.target_settings.get(target_id)
    return dict(setting) if setting else None


def constraint_enabled(profile: EffectiveProfile, constraint_id: str) -> bool:
    return as_bool(profile.override_for(constraint_id).get("enabled"), True)


def constraint_weight(profile: EffectiveProfile, constraint: dict[str, Any]) -> tuple[float, bool]:
    cid = str(constraint.get("constraint_id") or "")
    override = profile.override_for(cid)
    default = profile.constraint_defaults.get(str(constraint.get("weight_key"))) or {}
    include = as_bool(override.get("include_in_score", default.get("include_in_score")), False)
    raw = override.get("weight", default.get("weight"))
    if raw in (None, ""):
        return 0.0, include
    try:
        return float(raw), include
    except (TypeError, ValueError):
        return 0.0, include


def presence_severity(requirement_level: str | None) -> str:
    return {
        "MANDATORY": "ERROR",
        "RECOMMENDED": "WARNING",
        "OPTIONAL": "INFO",
    }.get(str(requirement_level or "").upper(), "WARNING")


def presence_blocking(profile: EffectiveProfile, requirement_level: str | None) -> bool:
    field = {
        "MANDATORY": "mandatory_failure_blocks",
        "RECOMMENDED": "recommended_failure_blocks",
        "OPTIONAL": "optional_failure_blocks",
    }.get(str(requirement_level or "").upper())
    return as_bool(profile.profile.get(field), False) if field else False


def constraint_severity_and_blocking(
    profile: EffectiveProfile,
    constraint: dict[str, Any],
    setting: dict[str, Any],
) -> tuple[str, bool]:
    cid = str(constraint.get("constraint_id") or "")
    override = profile.override_for(cid)
    default = profile.constraint_defaults.get(str(constraint.get("weight_key"))) or {}
    basis = str(default.get("behavior_basis") or "FIXED").upper()

    if basis == "TARGET_REQUIREMENT_LEVEL":
        severity = presence_severity(setting.get("requirement_level"))
        blocking = presence_blocking(profile, setting.get("requirement_level"))
    else:
        severity = str(default.get("default_severity") or "ERROR")
        blocking = as_bool(default.get("default_blocking"), True)

    if override.get("severity") not in (None, ""):
        severity = str(override.get("severity"))
    if override.get("blocking") not in (None, ""):
        blocking = as_bool(override.get("blocking"), blocking)
    return severity, blocking
