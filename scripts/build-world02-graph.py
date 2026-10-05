#!/usr/bin/env python3
"""Build a bounded World 02 display graph from locked page evidence."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("level", type=int, choices=tuple(range(11, 18)))
    args = parser.parse_args()
    level = args.level
    evidence_rel = f"orchestration/content-sources/world02-level{level}-page-evidence.json"
    out = ROOT / f"orchestration/content-packs/world02/level{level}.en.candidate.json"
    evidence = json.loads((ROOT / evidence_rel).read_text(encoding="utf-8"))
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
        "content_pack_id": f"world02_mission_{level:03d}_source_graph",
        "content_version": "0.1.0",
        "canonical_locale": "en",
        "supported_locales": ["en"],
        "planned_locales": ["pl-PL"],
        "minimum_runtime_contract": "1.0.0",
        "mission_id": evidence["mission_id"],
        "candidate_scope": f"published_mission_{level:03d}_pages_{source['page_range'][0]}_{source['page_range'][1]}",
        "source": {
            "source_id": source["source_id"],
            "source_sha256": source["sha256"],
            "source_bytes": source["bytes"],
            "source_pages": source["pages"],
            "page_range": source["page_range"],
            "evidence_manifest": evidence_rel,
        },
        "nodes": nodes,
        "localized_copy": copy,
    }

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(nodes)} nodes: {out.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
