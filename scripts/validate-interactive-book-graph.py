#!/usr/bin/env python3
"""Validate a published-source interactive book graph and its custody boundary."""

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACK = ROOT / "orchestration/content-packs/world01/level1.en.candidate.json"
NODE_TYPES = {"opener", "system_log", "dialogue", "inventory", "system_note", "exercise", "console", "quest", "science", "secret_code"}
SPEAKERS = {"system", "dilo", "alio", "nini", "luli", "mimi"}
PACK_KEYS = {"schema_version", "product_id", "content_pack_id", "content_version", "canonical_locale", "supported_locales", "planned_locales", "minimum_runtime_contract", "mission_id", "candidate_scope", "source", "nodes", "localized_copy"}
NODE_KEYS = {"node_id", "sequence", "node_type", "subtype", "speaker_id", "next_id", "provenance"}
PROVENANCE_KEYS = {"source_id", "source_sha256", "page", "evidence_id"}
SOURCE_KEYS = {"source_id", "source_sha256", "source_bytes", "source_pages", "page_range", "evidence_manifest"}
COPY_KEYS = {"locale", "node_id", "fields"}
CANONICAL_SHA256 = "adf9d384985ec7ad0fb1d7f9f6c3d46189592a171474c38ee93ac35bb808c549"
MISSION_SPECS = {
    "world01_mission_001": {"level": 1, "pages": [15, 22], "blocks": 26},
    "world01_mission_002": {"level": 2, "pages": [23, 32], "blocks": 32},
    "world01_mission_003": {"level": 3, "pages": [33, 41], "blocks": 30},
    "world01_mission_004": {"level": 4, "pages": [42, 50], "blocks": 35},
    "world01_mission_005": {"level": 5, "pages": [51, 59], "blocks": 29},
    "world01_mission_006": {"level": 6, "pages": [60, 67], "blocks": 26},
    "world01_mission_007": {"level": 7, "pages": [68, 75], "blocks": 27},
    "world01_mission_008": {"level": 8, "pages": [76, 83], "blocks": 25},
    "world01_mission_009": {"level": 9, "pages": [84, 91], "blocks": 25},
    "world01_mission_010": {"level": 10, "pages": [92, 99], "blocks": 27},
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def keys_exact(obj, expected, label):
    require(isinstance(obj, dict), f"{label} must be an object")
    require(set(obj) == expected, f"{label} keys differ: missing={sorted(expected - set(obj))}, extra={sorted(set(obj) - expected)}")


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate(pack, evidence):
    keys_exact(pack, PACK_KEYS, "pack")
    mission_id = evidence["mission_id"]
    require(mission_id in MISSION_SPECS, "mission has no bounded published-source specification")
    spec = MISSION_SPECS[mission_id]
    level = spec["level"]
    first, last = spec["pages"]
    require(pack["schema_version"] == "1.0.0", "wrong graph contract version")
    require(pack["minimum_runtime_contract"] == "1.0.0", "wrong runtime contract")
    require(pack["canonical_locale"] == "en", "canonical locale must be English")
    require(pack["supported_locales"] == ["en"], "only source-proven English is supported")
    require(pack["planned_locales"] == ["pl-PL"], "planned locale must remain unavailable")
    require(pack["candidate_scope"] == f"published_mission_{level:03d}_pages_{first}_{last}", "scope drift")
    require(pack["mission_id"] == mission_id, "mission drift")
    require(pack["product_id"] == "level_up_your_brain_world_01", "product drift")
    require(pack["content_pack_id"] == f"world01_mission_{level:03d}_source_graph", "pack id drift")
    require(re.fullmatch(r"\d+\.\d+\.\d+", pack["content_version"]) is not None, "invalid content version")

    source = pack["source"]
    source_truth = evidence["source"]
    keys_exact(source, SOURCE_KEYS, "source")
    for pack_key, evidence_key in (("source_id", "source_id"), ("source_sha256", "sha256"), ("source_bytes", "bytes"), ("source_pages", "pages"), ("page_range", "page_range")):
        require(source[pack_key] == source_truth[evidence_key], f"source {pack_key} differs from evidence")
    require(source["page_range"] == spec["pages"], "mission page range drift")
    require(source["source_sha256"] == CANONICAL_SHA256, "canonical published PDF hash drift")
    require(source["source_bytes"] == 14523549, "canonical published PDF size drift")
    require(source["source_pages"] == 108, "published source page count drift")
    require(re.fullmatch(r"[0-9a-f]{64}", source["source_sha256"]) is not None, "invalid source hash")
    require(source["evidence_manifest"] == f"orchestration/content-sources/world01-level{level}-page-evidence.json", "evidence manifest path drift")

    inventory = evidence["page_inventory"]
    require([entry["page"] for entry in inventory] == list(range(first, last + 1)), "evidence inventory must cover every mission page")
    records = evidence["records"]
    require(sum(entry["content_blocks"] for entry in inventory) == len(records), "evidence inventory count differs")
    require([Counter(record["page"] for record in records)[entry["page"]] for entry in inventory] == [entry["content_blocks"] for entry in inventory], "evidence page counts differ")
    require(len(records) == spec["blocks"], "published evidence block count drift")
    require(len(pack["nodes"]) == len(records), "node count differs from evidence")
    require(len(pack["localized_copy"]) == len(records), "copy count differs from evidence")
    require(len({record["evidence_id"] for record in records}) == len(records), "duplicate evidence id")

    expected_ids = [f"world01_mission_{level:03d}_node_{i:03d}" for i in range(1, len(records) + 1)]
    require([record["node_id"] for record in records] == expected_ids, "evidence node IDs out of order")
    require([node["node_id"] for node in pack["nodes"]] == expected_ids, "graph node IDs out of order")

    for index, (node, record, copy) in enumerate(zip(pack["nodes"], records, pack["localized_copy"])):
        label = record["evidence_id"]
        keys_exact(node, NODE_KEYS, f"node {label}")
        keys_exact(node["provenance"], PROVENANCE_KEYS, f"provenance {label}")
        keys_exact(copy, COPY_KEYS, f"copy {label}")
        require(node["sequence"] == index + 1, f"sequence drift at {label}")
        require(record["type"] in NODE_TYPES and node["node_type"] == record["type"], f"node type drift at {label}")
        require(node["subtype"] == record["subtype"], f"subtype drift at {label}")
        require(node["speaker_id"] == record["speaker_id"], f"speaker drift at {label}")
        if record["type"] == "dialogue":
            require(node["speaker_id"] in SPEAKERS - {"system"}, f"invalid dialogue speaker at {label}")
        elif record["type"] == "system_log":
            require(node["speaker_id"] == "system", f"invalid system log speaker at {label}")
        else:
            require(node["speaker_id"] is None, f"unexpected speaker at {label}")
        require(node["next_id"] == (expected_ids[index + 1] if index + 1 < len(records) else None), f"transition drift at {label}")
        require(node["provenance"] == {"source_id": source["source_id"], "source_sha256": source["source_sha256"], "page": record["page"], "evidence_id": label}, f"provenance drift at {label}")
        require(copy["locale"] == "en" and copy["node_id"] == record["node_id"], f"copy identity drift at {label}")
        require(copy["fields"] == record["copy"], f"copy differs from published evidence at {label}")
        require(isinstance(copy["fields"], dict) and copy["fields"], f"empty copy at {label}")
        require(all(isinstance(value, str) and value.strip() for value in copy["fields"].values()), f"empty text at {label}")
    return Counter(node["node_type"] for node in pack["nodes"])


def normalized(text):
    # The published PDF has a few words split inside glyph runs (e.g. "e xact").
    # Ignore only extraction whitespace; retain letters and punctuation.
    return re.sub(r"\s+", "", text).casefold()


def verify_pdf(pdf_path, evidence):
    from pypdf import PdfReader

    data = Path(pdf_path).read_bytes()
    require(hashlib.sha256(data).hexdigest() == evidence["source"]["sha256"], "PDF SHA-256 differs from custody record")
    require(len(data) == evidence["source"]["bytes"], "PDF byte size differs from custody record")
    reader = PdfReader(pdf_path)
    require(len(reader.pages) == evidence["source"]["pages"], "PDF page count differs from custody record")
    # PDF text extraction is a second check of the visual transcription. Layout
    # extraction can reorder separate visual blocks, so verify each field alone.
    for record in evidence["records"]:
        extracted = normalized(reader.pages[record["page"] - 1].extract_text())
        visual_only_fields = set(record.get("visual_only_fields", []))
        for name, value in record["copy"].items():
            if name in visual_only_fields:
                continue
            fragments = record.get("extraction_fragments", {}).get(name)
            if fragments:
                require(normalized("".join(fragments)) == normalized(value), f"PDF extraction fragments do not reconstruct {record['evidence_id']}.{name}")
                require(all(normalized(fragment) in extracted for fragment in fragments), f"PDF page {record['page']} lacks fragment of {record['evidence_id']}.{name}")
                continue
            for segment in value.split("\n\n"):
                require(normalized(segment) in extracted, f"PDF page {record['page']} lacks {record['evidence_id']}.{name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack", nargs="?", type=Path, default=DEFAULT_PACK)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--pdf", type=Path, help="private canonical PDF; enables binary and page text verification")
    args = parser.parse_args()
    try:
        pack = load_json(args.pack)
        evidence_path = args.evidence or ROOT / pack["source"]["evidence_manifest"]
        evidence = load_json(evidence_path)
        counts = validate(pack, evidence)
        if args.pdf:
            verify_pdf(args.pdf, evidence)
    except (ValueError, KeyError, OSError, ImportError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    first, last = pack["source"]["page_range"]
    print(f"VALID: {len(pack['nodes'])} source-proven nodes, pages {first}-{last}, types {dict(sorted(counts.items()))}" + ("; PDF verified" if args.pdf else "; locked evidence verified"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
