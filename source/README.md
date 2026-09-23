# Authoritative source

`rsr.xlsx` is the authoritative human-maintained Rule Specification Repository (RSR) and Data Quality Profile source.

RSR schema 2.0.2 / repository version 2.0.3 uses the same direct canonical relationship:

```text
Validation Target -> one or more Constraints
```

The former one-to-one `Rule` layer has been removed.

The main authoring sheets are:

- `Assessment Dimensions`
- `Validation Targets`
- `Constraints`
- `Constraint Parameters`
- `Messages`
- `Resolvers`
- `Vocabularies` / `Vocabulary Terms`
- `Governance Sources` / `Governance Dimensions` / `Governance Metrics` / `Governance Requirements`
- `Governance Mappings`
- `Data Quality Profiles`
- `Profile Target Settings`
- `Profile Constraint Defaults`
- `Profile Overrides`
- `Implementation Bindings`
- `Implementation Profiles`
- `Implementation Target Weights`
- `Implementation Runtime Rules`
- `Implementation Runtime Parameters`

Two different JSON projections are generated deliberately:

- `generated/rsr/rsr.json` is the full-fidelity canonical machine-readable projection of the XLSX.
- `generated/implementation/pt-master/PTCRIS-DATAGOV-1.0.0/1.0.0.json` is the improved RSR-driven configuration for the current Java engine. It preserves the current Java runtime keys/targets and constraint parameter names/types, while using canonical messages/profile behaviour/values where safely bound. It intentionally contains no future-only resolver/vocabulary model.
- `generated/implementation/pt-master/PTCRIS-DATAGOV-1.0.0/2.0.0-preview.json` is the future generic runtime contract: all RSR Constraints, four-language messages, typed parameter definitions, resolver/vocabulary registries, governance traceability and explicit `javaSupport` migration status/comments.

`pt-master-current-java-1.0.0.json` is the implementation compatibility contract for the currently deployed Java reader/evaluator. It is intentionally separate from the canonical RSR workbook: the workbook defines the target data-quality policy, while this JSON defines which 1.x runtime keys, targets, dimensions and parameter names/types the current Java code can consume immediately.

All generated artefacts must be reproducible from `rsr.xlsx` plus this explicitly versioned current-Java compatibility contract.
