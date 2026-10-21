#!/usr/bin/env python3
"""Regression and adversarial checks for the bounded World 02 endgame source pack."""

import copy
import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


validator = module("endgame_validator", "validate-world02-endgame.py")
builder = module("endgame_builder", "build-world02-endgame.py")


class EndgameSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evidence = json.loads((ROOT / validator.EVIDENCE_REL).read_text(encoding="utf-8"))
        cls.pack = json.loads((ROOT / validator.PACK_REL).read_text(encoding="utf-8"))

    def test_full_published_page_coverage(self):
        validator.validate(self.pack, self.evidence)
        self.assertEqual([p["page"] for p in self.pack["page_inventory"]], list(range(93, 105)))
        self.assertEqual(len(self.pack["nodes"]), 95)

    def test_deterministic_rebuild_matches_candidate(self):
        self.assertEqual(builder.build(self.evidence), self.pack)
        self.assertEqual(builder.build(self.evidence), builder.build(self.evidence))

    def test_cutout_and_reference_duplicate_have_distinct_provenance(self):
        records = self.evidence["records"]
        rows = lambda page: [r for r in records if r["page"] == page and r["type"] == "loadout_row"]
        self.assertEqual(len(rows(97)), 12)
        self.assertEqual([r["copy"] for r in rows(97)], [r["copy"] for r in rows(99)])
        self.assertEqual([r["source_features"]["row_id"] for r in rows(97)],
                         [r["source_features"]["row_id"] for r in rows(99)])
        self.assertTrue(all(a["node_id"] != b["node_id"] for a, b in zip(rows(97), rows(99))))
        roles = {p["page"]: p.get("print_role") for p in self.pack["page_inventory"]}
        self.assertEqual([roles[p] for p in (97, 98, 99)],
                         ["cutout_front", "cutout_reverse", "reference_duplicate"])

    def test_printed_emergency_variants_remain_distinct(self):
        records = self.evidence["records"]
        full = [r["copy"]["code"] for r in records if r["type"] == "emergency_code"]
        short = [r["copy"]["code"].replace("\n", " ") for r in records
                 if r["page"] == 97 and r["type"] == "loadout_row"][-2:]
        self.assertEqual(full, ["“CAPTAIN, YOUR LIZARD IS DRIVING!”", "“CAPTAIN IS ON 1% BATTERY.”"])
        self.assertEqual(short, ["CAPTAIN ON 1% BATTERY", "LIZARD IS DRIVING!"])

    def test_all_ten_loadout_codes_match_canonical_world02_missions(self):
        normalize = lambda s: re.sub(r"\s+", " ", s.strip('“”\"')).strip()
        rows = [r for r in self.evidence["records"] if r["page"] == 97
                and r["type"] == "loadout_row" and r["source_features"]["level"]]
        for row in rows:
            level = row["source_features"]["level"]
            mission = json.loads((ROOT / f"orchestration/content-packs/world02/level{level}.en.candidate.json")
                                 .read_text(encoding="utf-8"))
            secret = next(n for n in mission["nodes"] if n["node_type"] == "secret_code")
            code = next(c for c in mission["localized_copy"] if c["node_id"] == secret["node_id"])["fields"]["code"]
            self.assertEqual(normalize(row["copy"]["code"]), normalize(code), f"Level {level}")

    def test_source_forms_are_four_blank_writing_fields(self):
        forms = [n for n in self.pack["nodes"] if n["node_type"] == "blank_form"]
        fields = [f for n in forms for f in n["source_features"]["writable_fields"]]
        self.assertEqual([f["field_id"] for f in fields], ["secret_code", "meaning", "operation", "player_name"])
        self.assertTrue(all(f["value"] == "" for f in fields))

    def test_qr_target_is_source_decoded_hub(self):
        qr = [r for r in self.evidence["records"] if r["type"] == "qr_link"]
        self.assertEqual(qr[0]["copy"]["target"], "https://rise-shine-evolve-learning-hub.com/")

    def test_source_artwork_is_not_fabricated_copy(self):
        artwork = [n for n in self.pack["nodes"] if n["node_type"] == "artwork"][0]
        content = next(c for c in self.pack["localized_copy"] if c["node_id"] == artwork["node_id"])
        self.assertEqual(content["fields"], {})
        self.assertIn("not yet exported", artwork["source_features"]["description"])

    def test_rejects_copy_tamper(self):
        pack = copy.deepcopy(self.pack)
        pack["localized_copy"][0]["fields"]["heading"] = "New completion game"
        with self.assertRaisesRegex(ValueError, "copy differs"):
            validator.validate(pack, self.evidence)

    def test_rejects_coordinated_copy_and_evidence_tamper(self):
        pack, evidence = copy.deepcopy(self.pack), copy.deepcopy(self.evidence)
        evidence["records"][0]["copy"]["heading"] = "New completion game"
        pack["localized_copy"][0]["fields"] = evidence["records"][0]["copy"]
        with self.assertRaisesRegex(ValueError, "evidence hash"):
            validator.validate(pack, evidence)

    def test_rejects_missing_printed_duplicate(self):
        pack = copy.deepcopy(self.pack)
        pack["nodes"] = [n for n in pack["nodes"] if n["provenance"]["page"] != 99]
        with self.assertRaisesRegex(ValueError, "count differs"):
            validator.validate(pack, self.evidence)

    def test_rejects_reordered_graph_or_provenance(self):
        for field, value in [("sequence", 99), ("next_id", None)]:
            pack = copy.deepcopy(self.pack)
            pack["nodes"][0][field] = value
            with self.assertRaises(ValueError):
                validator.validate(pack, self.evidence)
        pack = copy.deepcopy(self.pack)
        pack["nodes"][0]["provenance"]["page"] = 96
        with self.assertRaisesRegex(ValueError, "provenance"):
            validator.validate(pack, self.evidence)

    def test_rejects_world01_and_public_release_drift(self):
        for field, value in [("product_id", "level_up_your_brain_world_01"),
                             ("release_status", "published"), ("scope_id", "world02_mission_021")]:
            pack = copy.deepcopy(self.pack)
            pack[field] = value
            with self.assertRaisesRegex(ValueError, "drift"):
                validator.validate(pack, self.evidence)

    def test_rejects_added_timer_and_prefilled_form(self):
        pack = copy.deepcopy(self.pack)
        pack["nodes"][0]["source_features"]["countdown_seconds"] = 3
        with self.assertRaisesRegex(ValueError, "source features"):
            validator.validate(pack, self.evidence)
        pack = copy.deepcopy(self.pack)
        form = next(n for n in pack["nodes"] if n["node_type"] == "blank_form")
        form["source_features"]["writable_fields"][0]["value"] = "Captain"
        with self.assertRaisesRegex(ValueError, "source features"):
            validator.validate(pack, self.evidence)

    def test_builder_rejects_unlocked_evidence(self):
        evidence = copy.deepcopy(self.evidence)
        evidence["records"].pop()
        with self.assertRaisesRegex(ValueError, "evidence hash"):
            builder.build(evidence)


if __name__ == "__main__":
    unittest.main()
