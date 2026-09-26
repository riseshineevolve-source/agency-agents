#!/usr/bin/env python3
"""Fail closed on the bounded published World 01 mission-opener candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "orchestration/content-packs/world01/mission-openers.en.candidate.json"
EVIDENCE = ROOT / "orchestration/content-sources/world01-paperback-opener-evidence.json"
EVIDENCE_REF = EVIDENCE.relative_to(ROOT).as_posix()
SOURCE_ID = "world01_paperback_2026_09_18"
SOURCE_SHA256 = "adf9d384985ec7ad0fb1d7f9f6c3d46189592a171474c38ee93ac35bb808c549"
SOURCE_BYTES = 14523549
SOURCE_PAGES = 108


def read_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate(pack: dict, evidence: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(pack, dict) or not isinstance(evidence, dict):
        return ["pack and evidence must be objects"]

    expected_top_keys = {
        "schema_version", "product_id", "content_pack_id", "content_version",
        "canonical_locale", "supported_locales", "planned_locales",
        "minimum_runtime_contract", "candidate_scope", "provenance",
        "activities", "localized_copy", "activity_provenance",
    }
    if set(pack) != expected_top_keys:
        errors.append("unexpected or missing pack fields")
    expected_envelope = {
        "schema_version": "0.1.0",
        "product_id": "level_up_your_brain_world_01",
        "content_pack_id": "world01_mission_openers_pilot",
        "content_version": "0.1.0",
        "canonical_locale": "en",
        "supported_locales": ["en"],
        "planned_locales": ["pl-PL"],
        "minimum_runtime_contract": "0.1.0",
        "candidate_scope": "published_mission_openers_only",
        "provenance": {
            "source_id": SOURCE_ID,
            "source_sha256": SOURCE_SHA256,
            "evidence_manifest": EVIDENCE_REF,
        },
    }
    for key, expected in expected_envelope.items():
        if pack.get(key) != expected:
            errors.append(f"incorrect {key}")

    expected_source = {
        "evidence_version": 1,
        "source_id": SOURCE_ID,
        "role": "published_paperback_evidence",
        "filename": "10 STORIES WORLD 01 FINAL paperback.pdf",
        "sha256": SOURCE_SHA256,
        "bytes": SOURCE_BYTES,
        "pages": SOURCE_PAGES,
        "isbn_paperback": "9798247194682",
        "verification": "PDF text extraction plus visual inspection of pages 15, 23, and 33",
    }
    for key, expected in expected_source.items():
        if evidence.get(key) != expected:
            errors.append(f"incorrect evidence {key}")
    openers = evidence.get("mission_openers")
    if not isinstance(openers, list) or len(openers) != 3:
        return errors + ["evidence must contain exactly three mission openers"]

    expected_activities = []
    expected_copy = []
    expected_provenance = []
    for index, opener in enumerate(openers, 1):
        if not isinstance(opener, dict):
            errors.append(f"opener {index} must be an object")
            continue
        mission_id = f"world01_mission_{index:03d}"
        page = (15, 23, 33)[index - 1]
        if set(opener) != {"mission_id", "page", "title", "key_acquired", "objective"}:
            errors.append(f"opener {index} has unexpected or missing fields")
        if opener.get("mission_id") != mission_id or opener.get("page") != page:
            errors.append(f"opener {index} identity/page mismatch")
        for field in ("title", "key_acquired", "objective"):
            if not isinstance(opener.get(field), str) or not opener[field].strip():
                errors.append(f"opener {index} missing {field}")
        activity_id = f"{mission_id}_overview"
        next_id = f"world01_mission_{index + 1:03d}_overview" if index < 3 else None
        expected_activities.append({
            "activity_id": activity_id,
            "activity_type": "info_card",
            "sequence": index,
            "required": True,
            "interaction": {"mode": "continue", "option_ids": []},
            "progress": {"completion_rule": "submit_once", "unlock_ids": [next_id] if next_id else []},
            "assets": [],
            "accessibility": {
                "requires_audio_alternative": False,
                "requires_motion_reduction_variant": False,
            },
        })
        expected_copy.append({
            "locale": "en",
            "activity_id": activity_id,
            "title": opener.get("title"),
            "prompt": opener.get("objective"),
            "key_acquired": opener.get("key_acquired"),
            "options": {},
            "accessibility": {},
        })
        expected_provenance.append({
            "activity_id": activity_id,
            "source_id": SOURCE_ID,
            "page": page,
        })

    if pack.get("activities") != expected_activities:
        errors.append("activity graph differs from bounded overview candidate")
    if pack.get("localized_copy") != expected_copy:
        errors.append("canonical copy differs from published opener evidence")
    if pack.get("activity_provenance") != expected_provenance:
        errors.append("activity provenance differs from published opener evidence")
    return errors


def verify_pdf(pdf_path: Path, evidence: dict) -> list[str]:
    """Optional custody check against the private binary; CI uses the locked manifest."""
    from pypdf import PdfReader

    errors: list[str] = []
    with pdf_path.open("rb") as handle:
        digest = hashlib.file_digest(handle, "sha256").hexdigest()
    if digest != SOURCE_SHA256:
        errors.append("PDF SHA-256 differs from locked published evidence")
    if pdf_path.stat().st_size != SOURCE_BYTES:
        errors.append("PDF byte length differs from locked published evidence")
    if errors:
        return errors
    reader = PdfReader(pdf_path)
    if len(reader.pages) != SOURCE_PAGES:
        return ["PDF page count differs from locked published evidence"]
    collapse = lambda value: re.sub(r"\s+", " ", value).strip()
    for opener in evidence["mission_openers"]:
        page = opener["page"]
        text = collapse(reader.pages[page - 1].extract_text() or "")
        for field in ("title", "key_acquired", "objective"):
            if collapse(opener[field]) not in text:
                errors.append(f"PDF page {page} does not contain {field}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, help="private published paperback for binary/page verification")
    args = parser.parse_args()
    try:
        pack = read_json(PACK)
        evidence = read_json(EVIDENCE)
        errors = validate(pack, evidence)
        if args.pdf and not errors:
            errors.extend(verify_pdf(args.pdf, evidence))
    except (OSError, ValueError, json.JSONDecodeError, ImportError) as exc:
        print(f"FAIL: {exc}")
        return 1
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: World 01 mission-opener candidate matches locked published evidence")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
