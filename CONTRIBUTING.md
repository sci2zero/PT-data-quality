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

Warnings marked `REVIEW_REQUIRED` may remain while migrated rules are being curated, but new validation errors must not be introduced.

## IDs

Persistent IDs such as `validation_target_id`, `rule_id`, `constraint_id`, `requirement_id`, `profile_id`, `resolver_id`, and `vocabulary_id` should not be changed after publication unless an explicit migration/deprecation decision has been made.

## Profile changes

Prefer creating a new profile version and setting `base_profile_id` rather than duplicating all target settings and rules. Record only the delta whenever possible.
