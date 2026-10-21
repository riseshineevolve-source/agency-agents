#!/usr/bin/env python3
"""Reproduce the source-only PNGs inspected by figure_consistency.

No candidate or production files are edited. The original review used
PyMuPDF 1.26.6 / MuPDF 1.26.11, page.get_pixmap(matrix=Matrix(1.15, 1.15)),
then Pixmap.save(path). Defaults are retained: RGB, no alpha, annotations on,
full-page clip. PNG byte hashes may differ with other renderer versions;
such a difference must not be treated as a changed source PDF.
"""
import argparse
import hashlib
import json
from pathlib import Path

import fitz

SOURCE_SHA256 = "9db84d4f138cbbde8eb1f4a0f783f4d126c639120a11cabb65fc00711b9f05a0"
PAGES = [13, 15, 16, 17, 18, 24, 25, 80, 122, 123, 130, 131,
         141, 142, 143, 144, 145, 146, 147, 158]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--review", type=Path, default=Path(__file__).with_name(
        "review-figure-dependencies.json"))
    args = parser.parse_args()
    observed = sha(args.pdf)
    if observed != SOURCE_SHA256:
        parser.error(f"Source hash mismatch: {observed}")
    review = json.loads(args.review.read_text())
    expected = {item["page"]: item["png_sha256"]
                for item in review["render_evidence"]}
    if set(expected) != set(PAGES):
        parser.error("Review evidence pages do not match the original 20-page scope")
    args.output.mkdir(parents=True, exist_ok=True)
    results = []
    with fitz.open(args.pdf) as doc:
        if len(doc) != 225:
            parser.error("Expected authoritative 225-page source")
        for number in PAGES:
            out = args.output / f"p{number:03}.png"
            doc[number - 1].get_pixmap(matrix=fitz.Matrix(1.15, 1.15)).save(out)
            actual = sha(out)
            results.append({"page": number, "png_sha256": actual,
                            "matches_recorded_hash": actual == expected[number]})
    report = {"source_pdf_sha256": observed,
              "renderer": fitz.__doc__.strip(),
              "settings": {"matrix": [1.15, 1.15],
                           "other_get_pixmap_arguments": "defaults"},
              "all_recorded_hashes_reproduced": all(
                  item["matches_recorded_hash"] for item in results),
              "renders": results}
    (args.output / "reproduction.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not report["all_recorded_hashes_reproduced"]:
        raise SystemExit("PNG hash differences: inspect renderer version before review")


if __name__ == "__main__":
    main()
