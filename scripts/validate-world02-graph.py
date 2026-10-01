#!/usr/bin/env python3
"""Validate source-proven World 02 mission graphs and custody boundaries."""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACK = ROOT / "orchestration/content-packs/world02/level11.en.candidate.json"
CANONICAL_SHA256 = "e94d2937cc459a5c7c3c5968c64ba39f2a03702f929488e42b00b5db3f9f7f76"
NODE_TYPES = {"opener", "system_log", "dialogue", "console", "quest", "science", "secret_code"}
SPEAKERS = {"system", "dilo", "alio", "nini", "luli", "mimi"}
PACK_KEYS = {"schema_version","product_id","content_pack_id","content_version","canonical_locale","supported_locales","planned_locales","minimum_runtime_contract","mission_id","candidate_scope","source","nodes","localized_copy"}
NODE_KEYS = {"node_id","sequence","node_type","subtype","speaker_id","next_id","provenance"}
PROVENANCE_KEYS = {"source_id","source_sha256","page","evidence_id"}
SOURCE_KEYS = {"source_id","source_sha256","source_bytes","source_pages","page_range","evidence_manifest"}
COPY_KEYS = {"locale","node_id","fields"}

MISSION_SPECS = {
    "world02_mission_011": {
        "level": 11,
        "pages": [13,21],
        "blocks": 27,
        "types": Counter({"dialogue":14,"system_log":5,"console":3,"quest":2,"opener":1,"science":1,"secret_code":1}),
    },
    "world02_mission_012": {
        "level": 12,
        "pages": [22,29],
        "blocks": 27,
        "types": Counter({"dialogue":13,"system_log":6,"console":3,"quest":2,"opener":1,"science":1,"secret_code":1}),
    },
    "world02_mission_013": {
        "level": 13,
        "pages": [30,37],
        "blocks": 31,
        "types": Counter({"dialogue":16,"system_log":7,"console":3,"quest":2,"opener":1,"science":1,"secret_code":1}),
    },
    "world02_mission_014": {
        "level": 14,
        "pages": [38,46],
        "blocks": 29,
        "types": Counter({"dialogue":16,"system_log":5,"console":3,"quest":2,"opener":1,"science":1,"secret_code":1}),
    },
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def keys_exact(obj, expected, label):
    require(isinstance(obj, dict), f"{label} must be an object")
    require(set(obj) == expected, f"{label} keys differ: missing={sorted(expected-set(obj))}, extra={sorted(set(obj)-expected)}")

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def validate(pack, evidence):
    keys_exact(pack, PACK_KEYS, "pack")
    mission_id = evidence["mission_id"]
    require(mission_id in MISSION_SPECS, "mission has no bounded World 02 specification")
    spec = MISSION_SPECS[mission_id]
    level = spec["level"]
    first, last = spec["pages"]

    require(pack["schema_version"] == "1.0.0", "wrong graph contract")
    require(pack["minimum_runtime_contract"] == "1.0.0", "wrong runtime contract")
    require(pack["product_id"] == "level_up_your_brain_world_02", "product drift")
    require(pack["content_pack_id"] == f"world02_mission_{level:03d}_source_graph", "pack id drift")
    require(pack["mission_id"] == mission_id, "mission drift")
    require(pack["candidate_scope"] == f"published_mission_{level:03d}_pages_{first}_{last}", "scope drift")
    require(pack["canonical_locale"] == "en", "canonical locale drift")
    require(pack["supported_locales"] == ["en"], "only source-proven EN may be supported")
    require(pack["planned_locales"] == ["pl-PL"], "PL must remain planned only")
    require(re.fullmatch(r"\d+\.\d+\.\d+", pack["content_version"]) is not None, "bad content version")

    source = pack["source"]
    truth = evidence["source"]
    keys_exact(source, SOURCE_KEYS, "source")
    require(source["source_id"] == truth["source_id"], "source id drift")
    require(source["source_sha256"] == truth["sha256"] == CANONICAL_SHA256, "canonical hash drift")
    require(source["source_bytes"] == truth["bytes"] == 66576954, "canonical byte-size drift")
    require(source["source_pages"] == truth["pages"] == 104, "canonical page-count drift")
    require(source["page_range"] == truth["page_range"] == spec["pages"], "page range drift")
    require(source["evidence_manifest"] == f"orchestration/content-sources/world02-level{level}-page-evidence.json", "evidence path drift")

    inventory = evidence["page_inventory"]
    require([x["page"] for x in inventory] == list(range(first,last+1)), "inventory page coverage drift")
    records = evidence["records"]
    require(len(records) == spec["blocks"], "source block count drift")
    require(sum(x["content_blocks"] for x in inventory) == len(records), "inventory count drift")
    require([Counter(r["page"] for r in records)[x["page"]] for x in inventory] == [x["content_blocks"] for x in inventory], "per-page counts drift")
    require(len(pack["nodes"]) == len(records) == len(pack["localized_copy"]), "node/copy count drift")

    expected_ids = [f"world02_mission_{level:03d}_node_{i:03d}" for i in range(1,len(records)+1)]
    require([r["node_id"] for r in records] == expected_ids, "evidence IDs out of order")
    require([n["node_id"] for n in pack["nodes"]] == expected_ids, "graph IDs out of order")

    for index, (node, record, copy) in enumerate(zip(pack["nodes"], records, pack["localized_copy"])):
        label = record["evidence_id"]
        keys_exact(node, NODE_KEYS, f"node {label}")
        keys_exact(node["provenance"], PROVENANCE_KEYS, f"provenance {label}")
        keys_exact(copy, COPY_KEYS, f"copy {label}")
        require(node["sequence"] == index + 1, f"sequence drift at {label}")
        require(node["node_type"] == record["type"] in NODE_TYPES, f"type drift at {label}")
        require(node["subtype"] == record["subtype"], f"subtype drift at {label}")
        require(node["speaker_id"] == record["speaker_id"], f"speaker drift at {label}")
        if record["type"] == "dialogue":
            require(node["speaker_id"] in SPEAKERS - {"system"}, f"bad dialogue speaker at {label}")
        elif record["type"] == "system_log":
            require(node["speaker_id"] == "system", f"bad system speaker at {label}")
        else:
            require(node["speaker_id"] is None, f"unexpected speaker at {label}")
        require(node["next_id"] == (expected_ids[index+1] if index+1 < len(records) else None), f"transition drift at {label}")
        require(node["provenance"] == {"source_id":source["source_id"],"source_sha256":source["source_sha256"],"page":record["page"],"evidence_id":label}, f"provenance drift at {label}")
        require(copy["locale"] == "en" and copy["node_id"] == record["node_id"], f"copy identity drift at {label}")
        require(copy["fields"] == record["copy"], f"copy differs from locked evidence at {label}")
        require(all(isinstance(v,str) and v.strip() for v in copy["fields"].values()), f"empty copy field at {label}")

    counts = Counter(n["node_type"] for n in pack["nodes"])
    require(counts == spec["types"], f"unexpected type counts: {dict(counts)}")
    return counts

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack", nargs="?", type=Path, default=DEFAULT_PACK)
    args = parser.parse_args()
    try:
        pack = load_json(args.pack)
        evidence = load_json(ROOT / pack["source"]["evidence_manifest"])
        counts = validate(pack, evidence)
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    first, last = pack["source"]["page_range"]
    print(f"VALID: {len(pack['nodes'])} World 02 source-proven nodes, pages {first}-{last}, types {dict(sorted(counts.items()))}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
