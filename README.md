# PT Data Quality Repository

This repository contains the executable **Rule Specification Repository (RSR)** and **Data Quality Profiles** for PTCRIS data quality assessment.

The authoritative authoring source is:

```text
source/rsr.xlsx
```

Everything below `generated/` is derived from that workbook and should not be edited manually.

## RSR schema 2.0

The core model is intentionally simple:

```text
Validation Target
      |
      +--> Constraint 1
      +--> Constraint 2
      +--> ...
```

The former one-to-one **Rule** layer has been removed. A Validation Target identifies what is assessed; each Constraint represents one reusable executable validation condition such as presence, minimum/maximum length, minimum/maximum date, regex, uniqueness, vocabulary membership, resolvability or a custom business rule.

Each Constraint can have:

- typed Constraint Parameters;
- one logical multilingual message (`en`, `sr`, `sr-cyr`, `pt`);
- zero or more authoritative governance mappings;
- implementation-specific bindings.

Operational assessment dimensions (`COMPLETENESS`, `VALIDITY`, `UNIQUENESS`, `CONSISTENCY`, `TIMELINESS`, `ACCURACY`, `CONFORMITY`, `INTEGRITY`) are maintained separately from PTCRIS Governance Dimensions.

## Two generated JSON projections

The generator deliberately produces two different JSON representations.

### Canonical RSR JSON

```text
generated/rsr/rsr.json
```

This is the full-fidelity machine-readable projection of `source/rsr.xlsx`. It preserves Validation Targets, Constraints, typed parameter rows, multilingual messages, governance hierarchy/mappings, profiles and implementation bindings.

### PT Master runtime JSON

```text
generated/implementation/pt-master/
  PTCRIS-DATAGOV-1.0.0/
  1.0.0.json
```

This is a compatibility-oriented projection for the current Java/PT Master evaluator. Its high-level shape intentionally remains close to the deployed configuration:

```json
{
  "minimumRequiredScore": 60,
  "dimensionDefinitions": {},
  "targetWeights": {},
  "dataQualityRemarks": {}
}
```

The runtime generator resolves profile-specific target importance, Constraint weights, severity/blocking behaviour, typed parameter values and implementation bindings. Existing `dataQualityRemarks` keys are reused where an explicit confident legacy binding exists; otherwise a deterministic key is generated.

`runtime-config.json` is the richer PT Master projection and retains canonical Constraint/Validation Target IDs and governance traceability.

## Governance model

Governance mapping is Constraint-centric:

```text
Constraint
   -> Governance Dimension
      -> Governance Metric
         -> Governance Requirement
```

Partial mappings are valid. An active Constraint may therefore be mapped only to a Dimension, to Dimension + Metric, or to a complete Requirement. Constraints with no authoritative mapping yet are represented explicitly as `UNMAPPED`; the generator never invents governance semantics.

## Constraint Parameters

Constraint Parameters include an explicit `value_type`, so JSON types are deterministic. For example:

```text
maxLength = 255, value_type = INTEGER
```

becomes:

```json
"maxLength": 255
```

rather than a string.

Multiple rows with the same parameter name are supported. `MIN`/`MAX` combinations are projected into expressions already understood by the PT Master runtime, for example:

```text
minDate = funding.dateSubmitted
minDate = 1950-01-01
combine_operator = MAX
```

becomes:

```json
"minDate": "max(funding.dateSubmitted, 1950-01-01)"
```

## Messages

There is exactly one logical message row per Constraint. Titles and messages are maintained in:

```text
en
sr
sr-cyr
pt
```

User-facing messages are intentionally generic and do not contain legacy runtime placeholders such as `{value}` or `{recordId}`. Record context is supplied by the application/UI.

## Data Quality Profiles

The current profile is:

```text
PTCRIS-DATAGOV-1.0.0
```

Profile-specific configuration is maintained in:

- `Data Quality Profiles`
- `Profile Target Settings`
- `Profile Constraint Defaults`
- `Profile Overrides`

Weights, severity, blocking behaviour and validity policy are profile-level decisions rather than intrinsic properties of reusable Constraints.

## Setup

Python 3.11+ is sufficient for the generator. The XLSX reader is dependency-free and read-only.

```bash
python -m venv .venv
source .venv/Scripts/activate      # Git Bash on Windows
# source .venv/bin/activate        # Linux/macOS

python -m pip install -e .
```

## Validate and build

```bash
pt-data-quality validate
pt-data-quality build
python -m unittest discover -s tests -v
```

Validation errors fail CI. Review markers, intentionally unresolved governance mappings and explicitly reported legacy-runtime collisions remain warnings while curation continues.

## Generated artefacts

```text
generated/
├── rsr/
│   ├── rsr.json
│   ├── resolvers.json
│   └── vocabularies.json
├── profiles/
│   └── PTCRIS-DATAGOV-1.0.0.json
├── implementation/
│   └── pt-master/
│       └── PTCRIS-DATAGOV-1.0.0/
│           ├── 1.0.0.json
│           ├── runtime-config.json
│           ├── shacl/
│           └── schematron/
├── docs/
└── reports/
    ├── validation.md
    ├── governance-traceability-PTCRIS-DATAGOV-1.0.0.md
    ├── coverage-PTCRIS-DATAGOV-1.0.0.json
    └── pt-master-compatibility-PTCRIS-DATAGOV-1.0.0.md
```

## Legacy-runtime compatibility

`tests/fixtures/pt-master-legacy-1.0.0.json` is a compatibility fixture containing the JSON currently used by the Java system. It is **not** the source of truth for current values.

The build creates:

```text
generated/reports/
  pt-master-compatibility-PTCRIS-DATAGOV-1.0.0.md
```

The report classifies runtime keys as `PRESERVED`, `CHANGED`, `REMOVED` or `ADDED` and identifies changes in target, severity, dimension, blocking, points and Constraint parameters. This makes intentional profile changes distinguishable from generator regressions.

## SHACL and Schematron

SHACL and Schematron remain binding-driven optional projections. The generator does not invent RDF or XML semantics. Only explicitly bound and safely representable Constraints are emitted; unsupported Constraints are reported in coverage files.

## Normal development workflow

```bash
git checkout -b rsr-v2

# edit source/rsr.xlsx and/or generator code
pt-data-quality validate
pt-data-quality build
python -m unittest discover -s tests -v

git status
git add source/rsr.xlsx src schema tests generated README.md CHANGELOG.md CONTRIBUTING.md
git commit -m "Upgrade data quality repository to RSR schema 2.0"
git push
```

CI regenerates the artefacts and fails if committed generated output is stale.
