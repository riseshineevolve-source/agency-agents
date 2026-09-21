"""A generated human-readable view of the single canonical terminology catalog."""
from .gates import load_terms


def markdown(catalog):
    load_terms(catalog)
    lines = ["# RSE Polish terminology and identity contract", "", "Generated from [engine/terminology.json](engine/terminology.json). Edit the JSON catalog, then run `python scripts/localization-engine.py terms-doc`. Historical calibration documents retain their original evidence; this catalog owns current lock states.", "", "Whole-segment recurring labels use exact normalized target forms. Embedded names use explicitly recorded inflections. Unlisted declensions require review; IDs, keys, URLs and answer data stay in the protected source contract. Provisional and owner-gated entries never become global approvals through reuse.", "", "| ID | Product | EN source | PL forms | State / mode | Rationale |", "|---|---|---|---|---|---|"]
    for t in sorted(catalog["terms"], key=lambda t:t["id"]):
        cells = [t["id"], ", ".join(t["products"]), t["source"], " / ".join(t["targets"]) or "Owner decision required", t["state"] + " / " + t["mode"], t["rationale"]]
        lines.append("| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |")
    lines += ["", "Each machine record retains source-language provenance and a target-language lock state. Unknown UI/CTA copy requires bilingual QA; this catalog does not invent translations for missing product copy.", ""]
    return "\n".join(lines)
