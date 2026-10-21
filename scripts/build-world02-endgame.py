#!/usr/bin/env python3
"""Build the bounded World 02 endgame source graph; does not enable a runtime."""

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_REL = "orchestration/content-sources/world02-endgame-page-evidence.json"
PACK_REL = "orchestration/content-packs/world02/endgame.en.candidate.json"


def validator_module():
    spec = importlib.util.spec_from_file_location(
        "world02_endgame_validator", ROOT / "scripts/validate-world02-endgame.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(evidence):
    validator = validator_module()
    validator.verify_evidence(evidence)
    records = evidence["records"]
    source = evidence["source"]
    nodes, copy = [], []
    for index, record in enumerate(records):
        nodes.append({
            "node_id": record["node_id"],
            "sequence": index + 1,
            "node_type": record["type"],
            "subtype": record["subtype"],
            "speaker_id": record["speaker_id"],
            "next_id": records[index + 1]["node_id"] if index + 1 < len(records) else None,
            "source_features": record["source_features"],
            "provenance": {
                "source_id": source["source_id"],
                "source_sha256": source["sha256"],
                "page": record["page"],
                "page_sequence": record["page_sequence"],
                "evidence_id": record["evidence_id"],
            },
        })
        copy.append({"locale": "en", "node_id": record["node_id"], "fields": record["copy"]})
    pack = {
        "schema_version": "1.0.0",
        "product_id": "level_up_your_brain_world_02",
        "content_pack_id": "world02_endgame_source_graph",
        "content_version": "0.1.0",
        "canonical_locale": "en",
        "supported_locales": ["en"],
        "planned_locales": ["pl-PL"],
        "minimum_runtime_contract": "world02-endgame-source-only-1.0.0",
        "scope_id": "world02_endgame",
        "candidate_scope": "published_endgame_pages_93_104",
        "release_status": "source_candidate_only",
        "source": {
            "source_id": source["source_id"],
            "source_sha256": source["sha256"],
            "source_bytes": source["bytes"],
            "source_pages": source["pages"],
            "page_range": source["page_range"],
            "evidence_manifest": EVIDENCE_REL,
            "evidence_sha256": validator.evidence_digest(evidence),
        },
        "page_inventory": evidence["page_inventory"],
        "nodes": nodes,
        "localized_copy": copy,
    }
    validator.validate(pack, evidence)
    return pack


def main():
    evidence = json.loads((ROOT / EVIDENCE_REL).read_text(encoding="utf-8"))
    pack = build(evidence)
    out = ROOT / PACK_REL
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(pack['nodes'])} source-only endgame nodes, pages 93-104: {PACK_REL}")


if __name__ == "__main__":
    main()
