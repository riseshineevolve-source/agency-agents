#!/usr/bin/env python3
"""Recovered World 02 Level 19 source locks and adversarial graph checks."""

import copy
import hashlib
import importlib.util
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("world02_validator", ROOT / "scripts/validate-world02-graph.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

PACK_PATH = ROOT / "orchestration/content-packs/world02/level19.en.candidate.json"
EVIDENCE_PATH = ROOT / "orchestration/content-sources/world02-level19-page-evidence.json"
PACK = json.loads(PACK_PATH.read_text(encoding="utf-8"))
EVIDENCE = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))


class LevelNineteenSourceLockTests(unittest.TestCase):
    def assert_rejected(self, edit_pack=lambda p: None, edit_evidence=lambda e: None):
        pack, evidence = copy.deepcopy(PACK), copy.deepcopy(EVIDENCE)
        edit_pack(pack)
        edit_evidence(evidence)
        with self.assertRaises(ValueError):
            validator.validate(pack, evidence)

    def test_recovered_source_pair_is_byte_exact(self):
        self.assertEqual(
            hashlib.sha256(EVIDENCE_PATH.read_bytes()).hexdigest(),
            "3015f761c6b431831f4646175ae6902c1b4e08f311d5b777a1ea888e6906a69c",
        )
        self.assertEqual(
            hashlib.sha256(PACK_PATH.read_bytes()).hexdigest(),
            "fd9cf11a23465f9b62e6d6eead0e0a576bc6dd7c033642ad934aab03df82fafb",
        )

    def test_exact_scope_counts_and_stable_ids(self):
        self.assertEqual(
            validator.validate(PACK, EVIDENCE),
            Counter(opener=1, dialogue=13, system_log=4, console=3, quest=2, science=1, secret_code=1),
        )
        self.assertEqual(PACK["source"]["page_range"], [79, 85])
        self.assertEqual(
            Counter(node["provenance"]["page"] for node in PACK["nodes"]),
            Counter({79: 1, 80: 5, 81: 4, 82: 4, 83: 4, 84: 4, 85: 3}),
        )
        self.assertEqual(
            [node["node_id"] for node in PACK["nodes"]],
            [f"world02_mission_019_node_{index:03d}" for index in range(1, 26)],
        )
        self.assertEqual([node["sequence"] for node in PACK["nodes"]], list(range(1, 26)))
        self.assertEqual(
            [node["next_id"] for node in PACK["nodes"]],
            [node["node_id"] for node in PACK["nodes"][1:]] + [None],
        )

    def test_published_dialogue_speaker_order(self):
        self.assertEqual(
            [(node["provenance"]["evidence_id"], node["speaker_id"])
             for node in PACK["nodes"] if node["node_type"] == "dialogue"],
            [("p80_b02", "mimi"), ("p80_b03", "alio"), ("p80_b05", "nini"),
             ("p81_b01", "dilo"), ("p81_b02", "mimi"), ("p81_b03", "alio"),
             ("p81_b04", "mimi"), ("p82_b01", "luli"), ("p82_b02", "dilo"),
             ("p82_b03", "alio"), ("p82_b04", "mimi"), ("p83_b02", "dilo"),
             ("p83_b03", "alio")],
        )

    def test_published_identity_and_family_code(self):
        opener = PACK["localized_copy"][0]["fields"]
        self.assertEqual(opener["level_label"], "LEVEL 19:")
        self.assertEqual(opener["title"], "The Pivot Dance")
        self.assertEqual(opener["key_acquired"], "FLEXIBILITY")
        self.assertEqual(PACK["localized_copy"][-1]["fields"]["code"], "“WE ARE PIVOTING!”")

    def test_source_copy_and_family_code_tampering_fail_closed(self):
        self.assert_rejected(lambda p: p["localized_copy"][0]["fields"].__setitem__("title", "Legacy title"))
        self.assert_rejected(lambda p: p["localized_copy"][1]["fields"].__setitem__("text", "Invented narration"))
        self.assert_rejected(lambda p: p["localized_copy"][-1]["fields"].__setitem__("code", "Changed code"))

    def test_ids_sequence_speakers_and_transitions_fail_closed(self):
        self.assert_rejected(lambda p: p["nodes"][0].__setitem__("node_id", "world02_mission_001_node_001"))
        self.assert_rejected(lambda p: p["nodes"][1].__setitem__("sequence", 99))
        self.assert_rejected(lambda p: p["nodes"][2].__setitem__("speaker_id", "dilo"))
        self.assert_rejected(lambda p: p["nodes"][2].__setitem__("next_id", None))

    def test_canonical_hash_is_required_even_if_evidence_is_also_changed(self):
        self.assert_rejected(
            lambda p: p["source"].__setitem__("source_sha256", "0" * 64),
            lambda e: e["source"].__setitem__("sha256", "0" * 64),
        )

    def test_page_and_evidence_provenance_drift_fail_closed(self):
        self.assert_rejected(lambda p: p["nodes"][2]["provenance"].__setitem__("page", 79))
        self.assert_rejected(lambda p: p["nodes"][2]["provenance"].__setitem__("evidence_id", "p80_b99"))
        self.assert_rejected(edit_evidence=lambda e: e["page_inventory"][0].__setitem__("content_blocks", 2))
        self.assert_rejected(lambda p: p["nodes"].pop())

    def test_unsupported_scope_and_invented_mechanics_fail_closed(self):
        self.assert_rejected(lambda p: p.__setitem__("mission_id", "world02_mission_020"))
        self.assert_rejected(lambda p: p.__setitem__("supported_locales", ["en", "pl-PL"]))
        self.assert_rejected(lambda p: p["nodes"][0].__setitem__("xp", 100))
        self.assert_rejected(lambda p: p.__setitem__("entitlement", "paid"))

    def test_editorial_watchlist_copy_is_not_silently_rewritten(self):
        fields = {node["provenance"]["evidence_id"]: localized["fields"]
                  for node, localized in zip(PACK["nodes"], PACK["localized_copy"])}
        self.assertIn("placed a fan behind the toaster", fields["p82_b01"]["text"])
        self.assertIn("It feels physically painful.", fields["p84_b01"]["science"])
        self.assertIn("a blood oath", fields["p84_b03"]["science"])
        self.assertIn("physically burns off the stress chemicals", fields["p85_b02"]["body"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
