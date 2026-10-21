#!/usr/bin/env python3
"""Fail-closed validation for this published World 02 endgame source slice only."""

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_REL = "orchestration/content-packs/world02/endgame.en.candidate.json"
EVIDENCE_REL = "orchestration/content-sources/world02-endgame-page-evidence.json"
CANONICAL_SHA256 = "e94d2937cc459a5c7c3c5968c64ba39f2a03702f929488e42b00b5db3f9f7f76"
# Canonical JSON hash locks visual evidence, including copy and source-only features.
EVIDENCE_SHA256 = "ca24aeb4e87893e06d7d8ffe26239dd277a21447bf4708baca7a7a2f4e852d1c"
PAGE_COUNTS = {93: 5, 94: 9, 95: 10, 96: 4, 97: 14, 98: 3,
               99: 14, 100: 7, 101: 7, 102: 8, 103: 13, 104: 1}
TYPE_COUNTS = Counter({
    "page_header": 11, "achievement_banner": 1, "system_log": 4, "rank": 2,
    "closing": 2, "handover_banner": 1, "intro": 2, "skill": 4, "motto": 3,
    "callout": 1, "mission_data": 1, "section_heading": 2, "squad_motto": 5,
    "emergency_code": 2, "table_header": 2, "loadout_row": 24,
    "print_instructions": 1, "blank_form": 2, "glitch": 2, "hack": 2,
    "instruction_step": 6, "explanation": 2, "artwork": 1, "tools_intro": 1,
    "tool_description": 2, "qr_link": 1, "certificate_status": 1,
    "achievement": 5, "oath": 1, "approval": 1,
})
PACK_KEYS = {"schema_version", "product_id", "content_pack_id", "content_version",
             "canonical_locale", "supported_locales", "planned_locales",
             "minimum_runtime_contract", "scope_id", "candidate_scope", "release_status",
             "source", "page_inventory", "nodes", "localized_copy"}
NODE_KEYS = {"node_id", "sequence", "node_type", "subtype", "speaker_id", "next_id",
             "source_features", "provenance"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def evidence_digest(evidence):
    encoded = json.dumps(evidence, ensure_ascii=False, sort_keys=True,
                         separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def verify_evidence(evidence):
    require(evidence_digest(evidence) == EVIDENCE_SHA256, "locked visual evidence hash drift")
    require(evidence["scope_id"] == "world02_endgame", "endgame scope drift")
    require(evidence["source"]["sha256"] == CANONICAL_SHA256, "canonical source hash drift")
    require([p["page"] for p in evidence["page_inventory"]] == list(PAGE_COUNTS),
            "all twelve printed endgame pages are required")
    require({p["page"]: p["content_blocks"] for p in evidence["page_inventory"]} == PAGE_COUNTS,
            "visual block inventory drift")
    records = evidence["records"]
    require(len(records) == sum(PAGE_COUNTS.values()) == 95, "endgame block count drift")
    require(Counter(r["page"] for r in records) == Counter(PAGE_COUNTS), "page coverage drift")
    require(Counter(r["type"] for r in records) == TYPE_COUNTS, "source block types drift")
    expected_ids = [f"world02_endgame_p{p:03d}_block_{i:02d}"
                    for p, count in PAGE_COUNTS.items() for i in range(1, count + 1)]
    require([r["node_id"] for r in records] == expected_ids, "stable page/block IDs drift")


def validate(pack, evidence):
    verify_evidence(evidence)
    require(set(pack) == PACK_KEYS, "endgame pack keys drift")
    fixed = {
        "schema_version": "1.0.0", "product_id": "level_up_your_brain_world_02",
        "content_pack_id": "world02_endgame_source_graph", "content_version": "0.1.0",
        "canonical_locale": "en", "supported_locales": ["en"],
        "planned_locales": ["pl-PL"],
        "minimum_runtime_contract": "world02-endgame-source-only-1.0.0",
        "scope_id": "world02_endgame", "candidate_scope": "published_endgame_pages_93_104",
        "release_status": "source_candidate_only",
    }
    for key, value in fixed.items():
        require(pack[key] == value, f"{key} drift")
    source = evidence["source"]
    expected_source = {
        "source_id": source["source_id"], "source_sha256": CANONICAL_SHA256,
        "source_bytes": 66576954, "source_pages": 104, "page_range": [93, 104],
        "evidence_manifest": EVIDENCE_REL, "evidence_sha256": EVIDENCE_SHA256,
    }
    require(pack["source"] == expected_source, "canonical source custody drift")
    require(pack["page_inventory"] == evidence["page_inventory"], "printed page roles drift")
    records = evidence["records"]
    require(len(pack["nodes"]) == len(pack["localized_copy"]) == len(records),
            "node/copy/evidence count differs")
    for index, (node, copy, record) in enumerate(zip(pack["nodes"], pack["localized_copy"], records)):
        label = record["evidence_id"]
        require(set(node) == NODE_KEYS, f"node keys drift at {label}")
        require(node["node_id"] == copy["node_id"] == record["node_id"], f"identity drift at {label}")
        require(node["sequence"] == index + 1, f"printed sequence drift at {label}")
        require(node["node_type"] == record["type"], f"type drift at {label}")
        require(node["subtype"] == record["subtype"], f"surface drift at {label}")
        require(node["speaker_id"] == record["speaker_id"], f"speaker drift at {label}")
        require(node["next_id"] == (records[index + 1]["node_id"] if index + 1 < len(records) else None),
                f"printed transition drift at {label}")
        require(node["source_features"] == record["source_features"], f"source features drift at {label}")
        require(node["provenance"] == {
            "source_id": source["source_id"], "source_sha256": CANONICAL_SHA256,
            "page": record["page"], "page_sequence": record["page_sequence"], "evidence_id": label,
        }, f"page/block provenance drift at {label}")
        require(set(copy) == {"locale", "node_id", "fields"}, f"copy keys drift at {label}")
        require(copy["locale"] == "en", f"locale drift at {label}")
        require(copy["fields"] == record["copy"], f"copy differs from locked visual source at {label}")
        require(all(isinstance(v, str) and v.strip() for v in copy["fields"].values()),
                f"empty or nontext copy at {label}")
        if record["type"] == "artwork":
            require(copy["fields"] == {}, "artwork descriptions must not become product copy")
        if record["type"] == "blank_form":
            require(all(f["value"] == "" for f in node["source_features"]["writable_fields"]),
                    "printed blank fields must remain blank")
    return Counter(n["node_type"] for n in pack["nodes"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack", nargs="?", type=Path, default=ROOT / PACK_REL)
    args = parser.parse_args()
    try:
        pack = json.loads(args.pack.read_text(encoding="utf-8"))
        evidence = json.loads((ROOT / EVIDENCE_REL).read_text(encoding="utf-8"))
        validate(pack, evidence)
    except (ValueError, KeyError, TypeError, OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print("VALID: 95 source-only World 02 endgame nodes, all 12 pages 93-104; no runtime exposure")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
