#!/usr/bin/env python3
"""Synthetic regression suite for the interactive-book contract validator."""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate-interactive-book-pack.py"
FIXTURE = ROOT / "orchestration" / "architecture" / "fixtures" / "interactive-book" / "synthetic_world.valid.json"

spec = importlib.util.spec_from_file_location("interactive_book_validator", VALIDATOR)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
base = json.loads(FIXTURE.read_text(encoding="utf-8"))

assert not mod.validate(base), mod.validate(base)

cases = {}

def case(name, mutate):
    pack = copy.deepcopy(base); mutate(pack); cases[name] = pack

case("duplicate_ids", lambda p: p["activities"].append(copy.deepcopy(p["activities"][0])))
case("missing_required_locale", lambda p: p["supported_locales"].remove("pl-PL"))
case("missing_translation", lambda p: p["localized_copy"].pop())
case("orphan_translation", lambda p: p["localized_copy"].append({"locale":"en","activity_id":"ghost","options":{},"accessibility":{}}))
case("unknown_activity_type", lambda p: p["activities"][0].update(activity_type="unknown"))
case("missing_asset_reference", lambda p: p["activities"][0]["assets"][0].pop("bundled_path"))
case("invalid_unlock", lambda p: p["activities"][0]["progress"].update(unlock_ids=["ghost"]))
case("cycle", lambda p: p["activities"][2]["progress"].update(unlock_ids=["mission_001"]))
case("localization_behavior_mismatch", lambda p: p["localized_copy"][0].update(required=False))
case("unsupported_schema", lambda p: p.update(schema_version="9.9.9"))
case("malformed_accessibility", lambda p: p["activities"][0].update(accessibility={"requires_audio_alternative":"yes"}))
case("option_id_mismatch", lambda p: p["localized_copy"][0].update(options={"option_a":"A"}))

failures = []
for name, pack in cases.items():
    errors = mod.validate(pack)
    if not errors:
        failures.append(name)
    else:
        print(f"PASS fail-closed: {name} -> {errors[0]}")

if failures:
    raise SystemExit(f"Validator unexpectedly accepted broken cases: {failures}")
print(f"PASS: valid fixture accepted; {len(cases)} broken classes rejected")
