#!/usr/bin/env python3
"""Adversarial tests for World 02 source graph boundaries."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("world02_validator", ROOT / "scripts/validate-world02-graph.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

def load(level):
    pack = json.loads((ROOT / f"orchestration/content-packs/world02/level{level}.en.candidate.json").read_text(encoding="utf-8"))
    evidence = json.loads((ROOT / f"orchestration/content-sources/world02-level{level}-page-evidence.json").read_text(encoding="utf-8"))
    return pack, evidence

PACK11, EVIDENCE11 = load(11)
PACK12, EVIDENCE12 = load(12)

class LevelElevenBoundaryTests(unittest.TestCase):
    def test_complete_source_slice(self):
        counts = validator.validate(PACK11, EVIDENCE11)
        self.assertEqual(sum(counts.values()), 27)
        self.assertEqual(counts["dialogue"], 14)
        self.assertEqual({n["provenance"]["page"] for n in PACK11["nodes"]}, set(range(13,22)))

    def assert_rejected(self, edit):
        pack = copy.deepcopy(PACK11)
        edit(pack)
        with self.assertRaises(ValueError):
            validator.validate(pack, EVIDENCE11)

    def test_legacy_key_is_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][0]["fields"].__setitem__("key_acquired", "DISCIPLINE"))

    def test_renumbering_is_rejected(self):
        self.assert_rejected(lambda p: p.__setitem__("mission_id", "world02_mission_001"))

    def test_legacy_story_node_is_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][1]["fields"].__setitem__("text", "Legacy Lovable narration"))

    def test_source_page_drift_is_rejected(self):
        self.assert_rejected(lambda p: p["nodes"][20]["provenance"].__setitem__("page", 19))

    def test_glitch_correction_is_preserved(self):
        glitch = PACK11["localized_copy"][22]["fields"]
        self.assertEqual(glitch["correction_label"], "Correction:")
        self.assertIn("Future Me will be very angry", glitch["correction"])

class LevelTwelveBoundaryTests(unittest.TestCase):
    def test_complete_source_slice(self):
        counts = validator.validate(PACK12, EVIDENCE12)
        self.assertEqual(sum(counts.values()), 27)
        self.assertEqual(counts["dialogue"], 13)
        self.assertEqual(counts["system_log"], 6)
        self.assertEqual({n["provenance"]["page"] for n in PACK12["nodes"]}, set(range(22,30)))

    def assert_rejected(self, edit):
        pack = copy.deepcopy(PACK12)
        edit(pack)
        with self.assertRaises(ValueError):
            validator.validate(pack, EVIDENCE12)

    def test_rest_key_and_level_number_are_locked(self):
        self.assertEqual(PACK12["localized_copy"][0]["fields"]["key_acquired"], "REST")
        self.assertEqual(PACK12["localized_copy"][0]["fields"]["level_label"], "LEVEL 12:")

    def test_published_typo_is_preserved_not_silently_corrected(self):
        talk = PACK12["localized_copy"][23]["fields"]
        self.assertEqual(
            talk["in_story"],
            "Alio was bouncing on the bed beacuse hig brain was pumping out emergency adrenaline.",
        )

    def test_rocket_launch_sequence_is_preserved(self):
        glitch = PACK12["localized_copy"][22]["fields"]
        self.assertEqual(
            glitch["correction"],
            "Use the Rocket Launch. In the morning, don't think. Just count 5-4-3-2-1 and BLAST OFF out of bed!",
        )

    def test_secret_code_is_source_copy(self):
        self.assertEqual(PACK12["localized_copy"][26]["fields"]["code"], "“SYSTEM REBOOTING...”")

    def test_no_invented_mechanics(self):
        for pack in (PACK11, PACK12):
            for node in pack["nodes"]:
                self.assertNotIn("entitlement_id", node)
                self.assertNotIn("score", node)
                self.assertNotIn("xp", node)
            self.assertEqual(pack["supported_locales"], ["en"])
            self.assertEqual(pack["planned_locales"], ["pl-PL"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
