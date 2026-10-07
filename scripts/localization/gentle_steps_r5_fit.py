"""Deterministic intake validation for Gentle Steps PL V03 R5 template-fit evidence."""
from __future__ import annotations

import hashlib
from pathlib import Path

EXPECTED_FORMAT = "rse-gentle-steps-pl-v03-r5-template-fit-evidence-v1"
EXPECTED_SOURCE_PATH = (
    "localization/pl-PL/production/gentle-steps/book-versions/v3/"
    "GENTLE_STEPS_PL_BOOK_VERSION_03_PACKAGING_CANDIDATE_R5_2026-10-07.md"
)
EXPECTED_R5_BLOB = "04b4afcc438789d648ed34fa594f86ee97b02472"
REQUIRED_SURFACE_IDS = (
    "front_title_subtitle",
    "front_happy_makers",
    "front_how_book_works",
    "day_24",
    "day_18",
    "day_09",
    "day_01",
    "day_23",
    "day_07",
    "day_21",
    "day_22",
    "day_10",
)
REVIEW_FLAGS = (
    "no_clipping",
    "no_collisions",
    "diacritics_correct",
    "print_scale_reviewed",
    "readable",
    "copy_complete",
)


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _artifact(record: dict, label: str, root: Path, issues: list[str], *, rendered: bool) -> None:
    raw = record.get("path")
    if not isinstance(raw, str) or not raw.strip():
        issues.append(f"Missing artifact path: {label}")
        return
    path = (root / raw).resolve()
    try:
        inside = path.is_relative_to(root)
    except AttributeError:
        inside = str(path).startswith(str(root))
    if not inside or not path.is_file():
        issues.append(f"Missing/outside evidence artifact: {label}")
        return
    if path.stat().st_size <= 0:
        issues.append(f"Empty artifact: {label}")
        return
    expected = record.get("sha256")
    actual = sha256(path)
    if expected != actual:
        issues.append(f"Artifact hash mismatch: {label}")
    if rendered:
        header = path.read_bytes()[:8]
        if not (header.startswith(b"\x89PNG\r\n\x1a\n") or header.startswith(b"%PDF-")):
            issues.append(f"Expected PNG/PDF render: {label}")


def check_r5_fit_evidence(contract: dict, evidence: dict, evidence_root: Path, repo_root: Path) -> dict:
    """Return PASS/BLOCK proof for an exact-source-bound R5 render evidence bundle."""
    issues: list[str] = []
    evidence_root = Path(evidence_root).resolve()
    repo_root = Path(repo_root).resolve()

    source_lock = contract.get("source_lock", {})
    contract_blob = source_lock.get("r5_blob_sha")
    contract_path = source_lock.get("r5_packaging_path")

    if contract_blob != EXPECTED_R5_BLOB:
        issues.append("Proof contract R5 blob does not match canonical lock")
    if contract_path != EXPECTED_SOURCE_PATH:
        issues.append("Proof contract R5 path does not match canonical lock")

    source_path = (repo_root / EXPECTED_SOURCE_PATH).resolve()
    if not source_path.is_file():
        issues.append("Canonical R5 packaging source is missing")
    else:
        if git_blob_sha1(source_path) != EXPECTED_R5_BLOB:
            issues.append("Canonical R5 packaging source blob drifted")

    if evidence.get("format") != EXPECTED_FORMAT:
        issues.append("Wrong evidence format")
    if evidence.get("surface_kind") != "actual_final_template":
        issues.append("Proxy/non-final template evidence cannot close the gate")
    if evidence.get("source", {}).get("path") != EXPECTED_SOURCE_PATH:
        issues.append("Evidence source path does not match R5 lock")
    if evidence.get("source", {}).get("r5_blob_sha") != EXPECTED_R5_BLOB:
        issues.append("Evidence source blob does not match R5 lock")
    if source_path.is_file():
        if evidence.get("source", {}).get("sha256") != sha256(source_path):
            issues.append("Evidence source SHA-256 does not match canonical R5 bytes")

    renderer = evidence.get("renderer", {})
    if not renderer.get("name") or not renderer.get("revision"):
        issues.append("Renderer provenance missing")
    reviewer = evidence.get("reviewer", {})
    if not reviewer.get("name") or not reviewer.get("reviewed_at"):
        issues.append("Print-scale reviewer provenance missing")

    typography = evidence.get("typography", {})
    if typography.get("body_font_reduced_to_force_fit") is not False:
        issues.append("Body typography shrink-to-fit must be explicitly false")

    _artifact(evidence.get("template", {}), "final template snapshot", evidence_root, issues, rendered=False)
    _artifact(evidence.get("rendered_book", {}), "rendered book", evidence_root, issues, rendered=True)

    surfaces = evidence.get("surfaces", [])
    if not isinstance(surfaces, list):
        issues.append("Surfaces must be a list")
        surfaces = []
    ids = [s.get("id") for s in surfaces if isinstance(s, dict)]
    if len(ids) != len(set(ids)):
        issues.append("Duplicate surface IDs")
    if set(ids) != set(REQUIRED_SURFACE_IDS):
        issues.append("Evidence must contain exactly the required R5 review surfaces")

    for surface in surfaces:
        if not isinstance(surface, dict):
            issues.append("Invalid surface record")
            continue
        sid = surface.get("id", "<unknown>")
        _artifact(surface.get("render", {}), f"surface {sid}", evidence_root, issues, rendered=True)
        review = surface.get("review", {})
        if review.get("render_sha256") != surface.get("render", {}).get("sha256"):
            issues.append(f"{sid}: review is not bound to its render")
        for flag in REVIEW_FLAGS:
            if review.get(flag) is not True:
                issues.append(f"{sid}: {flag} not verified")

    return {
        "format": "rse-gentle-steps-pl-v03-r5-fit-intake-proof-v1",
        "status": "BLOCK" if issues else "PASS",
        "r5_blob_sha": EXPECTED_R5_BLOB,
        "required_surface_ids": list(REQUIRED_SURFACE_IDS),
        "issues": sorted(set(issues)),
        "limits": (
            "PASS validates source binding, artifact integrity and declared print-scale checks. "
            "It does not authorize CONTENT_FROZEN, PRINT_READY, publication or release."
        ),
    }
