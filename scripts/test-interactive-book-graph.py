#!/usr/bin/env python3
"""Positive and adversarial tests for the published World 01 graph boundary."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("graph_validator", ROOT / "scripts/validate-interactive-book-graph.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)
PACK = json.loads((ROOT / "orchestration/content-packs/world01/level1.en.candidate.json").read_text(encoding="utf-8"))
EVIDENCE = json.loads((ROOT / "orchestration/content-sources/world01-level1-page-evidence.json").read_text(encoding="utf-8"))
PACK2 = json.loads((ROOT / "orchestration/content-packs/world01/level2.en.candidate.json").read_text(encoding="utf-8"))
EVIDENCE2 = json.loads((ROOT / "orchestration/content-sources/world01-level2-page-evidence.json").read_text(encoding="utf-8"))
PACK3 = json.loads((ROOT / "orchestration/content-packs/world01/level3.en.candidate.json").read_text(encoding="utf-8"))
EVIDENCE3 = json.loads((ROOT / "orchestration/content-sources/world01-level3-page-evidence.json").read_text(encoding="utf-8"))
PACK4 = json.loads((ROOT / "orchestration/content-packs/world01/level4.en.candidate.json").read_text(encoding="utf-8"))
EVIDENCE4 = json.loads((ROOT / "orchestration/content-sources/world01-level4-page-evidence.json").read_text(encoding="utf-8"))


class GraphBoundaryTests(unittest.TestCase):
    def test_published_level_one_is_complete(self):
        counts = validator.validate(PACK, EVIDENCE)
        self.assertEqual(sum(counts.values()), 26)
        self.assertEqual(counts["dialogue"], 10)
        self.assertEqual([node["provenance"]["page"] for node in PACK["nodes"]][0], 15)
        self.assertEqual([node["provenance"]["page"] for node in PACK["nodes"]][-1], 22)

    def assert_rejected(self, edit):
        pack = copy.deepcopy(PACK)
        edit(pack)
        with self.assertRaises(ValueError):
            validator.validate(pack, EVIDENCE)

    def test_wrong_speaker_rejected(self):
        self.assert_rejected(lambda p: p["nodes"][2].__setitem__("speaker_id", "mimi"))

    def test_dialogue_order_rejected(self):
        self.assert_rejected(lambda p: p["nodes"].__setitem__(slice(2, 4), list(reversed(p["nodes"][2:4]))))

    def test_page_drift_rejected(self):
        self.assert_rejected(lambda p: p["nodes"][10]["provenance"].__setitem__("page", 17))

    def test_app_only_subtitle_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][0]["fields"].__setitem__("subtitle", "Ready to play?"))

    def test_app_only_console_sentence_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][21]["fields"].__setitem__("in_story", "New app narration"))

    def test_changed_source_hash_rejected(self):
        self.assert_rejected(lambda p: p["source"].__setitem__("source_sha256", "0" * 64))

    def test_extra_unsourced_node_rejected(self):
        self.assert_rejected(lambda p: p["nodes"].append(copy.deepcopy(p["nodes"][-1])))

    def test_missing_published_node_rejected(self):
        self.assert_rejected(lambda p: p["nodes"].pop(10))

    def test_unsupported_locale_rejected(self):
        self.assert_rejected(lambda p: p.__setitem__("supported_locales", ["en", "pl-PL"]))

    def test_hidden_entitlement_rejected(self):
        self.assert_rejected(lambda p: p["nodes"][0].__setitem__("entitlement_id", "premium"))

    def test_branching_transition_rejected(self):
        self.assert_rejected(lambda p: p["nodes"][0].__setitem__("next_id", p["nodes"][3]["node_id"]))

    def test_wrong_type_rejected(self):
        self.assert_rejected(lambda p: p["nodes"][19].__setitem__("node_type", "puzzle"))

    def test_split_visual_speech_bubble_rejected(self):
        self.assert_rejected(lambda p: p["nodes"].insert(12, copy.deepcopy(p["nodes"][11])))

    def test_source_ledger_tamper_detected_by_private_pdf(self):
        # Runs only when a caller supplies the canonical PDF via environment.
        import os
        pdf = os.environ.get("WORLD01_CANONICAL_PDF")
        if not pdf:
            self.skipTest("private canonical PDF not present in CI")
        changed = copy.deepcopy(EVIDENCE)
        changed["records"][2]["copy"]["text"] = "Unsupported replacement text"
        with self.assertRaises(ValueError):
            validator.verify_pdf(pdf, changed)


class LevelTwoBoundaryTests(unittest.TestCase):
    def test_published_level_two_is_complete(self):
        counts = validator.validate(PACK2, EVIDENCE2)
        self.assertEqual(sum(counts.values()), 32)
        self.assertEqual(counts["dialogue"], 15)
        self.assertEqual({n["provenance"]["page"] for n in PACK2["nodes"]}, set(range(23, 33)))

    def assert_rejected(self, edit):
        pack = copy.deepcopy(PACK2)
        edit(pack)
        with self.assertRaises(ValueError):
            validator.validate(pack, EVIDENCE2)

    def test_app_speaker_drift_rejected(self):
        self.assert_rejected(lambda p: p["nodes"][13].__setitem__("speaker_id", "nini"))

    def test_app_abridged_opening_log_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][1]["fields"].__setitem__("text", "The tragedy struck at exactly 14:03 on Tuesday on the Sidewalk of Doom."))

    def test_app_merged_speaker_bubbles_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][6]["fields"].__setitem__("text", p["localized_copy"][6]["fields"]["text"] + p["localized_copy"][7]["fields"]["text"]))

    def test_printed_order_rejected(self):
        self.assert_rejected(lambda p: p["nodes"].__setitem__(slice(23, 25), list(reversed(p["nodes"][23:25]))))

    def test_published_code_quotes_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][31]["fields"].__setitem__("code", "MY BUCKET TIPPED OVER!"))

    def test_page_boundary_rejected(self):
        self.assert_rejected(lambda p: p["nodes"][25]["provenance"].__setitem__("page", 29))

    def test_ledger_fragments_reconstruct_visual_copy(self):
        for record in EVIDENCE2["records"]:
            for field, fragments in record.get("extraction_fragments", {}).items():
                self.assertEqual(validator.normalized("".join(fragments)), validator.normalized(record["copy"][field]))

    def test_private_pdf_catches_level_two_ledger_tamper(self):
        import os
        pdf = os.environ.get("WORLD01_CANONICAL_PDF")
        if not pdf:
            self.skipTest("private canonical PDF not present in CI")
        changed = copy.deepcopy(EVIDENCE2)
        changed["records"][14]["extraction_fragments"]["text"][1] = "fake sentence"
        with self.assertRaises(ValueError):
            validator.verify_pdf(pdf, changed)


class LevelThreeBoundaryTests(unittest.TestCase):
    def test_published_level_three_is_complete(self):
        counts = validator.validate(PACK3, EVIDENCE3)
        self.assertEqual(sum(counts.values()), 30)
        self.assertEqual(counts["system_log"], 10)
        self.assertEqual({n["provenance"]["page"] for n in PACK3["nodes"]}, set(range(33, 42)))

    def assert_rejected(self, edit):
        pack = copy.deepcopy(PACK3)
        edit(pack)
        with self.assertRaises(ValueError):
            validator.validate(pack, EVIDENCE3)

    def test_app_em_dash_in_opening_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][0]["fields"].__setitem__("objective", EVIDENCE3["records"][0]["copy"]["objective"].replace(" - ", " — ")))

    def test_merged_mimi_bubbles_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][14]["fields"].__setitem__("text", p["localized_copy"][14]["fields"]["text"] + " " + p["localized_copy"][16]["fields"]["text"]))

    def test_missing_intervening_log_rejected(self):
        self.assert_rejected(lambda p: p["nodes"].pop(15))

    def test_reordered_system_log_rejected(self):
        self.assert_rejected(lambda p: p["nodes"].__setitem__(slice(6, 8), list(reversed(p["nodes"][6:8]))))

    def test_app_code_without_printed_quotes_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][29]["fields"].__setitem__("code", "I AM FARMING XP!"))

    def test_private_pdf_catches_level_three_ledger_tamper(self):
        import os
        pdf = os.environ.get("WORLD01_CANONICAL_PDF")
        if not pdf:
            self.skipTest("private canonical PDF not present in CI")
        changed = copy.deepcopy(EVIDENCE3)
        changed["records"][20]["copy"]["text"] = "Unprinted Dilo action"
        with self.assertRaises(ValueError):
            validator.verify_pdf(pdf, changed)


class LevelFourBoundaryTests(unittest.TestCase):
    def test_published_level_four_is_complete(self):
        counts = validator.validate(PACK4, EVIDENCE4)
        self.assertEqual(sum(counts.values()), 35)
        self.assertEqual(counts["dialogue"], 15)
        self.assertEqual(counts["system_log"], 11)
        self.assertEqual(counts["inventory"], 1)
        self.assertEqual({n["provenance"]["page"] for n in PACK4["nodes"]}, set(range(42, 51)))

    def assert_rejected(self, edit):
        pack = copy.deepcopy(PACK4)
        edit(pack)
        with self.assertRaises(ValueError):
            validator.validate(pack, EVIDENCE4)

    def test_app_only_subtitle_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][0]["fields"].__setitem__("subtitle", "Turning boredom into adventure"))

    def test_app_merged_page43_logs_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][3]["fields"].__setitem__("text", "Dilo rolled onto his side. Luli didn't look up from her book."))

    def test_app_abridged_alio_dialogue_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][16]["fields"].__setitem__("text", "Drop it! Drop it! Dilo said books are carnivorous!"))

    def test_printed_page47_order_rejected(self):
        self.assert_rejected(lambda p: p["nodes"].__setitem__(slice(23, 27), list(reversed(p["nodes"][23:27]))))

    def test_inventory_block_cannot_be_flattened_into_system_log(self):
        self.assert_rejected(lambda p: p["nodes"][27].__setitem__("node_type", "system_log"))

    def test_unprinted_science_label_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][33]["fields"].__setitem__("body_label", "Scientific Fact:"))

    def test_app_em_dash_in_console_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][30]["fields"].__setitem__("in_story", EVIDENCE4["records"][30]["copy"]["in_story"].replace(" - ", " — ")))

    def test_app_code_without_printed_quotes_rejected(self):
        self.assert_rejected(lambda p: p["localized_copy"][34]["fields"].__setitem__("code", "SPY GEAR OFFLINE"))

    def test_private_pdf_catches_level_four_ledger_tamper(self):
        import os
        pdf = os.environ.get("WORLD01_CANONICAL_PDF")
        if not pdf:
            self.skipTest("private canonical PDF not present in CI")
        changed = copy.deepcopy(EVIDENCE4)
        changed["records"][27]["copy"]["item"] = "Invented inventory reward"
        with self.assertRaises(ValueError):
            validator.verify_pdf(pdf, changed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
