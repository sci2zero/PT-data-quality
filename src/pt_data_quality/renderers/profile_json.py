from __future__ import annotations

from typing import Any

from ..model import Repository
from ..profile import constraint_enabled, enabled_target, resolve_profile, rule_enabled


def render_profile(repository: Repository, profile_id: str) -> dict[str, Any]:
    effective = resolve_profile(repository, profile_id)
    active_targets = {
        tid: dict(setting)
        for tid, setting in effective.target_settings.items()
        if enabled_target(effective, tid)
    }
    active_rules = [
        str(r.get("rule_id"))
        for r in repository.rules
        if str(r.get("validation_target_id")) in active_targets
        and rule_enabled(effective, str(r.get("rule_id")))
        and str(r.get("status")).upper() not in {"RETIRED", "ARCHIVED", "DEPRECATED"}
    ]
    active_rule_set = set(active_rules)
    active_constraints = [
        str(c.get("constraint_id"))
        for c in repository.constraints
        if str(c.get("rule_id")) in active_rule_set
        and constraint_enabled(effective, str(c.get("constraint_id")))
        and str(c.get("status")).upper() not in {"RETIRED", "ARCHIVED", "DEPRECATED"}
    ]
    return {
        "profile": dict(effective.profile),
        "targetSettings": active_targets,
        "constraintDefaults": effective.constraint_defaults,
        "overrides": [
            {"artifactType": k[0], "artifactId": k[1], "properties": v}
            for k, v in sorted(effective.overrides.items())
        ],
        "activeRuleIds": active_rules,
        "activeConstraintIds": active_constraints,
        "summary": {
            "validationTargets": len(active_targets),
            "rules": len(active_rules),
            "constraints": len(active_constraints),
        },
    }
