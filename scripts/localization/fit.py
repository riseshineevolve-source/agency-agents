"""Bind real-template render/review evidence to the four unchanged PL headings."""
from __future__ import annotations

from pathlib import Path
from .io import digest, file_digest
from .contracts import require


def fit_request(spec):
    return {"format": "rse-real-template-fit-request-v1", "product": spec["product"],
            "status": "BLOCKED_REAL_TEMPLATE", "spec_sha256": digest(spec), "pages": spec["pages"],
            "requirements": ["Use actual editable/rendering source", "Preserve body font size and leading", "Review all pages at print size", "No clipping, collisions or missing Polish diacritics", "No proxy-based approval"]}


def check_evidence(spec, evidence, base):
    issues = []
    base = Path(base).resolve()
    def check(condition, message):
        if not condition:
            issues.append(message)
    def artifact(record, label):
        path = (base / record.get("path", "")).resolve()
        # Evidence bundles must be portable and cannot refer outside their root.
        if not path.is_relative_to(base) or not path.is_file():
            issues.append(f"Missing/outside evidence artifact: {label}")
            return
        check(record.get("sha256") == file_digest(path), f"Artifact hash mismatch: {label}")
        check(path.stat().st_size > 0, f"Empty artifact: {label}")
    check(evidence.get("format") == "rse-real-template-fit-evidence-v1", "Wrong evidence format")
    check(evidence.get("spec_sha256") == digest(spec), "Evidence uses stale headings/spec")
    check(evidence.get("surface_kind") == "actual_template", "Proxy surfaces cannot close the gate")
    check(bool(evidence.get("renderer")) and bool(evidence.get("renderer_revision")), "Renderer provenance missing")
    check(bool(evidence.get("reviewer")), "Print-scale reviewer missing")
    artifact(evidence.get("template", {}), "real template")
    actual = evidence.get("pages", [])
    expected = {p["source_pdf_page"]: p for p in spec["pages"]}
    check(len(actual) == len(expected) and {p.get("source_pdf_page") for p in actual} == set(expected), "Must supply exactly pages 25, 26, 35, 38")
    for page in actual:
        number = page.get("source_pdf_page")
        wanted = expected.get(number)
        if wanted is None:
            continue
        check(page.get("heading") in wanted["approved_line_breaks"], f"Page {number}: unapproved heading or line break")
        check(page.get("heading_sha256") == digest(page.get("heading")), f"Page {number}: heading hash mismatch")
        artifact(page.get("render", {}), f"page {number}")
        review = page.get("review", {})
        check(review.get("render_sha256") == page.get("render", {}).get("sha256"), f"Page {number}: review is not bound to this render")
        for flag in ("no_clipping", "no_collisions", "diacritics_correct", "print_scale_reviewed", "heading_legible", "tracking_acceptable"):
            check(review.get(flag) is True, f"Page {number}: {flag} not verified")
        for field in ("body_font_pt", "body_leading_pt"):
            original, rendered = page.get("source_" + field), page.get("rendered_" + field)
            check(isinstance(original, (int, float)) and original > 0 and original == rendered, f"Page {number}: body typography changed or unmeasured ({field})")
    return {"format": "rse-fit-proof-v1", "product": spec["product"], "status": "BLOCK" if issues else "PASS", "issues": sorted(set(issues)), "spec_sha256": digest(spec), "limits": "PASS relies on the named reviewer's real-template and print-scale attestations; hashes bind artifacts, not visual truth."}
