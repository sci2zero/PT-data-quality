# PT Data Quality Repository

This repository contains the executable **Rule Specification Repository (RSR)** and **Data Quality Profiles** for PTCRIS data quality assessment.

The authoritative authoring source is:

```text
source/rsr.xlsx
```

Everything below `generated/` is derived from that workbook and should not be edited manually.

## Architecture

```text
XLSX Rule Specification Repository
        |
        +--> canonical RSR JSON
        +--> effective Data Quality Profile JSON
        +--> PT Master runtime JSON
        +--> profile-based Markdown documentation
        +--> validation / coverage / traceability reports
        +--> SHACL (when RDF bindings exist)
        +--> Schematron (when XML bindings exist)
```

The workbook separates reusable RSR artefacts from profile-specific decisions. A Constraint can therefore be reused by several Data Quality Profiles without duplication. Profile versions inherit through `base_profile_id`, while `Profile Target Settings`, `Profile Constraint Defaults`, and `Profile Overrides` carry the differences.

## Current profile

The initial workbook contains:

```text
PTCRIS-DATAGOV-1.0.0
```

It represents the current PTCRIS Data Governance configuration migrated from the previous domain-based Constraints workbook.

## Domain-based implementation

Although reusable rules are now stored in normalized sheets, every Validation Target, Rule and Constraint has a `domain_id`. Generated profile documentation is split into implementation-friendly domain pages:

```text
PERSON
ORGANISATION_UNIT
PROJECT
FUNDING
OUTPUT
ACTIVITY
SHARED_COMPONENTS
```

This allows different developers to work on different domains while keeping one normalized source of truth.

## Setup

Python 3.11+ is sufficient for the generator. The XLSX reader is dependency-free and read-only; it uses Python's standard library and does not require Excel or LibreOffice.

```bash
python -m venv .venv
source .venv/Scripts/activate      # Git Bash on Windows
# source .venv/bin/activate        # Linux/macOS

python -m pip install -e .
```

Check the CLI:

```bash
pt-data-quality --help
```

## Build

```bash
pt-data-quality build
```

Equivalent explicit command:

```bash
pt-data-quality build source/rsr.xlsx --output generated
```

To build one profile only:

```bash
pt-data-quality build --profile PTCRIS-DATAGOV-1.0.0
```

## Validate

```bash
pt-data-quality validate
```

The command exits with a non-zero status when validation **errors** exist. Review markers and intentionally unresolved migration items are warnings and remain visible in `generated/reports/validation.md`.

Current warnings are intentional migration/review work, not silent failures.

## Generated artefacts

For the current profile the important outputs are:

```text
generated/
├── rsr/
│   ├── rsr.json
│   ├── resolvers.json
│   └── vocabularies.json
├── profiles/
│   └── PTCRIS-DATAGOV-1.0.0.json
├── docs/
│   └── profiles/
│       └── ptcris-datagov-1-0-0/
│           ├── index.md
│           ├── scoring.md
│           ├── governance.md
│           ├── implementation.md
│           ├── review-required.md
│           └── domains/
├── implementation/
│   └── pt-master/
│       └── PTCRIS-DATAGOV-1.0.0/
│           ├── 1.0.0.json
│           ├── runtime-config.json
│           ├── shacl/
│           └── schematron/
└── reports/
```

### `1.0.0.json`

This is the compatibility-oriented PT Master projection using the same high-level structure as the existing hand-written configuration:

```json
{
  "minimumRequiredScore": 60,
  "targetWeights": {},
  "dataQualityRemarks": {}
}
```

The important difference is that **weights are never copied from the old hand-written JSON**. Target importance and constraint weights are resolved from the active Data Quality Profile in the XLSX.

Presence constraints are currently excluded from scoring because `Profile Constraint Defaults` defines `PRESENCE` with `include_in_score = false`; their generated `points` value is therefore `0`.

`runtime-config.json` is the richer projection and additionally retains Constraint, Rule, Validation Target and governance traceability identifiers.

## Profile inheritance

A future profile can reuse the same Constraints:

```text
PTCRIS-DATAGOV-1.0.0
        |
        +--> PTCRIS-DATAGOV-1.1.0
        +--> INSTITUTION-X-1.0.0
```

Create a new row in `Profiles`, set `base_profile_id`, and enter only changed values in the profile-specific sheets. The generator resolves the effective configuration deterministically.

## SHACL

SHACL generation is implemented, but the generator intentionally does **not** invent RDF semantics.

To emit SHACL shapes, add `Implementation Bindings` rows with:

```text
representation = RDF_SHACL
artifact_type = VALIDATION_TARGET
entity_selector = RDF class IRI/CURIE
value_selector = RDF property/path IRI/CURIE
```

The current automatic renderer supports common SHACL Core equivalents such as presence/cardinality, min/max length, regex, numeric min/max and local vocabulary membership. Resolver, repository-wide uniqueness and arbitrary custom constraints remain explicitly reported as unsupported unless a future custom binding mechanism is added.

## Schematron

Schematron follows the same principle. Add bindings with:

```text
representation = XML_SCHEMATRON
entity_selector = rule context XPath
value_selector = relative value XPath
```

The generator emits XPath 2.0 assertions for the constraint types it can represent safely and reports the remainder in the coverage file.

## PT Master runtime-target collisions

The migrated source currently contains two reused PT Master runtime paths (`Involvement.fromDate` and `Involvement.toDate`) across PERSON and ACTIVITY contexts. This is reported by validation. The legacy `targetWeights` JSON shape cannot represent two contextual weights for the same runtime path, so the compatibility renderer deterministically uses the maximum configured importance while the richer `runtime-config.json` retains traceability. This should eventually be resolved either by unifying the underlying Validation Target or by introducing context-aware implementation bindings.

## Documentation site

Install documentation dependencies:

```bash
python -m pip install -e ".[docs]"
mkdocs serve
```

The site uses the generated Markdown directly.

## Normal development workflow

```bash
git checkout -b dq-change

# edit source/rsr.xlsx
pt-data-quality validate
pt-data-quality build
python -m unittest discover -s tests -v

git status
git add source/rsr.xlsx generated/
git commit -m "Update PTCRIS data quality rules"
git push
```

CI regenerates the artefacts and fails if the committed generated output is stale.
