#!/usr/bin/env python3
"""Hash-bound R6 print-proof intake. Never a substitute for examining printed pages.

Draft deliberately blocks; structural PASS verifies the receipt, not visual truth.
Does not authorize CONTENT_FROZEN, PRINT_READY, or KDP publication.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from localization.gentle_steps_r5_fit import (  # noqa: E402
    REQUIRED_SURFACE_IDS, REVIEW_FLAGS, _artifact, git_blob_sha1, sha256,
)

REL = "localization/pl-PL/production/gentle-steps/book-versions/v3/"
SOURCE = REL + "GENTLE_STEPS_PL_BOOK_VERSION_03_PACKAGING_CANDIDATE_R6_2026-10-08.md"
R5_SOURCE = REL + "GENTLE_STEPS_PL_BOOK_VERSION_03_PACKAGING_CANDIDATE_R5_2026-10-07.md"
CONTRACT = REL + "V03_R6_FINAL_TEMPLATE_PROOF_CONTRACT_2026-10-08.json"
R6_BLOB = "896cf92bf6ed126ef62e623fd9cac640270e853f"
R5_BLOB = "04b4afcc438789d648ed34fa594f86ee97b02472"
FORMAT = "rse-gentle-steps-pl-v03-r6-template-fit-evidence-v1"
REVIEW_FONT_KEYS = (
    "source_body_font_pt", "rendered_body_font_pt",
    "source_body_leading_pt", "rendered_body_leading_pt",
)


def _is_object(item: object, issues: list[str], label: str) -> dict:
    if isinstance(item, dict):
        return item
    issues.append(f"{label} must be an object")
    return {}


def _canonical_source(issues: list[str], repo: Path) -> Path:
    r6 = repo / SOURCE
    r5 = repo / R5_SOURCE
    for path, expected, label in ((r6, R6_BLOB, "R6"), (r5, R5_BLOB, "R5")):
        if not path.is_file():
            issues.append(f"{label} source missing")
        elif git_blob_sha1(path) != expected:
            issues.append(f"{label} source Git blob drift")
    if r6.is_file() and r5.is_file():
        boundary = "## DZIEŃ 1"
        before = r5.read_text(encoding="utf-8")
        after = r6.read_text(encoding="utf-8")
        if boundary not in before or boundary not in after:
            issues.append("R5/R6 body boundary missing")
        elif before[before.index(boundary):] != after[after.index(boundary):]:
            issues.append("R6 24-day body changed relative to locked R5")
    return r6


def _file_record(record: object, root: Path, issues: list[str],
                 label: str, *, kind: str) -> None:
    record = _is_object(record, issues, label)
    _artifact(record, label, root, issues, rendered=(kind != "template"),
              require_pdf=(kind == "pdf"))
    raw = record.get("path")
    if not isinstance(raw, str) or not raw:
        return
    target = (root / raw).resolve()
    if not target.is_relative_to(root) or not target.is_file():
        return
    if kind == "png":
        if target.suffix.lower() != ".png" or target.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
            issues.append(f"{label} must be a PNG")
    if kind == "template" and target.suffix.lower() not in (".html", ".css", ".json", ".zip"):
        issues.append(f"{label} has unsupported template snapshot extension")


def check_r6_fit_evidence(contract: object, evidence: object, evidence_root: Path,
                          repo_root: Path = ROOT) -> dict:
    issues: list[str] = []
    root = Path(evidence_root).resolve()
    repo = Path(repo_root).resolve()
    contract = _is_object(contract, issues, "contract")
    evidence = _is_object(evidence, issues, "evidence")
    lock = _is_object(contract.get("source_lock"), issues, "contract.source_lock")
    if (lock.get("r6_packaging_path"), lock.get("r6_blob_sha")) != (SOURCE, R6_BLOB):
        issues.append("R6 proof contract differs from the canonical source lock")
    contract_ids = contract.get("required_surface_ids")
    if not isinstance(contract_ids, list) or tuple(contract_ids) != REQUIRED_SURFACE_IDS:
        issues.append("R6 proof contract surface set changed")
    contract_flags = contract.get("required_surface_review_flags")
    if not isinstance(contract_flags, list) or tuple(contract_flags) != REVIEW_FLAGS:
        issues.append("R6 proof contract review flags changed")
    source = _canonical_source(issues, repo)
    if evidence.get("format") != FORMAT:
        issues.append("wrong R6 evidence format")
    if evidence.get("surface_kind") != "actual_final_template":
        issues.append("proxy or unverified template cannot close the R6 gate")
    if evidence.get("_draft_status") or evidence.get("publication_authorized"):
        issues.append("unreviewed or unauthorized evidence")
    info = _is_object(evidence.get("source"), issues, "evidence.source")
    if (info.get("path"), info.get("r6_blob_sha")) != (SOURCE, R6_BLOB):
        issues.append("R6 evidence source identity mismatch")
    if source.is_file() and info.get("sha256") != sha256(source):
        issues.append("R6 evidence source SHA-256 mismatch")
    renderer = _is_object(evidence.get("renderer"), issues, "renderer")
    if not isinstance(renderer.get("name"), str) or not renderer["name"].strip():
        issues.append("missing renderer name")
    if not isinstance(renderer.get("revision"), str) or not renderer["revision"].strip():
        issues.append("missing renderer revision")
    if any(x in str(renderer.get("name", "")).lower() for x in ("synthetic", "proxy")):
        issues.append("synthetic/proxy renderer is not production evidence")
    reviewer = _is_object(evidence.get("reviewer"), issues, "reviewer")
    if not isinstance(reviewer.get("name"), str) or not reviewer["name"].strip():
        issues.append("named print-scale reviewer required")
    try:
        stamp = datetime.fromisoformat(str(reviewer.get("reviewed_at", "")).replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            raise ValueError("timezone absent")
    except ValueError:
        issues.append("timezone-aware print-scale review timestamp required")
    typography = _is_object(evidence.get("typography"), issues, "typography")
    if typography.get("body_font_reduced_to_force_fit") is not False:
        issues.append("body font shrink-to-fit must be explicitly false")
    for field in REVIEW_FONT_KEYS:
        number = typography.get(field)
        if not isinstance(number, (int, float)) or isinstance(number, bool) or number <= 0:
            issues.append(f"missing/invalid actual font metric: {field}")
    if all(isinstance(typography.get(k), (int, float)) and
           not isinstance(typography.get(k), bool) for k in REVIEW_FONT_KEYS):
        if typography["rendered_body_font_pt"] < typography["source_body_font_pt"]:
            issues.append("body font was reduced")
        if typography["rendered_body_leading_pt"] < typography["source_body_leading_pt"]:
            issues.append("body leading was reduced")
    _file_record(evidence.get("template"), root, issues, "final template", kind="template")
    _file_record(evidence.get("rendered_book"), root, issues, "whole-book render", kind="pdf")
    surfaces = evidence.get("surfaces")
    if not isinstance(surfaces, list):
        issues.append("surfaces must be a list")
        surfaces = []
    ids, paths, hashes = [], [], []
    for item in surfaces:
        surface = _is_object(item, issues, "surface")
        sid = surface.get("id")
        if not isinstance(sid, str):
            issues.append("invalid surface ID")
            sid = None
        ids.append(sid)
        render = _is_object(surface.get("render"), issues, f"{sid}.render")
        review = _is_object(surface.get("review"), issues, f"{sid}.review")
        _file_record(render, root, issues, f"surface {sid}", kind="png")
        if isinstance(render.get("path"), str):
            paths.append(str((root / render["path"]).resolve()))
        if isinstance(render.get("sha256"), str):
            hashes.append(render["sha256"])
        if review.get("render_sha256") != render.get("sha256"):
            issues.append(f"{sid}: review is not bound to its render")
        for flag in REVIEW_FLAGS:
            if review.get(flag) is not True:
                issues.append(f"{sid}: {flag} not verified")
    if len(surfaces) != len(REQUIRED_SURFACE_IDS) or set(ids) != set(REQUIRED_SURFACE_IDS):
        issues.append("evidence must contain all 12 unique R6 review surfaces")
    if len(ids) != len(set(ids)) or len(paths) != len(set(paths)) or len(hashes) != len(set(hashes)):
        issues.append("duplicate surface id, artifact path or render bytes")
    return {
        "format": "rse-gentle-steps-pl-v03-r6-fit-intake-proof-v1",
        "status": "BLOCK" if issues else "PASS",
        "r6_blob_sha": R6_BLOB,
        "surfaces_required": list(REQUIRED_SURFACE_IDS),
        "issues": sorted(set(issues)),
        "limits": ("PASS verifies source/invariant/hash binding and a named print-scale "
                   "reviewer's declarations; it cannot verify visual truth or authorize "
                   "CONTENT_FROZEN, PRINT_READY, publishing, pricing or release."),
    }


def _capture(root: Path, relative: str, kind: str) -> dict:
    if not relative or Path(relative).is_absolute():
        raise ValueError("artifact path must be relative")
    target = (root / relative).resolve()
    if not target.is_relative_to(root) or not target.is_file():
        raise ValueError(f"missing/outside artifact: {relative}")
    if not target.stat().st_size:
        raise ValueError(f"empty artifact: {relative}")
    issues: list[str] = []
    _file_record({"path": relative, "sha256": sha256(target)}, root, issues, relative, kind=kind)
    if issues:
        raise ValueError("; ".join(issues))
    return {"path": relative, "sha256": sha256(target)}


def create_r6_draft(artifact_root: Path, template: str, book: str, surface_dir: str,
                    renderer_name: str, renderer_revision: str, repo_root: Path = ROOT) -> dict:
    root = Path(artifact_root).resolve()
    issues: list[str] = []
    source = _canonical_source(issues, Path(repo_root))
    if issues:
        raise ValueError("; ".join(issues))
    if not renderer_name.strip() or not renderer_revision.strip():
        raise ValueError("renderer name and revision are required")
    surfaces = []
    for sid in REQUIRED_SURFACE_IDS:
        snapshot = _capture(root, str(Path(surface_dir) / (sid + ".png")), "png")
        surfaces.append({"id": sid, "render": snapshot,
                         "review": {"render_sha256": snapshot["sha256"],
                                    **{flag: False for flag in REVIEW_FLAGS}}})
    if len({s["render"]["sha256"] for s in surfaces}) != len(surfaces):
        raise ValueError("distinct screenshot names must not contain identical bytes")
    return {
        "format": FORMAT,
        "surface_kind": "PENDING_ACTUAL_FINAL_TEMPLATE_CONFIRMATION",
        "source": {"path": SOURCE, "r6_blob_sha": R6_BLOB, "sha256": sha256(source)},
        "renderer": {"name": renderer_name.strip(), "revision": renderer_revision.strip()},
        "reviewer": {"name": "", "reviewed_at": ""},
        "typography": {"body_font_reduced_to_force_fit": None,
                       **{k: None for k in REVIEW_FONT_KEYS}},
        "template": _capture(root, template, "template"),
        "rendered_book": _capture(root, book, "pdf"),
        "surfaces": surfaces,
        "_draft_status": "UNREVIEWED__MUST_BLOCK",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    draft = commands.add_parser("draft")
    draft.add_argument("--artifact-root", required=True, type=Path)
    draft.add_argument("--template", default="template/final_template.html")
    draft.add_argument("--book", default="book/full_book.pdf")
    draft.add_argument("--surface-dir", default="reviews")
    draft.add_argument("--renderer-name", required=True)
    draft.add_argument("--renderer-revision", required=True)
    draft.add_argument("--output", required=True, type=Path)
    verify = commands.add_parser("verify")
    verify.add_argument("--evidence", required=True, type=Path)
    verify.add_argument("--artifact-root", required=True, type=Path)
    verify.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "draft":
            result = create_r6_draft(args.artifact_root, args.template, args.book,
                                     args.surface_dir, args.renderer_name,
                                     args.renderer_revision)
            output = args.output
            output.parent.mkdir(parents=True, exist_ok=True)
            with output.open("x", encoding="utf-8") as handle:
                json.dump(result, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
            print(f"UNREVIEWED DRAFT — deliberately BLOCK: {output}")
            return 0
        contract = json.loads((ROOT / CONTRACT).read_text(encoding="utf-8"))
        evidence = json.loads(args.evidence.read_text(encoding="utf-8"))
        proof = check_r6_fit_evidence(contract, evidence, args.artifact_root)
        payload = json.dumps(proof, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(payload, encoding="utf-8")
        print(payload, end="")
        return 0 if proof["status"] == "PASS" else 2
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"BLOCK: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
