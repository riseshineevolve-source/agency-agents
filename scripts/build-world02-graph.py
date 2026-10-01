#!/usr/bin/env python3
"""Build the bounded World 02 Level 11 display graph from locked page evidence."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_REL = "orchestration/content-sources/world02-level11-page-evidence.json"
OUT = ROOT / "orchestration/content-packs/world02/level11.en.candidate.json"

def main() -> None:
    evidence = json.loads((ROOT / EVIDENCE_REL).read_text(encoding="utf-8"))
    records = evidence["records"]
    source = evidence["source"]
    nodes = []
    copy = []
    for index, record in enumerate(records):
        nodes.append({
            "node_id": record["node_id"],
            "sequence": index + 1,
            "node_type": record["type"],
            "subtype": record["subtype"],
            "speaker_id": record["speaker_id"],
            "next_id": records[index + 1]["node_id"] if index + 1 < len(records) else None,
            "provenance": {
                "source_id": source["source_id"],
                "source_sha256": source["sha256"],
                "page": record["page"],
                "evidence_id": record["evidence_id"],
            },
        })
        copy.append({"locale": "en", "node_id": record["node_id"], "fields": record["copy"]})

    pack = {
        "schema_version": "1.0.0",
        "product_id": "level_up_your_brain_world_02",
        "content_pack_id": "world02_mission_011_source_graph",
        "content_version": "0.1.0",
        "canonical_locale": "en",
        "supported_locales": ["en"],
        "planned_locales": ["pl-PL"],
        "minimum_runtime_contract": "1.0.0",
        "mission_id": evidence["mission_id"],
        "candidate_scope": "published_mission_011_pages_13_21",
        "source": {
            "source_id": source["source_id"],
            "source_sha256": source["sha256"],
            "source_bytes": source["bytes"],
            "source_pages": source["pages"],
            "page_range": source["page_range"],
            "evidence_manifest": EVIDENCE_REL,
        },
        "nodes": nodes,
        "localized_copy": copy,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(nodes)} nodes: {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
