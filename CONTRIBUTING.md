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

The Rule layer no longer exists in RSR schema 2.0.

## Constraint parameters

Every runtime-relevant parameter must have an explicit `value_type`. Multiple values for the same parameter name must use `sequence` and, when necessary, a `combine_operator`; the generator must never silently overwrite them.

## Governance mappings

Governance mapping is Constraint-centric. Every active Constraint must appear in `Governance Mappings`, including an explicit `UNMAPPED` row when no authoritative mapping is yet available.

## Profile changes

Prefer creating a new Data Quality Profile version and setting `base_profile_id` rather than duplicating all target settings/defaults. Record only the delta whenever possible.
