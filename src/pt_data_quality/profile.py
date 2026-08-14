from __future__ import annotations

from typing import Any

from .model import EffectiveProfile, Repository


def _as_bool(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def _coerce(value: Any, value_type: str | None = None) -> Any:
    if value_type:
        kind = value_type.upper()
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
            return _as_bool(value)
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
    overrides: dict[tuple[str, str], dict[str, Any]] = {}

    for pid in chain:
        profile_data.update(profiles[pid].data)
        for row in repository.profile_target_settings:
            if row.get("profile_id") != pid:
                continue
            target_settings[str(row.get("validation_target_id"))] = dict(row.data)
        for row in repository.profile_constraint_defaults:
            if row.get("profile_id") != pid:
                continue
            constraint_defaults[str(row.get("weight_key"))] = dict(row.data)
        for row in repository.profile_overrides:
            if row.get("profile_id") != pid:
                continue
            key = (str(row.get("artifact_type") or "").upper(), str(row.get("artifact_id") or ""))
            overrides.setdefault(key, {})[str(row.get("property"))] = _coerce(row.get("value"), row.get("value_type"))

    return EffectiveProfile(
        profile_id=profile_id,
        profile=profile_data,
        target_settings=target_settings,
        constraint_defaults=constraint_defaults,
        overrides=overrides,
    )


def enabled_target(profile: EffectiveProfile, target_id: str) -> bool:
    setting = profile.target_settings.get(target_id)
    if not setting:
        return False
    override = profile.override_for("TARGET", target_id)
    if "enabled" in override:
        return _as_bool(override["enabled"])
    return _as_bool(setting.get("enabled"), True)


def target_setting(profile: EffectiveProfile, target_id: str) -> dict[str, Any] | None:
    setting = profile.target_settings.get(target_id)
    if not setting:
        return None
    result = dict(setting)
    result.update(profile.override_for("TARGET", target_id))
    return result


def rule_enabled(profile: EffectiveProfile, rule_id: str) -> bool:
    override = profile.override_for("RULE", rule_id)
    return _as_bool(override.get("enabled"), True)


def constraint_enabled(profile: EffectiveProfile, constraint_id: str) -> bool:
    override = profile.override_for("CONSTRAINT", constraint_id)
    return _as_bool(override.get("enabled"), True)


def constraint_weight(profile: EffectiveProfile, constraint: dict[str, Any]) -> tuple[float, bool]:
    override = profile.override_for("CONSTRAINT", str(constraint.get("constraint_id")))
    default = profile.constraint_defaults.get(str(constraint.get("weight_key"))) or {}
    include = _as_bool(override.get("include_in_score", default.get("include_in_score")), False)
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
