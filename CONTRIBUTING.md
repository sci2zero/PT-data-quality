# Contributing

## Source of truth

Edit `source/rsr.xlsx`. Do not manually edit files under `generated/`.

## Before opening a pull request

```bash
pt-data-quality validate
pt-data-quality build
python -m unittest discover -s tests -v
git diff --exit-code -- generated
```

`REVIEW_REQUIRED`, intentionally `UNMAPPED` governance mappings, and known runtime-target compatibility warnings may remain while the repository is being curated, but new validation errors must not be introduced.

## IDs

Persistent IDs such as `validation_target_id`, `constraint_id`, `parameter_id`, `mapping_id`, `requirement_id`, `profile_id`, `resolver_id`, and `vocabulary_id` should not be changed after publication unless an explicit migration/deprecation decision has been made.

The Rule layer no longer exists in RSR schema 2.0.1.

## Constraint parameters

Every runtime-relevant parameter must have an explicit `value_type`. Multiple values for the same parameter name must use `sequence` and, when necessary, a `combine_operator`; the generator must never silently overwrite them.

## Governance mappings

Governance mapping is Constraint-centric. Every active Constraint must appear in `Governance Mappings`, including an explicit `UNMAPPED` row when no authoritative mapping is yet available.

## Profile changes

Prefer creating a new Data Quality Profile version and setting `base_profile_id` rather than duplicating all target settings/defaults. Record only the delta whenever possible.


## PT Master runtime contracts

The canonical DQP and the Java runtime contracts are intentionally separate. For `PT_MASTER`:

- preserve the current Java runtime keys, runtime targets and hard-coded parameter names/types through `Implementation Runtime Rules`, `Implementation Runtime Parameters` and `Implementation Bindings`;
- let `1.0.0.json` refresh messages, Portuguese localisation, DQP severity/blocking/points and compatible parameter values from the canonical RSR;
- do not add new unsupported runtime rule keys or unknown rule-level fields to `1.0.0.json`, because current Java counts configured rules/points even when it cannot report them;
- keep future-only concepts such as generic resolver/vocabulary execution, typed canonical parameter definitions and new RSR-only rules in `2.0.0-preview.json`;
- use N:M `Implementation Bindings` and explicit parameter transformations whenever the canonical Constraint model differs from the current Java parameter contract.

A valid current-Java build must make `generated/reports/pt-master-compatibility-PTCRIS-DATAGOV-1.0.0.md` report **Current Java runtime contract compatible: YES**, with zero missing/added 1.x runtime keys, zero runtime target changes and zero Java parameter contract issues. Content/scoring/message differences from the Java-branch baseline are expected and should be reviewed rather than rejected automatically.
