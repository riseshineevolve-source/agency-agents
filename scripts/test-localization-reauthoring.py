#!/usr/bin/env python3
from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from localization.contracts import require
from localization.io import ContractError, digest, load
from localization.reauthoring import (
    init_run, validate_functional_brief, writer_packet, validate_candidate,
    backcheck_packet, final_gate,
)

PROFILE = load(ROOT / "localization/pl-PL/engine/reauthoring/gentle-steps.json")


class NativeReauthoring(unittest.TestCase):
    def setup(self):
        td = tempfile.TemporaryDirectory()
        source = Path(td.name) / "english-source.txt"
        source.write_text("Synthetic English source. Do not expose this sentence to the native writer.", encoding="utf-8")
        run = init_run(source, "synthetic-revision", PROFILE)
        brief = {
            "format": "rse-functional-brief-v1",
            "product": "gentle-steps-christmas",
            "source_sha256": run["source_sha256"],
            "profile_sha256": run["profile_sha256"],
            "units": [{
                "id": "GS.D01.MM",
                "source_locator": "synthetic:p1:block1",
                "surface_type": "body_block",
                "audience": "family",
                "function": "Create a short shared pause before the playful activity.",
                "mechanics": ["Sit together.", "Keep the pause to one minute."],
                "immutable_facts": ["Duration is one minute."],
                "character_roles": ["Luli provides a dry micro-joke after the instruction."],
                "safety_claim_boundaries": ["Do not promise a guaranteed emotional outcome."],
                "tone_job": "Low-pressure family pause with a small knowing smile.",
                "humor_room": "Domestic reality is allowed if it does not change the task.",
                "cultural_friction": "Avoid imported mindfulness vocabulary.",
                "wording_is_disposable": True,
            }],
        }
        return td, source, run, brief

    def candidate(self, packet):
        return {
            "format": "rse-native-pl-candidate-v1",
            "product": packet["product"],
            "brief_sha256": packet["brief_sha256"],
            "authoring_basis": "functional_brief_only",
            "units": [{"id": "GS.D01.MM", "draft_pl": "Przez minutę niczego nie przyspieszamy. Nawet grudnia."}],
        }

    def test_writer_is_isolated_from_sentence_level_english(self):
        td, source, run, brief = self.setup()
        try:
            packet = writer_packet(run, PROFILE, brief)
            rendered = str(packet)
            self.assertNotIn("Synthetic English source", rendered)
            self.assertNotIn("source_locator", rendered)
            self.assertEqual(packet["source_visibility"], "functional_brief_only")
            self.assertEqual(packet["authoring_mode"], "from_function_not_from_english_wording")
        finally:
            td.cleanup()

    def test_brief_rejects_source_or_target_copy_leak(self):
        td, source, run, brief = self.setup()
        try:
            for key, value in [
                ("source_text", "Do this in English."),
                ("source_excerpt", "Copied phrase"),
                ("literal_translation", "Dosłowna wersja"),
                ("draft_pl", "Gotowy tekst"),
            ]:
                leaked = copy.deepcopy(brief)
                leaked["units"][0][key] = value
                with self.assertRaises(ContractError):
                    validate_functional_brief(run, PROFILE, leaked)
        finally:
            td.cleanup()

    def test_candidate_must_attest_brief_only_authoring_and_exact_units(self):
        td, source, run, brief = self.setup()
        try:
            packet = writer_packet(run, PROFILE, brief)
            candidate = self.candidate(packet)
            self.assertEqual(validate_candidate(packet, candidate), candidate)
            bad = copy.deepcopy(candidate)
            bad["authoring_basis"] = "looked_at_english"
            with self.assertRaises(ContractError):
                validate_candidate(packet, bad)
            bad = copy.deepcopy(candidate)
            bad["units"][0]["id"] = "WRONG"
            with self.assertRaises(ContractError):
                validate_candidate(packet, bad)
        finally:
            td.cleanup()

    def test_backcheck_reopens_source_only_after_native_first_write(self):
        td, source, run, brief = self.setup()
        try:
            packet = writer_packet(run, PROFILE, brief)
            candidate = self.candidate(packet)
            back = backcheck_packet(run, PROFILE, brief, packet, candidate)
            self.assertEqual(back["source_file"], str(source))
            self.assertEqual(back["units"][0]["source_locator"], "synthetic:p1:block1")
            self.assertEqual(back["units"][0]["final_pl_for_review"], candidate["units"][0]["draft_pl"])
            self.assertIn("Do not rewrite Polish toward English syntax", back["instruction"])
        finally:
            td.cleanup()

    def test_final_gate_requires_all_independent_reviews_and_owner_gates(self):
        td, source, run, brief = self.setup()
        try:
            packet = writer_packet(run, PROFILE, brief)
            candidate = self.candidate(packet)
            candidate_sha = digest(candidate)
            reviews = {
                "format": "rse-reauthor-review-bundle-v1",
                "candidate_sha256": candidate_sha,
                "reviews": [
                    {"stage": stage, "reviewer": "synthetic-independent-role", "status": "PASS", "candidate_sha256": candidate_sha}
                    for stage in PROFILE["required_review_stages"]
                ],
                "owner_decisions": {},
            }
            result = final_gate(run, PROFILE, packet, candidate, reviews)
            self.assertEqual(result["status"], "READY_FOR_OWNER_GATE")
            self.assertEqual(set(result["unresolved_owner_gates"]), set(PROFILE["owner_gates"]))

            approved = copy.deepcopy(reviews)
            approved["owner_decisions"] = {
                gate: {"status": "APPROVED", "candidate_sha256": candidate_sha}
                for gate in PROFILE["owner_gates"]
            }
            self.assertEqual(final_gate(run, PROFILE, packet, candidate, approved)["status"], "PASS")

            broken = copy.deepcopy(reviews)
            broken["reviews"][0]["status"] = "FIX"
            self.assertEqual(final_gate(run, PROFILE, packet, candidate, broken)["status"], "BLOCK")
        finally:
            td.cleanup()


if __name__ == "__main__":
    unittest.main(verbosity=2)
