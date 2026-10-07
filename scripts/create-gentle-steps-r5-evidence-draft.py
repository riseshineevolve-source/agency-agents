#!/usr/bin/env python3
"""Create a hash-bound, deliberately UNAPPROVED Gentle Steps PL R5 fit-evidence draft.

The renderer provides the files. A human print-scale reviewer must verify each
surface and explicitly complete the review flags before the separate validator
can return PASS. This tool cannot authorize a content freeze or publication.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from localization.gentle_steps_r5_fit import (  # noqa: E402
    EXPECTED_FORMAT,
    EXPECTED_R5_BLOB,
    EXPECTED_SOURCE_PATH,
    REQUIRED_SURFACE_IDS,
    REVIEW_FLAGS,
    git_blob_sha1,
    sha256,
)


def artifact(root: Path, relative: str, *, extensions: tuple[str, ...]) -> dict[str, str]:
    """Return a content-addressed artifact inside the supplied evidence root."""
    if not relative or Path(relative).is_absolute():
        raise ValueError(f"Invalid relative artifact path: {relative!r}")
    target = (root / relative).resolve()
    try:
        clean = target.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Artifact escapes evidence root: {relative!r}") from exc
    if not target.is_file() or target.stat().st_size == 0:
        raise ValueError(f"Missing/empty artifact: {clean}")
    if target.suffix.lower() not in extensions:
        raise ValueError(f"Wrong artifact extension: {clean}; expected {extensions}")
    with target.open("rb") as stream:
        header = stream.read(8)
    if extensions == (".pdf",) and not header.startswith(b"%PDF-"):
        raise ValueError(f"Whole-book artifact does not have a PDF header: {clean}")
    if target.suffix.lower() == ".png" and header != bytes.fromhex("89504e470d0a1a0a"):
        raise ValueError(f"Review surface does not have a PNG header: {clean}")
    return {"path": clean.as_posix(), "sha256": sha256(target)}


def create_draft(
    artifact_root: Path, *,
    template_path: str, book_path: str, surface_dir: str,
    renderer_name: str, renderer_revision: str,
) -> dict:
    artifact_root = artifact_root.resolve()
    if not artifact_root.is_dir():
        raise ValueError(f"Artifact directory not found: {artifact_root}")
    source = ROOT / EXPECTED_SOURCE_PATH
    if not source.is_file() or git_blob_sha1(source) != EXPECTED_R5_BLOB:
        raise ValueError("Canonical R5 source missing or Git blob is not locked R5")
    if not renderer_name.strip() or not renderer_revision.strip():
        raise ValueError("Renderer name and exact revision are required")

    template = artifact(artifact_root, template_path, extensions=(".html", ".css", ".json", ".zip"))
    book = artifact(artifact_root, book_path, extensions=(".pdf",))
    surfaces = []
    hashes = []
    for sid in REQUIRED_SURFACE_IDS:
        rel = str(Path(surface_dir) / (sid + ".png"))
        item = artifact(artifact_root, rel, extensions=(".png",))
        hashes.append(item["sha256"])
        review = {"render_sha256": item["sha256"]}
        review.update({flag: False for flag in REVIEW_FLAGS})
        surfaces.append({"id": sid, "render": item, "review": review})
    if len(set(hashes)) != len(hashes):
        raise ValueError("Different review surfaces share identical bytes")

    return {
        "format": EXPECTED_FORMAT,
        "surface_kind": "PENDING_ACTUAL_FINAL_TEMPLATE_CONFIRMATION",
        "source": {
            "path": EXPECTED_SOURCE_PATH,
            "r5_blob_sha": EXPECTED_R5_BLOB,
            "sha256": sha256(source),
        },
        "renderer": {"name": renderer_name.strip(), "revision": renderer_revision.strip()},
        "reviewer": {"name": "", "reviewed_at": ""},
        "typography": {"body_font_reduced_to_force_fit": None},
        "template": template,
        "rendered_book": book,
        "surfaces": surfaces,
        "_draft_status": "UNREVIEWED__MUST_BLOCK",
        "_review_instructions": (
            "Inspect the actual final-template PDF and all twelve surface renders at print scale. "
            "Set surface_kind to actual_final_template only after confirming it. "
            "Add reviewer name and timestamp, confirm typography explicitly false, "
            "and mark each review flag true only for evidence personally checked. "
            "Then run validate-gentle-steps-r5-fit-evidence.py; PASS is not publication approval."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--artifact-root", type=Path, required=True)
    p.add_argument("--template", default="template/final_template.html")
    p.add_argument("--book", default="book/full_book.pdf")
    p.add_argument("--surface-dir", default="reviews")
    p.add_argument("--renderer-name", required=True)
    p.add_argument("--renderer-revision", required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    try:
        draft = create_draft(
            args.artifact_root,
            template_path=args.template,
            book_path=args.book,
            surface_dir=args.surface_dir,
            renderer_name=args.renderer_name,
            renderer_revision=args.renderer_revision,
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as f:
            json.dump(draft, f, ensure_ascii=False, indent=2)
            f.write(chr(10))
    except (ValueError, OSError) as exc:
        print(f"BLOCK: {exc}", file=sys.stderr)
        return 2
    print(f"DRAFT ONLY (intentionally unapproved): {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
