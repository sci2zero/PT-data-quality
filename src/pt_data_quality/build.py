from __future__ import annotations

from pathlib import Path

from .config import load_json
from .profile import resolve_profile
from .renderers.json_rsr import render_rsr
from .renderers.markdown import (
    domain_markdown,
    governance_markdown,
    implementation_markdown,
    index_markdown,
    profile_index,
    review_required_markdown,
    scoring_markdown,
)
from .renderers.profile_json import render_profile
from .renderers.pt_master import render_pt_master
from .renderers.pt_master_next import render_pt_master_next
from .renderers.reports import coverage, governance_traceability, next_runtime_support_markdown, runtime_compatibility_markdown, validation_markdown
from .renderers.schematron import render_schematron
from .renderers.shacl import render_shacl
from .util import ensure_dir, slug, write_json, write_text
from .config import load_json as load_json_file
from .validation import validate_repository
from .xlsx_loader import load_repository


def build_repository(source: str | Path, output: str | Path, schema_path: str | Path, profile_filter: str | None = None):
    schema = load_json(schema_path)
    repository = load_repository(source, schema)
    issues = validate_repository(repository, schema)
    output = Path(output)
    ensure_dir(output)

    # Canonical RSR exports.
    write_json(output / "rsr" / "rsr.json", render_rsr(repository))
    write_json(output / "rsr" / "resolvers.json", [dict(r.data) for r in repository.resolvers])
    write_json(output / "rsr" / "vocabularies.json", [dict(r.data) for r in repository.vocabularies])
    write_text(output / "reports" / "validation.md", validation_markdown(issues))

    profile_ids = [str(r.get("profile_id")) for r in repository.profiles]
    if profile_filter:
        if profile_filter not in profile_ids:
            raise KeyError(f"Unknown profile: {profile_filter}")
        profile_ids = [profile_filter]

    write_text(output / "docs" / "index.md", index_markdown(repository, profile_ids))

    for profile_id in profile_ids:
        effective = resolve_profile(repository, profile_id)
        profile_payload = render_profile(repository, profile_id)
        cov = coverage(repository, profile_id)
        write_json(output / "profiles" / f"{profile_id}.json", profile_payload)
        write_json(output / "reports" / f"coverage-{profile_id}.json", cov)
        write_text(output / "reports" / f"governance-traceability-{profile_id}.md", governance_traceability(repository, profile_id))

        legacy_runtime, _ = render_pt_master(repository, profile_id)
        next_runtime = render_pt_master_next(repository, profile_id)
        version = str(effective.profile.get("version") or "profile")
        impl = output / "implementation" / "pt-master" / profile_id
        write_json(impl / f"{version}.json", legacy_runtime)
        write_json(impl / "2.0.0-preview.json", next_runtime)
        write_text(
            output / "reports" / f"pt-master-next-support-{profile_id}.md",
            next_runtime_support_markdown(next_runtime, profile_id),
        )

        legacy_fixture = Path(__file__).resolve().parents[2] / "tests" / "fixtures" / "pt-master-legacy-1.0.0.json"
        if legacy_fixture.exists() and profile_id == "PTCRIS-DATAGOV-1.0.0":
            legacy_baseline = load_json_file(legacy_fixture)
            write_text(
                output / "reports" / f"pt-master-compatibility-{profile_id}.md",
                runtime_compatibility_markdown(legacy_baseline, legacy_runtime, profile_id),
            )

        shacl, shacl_cov = render_shacl(repository, profile_id)
        schematron, schematron_cov = render_schematron(repository, profile_id)
        write_text(impl / "shacl" / "shapes.ttl", shacl)
        write_json(impl / "shacl" / "coverage.json", shacl_cov)
        write_text(impl / "schematron" / "rules.sch", schematron)
        write_json(impl / "schematron" / "coverage.json", schematron_cov)

        docs = output / "docs" / "profiles" / slug(profile_id)
        write_text(docs / "index.md", profile_index(repository, profile_id, cov))
        write_text(docs / "scoring.md", scoring_markdown(repository, profile_id))
        write_text(docs / "governance.md", governance_markdown(repository, profile_id))
        write_text(docs / "implementation.md", implementation_markdown(profile_id, shacl_cov, schematron_cov))
        write_text(docs / "review-required.md", review_required_markdown(repository, profile_id))
        for domain_id in sorted(cov["domains"]):
            write_text(docs / "domains" / f"{slug(domain_id)}.md", domain_markdown(repository, profile_id, domain_id))

    return repository, issues
