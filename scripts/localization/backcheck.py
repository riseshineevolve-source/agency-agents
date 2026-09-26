"""Deterministic human backcheck packets for RSE localization.

This layer does not translate, score fluency, or claim semantic correctness. It
binds a human bilingual review to the exact source text, target text and segment
policy so a later copy/policy change invalidates the attestation automatically.
"""
from __future__ import annotations

from .contracts import require, segment_policy_hash, validate_manifest
from .io import digest


def _target_map(manifest, targets):
    validate_manifest(manifest)
    require(isinstance(targets, dict) and targets.get("version") == 1, "Unsupported target bundle")
    require(targets.get("product") == manifest["product"], "Target product does not match manifest")
    require(targets.get("contract_sha256") == manifest["contract_sha256"], "Targets reference a different source contract")
    records = targets.get("segments", [])
    require(isinstance(records, list), "Target segments must be a list")
    by_id = {}
    for record in records:
        sid = record.get("id")
        require(sid and sid not in by_id, f"Duplicate/missing target ID: {sid}")
        by_id[sid] = record
    expected = {segment["id"] for segment in manifest["segments"]}
    require(set(by_id) == expected, "Backcheck requires exact target coverage for the manifest scope")
    return by_id


def _required_checks(segment):
    checks = [
        "meaning_preserved",
        "native_pl_polish",
        "no_added_or_removed_claims",
        "terminology_context_checked",
    ]
    if segment.get("logic_sensitive"):
        checks.extend([
            "logic_atoms_preserved",
            "negation_quantifiers_directions_checked",
            "answer_identity_unchanged",
        ])
    if segment.get("character_sensitive") or segment.get("identity_mappings"):
        checks.append("character_identity_and_voice_checked")
    if segment.get("protected_tokens") or segment.get("number_mappings"):
        checks.append("protected_values_checked")
    if segment.get("fit_budget") is not None:
        checks.append("surface_budget_reviewed")
    return checks


def build_backcheck_packet(manifest, targets):
    """Create a review packet bound to exact source, target and policy hashes."""
    by_id = _target_map(manifest, targets)
    items = []
    for segment in manifest["segments"]:
        target = by_id[segment["id"]]
        text = target.get("target_text", "")
        require(isinstance(text, str) and text.strip(), f"Backcheck target text missing: {segment['id']}")
        require(target.get("source_sha256") == segment["source_sha256"], f"Backcheck target is stale: {segment['id']}")
        item = {
            "id": segment["id"],
            "source_text": segment["source_text"],
            "target_text": text,
            "source_sha256": segment["source_sha256"],
            "target_sha256": digest(text),
            "policy_sha256": segment_policy_hash(segment),
            "content_type": segment["content_type"],
            "surface_type": segment["surface_type"],
            "logic_sensitive": segment["logic_sensitive"],
            "character_sensitive": segment["character_sensitive"],
            "semantic_risk": segment["semantic_risk"],
            "logic_atoms": segment.get("logic_atoms", []),
            "identity_mappings": segment.get("identity_mappings", []),
            "protected_tokens": segment.get("protected_tokens", []),
            "number_mappings": segment.get("number_mappings", []),
            "fit_budget": segment.get("fit_budget"),
            "required_checks": _required_checks(segment),
        }
        items.append(item)
    packet = {
        "format": "rse-pl-backcheck-request-v1",
        "product": manifest["product"],
        "contract_sha256": manifest["contract_sha256"],
        "status": "REVIEW_REQUIRED",
        "items": items,
        "limits": "Human bilingual attestation only. This packet does not auto-approve semantics, puzzle logic, cultural naturalness or real-surface fit.",
    }
    packet["packet_sha256"] = digest({k: v for k, v in packet.items() if k != "packet_sha256"})
    return packet


def validate_backcheck_evidence(manifest, targets, evidence):
    """Validate that a human review is complete and bound to the current packet."""
    request = build_backcheck_packet(manifest, targets)
    issues = []

    def check(condition, message):
        if not condition:
            issues.append(message)

    check(isinstance(evidence, dict), "Backcheck evidence must be an object")
    if not isinstance(evidence, dict):
        return {"format": "rse-pl-backcheck-proof-v1", "status": "BLOCK", "issues": issues}
    check(evidence.get("format") == "rse-pl-backcheck-evidence-v1", "Wrong backcheck evidence format")
    check(evidence.get("product") == request["product"], "Backcheck product mismatch")
    check(evidence.get("contract_sha256") == request["contract_sha256"], "Backcheck source contract changed")
    check(evidence.get("packet_sha256") == request["packet_sha256"], "Backcheck packet is stale")
    check(bool(evidence.get("reviewer")), "Bilingual reviewer identity missing")
    check(bool(evidence.get("reviewed_at")), "Backcheck review timestamp/reference missing")

    reviews = evidence.get("items", [])
    check(isinstance(reviews, list), "Backcheck evidence items must be a list")
    reviews = reviews if isinstance(reviews, list) else []
    by_id = {}
    for review in reviews:
        sid = review.get("id") if isinstance(review, dict) else None
        if not sid or sid in by_id:
            issues.append(f"Duplicate/missing backcheck item ID: {sid}")
            continue
        by_id[sid] = review
    expected = {item["id"]: item for item in request["items"]}
    check(set(by_id) == set(expected), "Backcheck evidence must cover exactly the current manifest scope")

    for sid, item in expected.items():
        review = by_id.get(sid)
        if not review:
            continue
        check(review.get("source_sha256") == item["source_sha256"], f"{sid}: source hash mismatch")
        check(review.get("target_sha256") == item["target_sha256"], f"{sid}: target hash mismatch")
        check(review.get("policy_sha256") == item["policy_sha256"], f"{sid}: policy hash mismatch")
        flags = review.get("checks", {})
        check(isinstance(flags, dict), f"{sid}: review checks must be an object")
        flags = flags if isinstance(flags, dict) else {}
        for name in item["required_checks"]:
            check(flags.get(name) is True, f"{sid}: required human check not attested: {name}")
        if "notes" in review:
            check(isinstance(review["notes"], str), f"{sid}: notes must be text")

    return {
        "format": "rse-pl-backcheck-proof-v1",
        "product": request["product"],
        "contract_sha256": request["contract_sha256"],
        "packet_sha256": request["packet_sha256"],
        "status": "BLOCK" if issues else "PASS",
        "reviewer": evidence.get("reviewer"),
        "reviewed_at": evidence.get("reviewed_at"),
        "issues": sorted(set(issues)),
        "limits": "PASS proves the requested human attestations are complete and hash-bound. It is not independent proof of linguistic quality or real-template visual fit.",
    }
