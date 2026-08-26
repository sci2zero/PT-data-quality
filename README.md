# PT Data Quality Repository

This repository contains the executable **Rule Specification Repository (RSR)** and **Data Quality Profiles** for PTCRIS data quality assessment.

The authoritative authoring source is:

```text
source/rsr.xlsx
```

Everything below `generated/` is derived from that workbook and should not be edited manually.

## RSR schema 2.0.1

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

The generator deliberately produces two PT Master runtime configurations from the same `source/rsr.xlsx`.

### `1.0.0.json` — improved configuration for the current Java engine

```text
generated/implementation/pt-master/
  PTCRIS-DATAGOV-1.0.0/
  1.0.0.json
```

This file keeps the JSON contract that the current Java code can consume immediately:

```json
{
  "minimumRequiredScore": 60,
  "dimensionDefinitions": {},
  "targetWeights": {},
  "dataQualityRemarks": {}
}
```

Compatibility is **structural/runtime compatibility, not content identity**. The generator preserves the current Java runtime keys, runtime targets and the constraint parameter names/types that `DataQualityCalculator` reads (`minYear`, `maxFutureYears`, `min`, `max`, `minLength`, `maxLength`, `pattern`, ...). At the same time it refreshes the configuration from the canonical RSR wherever there is a stable binding:

- new multilingual messages (`en`, `sr`, `sr-cyr`, `pt`);
- DQP severity/blocking/scoring behaviour;
- canonical constraint values transformed into the legacy Java parameter names;
- expanded RSR-derived target weights.

The current Java code hard-codes the runtime issue keys it can report, so `1.0.0.json` deliberately does **not** add unsupported new rule keys. Adding such keys would incorrectly affect rule counts/scoring even though Java could never report them. The Java-branch `1.0.0.json` fixture is therefore used as a **contract baseline**, not as the generated content.

### `2.0.0-preview.json` — future generic runtime contract

The same build also creates:

```text
generated/implementation/pt-master/
  PTCRIS-DATAGOV-1.0.0/
  2.0.0-preview.json
```

This is the target configuration for future Java refactoring. It contains all active RSR Constraints and introduces configuration concepts that current Java does not yet execute generically:

- all 445 active Constraints / all modeled entities;
- four-language messages;
- typed canonical parameter definitions and combine operators;
- `resolverDefinitions` plus `resolverId` references;
- `vocabularyDefinitions` plus `vocabularyId` references;
- governance traceability;
- current-Java legacy runtime keys and parameter contracts as migration metadata.

Because standard JSON has no comments, every preview rule has a `javaSupport` object with a status (`LEGACY_SUPPORTED`, `LEGACY_CONFIG_ONLY`, `NOT_SUPPORTED`) and a human-readable migration comment. As generic Java evaluators are implemented, the support status can advance without redesigning the RSR or the 2.0.0 format.

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

Multiple rows with the same parameter name are supported in the canonical RSR. `MIN`/`MAX` combinations remain available in the canonical projection, for example:

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

Canonical RSR messages are intentionally generic and do not contain legacy runtime placeholders such as `{value}` or `{recordId}`. In `1.0.0.json`, 1:1 canonically bound runtime rules use these new four-language messages directly. Legacy-only and N:M compatibility rules keep their runtime-specific wording (including positional placeholders where Java supplies values) and receive a Portuguese compatibility translation. `2.0.0-preview.json` always uses the canonical RSR messages.

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
│           ├── 2.0.0-preview.json
│           ├── shacl/
│           └── schematron/
├── docs/
└── reports/
    ├── validation.md
    ├── governance-traceability-PTCRIS-DATAGOV-1.0.0.md
    ├── coverage-PTCRIS-DATAGOV-1.0.0.json
    ├── pt-master-compatibility-PTCRIS-DATAGOV-1.0.0.md
    └── pt-master-next-support-PTCRIS-DATAGOV-1.0.0.md
```

## Current-Java compatibility

`tests/fixtures/pt-master-legacy-1.0.0.json` is copied from `src/main/resources/dataQualityAssessment/ptcris/1.0.0.json` in the current TeslaRIS Java branch. It defines the **1.x runtime contract**: known runtime keys/targets and hard-coded constraint parameter names/types. It is not the source of the new RSR messages, scoring or parameter values.

The build creates:

```text
generated/reports/
  pt-master-compatibility-PTCRIS-DATAGOV-1.0.0.md
```

A valid `1.0.0.json` build must preserve all current runtime keys and targets, keep every Java-read constraint parameter name with the same JSON type, and avoid extra rule-level fields that the current DTO does not know. Messages, Portuguese localisation, target weights, severity/blocking and points may intentionally differ because those values are now generated from the RSR/DQP.

The separate `pt-master-next-support-...md` report summarizes the `2.0.0-preview.json` Java migration backlog.

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
git commit -m "Generate current-Java 1.x and future PT Master 2.x runtime contracts"
git push
```

CI regenerates the artefacts and fails if committed generated output is stale.
