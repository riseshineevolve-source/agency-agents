#!/usr/bin/env python3
"""Adversarial tests for the World 02 Level 11 source boundary."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("world02_validator", ROOT / "scripts/validate-world02-graph.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)
PACK = json.loads((ROOT / "orchestration/content-packs/world02/level11.en.candidate.json").read_text(encoding="utf-8"))
EVIDENCE = json.loads((ROOT / "orchestration/content-sources/world02-level11-page-evidence.json").read_text(encoding="utf-8"))

class LevelElevenBoundaryTests(unittest.TestCase):
    def test_complete_source_slice(self):
        counts = validator.validate(PACK, EVIDENCE)
        self.assertEqual(sum(counts.values()), 27)
        self.assertEqual(counts["dialogue"], 14)
        self.assertEqual(counts["system_log"], 5)
        self.assertEqual({n["provenance"]["page"] for n in PACK["nodes"]}, set(range(13,22)))

    def assert_rejected(self, edit):
        pack = copy.deepcopy(PACK)
        edit(pack)
        with self.assertRaises(ValueError):
            validator.validate(pack, EVIDENCE)

    def test_legacy_key_is_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][0]["fields"].__setitem__("key_acquired", "DISCIPLINE"))

    def test_renumbering_to_level_one_is_rejected(self):
        self.assert_rejected(lambda p: p.__setitem__("mission_id", "world02_mission_001"))

    def test_legacy_story_node_is_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][1]["fields"].__setitem__("text", "Legacy Lovable narration"))

    def test_speaker_order_drift_is_rejected(self):
        self.assert_rejected(lambda p: p["nodes"][2].__setitem__("speaker_id", "dilo"))

    def test_source_page_drift_is_rejected(self):
        self.assert_rejected(lambda p: p["nodes"][20]["provenance"].__setitem__("page", 19))

    def test_glitch_correction_is_preserved(self):
        glitch = next(c["fields"] for c in PACK["localized_copy"] if c["node_id"] == "world02_mission_011_node_023")
        self.assertEqual(glitch["correction_label"], "Correction:")
        self.assertIn("Future Me will be very angry", glitch["correction"])

    def test_no_invented_entitlement_or_score(self):
        for node in PACK["nodes"]:
            self.assertNotIn("entitlement_id", node)
            self.assertNotIn("score", node)
            self.assertNotIn("xp", node)

    def test_pl_is_not_enabled(self):
        self.assertEqual(PACK["supported_locales"], ["en"])
        self.assertEqual(PACK["planned_locales"], ["pl-PL"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
