#!/usr/bin/env python3
"""Exact canonical World 02 Level 18 graph regressions and fail-closed guards."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("world02_validator", ROOT / "scripts/validate-world02-graph.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

PACK = json.loads((ROOT / "orchestration/content-packs/world02/level18.en.candidate.json").read_text(encoding="utf-8"))
EVIDENCE = json.loads((ROOT / "orchestration/content-sources/world02-level18-page-evidence.json").read_text(encoding="utf-8"))


class LevelEighteenSourceLockTests(unittest.TestCase):
    def test_exact_scope_counts_and_speaker_order(self):
        counts = validator.validate(PACK, EVIDENCE)
        self.assertEqual(sum(counts.values()), 24)
        self.assertEqual(counts["dialogue"], 10)
        self.assertEqual(counts["system_log"], 6)
        self.assertEqual(PACK["source"]["page_range"], [72, 78])
        self.assertEqual(
            [n["provenance"]["page"] for n in PACK["nodes"]],
            [record["page"] for record in EVIDENCE["records"]],
        )
        self.assertEqual(
            [n["speaker_id"] for n in PACK["nodes"]],
            [record["speaker_id"] for record in EVIDENCE["records"]],
        )

    def test_published_identity_and_family_code(self):
        opener = PACK["localized_copy"][0]["fields"]
        self.assertEqual(opener["level_label"], "LEVEL 18:")
        self.assertEqual(opener["title"], "The Pixel Zombie")
        self.assertEqual(opener["key_acquired"], "BALANCE")
        self.assertEqual(PACK["localized_copy"][-1]["fields"]["code"], "“I NEED GREEN ENERGY”")
        self.assertEqual(PACK["supported_locales"], ["en"])
        self.assertEqual(PACK["planned_locales"], ["pl-PL"])

    def assert_rejected(self, edit):
        pack = copy.deepcopy(PACK)
        edit(pack)
        with self.assertRaises(ValueError):
            validator.validate(pack, EVIDENCE)

    def test_canonical_copy_changes_fail_closed(self):
        self.assert_rejected(lambda p: p["localized_copy"][0]["fields"].__setitem__("title", "Legacy title"))
        self.assert_rejected(lambda p: p["localized_copy"][-1]["fields"].__setitem__("code", "Changed family code"))

    def test_speaker_provenance_and_sequence_drift_fail_closed(self):
        self.assert_rejected(lambda p: p["nodes"][5].__setitem__("speaker_id", "dilo"))
        self.assert_rejected(lambda p: p["nodes"][5]["provenance"].__setitem__("page", 72))
        self.assert_rejected(lambda p: p["nodes"][5].__setitem__("sequence", 100))

    def test_uninvented_mechanics_and_unsupported_locales(self):
        self.assert_rejected(lambda p: p["nodes"][0].__setitem__("xp", 100))
        self.assert_rejected(lambda p: p.__setitem__("entitlement", "paid"))
        self.assert_rejected(lambda p: p.__setitem__("supported_locales", ["en", "pl-PL"]))
        for node in PACK["nodes"]:
            for forbidden in ("xp", "score", "rewards", "entitlement_id", "backend"):
                self.assertNotIn(forbidden, node)


if __name__ == "__main__":
    unittest.main(verbosity=2)
