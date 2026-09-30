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


class GentleStepsDays0103Production(unittest.TestCase):
    BASE = ROOT / "localization/pl-PL/production/gentle-steps/days01-03"

    def test_real_days_01_03_pipeline_artifacts_are_bound_and_blind(self):
        run = load(self.BASE / "source-run.json")
        brief = load(self.BASE / "functional-brief.json")
        stored_packet = load(self.BASE / "writer-packet.json")
        candidate = load(self.BASE / "voice-master-candidate.json")
        backcheck = load(self.BASE / "bilingual-backcheck.json")
        reviews = load(self.BASE / "review-bundle.json")
        gate = load(self.BASE / "owner-voice-gate.json")

        validate_functional_brief(run, PROFILE, brief)
        generated_packet = writer_packet(run, PROFILE, brief)
        self.assertEqual(stored_packet, generated_packet)
        self.assertNotIn("source_locator", str(stored_packet))
        self.assertEqual(stored_packet["source_visibility"], "functional_brief_only")

        validate_candidate(stored_packet, candidate)
        self.assertEqual([u["id"] for u in candidate["units"]],
                         [u["id"] for u in brief["units"]])
        self.assertEqual(backcheck_packet(run, PROFILE, brief, stored_packet, candidate), backcheck)

        candidate_sha = digest(candidate)
        self.assertEqual(reviews["candidate_sha256"], candidate_sha)
        self.assertEqual(gate["candidate_sha256"], candidate_sha)
        self.assertFalse(reviews["scaleout_authorized"])
        self.assertFalse(gate["scaleout_days_04_24"])
        self.assertEqual(gate["status"], "READY_FOR_WEEK1_OWNER_REVIEW")

        stage_status = {r["stage"]: r["status"] for r in reviews["reviews"]}
        for stage in (
            "polish_usage_idiom_context", "polish_book_register",
            "breath_reset_reauthoring", "activity_instruction_completeness",
            "polish_family_language_edit", "humor_character_voice",
            "kid_parent_ear_review", "anti_coaching_translationese",
            "bilingual_fidelity_backcheck", "logic_continuity", "proofread",
        ):
            self.assertEqual(stage_status[stage], "PASS")
        self.assertEqual(stage_status["surface_qa"], "DEFERRED_WEEK1_OWNER_GATE")

        # The full release gate must remain closed until exact surface QA and
        # product owner decisions are complete.
        self.assertEqual(final_gate(run, PROFILE, stored_packet, candidate, reviews)["status"], "BLOCK")

    def test_real_days_01_03_voice_master_keeps_owner_gated_labels(self):
        candidate = load(self.BASE / "voice-master-candidate.json")
        labels = candidate["recurring_label_candidates"]
        self.assertEqual(labels["lock_state"], "OWNER_GATE")
        self.assertEqual((labels["pause"], labels["play"], labels["connection"]),
                         ("RESET", "AKCJA", "U NAS"))

        rendered = "\n".join(u["draft_pl"] for u in candidate["units"])
        for regression in (
            "najpóźniejsza litera w alfabecie",
            "Może być duża. Może być zupełnie mała.",
            "przekąska też może wygrać dzień",
            "będzie mieć urodziny",
            "jeśli jej to pasuje",
            "chwili z dzisiaj, która była fajna",
            "oddychać normalnie",
            "na swojej klatce piersiowej",
        ):
            self.assertNotIn(regression, rendered)


class GentleStepsDays0407Production(unittest.TestCase):
    BASE = ROOT / "localization/pl-PL/production/gentle-steps/days04-07"

    def test_days_04_07_pipeline_is_blind_hash_bound_and_owner_gated(self):
        run = load(self.BASE / "source-run.json")
        brief = load(self.BASE / "functional-brief.json")
        packet = load(self.BASE / "writer-packet.json")
        candidate = load(self.BASE / "voice-master-candidate.json")
        backcheck = load(self.BASE / "bilingual-backcheck.json")
        reviews = load(self.BASE / "review-bundle.json")
        gate = load(self.BASE / "week1-owner-gate.json")

        validate_functional_brief(run, PROFILE, brief)
        self.assertEqual(packet, writer_packet(run, PROFILE, brief))
        self.assertNotIn("source_locator", str(packet))
        validate_candidate(packet, candidate)
        self.assertEqual(backcheck, backcheck_packet(run, PROFILE, brief, packet, candidate))

        candidate_sha = digest(candidate)
        self.assertEqual(reviews["candidate_sha256"], candidate_sha)
        self.assertEqual(gate["candidate_days04_07_sha256"], candidate_sha)
        self.assertFalse(reviews["scaleout_authorized"])
        self.assertFalse(gate["scaleout_days08_24"])

        stages = {r["stage"]: r["status"] for r in reviews["reviews"]}
        for stage in (
            "polish_usage_idiom_context", "polish_book_register",
            "breath_reset_reauthoring", "activity_instruction_completeness",
            "polish_family_language_edit", "humor_character_voice", "kid_parent_ear_review",
            "anti_coaching_translationese", "bilingual_fidelity_backcheck",
            "logic_continuity", "proofread",
        ):
            self.assertEqual(stages[stage], "PASS")
        self.assertEqual(stages["surface_qa"], "DEFERRED_WEEK1_OWNER_GATE")

    def test_week1_labels_remain_working_not_locked(self):
        candidate = load(self.BASE / "voice-master-candidate.json")
        labels = candidate["recurring_label_candidates"]
        self.assertEqual(labels["lock_state"], "OWNER_GATE")
        self.assertEqual((labels["pause"], labels["play"], labels["connection"]),
                         ("RESET", "AKCJA", "U NAS"))

    def test_days_04_07_known_translationese_regressions_absent(self):
        candidate = load(self.BASE / "voice-master-candidate.json")
        rendered = "\n".join(u["draft_pl"] for u in candidate["units"])
        for regression in (
            "i jedziecie dalej",
            "Finał: prowadzi najstarsza osoba",
            "Może mieszać wychylenia i kroki",
            "równowaga rośnie",
            "dom jest zbudowany z dźwięków",
            "spokój może podróżować",
            "wspólny oddech przepływa",
            "cichy bohater",
        ):
            self.assertNotIn(regression, rendered)


class GentleStepsDays0814Production(unittest.TestCase):
    BASE = ROOT / "localization/pl-PL/production/gentle-steps/days08-14"

    def test_days_08_14_pipeline_is_blind_hash_bound_and_reviewed(self):
        run = load(self.BASE / "source-run.json")
        brief = load(self.BASE / "functional-brief.json")
        packet = load(self.BASE / "writer-packet.json")
        candidate = load(self.BASE / "voice-master-candidate.json")
        backcheck = load(self.BASE / "bilingual-backcheck.json")
        reviews = load(self.BASE / "review-bundle.json")
        gate = load(self.BASE / "batch-gate.json")

        validate_functional_brief(run, PROFILE, brief)
        self.assertEqual(packet, writer_packet(run, PROFILE, brief))
        self.assertNotIn("source_locator", str(packet))
        validate_candidate(packet, candidate)
        self.assertEqual(backcheck, backcheck_packet(run, PROFILE, brief, packet, candidate))

        candidate_sha = digest(candidate)
        self.assertEqual(reviews["candidate_sha256"], candidate_sha)
        self.assertEqual(gate["candidate_sha256"], candidate_sha)
        self.assertTrue(reviews["scaleout_authorized"])
        self.assertTrue(gate["next_batch_days15_24_authorized"])
        self.assertFalse(gate["publication_authorized"])

        stages = {r["stage"]: r["status"] for r in reviews["reviews"]}
        for stage in (
            "polish_usage_idiom_context", "polish_book_register",
            "breath_reset_reauthoring", "activity_instruction_completeness",
            "polish_family_language_edit", "humor_character_voice",
            "kid_parent_ear_review", "anti_coaching_translationese",
            "bilingual_fidelity_backcheck", "logic_continuity", "proofread",
        ):
            self.assertEqual(stages[stage], "PASS")
        self.assertEqual(stages["surface_qa"], "DEFERRED_FULL_BOOK_OWNER_GATE")

    def test_days_08_14_detail_and_anti_mindfulness_regressions(self):
        candidate = load(self.BASE / "voice-master-candidate.json")
        rendered = "\n".join(u["draft_pl"] for u in candidate["units"])
        for required in (
            "dwa albo trzy pełne okrążenia",
            "dokładnie pięcioma pojedynczymi słowami",
            "trzy słowa muszą być prawdziwymi wskazówkami",
            "dwa słowa mają być całkowicie absurdalnymi kłamstwami",
            "przeciwnie do ruchu wskazówek zegara",
            "nie puszczajcie żadnej dłoni",
        ):
            self.assertIn(required, rendered)
        for regression in (
            "złote światło",
            "wewnętrzna rzeka",
            "energia pokoju",
            "ciepło przepływa między wami",
            "i jedziecie dalej",
        ):
            self.assertNotIn(regression, rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
