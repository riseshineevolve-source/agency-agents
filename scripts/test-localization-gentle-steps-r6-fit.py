#!/usr/bin/env python3
"""Adversarial unit tests for the R6 evidence gate; synthetic renders are TEST ONLY."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import runpy
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
tools = runpy.run_path(str(ROOT / "scripts/gentle-steps-r6-proof.py"))
check = tools["check_r6_fit_evidence"]
create_draft = tools["create_r6_draft"]
CONTRACT = json.loads((ROOT / tools["CONTRACT"]).read_text(encoding="utf-8"))
IDS = tools["REQUIRED_SURFACE_IDS"]
FLAGS = tools["REVIEW_FLAGS"]


def fixtures(root: Path) -> dict:
    (root / "template").mkdir()
    (root / "book").mkdir()
    (root / "reviews").mkdir()
    (root / "template/final_template.html").write_text("TEST TEMPLATE ONLY", encoding="utf-8")
    (root / "book/full_book.pdf").write_bytes(b"%PDF-1.7\nunit-test-only\n")
    for sid in IDS:
        (root / "reviews" / f"{sid}.png").write_bytes(b"\x89PNG\r\n\x1a\n" + sid.encode("ascii"))
    return create_draft(root, "template/final_template.html", "book/full_book.pdf",
                        "reviews", "test-renderer", "test-commit")


def attested(evidence: dict) -> dict:
    e = copy.deepcopy(evidence)
    e.pop("_draft_status")
    e["surface_kind"] = "actual_final_template"
    e["renderer"]["name"] = "named-renderer"
    e["reviewer"] = {"name": "unit-test reviewer", "reviewed_at": "2026-10-19T12:00:00+02:00"}
    e["typography"] = {
        "body_font_reduced_to_force_fit": False,
        "source_body_font_pt": 11, "rendered_body_font_pt": 11,
        "source_body_leading_pt": 14, "rendered_body_leading_pt": 14,
    }
    for s in e["surfaces"]:
        for flag in FLAGS:
            s["review"][flag] = True
    return e


class R6FitProofTests(unittest.TestCase):
    def proof(self, root: Path, e: object, contract: object = CONTRACT) -> dict:
        return check(contract, e, root, ROOT)

    def test_unreviewed_producer_draft_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            e = fixtures(root)
            self.assertEqual(len(e["surfaces"]), 12)
            proof = self.proof(root, e)
            self.assertEqual(proof["status"], "BLOCK")
            self.assertTrue(any("unreviewed" in i.lower() for i in proof["issues"]))

    def test_complete_structure_and_attestation_passes_only_receipt(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            proof = self.proof(root, attested(fixtures(root)))
            self.assertEqual(proof["status"], "PASS", proof)
            self.assertIn("cannot verify visual truth", proof["limits"])

    def test_old_source_or_wrong_revision_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            e = attested(fixtures(root))
            e["source"]["r6_blob_sha"] = tools["R5_BLOB"]
            self.assertEqual(self.proof(root, e)["status"], "BLOCK")
            e = attested(fixtures(root))
            e["source"]["sha256"] = "0" * 64
            self.assertEqual(self.proof(root, e)["status"], "BLOCK")
            e = attested(fixtures(root))
            e["format"] = "rse-gentle-steps-pl-v03-r5-template-fit-evidence-v1"
            self.assertEqual(self.proof(root, e)["status"], "BLOCK")

    def test_proxy_missing_reviewer_and_shrunk_font_block(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            e = attested(fixtures(root))
            e["surface_kind"] = "proxy"
            e["reviewer"]["name"] = ""
            e["typography"]["rendered_body_font_pt"] = 8
            e["typography"]["body_font_reduced_to_force_fit"] = True
            p = self.proof(root, e)
            self.assertEqual(p["status"], "BLOCK")
            self.assertTrue(any("body font was reduced" in i for i in p["issues"]))

    def test_bad_png_and_identical_screenshots_block(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            e = attested(fixtures(root))
            first, second = e["surfaces"][:2]
            second["render"] = copy.deepcopy(first["render"])
            second["review"]["render_sha256"] = first["render"]["sha256"]
            self.assertEqual(self.proof(root, e)["status"], "BLOCK")
            e = attested(fixtures(root))
            target = root / e["surfaces"][0]["render"]["path"]
            target.write_bytes(b"bad PNG")
            self.assertEqual(self.proof(root, e)["status"], "BLOCK")

    def test_missing_safety_review_or_incomplete_set_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            e = attested(fixtures(root))
            e["surfaces"][0]["review"]["copy_complete"] = False
            e["surfaces"].pop()
            self.assertEqual(self.proof(root, e)["status"], "BLOCK")

    def test_source_contract_mutation_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            e = attested(fixtures(root))
            c = copy.deepcopy(CONTRACT)
            c["source_lock"]["r6_blob_sha"] = tools["R5_BLOB"]
            self.assertEqual(self.proof(root, e, c)["status"], "BLOCK")
            c = copy.deepcopy(CONTRACT)
            c["required_surface_ids"].pop()
            self.assertEqual(self.proof(root, e, c)["status"], "BLOCK")

    def test_malformed_records_block_without_exception(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            clean = attested(fixtures(root))
            for field, value in (("source", []), ("renderer", True),
                                 ("reviewer", None), ("typography", "small"),
                                 ("surfaces", []), ("surfaces", "wrong")):
                with self.subTest(field=field, value=value):
                    e = copy.deepcopy(clean)
                    e[field] = value
                    self.assertEqual(self.proof(root, e)["status"], "BLOCK")
            self.assertEqual(self.proof(root, [], [])["status"], "BLOCK")


if __name__ == "__main__":
    unittest.main()
