from __future__ import annotations

from typing import Any

from ..model import Repository
from ..profile import constraint_enabled, enabled_target, resolve_profile


def render_profile(repository: Repository, profile_id: str) -> dict[str, Any]:
    effective = resolve_profile(repository, profile_id)
    active_targets = {
        tid: dict(setting)
        for tid, setting in effective.target_settings.items()
        if enabled_target(effective, tid)
    }
    active_constraints = [
        str(c.get("constraint_id"))
        for c in repository.constraints
        if str(c.get("validation_target_id")) in active_targets
        and constraint_enabled(effective, str(c.get("constraint_id")))
        and str(c.get("status")).upper() not in {"RETIRED", "ARCHIVED", "DEPRECATED"}
    ]
    return {
        "profile": dict(effective.profile),
        "targetSettings": active_targets,
        "constraintDefaults": effective.constraint_defaults,
        "overrides": [
            {"constraintId": cid, "properties": props}
            for cid, props in sorted(effective.overrides.items())
        ],
        "activeConstraintIds": active_constraints,
        "summary": {
            "validationTargets": len(active_targets),
            "constraints": len(active_constraints),
        },
    }
