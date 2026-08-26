from __future__ import annotations

from collections import defaultdict
from typing import Any

from ..model import Repository
from ..projection import constraint_parameter_rows, message_map


def _plain(rows) -> list[dict[str, Any]]:
    return [dict(r.data) for r in rows]


def render_rsr(repository: Repository) -> dict[str, Any]:
    parameter_rows = constraint_parameter_rows(repository)
    messages = message_map(repository)
    mappings: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in repository.governance_mappings:
        mappings[str(row.get("constraint_id"))].append(dict(row.data))

    constraints: list[dict[str, Any]] = []
    for row in repository.constraints:
        item = dict(row.data)
        cid = str(row.get("constraint_id"))
        item["parameters"] = parameter_rows.get(cid, [])
        item["messages"] = messages.get(cid, {})
        item["governanceMappings"] = mappings.get(cid, [])
        constraints.append(item)

    vocabulary_terms: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in repository.vocabulary_terms:
        vocabulary_terms[str(row.get("vocabulary_id"))].append(dict(row.data))
    vocabularies = []
    for row in repository.vocabularies:
        item = dict(row.data)
        item["terms"] = vocabulary_terms.get(str(row.get("vocabulary_id")), [])
        vocabularies.append(item)

    return {
        "repositoryMetadata": dict(repository.metadata),
        "domains": _plain(repository.domains),
        "assessmentDimensions": _plain(repository.assessment_dimensions),
        "governance": {
            "sources": _plain(repository.governance_sources),
            "dimensions": _plain(repository.governance_dimensions),
            "metrics": _plain(repository.governance_metrics),
            "requirements": _plain(repository.governance_requirements),
            "mappings": _plain(repository.governance_mappings),
        },
        "validationTargets": _plain(repository.validation_targets),
        "constraints": constraints,
        "constraintParameters": _plain(repository.constraint_parameters),
        "messages": _plain(repository.messages),
        "resolvers": _plain(repository.resolvers),
        "vocabularies": vocabularies,
        "dataQualityProfiles": _plain(repository.profiles),
        "profileTargetSettings": _plain(repository.profile_target_settings),
        "profileConstraintDefaults": _plain(repository.profile_constraint_defaults),
        "profileOverrides": _plain(repository.profile_overrides),
        "implementationBindings": _plain(repository.implementation_bindings),
        "implementationProfiles": _plain(repository.implementation_profiles),
        "implementationTargetWeights": _plain(repository.implementation_target_weights),
        "implementationRuntimeRules": _plain(repository.implementation_runtime_rules),
        "implementationRuntimeParameters": _plain(repository.implementation_runtime_parameters),
    }
