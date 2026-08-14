from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from pt_data_quality.build import build_repository
from pt_data_quality.config import load_json
from pt_data_quality.profile import constraint_weight, resolve_profile
from pt_data_quality.validation import validate_repository
from pt_data_quality.xlsx_loader import load_repository
from pt_data_quality.model import Row


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "rsr.xlsx"
SCHEMA = ROOT / "schema" / "repository-schema.json"


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_json(SCHEMA)
        cls.repo = load_repository(SOURCE, cls.schema)

    def test_expected_repository_size(self):
        self.assertEqual(163, len(self.repo.validation_targets))
        self.assertEqual(163, len(self.repo.rules))
        self.assertEqual(446, len(self.repo.constraints))
        self.assertEqual(1, len(self.repo.profiles))

    def test_current_source_has_no_validation_errors(self):
        issues = validate_repository(self.repo, self.schema)
        errors = [i for i in issues if i.severity == "error"]
        self.assertEqual([], errors)
        codes = {i.code for i in issues}
        self.assertIn("PT_MASTER_RUNTIME_TARGET_WEIGHT_CONFLICT", codes)

    def test_profile_weights_come_from_profile_defaults(self):
        profile = resolve_profile(self.repo, "PTCRIS-DATAGOV-1.0.0")
        vocab = next(c for c in self.repo.constraints if c.get("constraint_type") == "VOCABULARY")
        regex = next(c for c in self.repo.constraints if c.get("constraint_type") == "REGEX")
        presence = next(c for c in self.repo.constraints if c.get("constraint_type") == "PRESENCE")
        self.assertEqual((3.0, True), constraint_weight(profile, vocab.data))
        self.assertEqual((3.0, True), constraint_weight(profile, regex.data))
        self.assertEqual((0.0, False), constraint_weight(profile, presence.data))

    def test_build_generates_profile_based_runtime_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            build_repository(SOURCE, tmp, SCHEMA)
            runtime = Path(tmp) / "implementation" / "pt-master" / "PTCRIS-DATAGOV-1.0.0" / "1.0.0.json"
            data = json.loads(runtime.read_text(encoding="utf-8"))
            self.assertEqual(60, data["minimumRequiredScore"])
            self.assertEqual(5, data["targetWeights"]["Education.degreeType"])
            self.assertEqual(446, len(data["dataQualityRemarks"]))
            self.assertEqual(0, data["dataQualityRemarks"]["personEducationDegreeTypeMissing"]["points"])
            self.assertEqual(3.0, data["dataQualityRemarks"]["personEducationDegreeTypeInvalidVocabulary"]["points"])


    def test_profile_inheritance_reuses_parent_configuration(self):
        repo = self.repo
        child = Row(
            data={**repo.profiles[0].data, "profile_id": "PTCRIS-DATAGOV-1.1.0", "version": "1.1.0", "base_profile_id": "PTCRIS-DATAGOV-1.0.0"},
            sheet="Profiles",
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
                        "blocking_on_failure": True,
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
            base = Path(tmp) / "implementation" / "pt-master" / "PTCRIS-DATAGOV-1.0.0"
            shacl_cov = json.loads((base / "shacl" / "coverage.json").read_text(encoding="utf-8"))
            sch_cov = json.loads((base / "schematron" / "coverage.json").read_text(encoding="utf-8"))
            self.assertEqual(0, shacl_cov["boundTargets"])
            self.assertEqual(0, sch_cov["boundTargets"])
            self.assertGreater(len(shacl_cov["unboundTargets"]), 0)
            self.assertGreater(len(sch_cov["unboundTargets"]), 0)


if __name__ == "__main__":
    unittest.main()
