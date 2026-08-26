# Changelog

## 0.2.3 - 2026-08-25

- Redefined the two PT Master runtime projections around **Java contract compatibility**, not byte-for-byte content identity.
- `1.0.0.json` is now a refreshed RSR-driven configuration for the current Java code: the same DTO/top-level shape, the same 162 runtime keys and runtime targets, the same hard-coded constraint parameter names/types, but canonical four-language messages, DQP behaviour/scoring and RSR parameter values where stable bindings exist.
- Added Portuguese titles/messages to all current-Java runtime rules; 1:1 bound rules use canonical RSR Messages, while legacy-only/N:M rules use explicit compatibility fallbacks.
- Kept future-only concepts such as generic resolver/vocabulary execution out of `1.0.0.json`.
- Expanded `2.0.0-preview.json` into the future configuration contract with all 445 active Constraints, resolver and vocabulary registries, typed parameter definitions, governance traceability, Java legacy parameter contracts and per-rule migration comments.
- Updated compatibility reporting/tests so a valid 1.x build proves current-Java runtime/API compatibility while allowing intentional content/scoring/message changes.

## 0.2.2 - 2026-08-25

- Split the PT Master runtime output into two explicit contracts generated from the same `source/rsr.xlsx`.
- `1.0.0.json` is now a strict production compatibility artefact and is semantically identical to the current Java-branch baseline, with no additive/future-only fields.
- Added `2.0.0-preview.json` as the expanded PT Master runtime preview: same runtime JSON shape, all 163 active Validation Targets / 445 Constraints, Portuguese messages, and Java-support annotations.
- Added typed canonical parameter rows, four-language messages, resolver definitions, vocabulary definitions, governance traceability and N:M legacy-adapter mappings to the preview runtime.
- Added per-Constraint `javaSupport` annotations (`LEGACY_SUPPORTED`, `LEGACY_CONFIG_ONLY`, `NOT_SUPPORTED`) instead of non-standard JSON comments.
- Added a generated PT Master next-runtime support report to make the Java migration backlog explicit.
- Added regression tests proving exact legacy compatibility and deterministic generation of both runtime JSON files.

## 0.2.1 - 2026-08-25

- Added an explicit PT Master implementation compatibility overlay while keeping the canonical RSR Constraint model unchanged.
- Added `Implementation Profiles`, `Implementation Target Weights`, `Implementation Runtime Rules` and `Implementation Runtime Parameters` sheets.
- Extended `Implementation Bindings` with runtime rule identifiers, parameter transformations and compatibility roles, including N:M Constraint/runtime mappings.
- Switched the current PT Master `1.0.0.json` generator to the explicit Java compatibility profile instead of auto-generating one runtime remark per canonical Constraint.
- Preserved all 162 runtime remarks, all 62 target weights, existing scoring/severity/blocking values, messages and Java parameter names from the current TeslaRIS Java branch.
- Added non-breaking `resolverId` metadata to the existing DOI and Handle resolvability remarks for future generic Java resolver execution.
- Added regression tests proving that the generated runtime is byte-semantically equivalent to the current Java baseline after removing the two explicitly additive resolver parameters.
- Updated the compatibility report to distinguish `ADDITIVE_ONLY` enrichment from changes to existing runtime semantics.
- Updated GitHub Pages workflow to deploy only through manual `workflow_dispatch`.

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
