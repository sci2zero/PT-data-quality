from __future__ import annotations

import argparse
import sys
from collections import Counter

from .build import build_repository
from .config import load_json
from .profile import resolve_profile
from .validation import validate_repository
from .xlsx_loader import load_repository


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pt-data-quality", description="Build and validate the PT Data Quality Rule Specification Repository.")
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build", help="Generate RSR JSON, profile JSON, PT Master runtime JSON, docs, reports, SHACL and Schematron.")
    build.add_argument("source", nargs="?", default="source/rsr.xlsx")
    build.add_argument("--output", default="generated")
    build.add_argument("--schema", default="schema/repository-schema.json")
    build.add_argument("--profile", help="Generate only one Data Quality Profile.")

    validate = sub.add_parser("validate", help="Validate the XLSX source and references.")
    validate.add_argument("source", nargs="?", default="source/rsr.xlsx")
    validate.add_argument("--schema", default="schema/repository-schema.json")
    validate.add_argument("--allow-errors", action="store_true", help="Return exit code 0 even if errors are found.")

    show = sub.add_parser("show-profile", help="Print a concise effective-profile summary.")
    show.add_argument("profile_id")
    show.add_argument("source", nargs="?", default="source/rsr.xlsx")
    show.add_argument("--schema", default="schema/repository-schema.json")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    schema = load_json(args.schema)

    if args.command == "build":
        repo, issues = build_repository(args.source, args.output, args.schema, args.profile)
        counts = Counter(i.severity for i in issues)
        print(f"Generated {len(repo.validation_targets)} validation targets and {len(repo.constraints)} constraints ({counts.get('error', 0)} errors, {counts.get('warning', 0)} warnings).")
        return 1 if counts.get("error", 0) else 0

    repo = load_repository(args.source, schema)
    if args.command == "validate":
        issues = validate_repository(repo, schema)
        for issue in issues:
            location = issue.sheet or ""
            if issue.row_number:
                location += f":{issue.row_number}"
            print(f"{issue.severity.upper():7} {issue.code:30} {location:32} {issue.artifact_id or '':55} {issue.message}")
        counts = Counter(i.severity for i in issues)
        print(f"\nErrors: {counts.get('error', 0)}; warnings: {counts.get('warning', 0)}; info: {counts.get('info', 0)}")
        if counts.get("error", 0) and not args.allow_errors:
            return 1
        return 0

    if args.command == "show-profile":
        profile = resolve_profile(repo, args.profile_id)
        print(f"Profile: {profile.profile_id}")
        print(f"Version: {profile.profile.get('version')}")
        print(f"Base profile: {profile.profile.get('base_profile_id') or '-'}")
        print(f"Target settings: {len(profile.target_settings)}")
        print(f"Constraint defaults: {len(profile.constraint_defaults)}")
        print(f"Overrides: {sum(len(v) for v in profile.overrides.values())}")
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
