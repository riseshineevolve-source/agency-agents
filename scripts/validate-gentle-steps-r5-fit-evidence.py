#!/usr/bin/env python3
"""Validate an exact-source-bound Gentle Steps PL V03 R5 template-fit evidence bundle."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from localization.gentle_steps_r5_fit import check_r5_fit_evidence  # noqa: E402


CONTRACT = ROOT / (
    "localization/pl-PL/production/gentle-steps/book-versions/v3/"
    "V03_R5_FINAL_EDITORIAL_SAFETY_PROOF_CONTRACT_2026-10-07.json"
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--artifact-root", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    evidence = json.loads(args.evidence.read_text(encoding="utf-8"))
    proof = check_r5_fit_evidence(contract, evidence, args.artifact_root, ROOT)

    rendered = json.dumps(proof, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if proof["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
