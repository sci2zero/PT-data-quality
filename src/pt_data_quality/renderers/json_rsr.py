from __future__ import annotations

from collections import defaultdict
from typing import Any

from ..model import Repository


def _plain(rows) -> list[dict[str, Any]]:
    return [dict(r.data) for r in rows]


def render_rsr(repository: Repository) -> dict[str, Any]:
    parameters: defaultdict[str, dict[str, Any]] = defaultdict(dict)
    for row in repository.constraint_parameters:
        parameters[str(row.get("constraint_id"))][str(row.get("parameter_name"))] = row.get("parameter_value")

    messages: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in repository.messages:
        messages[str(row.get("constraint_id"))].append(dict(row.data))

    constraints: list[dict[str, Any]] = []
    for row in repository.constraints:
        item = dict(row.data)
        cid = str(row.get("constraint_id"))
        item["parameters"] = parameters.get(cid, {})
        item["messages"] = messages.get(cid, [])
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
        "governance": {
            "sources": _plain(repository.governance_sources),
            "dimensions": _plain(repository.governance_dimensions),
            "requirements": _plain(repository.governance_requirements),
            "mappings": _plain(repository.governance_mappings),
        },
        "validationTargets": _plain(repository.validation_targets),
        "rules": _plain(repository.rules),
        "constraints": constraints,
        "resolvers": _plain(repository.resolvers),
        "vocabularies": vocabularies,
        "implementationBindings": _plain(repository.implementation_bindings),
    }
