# Authoritative source

`rsr.xlsx` is the authoritative human-maintained Rule Specification Repository and Data Quality Profile source.

The generator reads normalized tables from this workbook. The main implementation sheets are `Validation Targets`, `Rules`, `Constraints`, `Constraint Parameters`, `Messages`, `Profiles`, `Profile Target Settings`, `Profile Constraint Defaults`, `Profile Overrides`, `Governance Mappings`, and `Implementation Bindings`.

All generated artefacts must be reproducible from this file.
