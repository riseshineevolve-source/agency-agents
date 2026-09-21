#!/usr/bin/env python3
"""Deterministic validator for RSE Interactive Book Content Contract v0.

Synthetic/content-structure validation only. No product conversion or deployment.
"""
import json
import re
import sys
from pathlib import Path

SUPPORTED_SCHEMA = {"0.1.0"}
SUPPORTED_RUNTIME = {"0.1.0"}
ACTIVITY_TYPES = {"reflection_choice", "info_card", "check_in"}
INTERACTION_MODES = {"single_choice", "continue", "acknowledge"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


def fail(errors, message):
    errors.append(message)


def validate(pack):
    errors = []
    required = ["schema_version", "product_id", "content_pack_id", "content_version", "canonical_locale"]
    for key in required:
        if not isinstance(pack.get(key), str) or not pack[key].strip():
            fail(errors, f"missing/non-empty string required: {key}")

    if pack.get("schema_version") not in SUPPORTED_SCHEMA:
        fail(errors, "unsupported schema_version")
    if pack.get("minimum_runtime_contract") not in SUPPORTED_RUNTIME:
        fail(errors, "unsupported minimum_runtime_contract")

    locales = pack.get("supported_locales")
    if not isinstance(locales, list) or not locales or any(not isinstance(x, str) or not x for x in locales):
        fail(errors, "supported_locales must be a non-empty string list")
        locales = []
    if pack.get("canonical_locale") not in locales:
        fail(errors, "canonical_locale missing from supported_locales")

    activities = pack.get("activities")
    if not isinstance(activities, list):
        fail(errors, "activities must be a list")
        activities = []

    ids, activities_by_id, asset_ids = [], {}, set()
    unlock_graph = {}
    for a in activities:
        if not isinstance(a, dict):
            fail(errors, "activity must be an object")
            continue
        aid = a.get("activity_id")
        if not isinstance(aid, str) or not ID_RE.match(aid):
            fail(errors, f"invalid activity_id: {aid!r}")
            continue
        ids.append(aid)
        activities_by_id[aid] = a
        if a.get("activity_type") not in ACTIVITY_TYPES:
            fail(errors, f"{aid}: unknown activity_type")
        interaction = a.get("interaction")
        if not isinstance(interaction, dict) or interaction.get("mode") not in INTERACTION_MODES:
            fail(errors, f"{aid}: unknown/missing interaction.mode")
        option_ids = interaction.get("option_ids", []) if isinstance(interaction, dict) else []
        if not isinstance(option_ids, list) or len(option_ids) != len(set(option_ids)):
            fail(errors, f"{aid}: option_ids must be a unique list")
        accessibility = a.get("accessibility")
        if not isinstance(accessibility, dict) or not all(isinstance(accessibility.get(k), bool) for k in ("requires_audio_alternative", "requires_motion_reduction_variant")):
            fail(errors, f"{aid}: malformed accessibility requirements")
        assets = a.get("assets", [])
        if not isinstance(assets, list):
            fail(errors, f"{aid}: assets must be a list")
            assets = []
        for asset in assets:
            if not isinstance(asset, dict) or not asset.get("asset_id") or not asset.get("bundled_path"):
                fail(errors, f"{aid}: malformed/missing referenced asset")
            else:
                asset_ids.add(asset["asset_id"])
        progress = a.get("progress", {})
        unlocks = progress.get("unlock_ids", []) if isinstance(progress, dict) else []
        if not isinstance(unlocks, list):
            fail(errors, f"{aid}: unlock_ids must be a list")
            unlocks = []
        unlock_graph[aid] = unlocks

    if len(ids) != len(set(ids)):
        fail(errors, "duplicate activity_id")
    for aid, targets in unlock_graph.items():
        for target in targets:
            if target not in activities_by_id:
                fail(errors, f"{aid}: invalid unlock target {target}")

    # Fail closed on progression cycles.
    visiting, visited = set(), set()
    def visit(node):
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for nxt in unlock_graph.get(node, []):
            if nxt in unlock_graph and visit(nxt):
                return True
        visiting.remove(node); visited.add(node)
        return False
    if any(visit(node) for node in list(unlock_graph) if node not in visited):
        fail(errors, "cyclic progression is unsupported")

    localized = pack.get("localized_copy")
    if not isinstance(localized, list):
        fail(errors, "localized_copy must be a list")
        localized = []
    seen_pairs = set()
    by_locale = {loc: set() for loc in locales}
    for item in localized:
        if not isinstance(item, dict):
            fail(errors, "localized copy record must be an object")
            continue
        loc, aid = item.get("locale"), item.get("activity_id")
        pair = (loc, aid)
        if pair in seen_pairs:
            fail(errors, f"duplicate localization: {loc}/{aid}")
        seen_pairs.add(pair)
        if loc not in locales:
            fail(errors, f"orphan/unsupported locale: {loc}")
        if aid not in activities_by_id:
            fail(errors, f"orphan translation object: {loc}/{aid}")
            continue
        by_locale.setdefault(loc, set()).add(aid)
        # Localization must contain copy only, never runtime behavior.
        forbidden = {"activity_type", "interaction", "progress", "required", "assets", "sequence"} & set(item)
        if forbidden:
            fail(errors, f"{loc}/{aid}: localization introduces behavior/config: {sorted(forbidden)}")
        options = item.get("options", {})
        canonical_options = set(activities_by_id[aid].get("interaction", {}).get("option_ids", []))
        if not isinstance(options, dict) or set(options) != canonical_options:
            fail(errors, f"{loc}/{aid}: option/action ID mismatch")
        req_audio = activities_by_id[aid].get("accessibility", {}).get("requires_audio_alternative")
        sr = item.get("accessibility", {}).get("screen_reader_prompt") if isinstance(item.get("accessibility"), dict) else None
        if req_audio and (not isinstance(sr, str) or not sr.strip()):
            fail(errors, f"{loc}/{aid}: required accessibility copy missing")

    required_ids = set(activities_by_id)
    for loc in locales:
        missing = required_ids - by_locale.get(loc, set())
        if missing:
            fail(errors, f"{loc}: missing translation objects: {sorted(missing)}")

    return errors


def main():
    if len(sys.argv) != 2:
        print("usage: validate-interactive-book-pack.py PACK.json", file=sys.stderr); return 2
    try:
        pack = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: unreadable/malformed JSON: {exc}"); return 1
    errors = validate(pack)
    if errors:
        for error in errors: print(f"FAIL: {error}")
        return 1
    print("PASS: interactive book content pack contract v0")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
