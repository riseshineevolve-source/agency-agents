#!/usr/bin/env python3
"""Canonical-pixel-verified Level 20 graph and fail-closed provenance checks."""

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
PACK_PATH = ROOT / "orchestration/content-packs/world02/level20.en.candidate.json"
EVIDENCE_PATH = ROOT / "orchestration/content-sources/world02-level20-page-evidence.json"
PACK = json.loads(PACK_PATH.read_text(encoding="utf-8"))
EVIDENCE = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))


class LevelTwentySourceLockTests(unittest.TestCase):
    def assert_rejected(self, edit_pack=lambda p: None, edit_evidence=lambda e: None):
        pack, evidence = copy.deepcopy(PACK), copy.deepcopy(EVIDENCE)
        edit_pack(pack)
        edit_evidence(evidence)
        with self.assertRaises(ValueError):
            validator.validate(pack, evidence)

    def test_exact_source_pair_hashes(self):
        self.assertEqual(
            hashlib.sha256(EVIDENCE_PATH.read_bytes()).hexdigest(),
            "a2e3a9929d9564378c266a1f64bc895798df6b5b892923c8da81b3143282cd4c",
        )
        self.assertEqual(
            hashlib.sha256(PACK_PATH.read_bytes()).hexdigest(),
            "844fc6392027ba5272f645491775adb3c8be9c1ecd537ae313a719cee5de511c",
        )

    def test_exact_scope_counts_ids_sequence_and_transitions(self):
        self.assertEqual(
            validator.validate(PACK, EVIDENCE),
            Counter(opener=1, dialogue=13, system_log=6, console=3, quest=2, science=1, secret_code=1),
        )
        self.assertEqual(PACK["source"]["page_range"], [86, 92])
        self.assertEqual(
            Counter(node["provenance"]["page"] for node in PACK["nodes"]),
            Counter({86: 1, 87: 5, 88: 5, 89: 4, 90: 5, 91: 4, 92: 3}),
        )
        self.assertEqual(
            [node["node_id"] for node in PACK["nodes"]],
            [f"world02_mission_020_node_{index:03d}" for index in range(1, 28)],
        )
        self.assertEqual([node["sequence"] for node in PACK["nodes"]], list(range(1, 28)))
        self.assertEqual(
            [node["next_id"] for node in PACK["nodes"]],
            [node["node_id"] for node in PACK["nodes"][1:]] + [None],
        )
        contract = json.loads((ROOT / "orchestration/content-sources/world02-level18-20-promotion-contract.json").read_text())
        self.assertEqual(contract["levels"]["20"]["types"], dict(validator.validate(PACK, EVIDENCE)))
        self.assertEqual(contract["levels"]["20"]["nodes"], len(PACK["nodes"]))
        self.assertEqual(contract["levels"]["20"]["pages"], PACK["source"]["page_range"])

    def test_published_dialogue_speaker_order(self):
        self.assertEqual(
            [(node["provenance"]["evidence_id"], node["speaker_id"])
             for node in PACK["nodes"] if node["node_type"] == "dialogue"],
            [("p87_b02", "dilo"), ("p87_b04", "alio"),
             ("p88_b01", "alio"), ("p88_b02", "dilo"), ("p88_b03", "alio"), ("p88_b04", "nini"),
             ("p89_b01", "dilo"), ("p89_b02", "luli"), ("p89_b03", "dilo"), ("p89_b04", "luli"),
             ("p90_b01", "mimi"), ("p90_b03", "alio"), ("p90_b05", "dilo")],
        )

    def test_stale_derived_twelve_dialogue_seven_log_counts_fail_closed(self):
        # The printed MIMI bubble at p90_b01 is dialogue. A matching edit to both
        # graph and ledger must not restore the erroneous historical 12/7 split.
        self.assert_rejected(
            lambda p: p["nodes"][15].update(node_type="system_log", speaker_id="system"),
            lambda e: e["records"][15].update(type="system_log", speaker_id="system"),
        )

    def test_opener_identity_and_published_family_code(self):
        opener = PACK["localized_copy"][0]["fields"]
        self.assertEqual(opener["level_label"], "LEVEL 20:")
        self.assertEqual(opener["title"], "The Reality Glitch")
        self.assertEqual(opener["key_acquired"], "TRUTH DETECTOR")
        self.assertEqual(opener["objective"], "How to spot Fake News and Deepfakes in the wild.")
        self.assertEqual(PACK["localized_copy"][-1]["fields"]["code"], "“PAUSE AND ZOOM”")

    def test_split_pdf_spans_are_restored_to_printed_bubble_order(self):
        self.assertEqual(
            PACK["localized_copy"][2]["fields"]["text"],
            "GUYS! LOOK! The President is playing Minecraft with a polar bear! It's LIVE!",
        )
        self.assertEqual(
            PACK["localized_copy"][7]["fields"]["text"],
            "Why? It's amazing! Two million people watched it!",
        )

    def test_console_bullets_and_correction_are_source_copy(self):
        tool = PACK["localized_copy"][21]["fields"]
        self.assertEqual(tool["file_label"], "// FILE: 059")
        self.assertEqual(tool["science"].count("• "), 3)
        self.assertIn("• Shadows: Do they match the light source in the background?", tool["science"])
        glitch = PACK["localized_copy"][22]["fields"]
        self.assertEqual(glitch["correction_label"], "Correction:")
        self.assertEqual(
            glitch["correction"],
            "Adopt the 'Skeptical Scientist' mindset. Always ask: 'Is this real, or is it a cool edit?'",
        )

    def test_science_watchlist_copy_is_not_silently_rewritten(self):
        self.assertIn("AI is famously bad at drawing fingers", PACK["localized_copy"][21]["fields"]["science"])
        self.assertIn("Visual Confirmation Bias", PACK["localized_copy"][20]["fields"]["science"])
        science = PACK["localized_copy"][25]["fields"]["body"]
        self.assertIn("shoot straight into the Amygdala", science)
        self.assertIn("Fake news spreads 6 times faster than real news", science)

    def test_reader_copy_tampering_fails_closed(self):
        self.assert_rejected(lambda p: p["localized_copy"][0]["fields"].__setitem__("title", "Legacy title"))
        self.assert_rejected(lambda p: p["localized_copy"][2]["fields"].__setitem__("text", "Invented speech"))
        self.assert_rejected(lambda p: p["localized_copy"][-1]["fields"].__setitem__("code", "Changed code"))

    def test_graph_identity_speaker_and_provenance_tampering_fail_closed(self):
        self.assert_rejected(lambda p: p["nodes"][2].__setitem__("speaker_id", "alio"))
        self.assert_rejected(lambda p: p["nodes"][0].__setitem__("node_id", "world02_mission_019_node_001"))
        self.assert_rejected(lambda p: p["nodes"][2].__setitem__("sequence", 99))
        self.assert_rejected(lambda p: p["nodes"][2].__setitem__("next_id", None))
        self.assert_rejected(lambda p: p["nodes"][2]["provenance"].__setitem__("page", 88))
        self.assert_rejected(lambda p: p["nodes"][2]["provenance"].__setitem__("evidence_id", "p87_b99"))

    def test_canonical_hash_and_page_inventory_fail_closed(self):
        self.assert_rejected(
            lambda p: p["source"].__setitem__("source_sha256", "0" * 64),
            lambda e: e["source"].__setitem__("sha256", "0" * 64),
        )
        self.assert_rejected(edit_evidence=lambda e: e["page_inventory"][0].__setitem__("content_blocks", 2))
        self.assert_rejected(lambda p: p["nodes"].pop())

    def test_new_mechanics_locales_and_endgame_scope_fail_closed(self):
        self.assert_rejected(lambda p: p["nodes"][0].__setitem__("xp", 100))
        self.assert_rejected(lambda p: p.__setitem__("entitlement", "paid"))
        self.assert_rejected(lambda p: p.__setitem__("supported_locales", ["en", "pl-PL"]))
        self.assert_rejected(lambda p: p["source"].__setitem__("page_range", [86, 104]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
