"""Derive bounded bilingual proof only from already-authorized calibration text.

Historical book fixtures lacking verbatim EN are scanned by the legacy regression;
we do not manufacture source prose to give them a fictitious coverage percentage.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import re

from .contracts import extract, segment_policy_hash
from .gates import qa, markdown_report, aggregate_reports
from .io import load, dump, digest, file_digest
from .packaging import package, build_memory

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "localization/pl-PL"
DATA = BASE / "engine"


def approved(segment, target, evidence):
    target.update(review_status="approved", semantic_review={"status": "pass", "reviewer": "Existing bounded calibration QA: " + evidence,
                  "source_sha256": segment["source_sha256"], "target_sha256": digest(target["target_text"]), "policy_sha256": segment_policy_hash(segment)})


def lines(block):
    return [line.strip().replace("**", "") for line in block.splitlines() if line.strip() and not line.startswith("#")]


def atom(kind, value, source, target):
    return {"kind": kind, "value": value, "source_anchor": source, "target_anchor": target}


def make(product, adapter, source_file, pairs, ids=None, policies=None):
    policies = policies or {}
    document, specs = {}, []
    for i, (source, target) in enumerate(pairs):
        sid = ids[i] if ids else f"{product}.calibration.{i+1:03d}"
        document[sid] = source
        spec = {"id": sid, "source_path": "/" + sid, "content_type": "narrative", "surface_type": "body_block", "logic_sensitive": False, "character_sensitive": False, "semantic_risk": True}
        spec.update(policies.get(i, {}))
        specs.append(spec)
    manifest, targets = extract(document, {"version": 1, "product": product, "adapter": adapter, "scope": "authorized_calibration", "segments": specs}, source_file, "sha256:" + file_digest(ROOT / source_file))
    for s, t, pair in zip(manifest["segments"], targets["segments"], pairs):
        t["target_text"] = pair[1]
        approved(s, t, source_file)
    return manifest, targets


def detective():
    path = "localization/pl-PL/golden-tests/detective-academy-calibration-round1.md"
    raw = (ROOT / path).read_text(encoding="utf-8")
    source = lines(raw.split("## SOURCE\n", 1)[1].split("## FINAL PL CANDIDATE", 1)[0])
    target = lines(raw.split("## FINAL PL CANDIDATE\n", 1)[1].split("## QA", 1)[0])
    if len(source) != len(target) or len(source) != 19:
        raise ValueError("Detective calibration structure changed; review the source/target mapping")
    policies = {
        14: {"number_mappings": [{"source": "2", "target": "drugim", "rationale": "Accepted ordinal row localization"}], "logic_atoms": [atom("row", 2, "row 2", "drugim rzędzie"), atom("column", "B", "column B", "kolumnie B")]},
        15: {"logic_atoms": [atom("coordinate", "corner", "corner", "rogu mapy"), atom("adjacent_to", "refrigerator", "beside a refrigerator", "obok lodówki")]},
        16: {"logic_atoms": [atom("negation", "Workshop", "not in the Workshop", "nie było w Warsztacie")]},
        17: {"logic_atoms": [atom("south_of", "Nova", "south of NOVA", "na południe"), atom("east_of", "Nova", "east of her", "na wschód")]},
        18: {"logic_atoms": [atom("exactly", 1, "Exactly one other person", "dokładnie jedna osoba"), atom("room", "Sage", "SAGE's room", "pomieszczeniu Sage")]},
    }
    for i in range(14,19):
        policies[i].update(logic_sensitive=True, character_sensitive=True, content_type="detective_clue", surface_type="clue_card")
    for i in range(3,14):
        policies.setdefault(i, {}).update(content_type="short_label", surface_type="short_label")
    return make("detective-academy", "puzzle", path, list(zip(source, target)), policies=policies)


def web():
    path = "localization/pl-PL/golden-tests/project-unstoppable-batch-001.md"
    raw = (ROOT / path).read_text(encoding="utf-8")
    pairs, ids = [], []
    for match in re.finditer(r"### (PU-HERO-\d+)\n(.*?)(?=\n### PU-HERO-|\n## Provisional|\Z)", raw, re.S):
        section = match[2]
        en = re.search(r"\*\*SOURCE(?: ALT)?\*\*\s*\n(.*?)(?=\n\*\*)", section, re.S)
        pl = re.search(r"\*\*FINAL PL(?: ALT)?\*\*\s*\n(.*?)(?=\n\*\*)", section, re.S)
        if not en or not pl:
            raise ValueError("Web calibration pairing changed")
        ids.append(match[1])
        pairs.append((en[1].strip(), pl[1].strip()))
    if len(pairs) != 4:
        raise ValueError("Expected four authorized web calibration pairs")
    return make("project-unstoppable", "web", path, pairs, ids=ids, policies={0: {"surface_type": "heading", "content_type": "marketing"}, 1: {"surface_type": "badge", "content_type": "ui"}, 3: {"surface_type": "short_label", "content_type": "ui"}})


def gentle():
    spec = load(DATA / "gentle-steps-fit.json")
    path = "localization/pl-PL/GENTLE_STEPS_WEEK1_REAL_TEMPLATE_FIT_GATE.md"
    raw = (ROOT/path).read_text(encoding="utf-8")
    for p in spec["pages"]:
        if p["target_heading"] not in raw:
            raise ValueError("Gentle Steps fit spec drifted from accepted gate headings")
    policies = {i: {"surface_type": "heading", "content_type": "family_activity", "fit_budget": {"max_lines": 2, "approved_line_breaks": p["approved_line_breaks"], "requires_real_surface": True}} for i,p in enumerate(spec["pages"])}
    week = make("gentle-steps-christmas", "book", path, [(p["source_heading"],p["target_heading"]) for p in spec["pages"]], ids=[f"GS.PAGE{p['source_pdf_page']}.HEADING" for p in spec["pages"]], policies=policies)
    terms = load(DATA / "terminology.json")
    labels = [t for t in terms["terms"] if "gentle" in t.get("regression_groups", [])]
    calibration = make("gentle-steps-christmas", "book", "localization/pl-PL/golden-tests/gentle-steps-christmas-calibration-round1.md", [(t["source"],t["targets"][0]) for t in labels], policies={i:{"surface_type":"short_label","content_type":"short_label"} for i in range(len(labels))})
    return calibration, week


def app():
    """Exercise app packaging using the already-approved web/app-store badge."""
    manifest, targets = web()
    s, t = manifest["segments"][1], targets["segments"][1]
    return make("project-unstoppable", "app", manifest["source_file"], [(s["source_text"], t["target_text"])], ids=[s["id"]], policies={0:{"surface_type":"badge","content_type":"ui"}})


def run(output):
    output = Path(output)
    terms = load(DATA / "terminology.json")
    phrases = re.findall(r'^\s*-\s*"([^"]+)"\s*$', (BASE / "FORBIDDEN_AIISMS_PL.yml").read_text(encoding="utf-8"), re.M)
    legacy_spec = importlib.util.spec_from_file_location("legacy_polish", ROOT / "scripts/validate-polish-localization.py")
    legacy = importlib.util.module_from_spec(legacy_spec)
    legacy_spec.loader.exec_module(legacy)
    legacy_result = legacy.main()
    cases = {"detective-calibration": detective(), "project-unstoppable-web": web()}
    cases["project-unstoppable-app"] = app()
    cases["gentle-calibration"], cases["gentle-week1-headings"] = gentle()
    reports = []
    memory_entries = []
    for name, (manifest, targets) in cases.items():
        directory = output / name
        report = qa(manifest, targets, terms, phrases)
        report["fixture"] = name
        dump(directory / "source-manifest.json", manifest)
        dump(directory / "targets.pl-PL.json", targets)
        dump(directory / "qa.json", report)
        (directory / "qa.md").write_text(markdown_report(report), encoding="utf-8", newline="\n")
        if report["counts"]["errors"] == 0:
            dump(directory / "candidate-package.json", package(manifest, targets, terms, phrases))
            memory_entries.extend(build_memory(manifest, targets, terms, phrases)["entries"])
        reports.append(report)
    # Same authorized badge exercises both adapters. Store its one identical
    # language record once; contradictory approvals must never be silently merged.
    unique_memory = {}
    for entry in memory_entries:
        key = (entry["product"], entry["source"]["id"])
        previous = unique_memory.get(key)
        if previous and previous["target_sha256"] != entry["target_sha256"]:
            raise ValueError("Conflicting fixture memory targets")
        unique_memory.setdefault(key, entry)
    dump(output / "approved-memory.json", {"version":1, "target_language":"pl-PL", "entries":list(unique_memory.values())})
    summary = {**aggregate_reports(reports), "deterministic_status": "PASS" if not legacy_result and not any(r["counts"]["errors"] for r in reports) else "BLOCK",
               "legacy_fixture_count": len(legacy.ACCEPTED), "legacy_scanned_characters": len("\n".join(legacy.extract_final_sections(p.read_text(encoding="utf-8")) for p in legacy.ACCEPTED)),
               "bilingual_segments": sum(r["counts"]["source_segments"] for r in reports),
               "distinct_bilingual_pairs": len({(m['product'],s['source_text'],t['target_text']) for m,ts in cases.values() for s,t in zip(m['segments'],ts['segments'])}),
               "reports": reports, "evidence_boundary": "All seven historical fixtures run through regression. Only verbatim source/target pairs already present in the repository receive paired invariant QA; other historic book prose has no fabricated EN source or invented coverage. The Week 1 real-template and web/browser fit gates remain OPEN."}
    dump(output / "summary.json", summary)
    (output / "summary.md").write_text(markdown_report(summary), encoding="utf-8", newline="\n")
    print(f"Production engine fixture proof: {summary['deterministic_status']}; {summary['bilingual_segments']} bilingual segments; designed-surface review remains open")
    return 0 if summary["deterministic_status"] == "PASS" else 1
