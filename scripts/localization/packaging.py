"""Reconstruct source-shaped payloads and reuse only reviewed, unchanged units."""
from __future__ import annotations

import copy
from .contracts import require, review_valid, segment_policy_hash
from .gates import qa
from .io import digest, put


def package(manifest, targets, terms, phrases=(), release=False):
    report = qa(manifest, targets, terms, phrases)
    require(report["counts"]["errors"] == 0, "Export blocked by deterministic QA failures")
    if release:
        require(report["status"] == "PASS" and report["counts"]["approved_language"] == len(manifest["segments"]), "Release export requires all language and surface gates; use candidate output for review")
    document = copy.deepcopy(manifest["source_document"])
    target_map = {t["id"]: t for t in targets["segments"]}
    pairs = []
    for s in sorted(manifest["segments"], key=lambda x: x["id"]):
        t = target_map[s["id"]]
        document = put(document, s["source_path"], t["target_text"])
        pairs.append({"source": s, "target": t})
    return {"format": "rse-localized-package-v1", "product": manifest["product"], "adapter": manifest["adapter"], "target_language": "pl-PL", "source_key_types": manifest.get("source_key_types", {}),
            "mode": "release" if release else "candidate", "localized_payload": document, "bilingual_segments": pairs, "qa": report}


def build_memory(manifest, targets, terms, phrases=()):
    report = qa(manifest, targets, terms, phrases)
    require(report["counts"]["errors"] == 0, "Cannot add failing segments to approved translation memory")
    smap = {s["id"]: s for s in manifest["segments"]}
    entries = []
    for target in sorted(targets["segments"], key=lambda t: t["id"]):
        source = smap[target["id"]]
        if target["review_status"] not in {"approved", "locked"} or not review_valid(source, target):
            continue
        entries.append({"product": manifest["product"], "source": copy.deepcopy(source), "target": copy.deepcopy(target),
                        "source_contract_sha256": manifest["contract_sha256"], "policy_sha256": segment_policy_hash(source),
                        "terminology_sha256": digest(terms), "target_sha256": digest(target["target_text"])})
    return {"version": 1, "target_language": "pl-PL", "entries": entries}


def reuse_memory(manifest, targets, memory, terms):
    require(memory.get("version") == 1 and memory.get("target_language") == "pl-PL", "Unsupported memory")
    index = {}
    for entry in memory["entries"]:
        source, target = entry["source"], entry["target"]
        key = (entry["product"], source["id"])
        require(key not in index, f"Conflicting memory entries: {key}")
        require(source["source_sha256"] == digest(source["source_text"]), "Memory source hash mismatch")
        require(entry["target_sha256"] == digest(target["target_text"]) and target["source_sha256"] == source["source_sha256"], "Memory target hash mismatch")
        require(target["review_status"] in {"approved", "locked"} and review_valid(source, target), "Memory contains unapproved or stale review")
        require(entry["policy_sha256"] == segment_policy_hash(source), "Memory policy hash mismatch")
        index[key] = entry
    result = copy.deepcopy(targets)
    smap = {s["id"]: s for s in manifest["segments"]}
    events = []
    for i, target in enumerate(result["segments"]):
        source = smap[target["id"]]
        entry = index.get((manifest["product"], source["id"]))
        if not entry:
            continue
        valid = (entry["source"]["source_sha256"] == source["source_sha256"]
                 and entry["policy_sha256"] == segment_policy_hash(source)
                 and entry["terminology_sha256"] == digest(terms))
        if not valid:
            # Existing target is retained as visible evidence, never promoted or silently overwritten.
            if target["target_text"]:
                target["review_status"] = "stale"
                target.pop("semantic_review", None)
            events.append({"id": source["id"], "status": "stale_memory", "reason": "Source, policy or terminology changed; translation must be reviewed"})
        elif not target["target_text"]:
            reused = copy.deepcopy(entry["target"])
            reused["reuse_provenance"] = {"source_file": entry["source"]["source_file"], "source_revision": entry["source"]["source_revision"], "source_contract_sha256": entry["source_contract_sha256"], "target_sha256": entry["target_sha256"]}
            result["segments"][i] = reused
            events.append({"id": source["id"], "status": "reused"})
        else:
            events.append({"id": source["id"], "status": "kept_existing_target"})
    return result, events
