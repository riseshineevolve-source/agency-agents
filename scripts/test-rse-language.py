#!/usr/bin/env python3
"""Regression checks for source preservation, stage boundaries and candidate integrity."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

SCRIPT = Path(__file__).with_name("rse-language.py")
spec = importlib.util.spec_from_file_location("rse_language", SCRIPT)
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)


class LanguageToolTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source.md"
        self.source.write_text("# A family book\n\nThis activity takes 10 minutes. Keep {name} in the story.\n")
        self.run = self.root / "run"
        self.profile = self.root / "profile.json"
        self.profile.write_text(json.dumps({"project": "generic", "locks": [{"id": "title", "en": "A family book", "pl": "Rodzinna książka"}], "languages": {"pl": {}, "en": {}}}))

    def cli(self, *args, expect=0):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = engine.main(list(map(str, args)))
        self.assertEqual(code, expect, err.getvalue() or out.getvalue())
        return json.loads(err.getvalue() or out.getvalue())

    def prepare(self, target="en", extra=()):
        return self.cli("prepare", "--source", self.source, "--from", "en", "--to", target,
                        "--project", "generic", "--profile", self.profile, "--output", self.run, *extra)

    def read(self, name):
        return json.loads((self.run / name).read_text())

    def write(self, name, data):
        (self.run / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

    def authorize_all(self):
        candidate = self.read("candidate.json")
        scope = self.read("change-scope.json")
        scope["allowed_changed_segments"] = [s["id"] for s in candidate["segments"]]
        scope["reason"] = "Improve precise source-backed wording"
        self.write("change-scope.json", scope)

    def check(self, expect=0, extra=()):
        return self.cli("check", "--run", self.run, "--candidate", self.run / "candidate.json", *extra, expect=expect)

    def complete_ledger(self, **updates):
        ledger = self.read("issue-ledger.json")
        ledger.update(diagnostic="COMPLETE", **updates)
        self.write("issue-ledger.json", ledger)

    def write_reviews(self):
        sha = engine.hash_bytes((self.run / "candidate.json").read_bytes())
        reviews = {"candidate_sha256": sha, "reviews": [{"stage": stage, "status": "PASS", "reviewer": "Independent reviewer", "candidate_sha256": sha, "evidence": "Read all source and target segments; findings recorded."} for stage in engine.STAGES]}
        self.write("reviews.json", reviews)


    def test_same_language_baseline_is_review_required(self):
        result = self.prepare()
        self.assertEqual(result["mode"], "upgrade")
        self.assertEqual((self.run / "source.md").read_bytes(), self.source.read_bytes())
        self.complete_ledger()
        checked = self.check()
        self.assertEqual(checked["deterministic_qa"], "PASS")
        self.assertEqual(checked["status"], "LANGUAGE_REVIEW_REQUIRED")
        self.assertFalse(checked["print_ready"])

    def test_cross_language_packet_never_includes_source_sentences(self):
        self.prepare("pl")
        packet = self.read("writer-packet.json")
        self.assertNotIn("This activity", json.dumps(packet))
        self.assertEqual(packet["status"], "FUNCTION_BRIEF_REQUIRED")
        self.assertTrue(all(s["text"] == "" for s in self.read("candidate.json")["segments"]))

    def test_empty_target_blocks(self):
        self.prepare("pl")
        self.assertIn("Empty/missing", self.check(expect=2)["reason"])

    def test_undeclared_change_blocks(self):
        self.prepare()
        candidate = self.read("candidate.json")
        candidate["segments"][1]["text"] += " Enjoy."
        self.write("candidate.json", candidate)
        self.assertIn("Undeclared", self.check(expect=2)["reason"])
        self.authorize_all()
        self.check()

    def test_omitted_duplicate_and_malicious_ids_block(self):
        self.prepare()
        original = self.read("candidate.json")
        for units in [original["segments"][:-1], original["segments"] + original["segments"][:1], [{"id": "../../evil", "text": "x"}] + original["segments"][1:]]:
            candidate = dict(original, segments=units)
            self.write("candidate.json", candidate)
            self.check(expect=2)

    def test_owner_lock_change_and_duplicate_block(self):
        self.prepare()
        self.authorize_all()
        candidate = self.read("candidate.json")
        candidate["segments"][0]["text"] = "# Another title"
        self.write("candidate.json", candidate)
        self.assertIn("Owner lock", self.check(expect=2)["reason"])
        candidate["segments"][0]["text"] = "# A family book A family book"
        self.write("candidate.json", candidate)
        self.assertIn("Owner lock", self.check(expect=2)["reason"])

    def test_placeholder_and_declared_number_drift_block(self):
        self.prepare(extra=("--preserve-numbers",))
        self.authorize_all()
        candidate = self.read("candidate.json")
        original = candidate["segments"][1]["text"]
        for changed in [original.replace("{name}", "{person}"), original.replace("10", "11")]:
            candidate["segments"][1]["text"] = changed
            self.write("candidate.json", candidate)
            self.check(expect=2)

    def test_original_source_mutation_blocks(self):
        self.prepare()
        self.source.write_text("Changed source")
        self.assertIn("original source changed", self.check(expect=2)["reason"])

    def test_snapshot_mutation_blocks(self):
        self.prepare()
        (self.run / "source.md").write_text("Changed snapshot")
        self.assertIn("snapshot changed", self.check(expect=2)["reason"])

    def test_manifest_mutation_blocks(self):
        self.prepare()
        manifest = self.read("run.json")
        manifest["target_language"] = "pl"
        self.write("run.json", manifest)
        self.assertIn("manifest changed", self.check(expect=2)["reason"])

    def test_candidate_language_metadata_blocks(self):
        self.prepare()
        candidate = self.read("candidate.json")
        candidate["language"] = "pl"
        self.write("candidate.json", candidate)
        self.assertIn("language mismatch", self.check(expect=2)["reason"])

    def test_stale_receipts_block_and_hash_bound_reviews_pass(self):
        self.prepare()
        self.complete_ledger()
        candidate_sha = engine.hash_bytes((self.run / "candidate.json").read_bytes())
        reviews = {"candidate_sha256": candidate_sha, "reviews": [{"stage": stage, "status": "PASS", "reviewer": "Independent reviewer", "candidate_sha256": candidate_sha, "evidence": "Read all source and target segments; findings recorded."} for stage in engine.STAGES]}
        self.write("reviews.json", reviews)
        result = self.check(extra=("--reviews", self.run / "reviews.json"))
        self.assertEqual(result["status"], "OWNER_READ_CANDIDATE")
        self.assertEqual(result["owner_approval"], "NOT_GRANTED")
        (self.run / "candidate.json").write_text((self.run / "candidate.json").read_text() + " ")
        self.assertIn("stale", self.check(expect=2, extra=("--reviews", self.run / "reviews.json"))["reason"])

    def test_unrun_diagnostic_blocks_owner_read_even_with_reviews(self):
        self.prepare()
        self.write_reviews()
        result = self.check(extra=("--reviews", self.run / "reviews.json"))
        self.assertEqual(result["status"], "DIAGNOSTIC_REQUIRED")
        self.assertEqual(result["deterministic_qa"], "PASS")
        self.assertEqual(result["diagnostic"], "NOT_RUN")

    def test_unresolved_issues_keep_their_real_gate(self):
        self.prepare()
        self.write_reviews()
        for classification, status, exit_code in [("FIX", "LANGUAGE_REVIEW_REQUIRED", 0), ("BLOCK", "BLOCK", 2), ("OWNER_GATE", "OWNER_GATE", 0)]:
            self.complete_ledger(issues=[{"id": "ISSUE-1", "segment_id": "s0002", "classification": classification, "reason": "Concrete source-backed defect"}])
            result = self.check(expect=exit_code, extra=("--reviews", self.run / "reviews.json"))
            self.assertEqual(result["status"], status)
            self.assertEqual(result["unresolved_issues"][0]["id"], "ISSUE-1")

    def test_stale_issue_ledger_blocks(self):
        self.prepare()
        self.complete_ledger()
        ledger = self.read("issue-ledger.json")
        ledger["run_sha256"] = "0" * 64
        self.write("issue-ledger.json", ledger)
        self.assertIn("ledger is stale", self.check(expect=2)["reason"])
        ledger["run_sha256"] = self.read("run.json")["manifest_sha256"]
        ledger["candidate_sha256"] = "0" * 64
        self.write("issue-ledger.json", ledger)
        self.assertIn("stale for candidate", self.check(expect=2)["reason"])

    def test_resolved_issues_need_evidence_before_owner_read(self):
        self.prepare()
        self.write_reviews()
        issue = {"id": "ISSUE-1", "segment_id": "s0002", "classification": "FIX", "final_classification": "KEEP"}
        self.complete_ledger(issues=[issue])
        self.assertIn("lacks resolution/evidence", self.check(expect=2, extra=("--reviews", self.run / "reviews.json"))["reason"])
        issue["resolution"] = "Targeted fix applied and independently reviewed on this candidate."
        self.complete_ledger(issues=[issue])
        result = self.check(extra=("--reviews", self.run / "reviews.json"))
        self.assertEqual(result["status"], "OWNER_READ_CANDIDATE")
        self.assertEqual(result["unresolved_issues"], [])

    def test_preserved_or_acknowledged_source_ambiguity_stays_open(self):
        self.prepare()
        self.write_reviews()
        for status in ["OPEN", "PRESERVE_SOURCE", "ACKNOWLEDGED"]:
            self.complete_ledger(source_ambiguities=[{"segment_id": "s0002", "status": status, "detail": "Timing and turn completion precedence undefined", "severity": "note", "rationale": "Do not invent source truth"}])
            result = self.check(extra=("--reviews", self.run / "reviews.json"))
            self.assertEqual(result["status"], "SOURCE_REVIEW_REQUIRED")
            self.assertTrue(result["unresolved_source_ambiguities"])
        self.complete_ledger(source_ambiguities=[{"segment_id": "s0002", "status": "RESOLVED", "resolution": "Source owner supplied exact missing precedence; authorized source authority recorded."}])
        self.assertEqual(self.check(extra=("--reviews", self.run / "reviews.json"))["status"], "OWNER_READ_CANDIDATE")

    def test_invalid_issue_status_is_not_silently_clean(self):
        self.prepare()
        for issue in [{"id": "I1", "classification": "APPROVED"}, {"id": "I1", "classification": "KEEP", "segment_id": "unknown"}]:
            self.complete_ledger(issues=[issue])
            self.check(expect=2)


    def test_missing_or_unresolved_review_does_not_pass(self):
        self.prepare()
        sha = engine.hash_bytes((self.run / "candidate.json").read_bytes())
        self.write("reviews.json", {"candidate_sha256": sha, "reviews": []})
        self.assertIn("Missing specialist", self.check(expect=2, extra=("--reviews", self.run / "reviews.json"))["reason"])

    def test_output_collision_never_overwrites(self):
        self.prepare()
        before = (self.run / "run.json").read_bytes()
        self.prepare_result = self.cli("prepare", "--source", self.source, "--from", "en", "--to", "en", "--output", self.run, expect=2)
        self.assertEqual(before, (self.run / "run.json").read_bytes())
        self.assertFalse(list(self.root.glob(".rse-language-*")))

    def test_invalid_preflight_is_atomic(self):
        self.source.write_text("Ambiguous")
        self.cli("prepare", "--source", self.source, "--to", "pl", "--output", self.run, expect=2)
        self.assertFalse(self.run.exists())
        self.assertFalse(list(self.root.glob(".rse-language-*")))

    def test_detective_freeze_blocks_wrong_source_and_accepts_exact(self):
        detective_profile = self.root / "detective.json"
        detective_profile.write_text(json.dumps({"project": "detective-academy", "languages": {"pl": {}, "en": {}}}))
        args = ("prepare", "--source", self.source, "--from", "en", "--to", "pl", "--project", "detective-academy", "--profile", detective_profile, "--output", self.run)
        self.cli(*args, expect=2)
        self.assertFalse(self.run.exists())
        receipt = self.root / "freeze.json"
        receipt.write_text(json.dumps({"project": "detective-academy", "approved": True, "reference": "Owner explicitly froze this source", "source_sha256": "0" * 64}))
        self.cli(*args, "--freeze", receipt, expect=2)
        self.assertFalse(self.run.exists())
        value = json.loads(receipt.read_text())
        value["source_sha256"] = engine.hash_bytes(self.source.read_bytes())
        receipt.write_text(json.dumps(value))
        self.cli(*args, "--freeze", receipt)

    def test_structured_ids_protected_regions_and_json_export(self):
        self.source = self.root / "source.json"
        self.source.write_text(json.dumps({"language": "en", "count": 24, "segments": [{"id": "D01.title", "text": "A family book", "protected": True}, {"id": "D01.body", "text": "Spend 10 minutes together.", "protected_numbers": ["10"]}]}))
        self.prepare()
        self.assertEqual([s["id"] for s in self.read("candidate.json")["segments"]], ["D01.title", "D01.body"])
        self.authorize_all()
        candidate = self.read("candidate.json")
        candidate["segments"][0]["text"] = "Changed title"
        self.write("candidate.json", candidate)
        self.assertIn("Protected region", self.check(expect=2)["reason"])
        candidate["segments"][0]["text"] = "A family book"
        candidate["segments"][1]["text"] = "Share 10 minutes together."
        self.write("candidate.json", candidate)
        output = self.root / "export.json"
        self.cli("export", "--run", self.run, "--candidate", self.run / "candidate.json", "--output", output)
        exported = json.loads(output.read_text())
        self.assertEqual(exported["count"], 24)
        self.assertEqual(exported["language"], "en")
        self.assertEqual(exported["segments"][1]["text"], "Share 10 minutes together.")

    def test_json_duplicate_keys_and_ids_block(self):
        self.source = self.root / "source.json"
        for text in ['{"x":"one","x":"two"}', '{"segments":[{"id":"D01","text":"One"},{"id":"D01","text":"Two"}]}']:
            self.source.write_text(text)
            self.cli("prepare", "--source", self.source, "--from", "en", "--to", "pl", "--output", self.run, expect=2)
            self.assertFalse(self.run.exists())

    def test_json_empty_key_is_not_confused_with_root_string(self):
        self.source = self.root / "source.json"
        self.source.write_text(json.dumps({"": "A family book", "count": 24}))
        self.prepare()
        output = self.root / "empty-key.json"
        self.cli("export", "--run", self.run, "--candidate", self.run / "candidate.json", "--output", output)
        self.assertEqual(json.loads(output.read_text()), {"": "A family book", "count": 24})


    def test_docx_headers_notes_and_textboxes_without_duplicate_text(self):
        self.source = self.root / "source.docx"
        ns = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
        body = '<w:document ' + ns + '><w:body><w:p><w:r><w:t>A family book</w:t></w:r><w:p><w:r><w:t>Textbox</w:t></w:r></w:p></w:p></w:body></w:document>'
        note = '<w:footnotes ' + ns + '><w:p><w:r><w:t>Note text</w:t></w:r></w:p></w:footnotes>'
        header = '<w:hdr ' + ns + '><w:p><w:r><w:t>Header</w:t><w:tab/><w:t>text</w:t></w:r></w:p></w:hdr>'
        with zipfile.ZipFile(self.source, "w") as archive:
            archive.writestr("word/document.xml", body)
            archive.writestr("word/footnotes.xml", note)
            archive.writestr("word/header1.xml", header)
        self.prepare()
        texts = [s["text"] for s in self.read("candidate.json")["segments"]]
        self.assertEqual(texts, ["A family book", "Textbox", "Note text", "Header\ttext"])

    def test_malformed_candidate_and_review_shape_return_block(self):
        self.prepare()
        original = self.read("candidate.json")
        for candidate in [[], dict(original, segments=[None])]:
            self.write("candidate.json", candidate)
            self.check(expect=2)
        self.write("candidate.json", original)
        self.write("reviews.json", [])
        self.check(expect=2, extra=("--reviews", self.run / "reviews.json"))


    def test_cross_language_check_requires_validated_hash_bound_packet(self):
        self.prepare("pl")
        self.authorize_all()
        candidate = self.read("candidate.json")
        candidate["segments"][0]["text"] = "# Rodzinna książka"
        candidate["segments"][1]["text"] = "Ta zabawa zajmuje 10 minut. {name} bierze udział."
        self.write("candidate.json", candidate)
        self.assertIn("requires --packet", self.check(expect=2)["reason"])
        brief = self.read("functional-brief.json")
        for unit in brief["units"]:
            for field in engine.BRIEF_FIELDS:
                unit[field] = "none" if field != "function" else "Invite family participation"
        self.write("complete-brief.json", brief)
        output = self.root / "ready-packet.json"
        result = self.cli("packet", "--run", self.run, "--brief", self.run / "complete-brief.json", "--output", output)
        self.assertIn("not bound", self.check(expect=2, extra=("--packet", output))["reason"])
        candidate["writer_packet_sha256"] = result["packet_sha256"]
        self.write("candidate.json", candidate)
        self.check(extra=("--packet", output))
        output.write_text(output.read_text() + " ")
        self.assertIn("changed after validation", self.check(expect=2, extra=("--packet", output))["reason"])

    def test_scalar_json_export_preserves_root_type(self):
        self.source = self.root / "source.json"
        self.source.write_text(json.dumps("A family book"))
        self.prepare()
        output = self.root / "scalar.json"
        self.cli("export", "--run", self.run, "--candidate", self.run / "candidate.json", "--output", output)
        self.assertEqual(json.loads(output.read_text()), "A family book")

    def test_actual_project_profile_supplies_voice_and_locked_strings(self):
        self.source.write_text("BEFORE CHRISTMAS SLIPS BY\n\nLET’S TALK\n\nSpend 10 minutes together. {name}")
        self.cli("prepare", "--source", self.source, "--from", "en", "--to", "pl", "--project", "gentle-steps", "--output", self.run)
        run = self.read("run.json")
        self.assertIn("ŚWIĘTA SĄ TEŻ PO DRODZE", run["required_strings"])
        self.assertEqual(run["required_string_counts"]["POGADAJMY"], 1)
        self.assertEqual(run["segments"][2]["protected_tokens"], ["{name}"])
        brief = self.read("functional-brief.json")
        for unit in brief["units"]:
            for field in engine.BRIEF_FIELDS:
                unit[field] = "none"
        self.write("brief.json", brief)
        output = self.root / "ready.json"
        self.cli("packet", "--run", self.run, "--brief", self.run / "brief.json", "--output", output)
        payload = json.loads(output.read_text())
        self.assertIn("Naturalny", payload["voice"])
        self.assertEqual(payload["segment_constraints"][2]["protected_tokens"], ["{name}"])


    def test_completed_function_packet_and_wording_leak_rejection(self):
        self.prepare("pl")
        brief = self.read("functional-brief.json")
        for unit in brief["units"]:
            for field in engine.BRIEF_FIELDS:
                unit[field] = "none" if field != "function" else "Invite family participation in an activity"
        self.write("brief-complete.json", brief)
        output = self.root / "writer.json"
        self.cli("packet", "--run", self.run, "--brief", self.run / "brief-complete.json", "--output", output)
        self.assertNotIn("source_text", output.read_text())
        brief["units"][1]["function"] = self.read("run.json")["segments"][1]["source_text"]
        self.write("brief-leak.json", brief)
        self.cli("packet", "--run", self.run, "--brief", self.run / "brief-leak.json", "--output", self.root / "leaked.json", expect=2)
        self.assertFalse((self.root / "leaked.json").exists())


if __name__ == "__main__":
    unittest.main()
