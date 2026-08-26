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
IMPLEMENTATION_PROFILE = "PT_MASTER.CURRENT_JAVA.1.0.0"


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_json(SCHEMA)
        cls.repo = load_repository(SOURCE, cls.schema)
        cls.legacy = load_json(LEGACY)

    def test_expected_repository_size_and_v201_model(self):
        self.assertEqual("2.0.1", self.schema["repository_schema_version"])
        self.assertEqual("2.0.1", str(self.repo.metadata["schema_version"]))
        self.assertEqual(163, len(self.repo.validation_targets))
        self.assertEqual(445, len(self.repo.constraints))
        self.assertEqual(8, len(self.repo.assessment_dimensions))
        self.assertEqual(1, len(self.repo.profiles))
        self.assertEqual(1, len(self.repo.implementation_profiles))
        self.assertEqual(62, len(self.repo.implementation_target_weights))
        self.assertEqual(162, len(self.repo.implementation_runtime_rules))
        self.assertEqual(90, len(self.repo.implementation_runtime_parameters))
        self.assertFalse(hasattr(self.repo, "rules"))

    def test_current_source_has_no_validation_errors(self):
        issues = validate_repository(self.repo, self.schema)
        errors = [i for i in issues if i.severity == "error"]
        self.assertEqual([], errors)
        codes = {i.code for i in issues}
        self.assertIn("UNMAPPED_GOVERNANCE", codes)
        self.assertIn("PT_MASTER_RUNTIME_TARGET_WEIGHT_CONFLICT", codes)

    def test_profile_weights_and_behavior_come_from_canonical_profile_configuration(self):
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

    def test_typed_parameters_and_multi_value_combination_remain_canonical(self):
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
        # Implementation aliases must not leak back into the canonical parameter map.
        self.assertEqual("1950-01-01", params["C.OUTPUT.Document.DocumentDate.minDate"]["minDate"])
        self.assertNotIn("minYear", params["C.OUTPUT.Document.DocumentDate.minDate"])

    def test_known_source_corrections_are_present(self):
        params = runtime_parameter_map(self.repo)
        self.assertEqual(r"^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$", params["C.PERSON.Person.Orcid.pattern"]["pattern"])
        target = self.repo.targets_by_id["VT.FUNDING.Funding.ProjectReferenceId"]
        self.assertEqual("Funding.projectReferenceId", target.get("canonical_path"))
        self.assertEqual("FIELD", target.get("target_category"))
        ror_message = next(m for m in self.repo.messages if m.get("constraint_id") == "C.ORGANISATION_UNIT.OrganisationUnit.Ror.pattern")
        self.assertIn("exactly 9 characters", ror_message.get("message_en"))
        self.assertFalse(ror_message.get("review_required"))

    def test_implementation_profile_keeps_current_java_contract_baseline(self):
        profile = self.repo.implementation_profiles_by_id[IMPLEMENTATION_PROFILE]
        self.assertEqual(162, profile.get("runtime_rule_count"))
        self.assertEqual(62, len(self.legacy["targetWeights"]))
        self.assertEqual(162, len(self.legacy["dataQualityRemarks"]))
        self.assertFalse(self.legacy["dataQualityRemarks"]["noOrcidPresent"]["blocking"])
        self.assertIn("src/main/resources/dataQualityAssessment/ptcris/1.0.0.json", str(profile.get("baseline_resource")))

    def test_build_generates_refreshed_current_java_compatible_runtime_output(self):
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
            self.assertEqual({"en", "sr", "sr-cyr", "pt"}, set(data["dimensionDefinitions"]["VALIDITY"]))
            self.assertGreater(len(data["targetWeights"]), len(self.legacy["targetWeights"]))
            self.assertEqual(162, len(data["dataQualityRemarks"]))
            self.assertEqual(set(self.legacy["dataQualityRemarks"]), set(data["dataQualityRemarks"]))
            self.assertEqual(162, sum("pt" in r["message"] for r in data["dataQualityRemarks"].values()))
            self.assertFalse(data["dataQualityRemarks"]["noOrcidPresent"]["blocking"])
            self.assertEqual(0, data["dataQualityRemarks"]["noOrcidPresent"]["points"])
            self.assertEqual(
                r"^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$",
                data["dataQualityRemarks"]["invalidOrcidFormat"]["constraints"]["pattern"],
            )
            self.assertIsInstance(data["dataQualityRemarks"]["titleTooLong"]["constraints"]["maxLength"], int)
            self.assertEqual(1950, data["dataQualityRemarks"]["documentDateBefore"]["constraints"]["minYear"])
            self.assertEqual(3, data["dataQualityRemarks"]["documentDateTooFarInFuture"]["constraints"]["maxFutureYears"])
            self.assertEqual(-90.0, data["dataQualityRemarks"]["latitudeOutOfRange"]["constraints"]["min"])
            self.assertEqual(90.0, data["dataQualityRemarks"]["latitudeOutOfRange"]["constraints"]["max"])
            self.assertNotIn("constraints", data["dataQualityRemarks"]["doiNotResolvable"])

    def test_current_1x_runtime_preserves_java_keys_targets_and_parameter_contracts_but_refreshes_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            runtime = json.loads((Path(tmp) / "implementation" / "pt-master" / PROFILE / "1.0.0.json").read_text(encoding="utf-8"))
            self.assertNotEqual(self.legacy, runtime)
            self.assertEqual(set(self.legacy["dataQualityRemarks"]), set(runtime["dataQualityRemarks"]))
            for key, old_rule in self.legacy["dataQualityRemarks"].items():
                new_rule = runtime["dataQualityRemarks"][key]
                self.assertEqual(old_rule.get("target"), new_rule.get("target"), key)
                old_params = old_rule.get("constraints") or {}
                new_params = new_rule.get("constraints") or {}
                for pname, old_value in old_params.items():
                    self.assertIn(pname, new_params, f"{key}.{pname}")
                    new_value = new_params[pname]
                    old_num = isinstance(old_value, (int, float)) and not isinstance(old_value, bool)
                    new_num = isinstance(new_value, (int, float)) and not isinstance(new_value, bool)
                    self.assertTrue((old_num and new_num) or type(old_value) is type(new_value), f"{key}.{pname}")
            # Canonical RSR message replaces the legacy placeholder text for a 1:1 mapping.
            self.assertNotEqual(
                self.legacy["dataQualityRemarks"]["invalidOrcidFormat"]["message"],
                runtime["dataQualityRemarks"]["invalidOrcidFormat"]["message"],
            )
            self.assertIn("pt", runtime["dataQualityRemarks"]["invalidOrcidFormat"]["message"])
    def test_next_runtime_is_expanded_future_contract_with_all_constraints(self):
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            base = Path(tmp) / "implementation" / "pt-master" / PROFILE
            future = json.loads((base / "2.0.0-preview.json").read_text(encoding="utf-8"))
            self.assertEqual("2.0.0-preview", future["runtimeModelVersion"])
            self.assertEqual(8, len(future["dimensionDefinitions"]))
            self.assertEqual({"en", "sr", "sr-cyr", "pt"}, set(future["dimensionDefinitions"]["VALIDITY"]))
            self.assertEqual(445, len(future["dataQualityRemarks"]))
            self.assertGreater(len(future["targetWeights"]), len(self.legacy["targetWeights"]))
            self.assertEqual(4, len(future["resolverDefinitions"]))
            self.assertEqual(20, len(future["vocabularyDefinitions"]))
            self.assertIn("pt", future["dataQualityRemarks"]["invalidOrcidFormat"]["message"])
            self.assertEqual(
                r"^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$",
                future["dataQualityRemarks"]["invalidOrcidFormat"]["constraints"]["pattern"],
            )
            self.assertIn("javaSupport", future["dataQualityRemarks"]["invalidOrcidFormat"])
    def test_next_runtime_contains_expanded_entities_and_future_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            future = json.loads((Path(tmp) / "implementation" / "pt-master" / PROFILE / "2.0.0-preview.json").read_text(encoding="utf-8"))
            remarks = future["dataQualityRemarks"]
            funding = next(v for v in remarks.values() if v.get("constraintId") == "C.FUNDING.Funding.DateAwarded.minDate")
            self.assertEqual("Funding.dateAwarded", funding["target"])
            self.assertIn("minDate", funding["constraints"])
            self.assertEqual(2, len(funding["constraints"]["parameterDefinitions"]))
            self.assertEqual("MAX", funding["constraints"]["parameterDefinitions"][0]["combineOperator"])
            doi = next(v for v in remarks.values() if v.get("constraintId") == "C.OUTPUT.Document.Doi.resolvable")
            self.assertEqual("RES.DOI", doi["constraints"]["resolverId"])
            self.assertEqual("https://doi.org/{value}", future["resolverDefinitions"]["RES.DOI"]["uriTemplate"])
            self.assertEqual("LEGACY_SUPPORTED", doi["javaSupport"]["status"])
            orcid_resolvable = next(v for v in remarks.values() if v.get("constraintId") == "C.PERSON.Person.Orcid.resolvable")
            self.assertEqual("RES.ORCID", orcid_resolvable["constraints"]["resolverId"])
            self.assertEqual("NOT_SUPPORTED", orcid_resolvable["javaSupport"]["status"])
            self.assertIn("comment", orcid_resolvable["javaSupport"])
    def test_current_runtime_messages_are_refreshed_and_portuguese_is_complete(self):
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            data = json.loads((Path(tmp) / "implementation" / "pt-master" / PROFILE / "1.0.0.json").read_text(encoding="utf-8"))
            sample = data["dataQualityRemarks"]["invalidOrcidFormat"]
            self.assertEqual({"en", "sr", "sr-cyr", "pt"}, set(sample["message"]))
            self.assertNotIn("{0}", sample["message"]["en"])
            # N:M rules keep Java-specific wording/parameters but also receive Portuguese.
            latitude = data["dataQualityRemarks"]["latitudeOutOfRange"]
            self.assertIn("{0}", latitude["message"]["en"])
            self.assertIn("pt", latitude["message"])
    def test_canonical_rsr_is_full_fidelity_and_includes_implementation_overlay(self):
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            data = json.loads((Path(tmp) / "rsr" / "rsr.json").read_text(encoding="utf-8"))
            self.assertNotIn("rules", data)
            self.assertIn("assessmentDimensions", data)
            self.assertIn("metrics", data["governance"])
            self.assertEqual(1, len(data["implementationProfiles"]))
            self.assertEqual(62, len(data["implementationTargetWeights"]))
            self.assertEqual(162, len(data["implementationRuntimeRules"]))
            self.assertEqual(90, len(data["implementationRuntimeParameters"]))
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
            self.assertIn("Current Java runtime contract compatible: **YES**", text)
            self.assertIn("Baseline runtime keys: **162**", text)
            self.assertIn("Generated runtime keys: **162**", text)
            self.assertIn("Missing baseline keys: **0**", text)
            self.assertIn("Added unsupported 1.x keys: **0**", text)
            self.assertIn("Portuguese messages: **162/162**", text)

    def test_build_is_deterministic(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            build_repository(SOURCE, a, SCHEMA)
            build_repository(SOURCE, b, SCHEMA)
            base = Path("implementation") / "pt-master" / PROFILE
            for name in ("1.0.0.json", "2.0.0-preview.json"):
                rel = base / name
                self.assertEqual((Path(a) / rel).read_bytes(), (Path(b) / rel).read_bytes())


if __name__ == "__main__":
    unittest.main()
