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
                         ("ZWOLNIJ", "GRAMY", "MIĘDZY NAMI"))

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
                         ("ZWOLNIJ", "GRAMY", "MIĘDZY NAMI"))

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


class GentleStepsDays1521Production(unittest.TestCase):
    BASE = ROOT / "localization/pl-PL/production/gentle-steps/days15-21"

    def test_days_15_21_pipeline_is_blind_hash_bound_and_reviewed(self):
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
        self.assertTrue(gate["next_batch_days22_24_authorized"])
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

    def test_days_15_21_detail_safety_and_register_regressions(self):
        candidate = load(self.BASE / "voice-master-candidate.json")
        rendered = "\n".join(u["draft_pl"] for u in candidate["units"])
        for required in (
            "przez 15 sekund",
            "dokładne wskazówki krok po kroku",
            "W dwie osoby",
            "trzy razy od początku do końca",
            "dwie różne fale",
            "przeciwnie do ruchu wskazówek zegara",
        ):
            self.assertIn(required, rendered)
        for regression in (
            "chciałbym / chciałabym",
            "Tunel dopingu",
            "i jedziecie dalej",
            "wewnętrzne światło",
            "ciepło przepływa między wami",
        ):
            self.assertNotIn(regression, rendered)


class GentleStepsDays2224Production(unittest.TestCase):
    BASE = ROOT / "localization/pl-PL/production/gentle-steps/days22-24"

    def test_days_22_24_pipeline_is_blind_hash_bound_and_reviewed(self):
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
        self.assertFalse(reviews["scaleout_authorized"])
        self.assertFalse(gate["publication_authorized"])
        self.assertEqual(gate["status"], "READY_FOR_FULL_DAYS_01_24_AUDIT")

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

    def test_days_22_24_final_mechanics_and_anti_mindfulness(self):
        candidate = load(self.BASE / "voice-master-candidate.json")
        rendered = "\n".join(u["draft_pl"] for u in candidate["units"])
        for required in (
            "przeciwnie do ruchu wskazówek zegara",
            "mniej więcej 1 lipca",
            "Runda 1: KOLORY",
            "Runda 2: LUBIĘ / NIE LUBIĘ",
            "Runda 3: NAWYKI I CECHY",
            "Przez minutę",
            "najbardziej świąteczny kolor",
            "dwie krótkie rundy",
        ):
            self.assertIn(required, rendered)
        for regression in (
            "złote światło",
            "ciepła aureola",
            "wspólne światło",
            "energia pokoju",
            "uważność",
        ):
            self.assertNotIn(regression, rendered.lower())


class GentleStepsFullDaysOwnerReview(unittest.TestCase):
    ROOT_DIR = ROOT / "localization/pl-PL/production/gentle-steps"
    BATCHES = [
        ROOT_DIR / "days01-03" / "voice-master-candidate.json",
        ROOT_DIR / "days04-07" / "voice-master-candidate.json",
        ROOT_DIR / "days08-14" / "voice-master-candidate.json",
        ROOT_DIR / "days15-21" / "voice-master-candidate.json",
        ROOT_DIR / "days22-24" / "voice-master-candidate.json",
    ]

    def test_full_days_01_24_has_exactly_three_surfaces_per_day(self):
        units = []
        for path in self.BATCHES:
            units.extend(load(path)["units"])
        self.assertEqual(len(units), 72)
        self.assertEqual(len({u["id"] for u in units}), 72)

        for day in range(1, 25):
            prefix = f"GS.D{day:02d}."
            day_units = [u for u in units if u["id"].startswith(prefix)]
            self.assertEqual(len(day_units), 3, day)
            self.assertEqual(
                [u["section_label"] for u in day_units],
                ["ZWOLNIJ", "GRAMY", "MIĘDZY NAMI"],
                day,
            )

    def test_full_days_audit_and_gate_are_owner_review_only(self):
        audit = load(self.ROOT_DIR / "GENTLE_STEPS_PL_DAYS01_24_AUDIT_2026-10-01.json")
        gate = load(self.ROOT_DIR / "FULL_DAYS_OWNER_REVIEW_GATE.json")
        self.assertEqual(audit["status"], "READY_FOR_OWNER_REVIEW")
        self.assertEqual(audit["coverage"]["units"], 72)
        self.assertEqual(audit["coverage"]["missing_or_order_defects"], [])
        self.assertEqual(gate["status"], "READY_FOR_OWNER_REVIEW")
        self.assertFalse(gate["labels_locked"])
        self.assertFalse(gate["title_locked"])
        self.assertFalse(gate["publication_authorized"])
        self.assertEqual(gate["back_matter_pages_98_104"], "NOT_YET_REAUTHORED")

    def test_full_days_global_translationese_and_gender_regressions_absent(self):
        rendered = "\n".join(
            u["draft_pl"]
            for path in self.BATCHES
            for u in load(path)["units"]
        )
        self.assertNotIn("—", rendered)
        self.assertNotIn("brzmi sprawnie", rendered)
        self.assertNotIn("„bam”, „ding” albo „pff”", rendered)
        self.assertIn("„bum”, „dzyń” albo „puf”", rendered)

        for regression in (
            "chciałbym / chciałabym",
            "gotowy/gotowa",
            "najpóźniejsza litera w alfabecie",
            "przekąska też może wygrać dzień",
            "i jedziecie dalej",
            "wewnętrzne światło",
            "wspólny oddech przepływa",
        ):
            self.assertNotIn(regression, rendered)


class GentleStepsVersion02(unittest.TestCase):
    ROOT_DIR = ROOT / "localization/pl-PL/production/gentle-steps/versions/v02"
    MASTER = ROOT_DIR / "GENTLE_STEPS_PL_VERSION_02_MASTER.md"

    def test_v02_full_book_has_24_days_and_three_sections_each(self):
        rendered = self.MASTER.read_text(encoding="utf-8")
        daily = rendered[rendered.index("## DZIEŃ 1"):]
        self.assertEqual(daily.count("## DZIEŃ "), 24)
        self.assertEqual(daily.count("\n### ZWOLNIJ:"), 24)
        self.assertEqual(daily.count("\n### GRAMY:"), 24)
        self.assertEqual(daily.count("\n### MIĘDZY NAMI:"), 24)

    def test_v02_reader_copy_respects_polish_house_style(self):
        rendered = self.MASTER.read_text(encoding="utf-8")
        daily = rendered[rendered.index("## DZIEŃ 1"):]
        self.assertNotIn("—", daily)
        for regression in (
            "mindfulness",
            "uważność",
            "brzmi sprawnie",
            "„bam”, „ding” albo „pff”",
            "chciałbym / chciałabym",
            "gotowy/gotowa",
            "wewnętrzne światło",
            "wspólny oddech przepływa",
        ):
            self.assertNotIn(regression.lower(), daily.lower())


    def test_v02_multi_agent_reader_audit_regressions(self):
        rendered = self.MASTER.read_text(encoding="utf-8")
        daily = rendered[rendered.index("## DZIEŃ 1"):]
        self.assertIn("MIĘDZY NAMI: JEDNO SŁOWO NA TERAZ", daily)
        self.assertIn("Wyobraźcie sobie mapę waszej rodziny", daily)
        self.assertIn("Jeśli choć jedna osoba woli bez dotyku", daily)
        self.assertIn("MIĘDZY NAMI: NASZ ZNAK", daily)
        self.assertNotIn("NASZ TAJNY ZNAK", daily)
        self.assertNotIn("„bop”", daily)
        self.assertNotIn("?”.", daily)
        self.assertNotIn("dzisiejszego rodzinnego dnia", daily)
        self.assertNotIn("dobrze mu usłyszeć", daily)
        self.assertNotIn("rodzinne wartości mają inne wymagania bezpieczeństwa", daily)

    def test_v02_includes_reauthored_back_matter(self):
        rendered = self.MASTER.read_text(encoding="utf-8")
        for heading in (
            "## PO TYCH 24 DNIACH",
            "## NIE OBIECUJEMY IDEAŁU",
            "## NA KONIEC",
            "## LIST OD HAPPY MAKERS",
        ):
            self.assertIn(heading, rendered)

        gate = load(self.ROOT_DIR / "V02_OWNER_REVIEW_GATE.json")
        audit = load(self.ROOT_DIR / "V02_FULL_BOOK_AUDIT_2026-10-02.json")
        self.assertEqual(gate["status"], "READY_FOR_OWNER_REVIEW_AFTER_MULTI_AGENT_FULL_READER_AUDIT")
        self.assertFalse(gate["title_locked"])
        self.assertFalse(gate["recurring_labels_locked"])
        self.assertFalse(gate["publication_authorized"])
        self.assertEqual(audit["coverage"]["days"], 24)
        self.assertEqual(audit["coverage"]["sections"], 72)


class GentleStepsPolishBookVersion02(unittest.TestCase):
    ROOT_DIR = ROOT / "localization/pl-PL/production/gentle-steps/book-versions/v2"
    MASTER = ROOT_DIR / "GENTLE_STEPS_PL_BOOK_VERSION_02_WORKING.md"

    def test_book_v02_keeps_24x3_structure(self):
        rendered = self.MASTER.read_text(encoding="utf-8")
        daily = rendered[rendered.index("## DZIEŃ 1"):]
        self.assertEqual(daily.count("## DZIEŃ "), 24)
        self.assertEqual(daily.count("\n### ZWOLNIJ:"), 24)
        self.assertEqual(daily.count("\n### GRAMY:"), 24)
        self.assertEqual(daily.count("\n### MIĘDZY NAMI:"), 24)

    def test_book_v02_owner_style_locks(self):
        rendered = self.MASTER.read_text(encoding="utf-8")
        daily = rendered[rendered.index("## DZIEŃ 1"):]
        self.assertNotIn("—", daily)
        self.assertIn('### ZWOLNIJ: MINUTA BEZ „MUSZĘ”', daily)
        self.assertIn("### GRAMY: NIEWIDZIALNA PIŁKA", daily)
        self.assertIn("Okulary też chcą dożyć świąt.", daily)
        self.assertIn("### MIĘDZY NAMI: CO W GRUDNIU LUBIĘ, A CZEGO MAM DOŚĆ?", daily)
        self.assertIn("Nie mam stroju na WF", daily)
        self.assertIn("drugą skarpetkę", daily)
        self.assertIn("wolnym miejscem parkingowym", daily)
        self.assertIn("### ZWOLNIJ: ZOSTAW TO W PRZEDPOKOJU", daily)
        self.assertIn("### GRAMY: RADIO NA ŻYWO", daily)
        self.assertIn("czemu akurat teraz jest korek?", daily)
        self.assertIn("### GRAMY: LUSTRO BEZ LUSTRA", daily)
        self.assertIn("szybki ping-pong", daily)
        self.assertIn("Jeśli jest was troje", daily)
        self.assertNotIn("przez 30 sekund patrzcie na siebie", daily)
        self.assertIn("### ZWOLNIJ: TU, GDZIE JESTEŚMY", daily)
        self.assertIn("Trzy kolory, dwa dźwięki, jedna podłoga.", daily)
        self.assertIn("### MIĘDZY NAMI: CO DZIŚ BYŁO TRUDNIEJSZE, NIŻ WYGLĄDAŁO?", daily)
        self.assertIn("### MIĘDZY NAMI: CO CI OSTATNIO WYSZŁO?", daily)
        self.assertIn("### GRAMY: MISJA KRZESŁO", daily)
        self.assertIn("Dobierzcie się w pary. Jedna osoba jest nawigatorem", daily)
        self.assertIn("### MIĘDZY NAMI: KIEDY MOGĘ NA CIEBIE LICZYĆ?", daily)
        self.assertIn("### GRAMY: KALAMBURY NA OPAK", daily)
        self.assertIn("### ZWOLNIJ: ZACIŚNIJ. PUŚĆ.", daily)
        self.assertNotIn("### ZWOLNIJ: CZOŁO, OCZY, SZCZĘKA", daily)
        self.assertIn("Jeśli pasuje tylko jedna osoba, robi szybki obrót", daily)
        self.assertIn("Nie potrzebujecie pełnego okrążenia.", daily)
        self.assertNotIn("### GRAMY: KROK BLIŻEJ, KROK DALEJ", daily)
        self.assertIn("### MIĘDZY NAMI: CO CHCESZ ZAPAMIĘTAĆ Z TEGO GRUDNIA?", daily)
        self.assertIn("### ZWOLNIJ: SERCE ROBI SWOJE", daily)
        self.assertIn("### ZWOLNIJ: PUSTE RĘCE", daily)
        self.assertIn("### GRAMY: LINIA BEZ SŁÓW", daily)
        self.assertIn("### ZWOLNIJ: DALEKO, BLISKO", daily)
        self.assertNotIn("### GRAMY: DYRYGENT BEZ BATUTY", daily)
        self.assertNotIn("### GRAMY: TUNEL KIBICÓW", daily)
        self.assertNotIn("### GRAMY: KTO TEŻ TAK MA?", daily)
        self.assertNotIn("### ZWOLNIJ: DŁUŻSZY WYDECH", daily)
        self.assertNotIn("### ZWOLNIJ: CHWILA OBOK SIEBIE", daily)
        self.assertIn("# PO 24 DNIACH", daily)
        self.assertIn("## JEDEN WIECZÓR PÓŹNIEJ", daily)
        self.assertIn("## LIST OD HAPPY MAKERS", daily)
        self.assertNotIn("## NIE OBIECUJEMY IDEAŁU", daily)
        self.assertNotIn("## NA KONIEC", daily)
        self.assertIn("W tej rundzie nie robicie kroków.", daily)
        self.assertIn("Jeśli choć jedna osoba woli bez dotyku", daily)
        self.assertIn("reaguje dopiero wtedy, gdy sygnał dotrze właśnie do niego", daily)
        self.assertIn("Nie przebiegajcie przez środek na oślep.", daily)
        self.assertIn("nie musi od razu odpowiadać ani mówić „nic się nie stało”", daily)
        self.assertNotIn("„bop”", daily)
        self.assertNotIn("Luli: „Dobrze” jest bezpieczne.", daily)
        self.assertNotIn("prawdziwy wtorek", daily)
        self.assertNotIn("PowerPoincie", daily)
        self.assertNotIn("NASZ TAJNY ZNAK", daily)

    def test_book_v02_has_no_duplicate_daily_titles(self):
        rendered = self.MASTER.read_text(encoding="utf-8")
        daily = rendered[rendered.index("## DZIEŃ 1"):]
        headings = [
            line.strip()
            for line in daily.splitlines()
            if line.startswith("### ")
        ]
        self.assertEqual(len(headings), 72)
        self.assertEqual(len(set(headings)), 72)

    def test_book_v02_version01_reference_is_preserved(self):
        manifest = load(self.ROOT_DIR / "BOOK_VERSION_02_MANIFEST.json")
        self.assertEqual(manifest["base_book_version"], "1")
        self.assertFalse(manifest["title_locked"])
        self.assertFalse(manifest["recurring_labels_locked"])
        self.assertFalse(manifest["publication_authorized"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
