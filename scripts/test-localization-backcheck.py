#!/usr/bin/env python3
"""Adversarial tests for hash-bound bilingual localization backchecks."""
from __future__ import annotations

import copy
import unittest

from localization.backcheck import build_backcheck_packet, validate_backcheck_evidence
from localization.contracts import extract
from localization.io import ContractError, digest


def fixture(logic=False):
    atom = {"kind": "coordinate", "value": "B2", "source_anchor": "B2", "target_anchor": "B2"}
    spec = {
        "id": "TEST.BACKCHECK.001",
        "source_path": "/copy",
        "content_type": "detective_clue" if logic else "ui",
        "surface_type": "clue_card" if logic else "button",
        "logic_sensitive": logic,
        "character_sensitive": False,
        "semantic_risk": True,
        "logic_atoms": [atom] if logic else [],
        "fit_budget": {"max_chars": 60, "requires_real_surface": False},
    }
    manifest, targets = extract(
        {"copy": "Find B2." if logic else "Continue", "answer": "B2"},
        {"version": 1, "product": "synthetic-backcheck", "adapter": "puzzle" if logic else "app", "segments": [spec], "protected_paths": ["/answer"]},
        "synthetic.json",
        "r1",
    )
    targets["segments"][0].update(
        target_text="Znajdź B2." if logic else "Dalej",
        review_status="draft",
    )
    return manifest, targets


def evidence_for(packet):
    items = []
    for item in packet["items"]:
        items.append({
            "id": item["id"],
            "source_sha256": item["source_sha256"],
            "target_sha256": item["target_sha256"],
            "policy_sha256": item["policy_sha256"],
            "checks": {name: True for name in item["required_checks"]},
            "notes": "synthetic test attestation only",
        })
    return {
        "format": "rse-pl-backcheck-evidence-v1",
        "product": packet["product"],
        "contract_sha256": packet["contract_sha256"],
        "packet_sha256": packet["packet_sha256"],
        "reviewer": "synthetic-bilingual-reviewer",
        "reviewed_at": "synthetic-test",
        "items": items,
    }


class Backcheck(unittest.TestCase):
    def test_packet_is_hash_bound_and_does_not_auto_approve(self):
        manifest, targets = fixture(logic=True)
        packet = build_backcheck_packet(manifest, targets)
        self.assertEqual(packet["status"], "REVIEW_REQUIRED")
        item = packet["items"][0]
        self.assertIn("logic_atoms_preserved", item["required_checks"])
        self.assertIn("surface_budget_reviewed", item["required_checks"])
        self.assertEqual(item["target_sha256"], digest(targets["segments"][0]["target_text"]))

    def test_complete_human_evidence_passes_contract(self):
        manifest, targets = fixture(logic=True)
        packet = build_backcheck_packet(manifest, targets)
        proof = validate_backcheck_evidence(manifest, targets, evidence_for(packet))
        self.assertEqual(proof["status"], "PASS", proof)

    def test_missing_required_attestation_blocks(self):
        manifest, targets = fixture(logic=True)
        packet = build_backcheck_packet(manifest, targets)
        evidence = evidence_for(packet)
        evidence["items"][0]["checks"]["logic_atoms_preserved"] = False
        proof = validate_backcheck_evidence(manifest, targets, evidence)
        self.assertEqual(proof["status"], "BLOCK")
        self.assertTrue(any("logic_atoms_preserved" in issue for issue in proof["issues"]))

    def test_target_or_policy_change_invalidates_old_evidence(self):
        manifest, targets = fixture(logic=False)
        packet = build_backcheck_packet(manifest, targets)
        evidence = evidence_for(packet)
        changed_targets = copy.deepcopy(targets)
        changed_targets["segments"][0]["target_text"] = "Kontynuuj"
        proof = validate_backcheck_evidence(manifest, changed_targets, evidence)
        self.assertEqual(proof["status"], "BLOCK")
        self.assertTrue(any("stale" in issue.lower() or "target hash mismatch" in issue.lower() for issue in proof["issues"]))

    def test_stale_source_hash_and_partial_scope_fail_closed(self):
        manifest, targets = fixture()
        stale = copy.deepcopy(targets)
        stale["segments"][0]["source_sha256"] = "old"
        with self.assertRaises(ContractError):
            build_backcheck_packet(manifest, stale)
        missing = copy.deepcopy(targets)
        missing["segments"] = []
        with self.assertRaises(ContractError):
            build_backcheck_packet(manifest, missing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
