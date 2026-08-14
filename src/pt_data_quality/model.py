from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable


@dataclass(frozen=True)
class Row:
    data: dict[str, Any]
    sheet: str
    row_number: int

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]


@dataclass
class Repository:
    metadata: dict[str, Any]
    domains: list[Row] = field(default_factory=list)
    governance_sources: list[Row] = field(default_factory=list)
    governance_dimensions: list[Row] = field(default_factory=list)
    governance_requirements: list[Row] = field(default_factory=list)
    validation_targets: list[Row] = field(default_factory=list)
    rules: list[Row] = field(default_factory=list)
    constraints: list[Row] = field(default_factory=list)
    constraint_parameters: list[Row] = field(default_factory=list)
    messages: list[Row] = field(default_factory=list)
    resolvers: list[Row] = field(default_factory=list)
    vocabularies: list[Row] = field(default_factory=list)
    vocabulary_terms: list[Row] = field(default_factory=list)
    governance_mappings: list[Row] = field(default_factory=list)
    profiles: list[Row] = field(default_factory=list)
    profile_target_settings: list[Row] = field(default_factory=list)
    profile_constraint_defaults: list[Row] = field(default_factory=list)
    profile_overrides: list[Row] = field(default_factory=list)
    implementation_bindings: list[Row] = field(default_factory=list)

    def index(self, rows: Iterable[Row], key: str) -> dict[str, Row]:
        return {str(r.get(key)): r for r in rows if r.get(key) not in (None, "")}

    @property
    def domains_by_id(self) -> dict[str, Row]:
        return self.index(self.domains, "domain_id")

    @property
    def targets_by_id(self) -> dict[str, Row]:
        return self.index(self.validation_targets, "validation_target_id")

    @property
    def rules_by_id(self) -> dict[str, Row]:
        return self.index(self.rules, "rule_id")

    @property
    def constraints_by_id(self) -> dict[str, Row]:
        return self.index(self.constraints, "constraint_id")

    @property
    def requirements_by_id(self) -> dict[str, Row]:
        return self.index(self.governance_requirements, "requirement_id")

    @property
    def profiles_by_id(self) -> dict[str, Row]:
        return self.index(self.profiles, "profile_id")

    @property
    def resolvers_by_id(self) -> dict[str, Row]:
        return self.index(self.resolvers, "resolver_id")

    @property
    def vocabularies_by_id(self) -> dict[str, Row]:
        return self.index(self.vocabularies, "vocabulary_id")


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    message: str
    sheet: str | None = None
    row_number: int | None = None
    artifact_id: str | None = None


@dataclass
class EffectiveProfile:
    profile_id: str
    profile: dict[str, Any]
    target_settings: dict[str, dict[str, Any]]
    constraint_defaults: dict[str, dict[str, Any]]
    overrides: dict[tuple[str, str], dict[str, Any]]

    def override_for(self, artifact_type: str, artifact_id: str) -> dict[str, Any]:
        return self.overrides.get((artifact_type.upper(), artifact_id), {})
