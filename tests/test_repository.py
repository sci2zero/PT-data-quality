from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from pt_data_quality.build import build_repository
from pt_data_quality.config import load_json
from pt_data_quality.model import Row
from pt_data_quality.profile import constraint_severity_and_blocking, constraint_weight, resolve_profile
from pt_data_quality.projection import runtime_parameter_map
from pt_data_quality.validation import validate_repository
from pt_data_quality.xlsx_loader import load_repository


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "rsr.xlsx"
SCHEMA = ROOT / "schema" / "repository-schema.json"
LEGACY = ROOT / "tests" / "fixtures" / "pt-master-legacy-1.0.0.json"
PROFILE = "PTCRIS-DATAGOV-1.0.0"


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_json(SCHEMA)
        cls.repo = load_repository(SOURCE, cls.schema)

    def test_expected_repository_size_and_v2_model(self):
        self.assertEqual("2.0.0", self.schema["repository_schema_version"])
        self.assertEqual(163, len(self.repo.validation_targets))
        self.assertEqual(445, len(self.repo.constraints))
        self.assertEqual(8, len(self.repo.assessment_dimensions))
        self.assertEqual(1, len(self.repo.profiles))
        self.assertFalse(hasattr(self.repo, "rules"))

    def test_current_source_has_no_validation_errors(self):
        issues = validate_repository(self.repo, self.schema)
        errors = [i for i in issues if i.severity == "error"]
        self.assertEqual([], errors)
        codes = {i.code for i in issues}
        self.assertIn("UNMAPPED_GOVERNANCE", codes)
        self.assertIn("PT_MASTER_RUNTIME_TARGET_WEIGHT_CONFLICT", codes)

    def test_profile_weights_and_behavior_come_from_profile_configuration(self):
        profile = resolve_profile(self.repo, PROFILE)
        vocab = next(c for c in self.repo.constraints if c.get("constraint_type") == "VOCABULARY")
        regex = next(c for c in self.repo.constraints if c.get("constraint_type") == "REGEX")
        presence = next(c for c in self.repo.constraints if c.get("constraint_type") == "PRESENCE")
        self.assertEqual((3.0, True), constraint_weight(profile, vocab.data))
        self.assertEqual((3.0, True), constraint_weight(profile, regex.data))
        self.assertEqual((0.0, False), constraint_weight(profile, presence.data))
        mandatory_setting = next(s.data for s in self.repo.profile_target_settings if s.get("requirement_level") == "MANDATORY")
        severity, blocking = constraint_severity_and_blocking(profile, presence.data, mandatory_setting)
        self.assertEqual("ERROR", severity)
        self.assertTrue(blocking)

    def test_typed_parameters_and_multi_value_combination(self):
        params = runtime_parameter_map(self.repo)
        self.assertIsInstance(params["C.PERSON.Person.Orcid.maxLength"]["maxLength"], int)
        self.assertEqual(19, params["C.PERSON.Person.Orcid.maxLength"]["maxLength"])
        self.assertEqual(
            "max(funding.dateSubmitted, 1950-01-01)",
            params["C.FUNDING.Funding.DateAwarded.minDate"]["minDate"],
        )
        self.assertEqual(
            "min(project.fromDate, funding.fromDate, current date + 3 years)",
            params["C.FUNDING.Funding.DateAwarded.maxDate"]["maxDate"],
        )

    def test_known_source_corrections_are_present(self):
        params = runtime_parameter_map(self.repo)
        self.assertEqual(r"^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$", params["C.PERSON.Person.Orcid.pattern"]["pattern"])
        target = self.repo.targets_by_id["VT.FUNDING.Funding.ProjectReferenceId"]
        self.assertEqual("Funding.projectReferenceId", target.get("canonical_path"))
        self.assertEqual("FIELD", target.get("target_category"))
        ror_message = next(m for m in self.repo.messages if m.get("constraint_id") == "C.ORGANISATION_UNIT.OrganisationUnit.Ror.pattern")
        self.assertIn("exactly 9 characters", ror_message.get("message_en"))
        self.assertFalse(ror_message.get("review_required"))

    def test_build_generates_legacy_shaped_runtime_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            runtime = Path(tmp) / "implementation" / "pt-master" / PROFILE / "1.0.0.json"
            data = json.loads(runtime.read_text(encoding="utf-8"))
            self.assertEqual(
                {"minimumRequiredScore", "dimensionDefinitions", "targetWeights", "dataQualityRemarks"},
                set(data),
            )
            self.assertEqual(60, data["minimumRequiredScore"])
            self.assertEqual(8, len(data["dimensionDefinitions"]))
            self.assertEqual(445, len(data["dataQualityRemarks"]))
            self.assertIn("invalidOrcidFormat", data["dataQualityRemarks"])
            self.assertEqual(
                r"^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$",
                data["dataQualityRemarks"]["invalidOrcidFormat"]["constraints"]["pattern"],
            )
            self.assertIn("Funding.projectReferenceId", data["targetWeights"])
            self.assertNotIn("Funding.projectReferenceId / grantAgreementId???", data["targetWeights"])
            self.assertIsInstance(
                data["dataQualityRemarks"]["personLanguageKnowledgeAcademicReviewTooLong"]["constraints"]["maxLength"],
                int,
            )

    def test_runtime_messages_include_four_languages_without_placeholders(self):
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            data = json.loads((Path(tmp) / "implementation" / "pt-master" / PROFILE / "1.0.0.json").read_text(encoding="utf-8"))
            sample = data["dataQualityRemarks"]["invalidRorFormat"]
            self.assertEqual({"en", "sr", "sr-cyr", "pt"}, set(sample["message"]))
            for text in sample["message"].values():
                self.assertNotIn("{value", text)
                self.assertNotIn("{recordId", text)

    def test_canonical_rsr_is_full_fidelity_and_has_no_rule_layer(self):
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            data = json.loads((Path(tmp) / "rsr" / "rsr.json").read_text(encoding="utf-8"))
            self.assertNotIn("rules", data)
            self.assertIn("assessmentDimensions", data)
            self.assertIn("metrics", data["governance"])
            constraint = next(c for c in data["constraints"] if c["constraint_id"] == "C.FUNDING.Funding.DateAwarded.minDate")
            self.assertEqual(2, len(constraint["parameters"]))
            self.assertIn("messages", constraint)
            self.assertIn("governanceMappings", constraint)

    def test_profile_inheritance_reuses_parent_configuration(self):
        repo = self.repo
        child = Row(
            data={**repo.profiles[0].data, "profile_id": "PTCRIS-DATAGOV-1.1.0", "version": "1.1.0", "base_profile_id": PROFILE},
            sheet="Data Quality Profiles",
            row_number=999,
        )
        original_profiles = repo.profiles
        original_settings = repo.profile_target_settings
        try:
            repo.profiles = original_profiles + [child]
            repo.profile_target_settings = original_settings + [
                Row(
                    data={
                        "profile_id": "PTCRIS-DATAGOV-1.1.0",
                        "domain_id": "PERSON",
                        "validation_target_id": "VT.PERSON.Education.DegreeType",
                        "enabled": True,
                        "importance": 4,
                        "requirement_level": "MANDATORY",
                        "status": "ACTIVE",
                    },
                    sheet="Profile Target Settings",
                    row_number=999,
                )
            ]
            child_profile = resolve_profile(repo, "PTCRIS-DATAGOV-1.1.0")
            self.assertEqual(163, len(child_profile.target_settings))
            self.assertEqual(4, child_profile.target_settings["VT.PERSON.Education.DegreeType"]["importance"])
            self.assertEqual(8, len(child_profile.constraint_defaults))
        finally:
            repo.profiles = original_profiles
            repo.profile_target_settings = original_settings

    def test_shacl_and_schematron_wait_for_explicit_bindings(self):
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            base = Path(tmp) / "implementation" / "pt-master" / PROFILE
            shacl_cov = json.loads((base / "shacl" / "coverage.json").read_text(encoding="utf-8"))
            sch_cov = json.loads((base / "schematron" / "coverage.json").read_text(encoding="utf-8"))
            self.assertEqual(0, shacl_cov["boundTargets"])
            self.assertEqual(0, sch_cov["boundTargets"])
            self.assertGreater(len(shacl_cov["unboundTargets"]), 0)
            self.assertGreater(len(sch_cov["unboundTargets"]), 0)

    def test_runtime_compatibility_report_is_generated(self):
        self.assertTrue(LEGACY.exists())
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            report = Path(tmp) / "reports" / f"pt-master-compatibility-{PROFILE}.md"
            text = report.read_text(encoding="utf-8")
            self.assertIn("Legacy remarks: **162**", text)
            self.assertIn("Generated remarks: **445**", text)
            self.assertIn("invalidOrcidFormat", text)

    def test_build_is_deterministic(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            build_repository(SOURCE, a, SCHEMA)
            build_repository(SOURCE, b, SCHEMA)
            rel = Path("implementation") / "pt-master" / PROFILE / "1.0.0.json"
            self.assertEqual((Path(a) / rel).read_bytes(), (Path(b) / rel).read_bytes())


if __name__ == "__main__":
    unittest.main()
