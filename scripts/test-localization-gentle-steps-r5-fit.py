#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from localization.gentle_steps_r5_fit import (  # noqa: E402
    EXPECTED_FORMAT,
    EXPECTED_R5_BLOB,
    EXPECTED_SOURCE_PATH,
    REQUIRED_SURFACE_IDS,
    REVIEW_FLAGS,
    check_r5_fit_evidence,
    sha256,
)

CONTRACT = json.loads(
    (
        ROOT
        / "localization/pl-PL/production/gentle-steps/book-versions/v3/"
        "V03_R5_FINAL_EDITORIAL_SAFETY_PROOF_CONTRACT_2026-10-07.json"
    ).read_text(encoding="utf-8")
)


def build_bundle(root: Path) -> dict:
    (root / "template.html").write_text("<html>final template snapshot</html>", encoding="utf-8")
    (root / "book.pdf").write_bytes(b"%PDF-1.4\nsynthetic proof\n")

    source = ROOT / EXPECTED_SOURCE_PATH
    evidence = {
        "format": EXPECTED_FORMAT,
        "surface_kind": "actual_final_template",
        "source": {
            "path": EXPECTED_SOURCE_PATH,
            "r5_blob_sha": EXPECTED_R5_BLOB,
            "sha256": sha256(source),
        },
        "renderer": {"name": "synthetic-test-renderer", "revision": "test-1"},
        "reviewer": {"name": "synthetic-reviewer", "reviewed_at": "2026-10-07T19:00:00+02:00"},
        "typography": {"body_font_reduced_to_force_fit": False},
        "template": {"path": "template.html", "sha256": sha256(root / "template.html")},
        "rendered_book": {"path": "book.pdf", "sha256": sha256(root / "book.pdf")},
        "surfaces": [],
    }
    for index, sid in enumerate(REQUIRED_SURFACE_IDS):
        filename = f"{index:02d}-{sid}.png"
        target = root / filename
        target.write_bytes(b"\x89PNG\r\n\x1a\n" + sid.encode("utf-8"))
        render_hash = sha256(target)
        review = {flag: True for flag in REVIEW_FLAGS}
        review["render_sha256"] = render_hash
        evidence["surfaces"].append(
            {
                "id": sid,
                "render": {"path": filename, "sha256": render_hash},
                "review": review,
            }
        )
    return evidence


class R5FitEvidence(unittest.TestCase):
    def test_complete_exact_bound_bundle_passes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            proof = check_r5_fit_evidence(CONTRACT, build_bundle(root), root, ROOT)
            self.assertEqual(proof["status"], "PASS", proof)

    def test_wrong_source_blob_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            evidence = build_bundle(root)
            evidence["source"]["r5_blob_sha"] = "0" * 40
            proof = check_r5_fit_evidence(CONTRACT, evidence, root, ROOT)
            self.assertEqual(proof["status"], "BLOCK")
            self.assertTrue(any("source blob" in issue.lower() for issue in proof["issues"]))

    def test_proxy_and_shrink_to_fit_block(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            evidence = build_bundle(root)
            evidence["surface_kind"] = "proxy"
            evidence["typography"]["body_font_reduced_to_force_fit"] = True
            proof = check_r5_fit_evidence(CONTRACT, evidence, root, ROOT)
            self.assertEqual(proof["status"], "BLOCK")
            self.assertTrue(any("Proxy" in issue for issue in proof["issues"]))
            self.assertTrue(any("shrink-to-fit" in issue for issue in proof["issues"]))

    def test_missing_surface_and_unbound_review_block(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            evidence = build_bundle(root)
            evidence["surfaces"].pop()
            evidence["surfaces"][0]["review"]["render_sha256"] = "bad"
            proof = check_r5_fit_evidence(CONTRACT, evidence, root, ROOT)
            self.assertEqual(proof["status"], "BLOCK")
            self.assertTrue(any("exactly the required" in issue for issue in proof["issues"]))
            self.assertTrue(any("not bound to its render" in issue for issue in proof["issues"]))

    def test_artifact_hash_mismatch_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            evidence = build_bundle(root)
            first = root / evidence["surfaces"][0]["render"]["path"]
            first.write_bytes(first.read_bytes() + b"tamper")
            proof = check_r5_fit_evidence(CONTRACT, evidence, root, ROOT)
            self.assertEqual(proof["status"], "BLOCK")
            self.assertTrue(any("Artifact hash mismatch" in issue for issue in proof["issues"]))


    def test_reused_render_artifact_is_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            evidence = build_bundle(root)
            one, two = evidence["surfaces"][:2]
            two["render"] = copy.deepcopy(one["render"])
            two["review"]["render_sha256"] = one["render"]["sha256"]
            proof = check_r5_fit_evidence(CONTRACT, evidence, root, ROOT)
            self.assertEqual(proof["status"], "BLOCK")
            self.assertTrue(any("distinct render" in i for i in proof["issues"]))

    def test_identical_bytes_different_paths_are_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            evidence = build_bundle(root)
            one, two = evidence["surfaces"][:2]
            (root / two["render"]["path"]).write_bytes((root / one["render"]["path"]).read_bytes())
            two["render"]["sha256"] = sha256(root / two["render"]["path"])
            two["review"]["render_sha256"] = two["render"]["sha256"]
            self.assertEqual(check_r5_fit_evidence(CONTRACT, evidence, root, ROOT)["status"], "BLOCK")

    def test_whole_book_png_and_malformed_surfaces_block(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            evidence = build_bundle(root)
            evidence["rendered_book"] = copy.deepcopy(evidence["surfaces"][0]["render"])
            evidence["surfaces"][1]["render"] = []
            evidence["surfaces"][2]["review"] = []
            evidence["surfaces"][3] = None
            proof = check_r5_fit_evidence(CONTRACT, evidence, root, ROOT)
            self.assertEqual(proof["status"], "BLOCK")
            self.assertTrue(any("Whole-book render must be PDF" in i for i in proof["issues"]))


    def test_malformed_top_level_metadata_blocks_without_crashing(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            clean = build_bundle(root)
            for field, invalid in (
                ("source", []),
                ("renderer", "unknown"),
                ("reviewer", None),
                ("typography", True),
            ):
                with self.subTest(field=field):
                    evidence = copy.deepcopy(clean)
                    evidence[field] = invalid
                    proof = check_r5_fit_evidence(CONTRACT, evidence, root, ROOT)
                    self.assertEqual(proof["status"], "BLOCK", proof)
                    self.assertTrue(proof["issues"])

    def test_invalid_top_level_and_contract_block_without_crashing(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            evidence = build_bundle(root)
            for invalid_contract in (None, [], {"source_lock": []}):
                with self.subTest(contract=invalid_contract):
                    proof = check_r5_fit_evidence(invalid_contract, evidence, root, ROOT)
                    self.assertEqual(proof["status"], "BLOCK", proof)
            for invalid_evidence in (None, [], "invalid"):
                with self.subTest(evidence=invalid_evidence):
                    proof = check_r5_fit_evidence(CONTRACT, invalid_evidence, root, ROOT)
                    self.assertEqual(proof["status"], "BLOCK", proof)



if __name__ == "__main__":
    unittest.main()
