# Changelog

## 0.2.0 - 2026-08-24

- Upgraded the authoritative RSR authoring schema to 2.0.0.
- Removed the redundant one-to-one Rule layer; Constraints now reference Validation Targets directly.
- Added separate operational `Assessment Dimensions`, distinct from PTCRIS Governance Dimensions.
- Added the Governance Dimension -> Metric -> Requirement hierarchy.
- Made governance coverage Constraint-centric, including explicit partial and `UNMAPPED` mappings.
- Added typed Constraint Parameters with support for multiple values, sequence and combination operators.
- Consolidated legacy message fragments into one logical multilingual message per Constraint (`en`, `sr`, `sr-cyr`, `pt`) without runtime placeholders.
- Added explicit PT Master Validation Target and Constraint runtime bindings, including preservation of legacy runtime keys where confidently matched.
- Restored legacy-compatible `dimensionDefinitions` in the PT Master runtime JSON.
- Preserved JSON scalar types for runtime parameters instead of serializing all XLSX values as strings.
- Added a deployed legacy PT Master runtime fixture and generated compatibility report.
- Added regression tests for ORCID check-digit `X`, ROR messages, Funding projectReferenceId, parameter typing, multi-value date constraints and deterministic generation.
- Updated canonical RSR JSON, profile JSON, reports, documentation, SHACL/Schematron projections and validation for RSR schema 2.0.

## 0.1.0 - 2026-08-14

- Initial PT Data Quality Repository generator.
- Normalized XLSX Rule Specification Repository as source of truth.
- Profile inheritance and reusable Constraints.
- PTCRIS-DATAGOV-1.0.0 profile generation.
- PT Master compatibility JSON and enriched runtime JSON.
- Profile/domain-based Markdown documentation.
- Consistency validation, coverage and governance traceability reports.
- Binding-driven SHACL and Schematron generators.
- GitHub Actions for validation, Pages and releases.
