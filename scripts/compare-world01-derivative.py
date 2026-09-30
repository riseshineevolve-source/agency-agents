#!/usr/bin/env python3
"""Reproducible lexical audit of World 01 app fields against the published PDF.

This is a triage tool, not a parity certificate. PDF extraction cannot prove speaker,
ordering, punctuation, or layout; visual review is required before promotion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path

LEVEL_PAGES = {1: range(15, 23), 2: range(23, 33), 3: range(33, 42)}
FIELD_RE = re.compile(
    r'\b(?P<field>text|title|subtitle|key|missionObjective|science|inStory|yourTurn|code|meaning|operation|parentSays|teachToSay|topSecretScience):\s*"(?P<value>(?:\\.|[^"\\])*)"'
)


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).lower()
    return re.sub(r"[^a-z0-9]", "", value)


def sections(source: str) -> dict[int, str]:
    result = {}
    for level in LEVEL_PAGES:
        start = source.find(f"WORLD 01 — LEVEL {level}:")
        if start < 0:
            raise ValueError(f"missing World 01 level {level} marker")
        next_level = source.find(f"WORLD 01 — LEVEL {level + 1}:", start)
        if next_level < 0 and level < 3:
            raise ValueError(f"missing World 01 level {level + 1} marker")
        if level == 3 and next_level < 0:
            next_level = source.find("WORLD 02 — LEVEL", start)
        result[level] = source[start:next_level if next_level >= 0 else None]
    return result


def compare(app_source: str, page_texts: dict[int, str]) -> dict:
    result = {}
    for level, section in sections(app_source).items():
        fields = []
        for match in FIELD_RE.finditer(section):
            value = json.loads('"' + match.group("value") + '"')
            needle = normalized(value)
            matching_pages = [
                page for page in LEVEL_PAGES[level]
                if needle and needle in normalized(page_texts.get(page, ""))
            ]
            fields.append({
                "field": match.group("field"),
                "value": value,
                "matching_pdf_pages": matching_pages,
                "classification": "lexical_match_only" if matching_pages else "not_found_by_extraction",
            })
        result[str(level)] = {
            "field_count": len(fields),
            "lexical_match_count": sum(bool(field["matching_pdf_pages"]) for field in fields),
            "fields": fields,
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("app_story_content", type=Path, help="read-only copy of spark-joy-fam/src/data/storyContent.ts")
    parser.add_argument("published_pdf", type=Path)
    parser.add_argument("--output", type=Path, help="optional JSON audit file")
    args = parser.parse_args()
    from pypdf import PdfReader

    app_bytes = args.app_story_content.read_bytes()
    pdf_bytes = args.published_pdf.read_bytes()
    reader = PdfReader(args.published_pdf)
    page_texts = {page: reader.pages[page - 1].extract_text() or "" for pages in LEVEL_PAGES.values() for page in pages}
    result = {
        "app_file_sha256": hashlib.sha256(app_bytes).hexdigest(),
        "pdf_sha256": hashlib.sha256(pdf_bytes).hexdigest(),
        "normalization": "NFKD lowercase ASCII letters/digits only; same-page substring search",
        "warning": "A lexical match does not establish published wording, speaker, order, or science approval.",
        "levels": compare(app_bytes.decode("utf-8"), page_texts),
    }
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for level, audit in result["levels"].items():
        print(f"Level {level}: {audit['lexical_match_count']}/{audit['field_count']} lexical matches")
        for field in audit["fields"]:
            if not field["matching_pdf_pages"]:
                print(f"  NOT FOUND {field['field']}: {field['value'][:100]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
