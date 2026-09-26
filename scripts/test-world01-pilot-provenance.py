#!/usr/bin/env python3
"""Mutation checks for the bounded published-source candidate."""

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/validate-world01-pilot-provenance.py"
spec = importlib.util.spec_from_file_location("world01_provenance", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

pack = json.loads(validator.PACK.read_text(encoding="utf-8"))
evidence = json.loads(validator.EVIDENCE.read_text(encoding="utf-8"))
assert not validator.validate(pack, evidence), validator.validate(pack, evidence)

cases = []


def case(name, mutate_pack=None, mutate_evidence=None):
    candidate = copy.deepcopy(pack)
    source = copy.deepcopy(evidence)
    if mutate_pack:
        mutate_pack(candidate)
    if mutate_evidence:
        mutate_evidence(source)
    cases.append((name, candidate, source))


case("app_only_subtitle", lambda p: p["localized_copy"][0].update(subtitle="Learning to shake off heavy school energy"))
case("app_punctuation_promoted", lambda p: p["localized_copy"][2].update(
    prompt="Realizing that real life isn't 'broken' — it just has slow download speeds. Grinding is where the magic happens."
))
case("copy_divergence", lambda p: p["localized_copy"][1].update(title="Changed title"))
case("key_divergence", lambda p: p["localized_copy"][0].update(key_acquired="CALM"))
case("wrong_source_hash", lambda p: p["provenance"].update(source_sha256="0" * 64))
case("wrong_source_page", lambda p: p["activity_provenance"][0].update(page=16))
case("extra_app_activity", lambda p: p["activities"].append(copy.deepcopy(p["activities"][0])))
case("unapproved_translation", lambda p: p["supported_locales"].append("pl-PL"))
case("removed_custody", lambda p: p.pop("provenance"))
case("unsupported_behavior", lambda p: p["activities"][0]["interaction"].update(mode="single_choice"))
case("evidence_page_drift", mutate_evidence=lambda e: e["mission_openers"][0].update(page=16))
case("evidence_source_drift", mutate_evidence=lambda e: e.update(sha256="0" * 64))

for name, candidate, source in cases:
    errors = validator.validate(candidate, source)
    assert errors, f"accepted broken case: {name}"
    print(f"PASS fail-closed: {name} -> {errors[0]}")

print(f"PASS: valid World 01 candidate accepted; {len(cases)} provenance/parity mutations rejected")
