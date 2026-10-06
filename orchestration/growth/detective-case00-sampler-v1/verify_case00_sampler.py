#!/usr/bin/env python3
"""Fail-closed checks for the non-production Detective CASE 00 sampler."""
import itertools
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
HTML = ROOT / "index.html"
html = HTML.read_text(encoding="utf-8")

symbols = ["BALL", "STAR", "BOLT", "HEART", "KEY", "MOON"]
declared = tuple(symbols)
clues = [
    "STAR comes immediately before BOLT.",
    "BALL appears somewhere before STAR.",
    "HEART appears somewhere after BOLT.",
    "KEY appears somewhere before MOON.",
    "HEART appears somewhere before MOON.",
    "HEART is not fifth.",
]

def fail(message):
    print("FAIL:", message, file=sys.stderr)
    raise SystemExit(1)

def satisfies(order):
    pos = {value: i for i, value in enumerate(order)}
    return (
        pos["BOLT"] == pos["STAR"] + 1
        and pos["BALL"] < pos["STAR"]
        and pos["HEART"] > pos["BOLT"]
        and pos["KEY"] < pos["MOON"]
        and pos["HEART"] < pos["MOON"]
        and pos["HEART"] != 4
    )

solutions = [order for order in itertools.permutations(symbols) if satisfies(order)]
if solutions != [declared]:
    fail(f"expected one solution {declared}, found {solutions}")

for clue in clues:
    if clue not in html:
        fail(f"missing source-locked clue: {clue}")

if "NON-PRODUCTION V12-LOCKED SAMPLER" not in html:
    fail("visible non-production V12 guard missing")
if "Full book link unlocks after verified live listing" not in html:
    fail("pre-live CTA guard missing")
if re.search(r"<script\s+[^>]*src=", html, flags=re.I):
    fail("external script detected")
if re.search(r"https?://", html, flags=re.I):
    fail("external URL detected")

print("PASS: CASE 00 unique solution, clue integrity, provenance label and no-deploy guards.")
