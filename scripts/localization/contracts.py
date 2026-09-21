"""An exhaustive source plan freezes IDs, source text, policy and protected data."""
from __future__ import annotations

import copy
import re
from .io import ContractError, digest, get, leaves

SURFACES = {"heading", "subtitle", "button", "badge", "clue_card", "map_label", "app_control", "body_block", "callout", "cover_copy", "back_cover_copy", "short_label"}
ADAPTERS = {"book", "app", "web", "puzzle", "structured"}
STATUSES = {"untranslated", "draft", "review_required", "approved", "locked", "stale"}
ATOM_KINDS = {"identity", "row", "column", "coordinate", "room", "zone", "negation", "exactly", "at_least", "at_most", "north_of", "south_of", "east_of", "west_of", "adjacent_to", "diagonal_to", "same_room", "different_room", "order", "answer", "code", "count"}
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$")


def require(condition, message):
    if not condition:
        raise ContractError(message)


def source_contract_hash(manifest):
    return digest({k: v for k, v in manifest.items() if k != "contract_sha256"})


def extract(document, plan, source_file, revision):
    require(plan.get("version") == 1, "Unsupported plan version")
    require(plan.get("adapter") in ADAPTERS, "Unknown adapter")
    require(bool(plan.get("product")) and bool(revision), "Product and source revision are required")
    selections = plan.get("segments", [])
    protected = plan.get("protected_paths", [])
    exclusions = plan.get("excluded_paths", {})
    paths = [s["source_path"] for s in selections]
    require(len(paths + protected + list(exclusions)) == len(set(paths + protected + list(exclusions))), "Duplicate/overlapping source classification")
    leaf_map = dict(leaves(document))
    classified = set(paths + protected + list(exclusions))
    require(classified <= set(leaf_map), "Plans must name existing leaf paths, never objects")
    strings = {p for p, v in leaf_map.items() if isinstance(v, str)}
    require(strings <= classified, f"Unclassified source strings: {sorted(strings - classified)}")
    require(all(isinstance(reason, str) and reason.strip() for reason in exclusions.values()), "Exclusions need a rationale")
    segments = []
    for spec in selections:
        text = get(document, spec["source_path"])
        require(isinstance(text, str) and bool(text.strip()), "Only nonempty string values can be localized")
        segment = copy.deepcopy(spec)
        segment.update(source_text=text, source_sha256=digest(text), source_file=source_file, source_revision=revision)
        segment.setdefault("protected_tokens", [])
        segment.setdefault("logic_atoms", [])
        segment.setdefault("term_ids", [])
        segment.setdefault("number_mappings", [])
        segment.setdefault("fit_budget", None)
        segment.setdefault("semantic_risk", True)
        segments.append(segment)
    manifest = {
        "version": 1, "product": plan["product"], "adapter": plan["adapter"],
        "source_language": "en", "target_language": "pl-PL", "source_file": source_file,
        "source_revision": revision, "source_document": document, "source_document_sha256": digest(document),
        "segments": segments, "protected_paths": sorted(set(leaf_map) - set(paths)),
        "excluded_paths": exclusions, "scope": plan.get("scope", "bounded"),
    }
    manifest["contract_sha256"] = source_contract_hash(manifest)
    validate_manifest(manifest)
    targets = {"version": 1, "product": plan["product"], "contract_sha256": manifest["contract_sha256"], "segments": [
        {"id": s["id"], "source_sha256": s["source_sha256"], "target_text": "", "review_status": "untranslated", "logic_atoms": copy.deepcopy(s["logic_atoms"])} for s in segments
    ]}
    return manifest, targets


def validate_manifest(manifest):
    require(isinstance(manifest, dict) and manifest.get("version") == 1, "Unsupported source manifest")
    require(manifest.get("adapter") in ADAPTERS, "Unknown adapter")
    require(manifest.get("source_language") == "en" and manifest.get("target_language") == "pl-PL", "This contract is en -> pl-PL")
    require(manifest.get("contract_sha256") == source_contract_hash(manifest), "Source contract digest mismatch")
    require(manifest.get("source_document_sha256") == digest(manifest["source_document"]), "Source document digest mismatch")
    require(bool(manifest.get("product")) and bool(manifest.get("source_revision")) and bool(manifest.get("source_file")), "Missing source provenance")
    require(isinstance(manifest.get("segments"), list) and bool(manifest["segments"]), "Empty source segment set")
    ids, paths = set(), set()
    for s in manifest["segments"]:
        sid = s.get("id")
        require(isinstance(sid, str) and ID_RE.fullmatch(sid), "Invalid stable segment ID")
        require(sid not in ids, f"Duplicate source ID: {sid}")
        ids.add(sid)
        require(s.get("source_path") not in paths, f"Duplicate source path: {sid}")
        paths.add(s["source_path"])
        require(s.get("source_text") == get(manifest["source_document"], s["source_path"]), f"Source text mismatch: {sid}")
        require(isinstance(s["source_text"], str) and s["source_text"].strip(), f"Invalid source text: {sid}")
        require(s.get("source_sha256") == digest(s["source_text"]), f"Source text hash mismatch: {sid}")
        require(s.get("source_file") == manifest["source_file"] and s.get("source_revision") == manifest["source_revision"], f"Segment provenance mismatch: {sid}")
        require(s.get("surface_type") in SURFACES, f"Unknown surface: {sid}")
        require(isinstance(s.get("content_type"), str) and bool(s["content_type"]), f"Missing content type: {sid}")
        for flag in ("logic_sensitive", "character_sensitive", "semantic_risk"):
            require(type(s.get(flag)) is bool, f"Missing boolean {flag}: {sid}")
        if s["logic_sensitive"]:
            require(bool(s["logic_atoms"]), f"Logic-sensitive segment needs atoms: {sid}")
        for atom in s["logic_atoms"]:
            require(atom.get("kind") in ATOM_KINDS and "value" in atom, f"Invalid logic atom: {sid}")
            require(bool(atom.get("source_anchor")) and bool(atom.get("target_anchor")), f"Logic atom needs bilingual anchors: {sid}")
            require(atom["source_anchor"].casefold() in s["source_text"].casefold(), f"Missing source logic anchor: {sid}")
        for mapping in s["number_mappings"]:
            require(all(isinstance(mapping.get(k), str) and mapping[k] for k in ("source", "target", "rationale")), f"Invalid number mapping: {sid}")
            require(mapping["source"] in s["source_text"], f"Number mapping absent from source: {sid}")
        for token in s["protected_tokens"]:
            require(isinstance(token, str) and token in s["source_text"], f"Protected token absent from source: {sid}")
        budget = s["fit_budget"]
        if budget is not None:
            require(isinstance(budget, dict), f"Invalid fit budget: {sid}")
            for key in ("max_chars", "max_lines", "max_line_chars"):
                if key in budget:
                    require(type(budget[key]) is int and budget[key] > 0, f"Invalid {key}: {sid}")
            require(type(budget.get("requires_real_surface", True)) is bool, f"Invalid surface gate: {sid}")
    all_leaves = set(dict(leaves(manifest["source_document"])))
    protected = manifest.get("protected_paths", [])
    require(len(protected) == len(set(protected)) and not paths.intersection(protected), "Overlapping protected/localized paths")
    require(paths | set(protected) == all_leaves, "Source coverage classification is incomplete")


def segment_policy_hash(segment):
    """Review and TM reuse depend on text AND its logic/surface/terminology contract."""
    return digest({k: v for k, v in segment.items() if k not in {"source_revision", "source_file"}})


def review_valid(segment, target):
    review = target.get("semantic_review", {})
    return (review.get("status") == "pass" and bool(review.get("reviewer"))
            and review.get("source_sha256") == segment["source_sha256"]
            and review.get("target_sha256") == digest(target["target_text"])
            and review.get("policy_sha256") == segment_policy_hash(segment))
