# Authoritative source

`rsr.xlsx` is the authoritative human-maintained Rule Specification Repository (RSR) and Data Quality Profile source.

RSR schema 2.0 uses a direct relationship:

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

Two different JSON projections are generated deliberately:

- `generated/rsr/rsr.json` is the full-fidelity canonical machine-readable projection of the XLSX.
- `generated/implementation/pt-master/PTCRIS-DATAGOV-1.0.0/1.0.0.json` is the compatibility-oriented runtime projection used by the Java/PT Master implementation.

All generated artefacts must be reproducible from this workbook.
