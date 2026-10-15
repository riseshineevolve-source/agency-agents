"""Byte-bound pre-freeze checks for the Detective V3 text master.

This is an inventory/receipt guard, not a translator or a layout verifier.
"""
from __future__ import annotations

import hashlib
import re

from .contracts import require
from .detective import freeze_gate
from .io import digest


SOURCE_PATH = "orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md"
CASE = re.compile(r"^## CASE (\d{2}) // ", re.M)
HINT_CASE = re.compile(r"^## CASE (\d{2})\s*$", re.M)
REQUIRED_CASE_HEADINGS = (
    "### CASE FILE // WHAT HAPPENED",
    "### YOUR OBJECTIVE",
    "### INVESTIGATION RULES",
    "### HAPPY MAKERS CHAT",
    "### PUZZLE / EVIDENCE SURFACE",
    "### YOUR VERDICT / RESPONSE",
)


def git_blob_sha1(raw):
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def verify_candidate(raw, receipt):
    """Fail closed if bytes or the reader-facing V3 case apparatus drift."""
    require(receipt.get("canonical_text_path") == SOURCE_PATH, "Detective V3 source path differs from receipt")
    require(receipt.get("canonical_text_git_blob") == git_blob_sha1(raw), "Detective V3 Git blob differs from receipt")
    require(receipt.get("canonical_text_sha256") == hashlib.sha256(raw).hexdigest(), "Detective V3 bytes differ from receipt")
    text = raw.decode("utf-8")
    required_sections = (
        "# FRONT MATTER // LOCKED READER PAGES 1-10",
        "## YOUR CASE WALL + HINT VAULT",
        "# ROOM ZERO // THE EXPLANATION",
        "# FIELD CERTIFICATION",
        "# ARCHIVE FILE 001 // STILL OPEN",
        "# HINT VAULT // LEVEL 1",
        "# HINT VAULT // LEVEL 2",
        "# HINT VAULT // LEVEL 3",
        "# SOLUTION FILES",
        "# EDITORIAL LOCKS // NOT PRINTED",
    )
    positions = [text.find(section) for section in required_sections]
    require(all(pos >= 0 for pos in positions) and positions == sorted(positions), "Detective V3 section order/coverage changed")
    expected = [f"{n:02d}" for n in range(1, 31)]
    story = text[positions[0]:positions[2]]
    cases = list(CASE.finditer(story))
    require([m.group(1) for m in cases] == expected, "Detective V3 must have 30 ordered reader cases")
    for i, match in enumerate(cases):
        end = cases[i + 1].start() if i + 1 < len(cases) else len(story)
        section = story[match.start():end]
        next_top_level = re.search(r"^# ", section, re.M)
        if next_top_level:
            section = section[:next_top_level.start()]
        require(all(section.count(heading) == 1 for heading in REQUIRED_CASE_HEADINGS),
                f"Detective V3 Case {match.group(1)} apparatus changed")
    for level in range(3):
        section = text[positions[5 + level]:positions[6 + level]]
        require(HINT_CASE.findall(section) == expected, f"Detective V3 Hint Level {level + 1} coverage changed")
    solutions = text[positions[8]:positions[9]]
    require([m.group(1) for m in CASE.finditer(solutions)] == expected,
            "Detective V3 solution coverage changed")
    return {"canonical_text_git_blob": git_blob_sha1(raw),
            "canonical_text_sha256": hashlib.sha256(raw).hexdigest(),
            "reader_cases": 30, "hint_levels": 3, "hint_entries": 90,
            "solution_entries": 30, "status": "PREFREEZE_SOURCE_VERIFIED"}


def verify_frozen(raw, receipt, frozen_source, aliases):
    """Add existing owner/ALL-15/alias gates to the V3 receipt check."""
    result = verify_candidate(raw, receipt)
    freeze_gate(receipt, hashlib.sha256(frozen_source).hexdigest())
    require(receipt.get("aliases_sha256") == digest(aliases), "Frozen alias snapshot hash mismatch")
    result["status"] = "FROZEN_SOURCE_RECEIPT_VERIFIED"
    return result
