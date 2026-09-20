#!/usr/bin/env python3
"""Deterministic validator for synthetic RSE Interactive Book content packs.

This validator intentionally knows nothing about real RSE product copy. It enforces
v0 structural/localization/progression invariants before any real-product conversion.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SUPPORTED_SCHEMA = {"0.1.0"}
ALLOWED_ACTIVITY_TYPES = {"reflection_choice", "instruction", "checklist"}
ALLOWED_INTERACTION_MODES = {"single_choice", "display_only", "multi_choice"}
REQUIRED_LOCALES = {"en", "pl-PL"}


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate(pack: dict, base: Path) -> list[str]:
    errors: list[str] = []
    for key in ("schema_version", "product_id", "content_pack_id", "content_version", "canonical_locale"):
        if not isinstance(pack.get(key), str) or not pack[key].strip():
            errors.append(f"missing/non-empty string required: {key}")

    if pack.get("schema_version") not in SUPPORTED_SCHEMA:
        errors.append("unsupported schema_version")

    locales = pack.get("supported_locales")
    if not isinstance(locales, list) or not all(isinstance(x, str) for x in locales):
        errors.append("supported_locales must be a string list")
        locales = []
    if pack.get("canonical_locale") not in locales:
        errors.append("canonical_locale must occur in supported_locales")
    missing_required = REQUIRED_LOCALES - set(locales)
    if missing_required:
        errors.append("missing required locale(s): " + ", ".join(sorted(missing_required)))

    activities = pack.get("activities")
    if not isinstance(activities, list):
        errors.append("activities must be a list")
        activities = []

    ids: list[str] = []
    option_ids: dict[str, set[str]] = {}
    unlocks: dict[str, list[str]] = {}
    for activity in activities:
        if not isinstance(activity, dict):
            errors.append("activity must be an object")
            continue
        aid = activity.get("activity_id")
        if not isinstance(aid, str) or not aid:
            errors.append("activity_id must be non-empty")
            continue
        ids.append(aid)
        if activity.get("activity_type") not in ALLOWED_ACTIVITY_TYPES:
            errors.append(f"{aid}: unknown activity_type")
        interaction = activity.get("interaction", {})
        if interaction.get("mode") not in ALLOWED_INTERACTION_MODES:
            errors.append(f"{aid}: unknown interaction.mode")
        opts = interaction.get("option_ids", [])
        if not isinstance(opts, list) or not all(isinstance(x, str) and x for x in opts):
            errors.append(f"{aid}: option_ids must be non-empty strings")
            opts = []
        if len(opts) != len(set(opts)):
            errors.append(f"{aid}: duplicate option_ids")
        option_ids[aid] = set(opts)
        progress = activity.get("progress", {})
        targets = progress.get("unlock_ids", [])
        if not isinstance(targets, list) or not all(isinstance(x, str) for x in targets):
            errors.append(f"{aid}: unlock_ids must be a string list")
            targets = []
        unlocks[aid] = targets
        for asset in activity.get("assets", []):
            if not isinstance(asset, dict):
                errors.append(f"{aid}: asset must be an object")
                continue
            bundled = asset.get("bundled_path")
            if bundled and not (base / bundled).is_file():
                errors.append(f"{aid}: missing referenced asset: {bundled}")

    if len(ids) != len(set(ids)):
        errors.append("duplicate activity_id")
    known = set(ids)
    for aid, targets in unlocks.items():
        for target in targets:
            if target not in known:
                errors.append(f"{aid}: invalid unlock target: {target}")

    # v0 progression is acyclic unless a future contract explicitly adds cycle support.
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(node: str):
        if node in visiting:
            errors.append(f"cyclic progression detected at {node}")
            return
        if node in visited:
            return
        visiting.add(node)
        for nxt in unlocks.get(node, []):
            if nxt in known:
                visit(nxt)
        visiting.remove(node)
        visited.add(node)
    for aid in ids:
        visit(aid)

    localizations = pack.get("localizations")
    if not isinstance(localizations, list):
        errors.append("localizations must be a list")
        localizations = []
    by_pair: dict[tuple[str, str], dict] = {}
    for item in localizations:
        if not isinstance(item, dict):
            errors.append("localization must be an object")
            continue
        pair = (item.get("locale"), item.get("activity_id"))
        if pair in by_pair:
            errors.append(f"duplicate localization: {pair}")
        by_pair[pair] = item
        if pair[0] not in locales:
            errors.append(f"orphan/unsupported locale: {pair[0]}")
        if pair[1] not in known:
            errors.append(f"orphan translation activity_id: {pair[1]}")

    for locale in REQUIRED_LOCALES:
        for aid in ids:
            item = by_pair.get((locale, aid))
            if not item:
                errors.append(f"missing translation: {locale}/{aid}")
                continue
            translated_opts = item.get("options", {})
            if not isinstance(translated_opts, dict):
                errors.append(f"{locale}/{aid}: options must be an object")
                translated_opts = {}
            if set(translated_opts) != option_ids.get(aid, set()):
                errors.append(f"{locale}/{aid}: option/action ID mismatch")
            accessibility = next((a.get("accessibility", {}) for a in activities if isinstance(a, dict) and a.get("activity_id") == aid), {})
            if accessibility.get("requires_audio_alternative"):
                loc_access = item.get("accessibility", {})
                if not isinstance(loc_access, dict) or not loc_access.get("screen_reader_prompt"):
                    errors.append(f"{locale}/{aid}: missing required accessibility string")

    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack", type=Path)
    args = parser.parse_args()
    try:
        pack = load(args.pack)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot load pack: {exc}", file=sys.stderr)
        return 2
    errors = validate(pack, args.pack.parent)
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print("PASS: interactive book pack satisfies v0 deterministic invariants")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
