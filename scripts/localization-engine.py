#!/usr/bin/env python3
"""RSE source segmentation, QA, packaging, approved reuse and real-template gates."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

from localization.contracts import extract, require
from localization.gates import qa, markdown_report, aggregate_reports
from localization.io import ContractError, load, dump, dump_payload, leaves, file_digest
from localization.detective import prepare as prepare_detective, freeze_gate
from localization.packaging import package, build_memory, reuse_memory
from localization.fit import fit_request, check_evidence
from localization.terminology import markdown as terminology_markdown

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "localization/pl-PL/engine"


def phrases():
    return re.findall(r'^\s*-\s*"([^"]+)"\s*$', (ROOT / "localization/pl-PL/FORBIDDEN_AIISMS_PL.yml").read_text(encoding="utf-8"), re.M)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    terminology = sub.add_parser("terms-doc")
    terminology.add_argument("--check", action="store_true")
    suite = sub.add_parser("qa-suite")
    suite.add_argument("--reports", nargs="+", required=True)
    suite.add_argument("--output", required=True)
    detective = sub.add_parser("detective-prepare")
    for option in ("source", "freeze", "aliases", "output"):
        detective.add_argument("--" + option, required=True)
    inventory = sub.add_parser("inventory", help="Enumerate source paths for exhaustive classification; does not translate")
    inventory.add_argument("--source", required=True)
    inventory.add_argument("--output", required=True)
    ingest = sub.add_parser("extract")
    for option in ("source", "plan", "revision", "output"):
        ingest.add_argument("--" + option, required=True)
    for name in ("qa", "export", "tm-build", "tm-reuse"):
        cmd = sub.add_parser(name)
        for option in ("manifest", "targets", "output"):
            cmd.add_argument("--" + option, required=True)
        cmd.add_argument("--terms", default=str(DATA / "terminology.json"))
        cmd.add_argument("--current-source", help="Optionally verify a structured source file still matches the frozen snapshot")
        if name == "export":
            cmd.add_argument("--release", action="store_true")
            cmd.add_argument("--payload-output")
        if name == "tm-reuse":
            cmd.add_argument("--memory", required=True)
    for name in ("fit-request", "fit-proof"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--spec", default=str(DATA / "gentle-steps-fit.json"))
        cmd.add_argument("--output", required=True)
        if name == "fit-proof":
            cmd.add_argument("--evidence")
    args = ap.parse_args(argv)
    try:
        if args.command == "terms-doc":
            path = ROOT / "localization/pl-PL/ACCEPTED_TERMINOLOGY.md"
            rendered = terminology_markdown(load(DATA / "terminology.json"))
            if args.check:
                require(path.read_text(encoding="utf-8") == rendered, "Generated terminology documentation is stale")
            else:
                path.write_text(rendered, encoding="utf-8", newline="\n")
        elif args.command == "qa-suite":
            result = aggregate_reports([load(path) for path in args.reports])
            dump(args.output, result)
            Path(args.output).with_suffix(".md").write_text(markdown_report(result), encoding="utf-8", newline="\n")
            return 1 if result["counts"]["errors"] else 0
        elif args.command == "detective-prepare":
            document, key_types = load(args.source, with_key_types=True)
            plan = prepare_detective(document, load(args.freeze), file_digest(args.source), load(args.aliases))
            plan['source_key_types'] = key_types
            dump(args.output, plan)
        elif args.command == "inventory":
            document, key_types = load(args.source, with_key_types=True)
            dump(args.output, {"source_file": args.source, "source_key_types": key_types, "paths": [{"source_path": p, "type": type(v).__name__, "value": v} for p, v in leaves(document)]})
        elif args.command == "extract":
            plan = load(args.plan)
            # Scope is auditable. This CLI does not grant the owner freeze.
            require(plan.get("scope", "bounded") != "full_book" or bool(plan.get("owner_freeze_evidence")), "Full-book extraction needs a recorded owner freeze reference")
            if plan.get("product") == "detective-academy" and plan.get("scope") == "full_book":
                freeze_gate(plan.get("freeze_receipt", {}), file_digest(args.source))
            document, key_types = load(args.source, with_key_types=True)
            manifest, targets = extract(document, plan, args.source, args.revision, key_types)
            dump(Path(args.output) / "source-manifest.json", manifest)
            dump(Path(args.output) / "targets.pl-PL.json", targets)
        elif args.command.startswith("fit-"):
            spec = load(args.spec)
            if args.command == "fit-request":
                dump(args.output, fit_request(spec))
            else:
                result = check_evidence(spec, load(args.evidence), Path(args.evidence).parent) if args.evidence else {"status": "BLOCK", "issues": ["Real-template render evidence unavailable; proxy PASS forbidden"]}
                dump(args.output, result)
                print(result["status"])
                return 2 if result["status"] != "PASS" else 0
        else:
            manifest, targets, terms = load(args.manifest), load(args.targets), load(args.terms)
            if args.current_source:
                document, key_types = load(args.current_source, with_key_types=True)
                require(document == manifest["source_document"] and key_types == manifest.get("source_key_types", {}), "Current source changed; re-extract the source manifest and invalidate stale targets before QA/export")
            if args.command == "qa":
                result = qa(manifest, targets, terms, phrases())
                dump(args.output, result)
                Path(args.output).with_suffix(".md").write_text(markdown_report(result), encoding="utf-8", newline="\n")
                print(f"{result['product']}: {result['status']} ({result['counts']})")
                return 1 if result["counts"]["errors"] else 0
            if args.command == "export":
                result = package(manifest, targets, terms, phrases(), args.release)
                if args.payload_output:
                    require(Path(args.payload_output).resolve() != Path(manifest["source_file"]).resolve(), "Cannot overwrite English source truth")
                    dump_payload(args.payload_output, result["localized_payload"], result["source_key_types"])
                dump(args.output, result)
            elif args.command == "tm-build":
                dump(args.output, build_memory(manifest, targets, terms, phrases()))
            else:
                # Validate shape/integrity first, allowing empty and stale target texts.
                qa(manifest, targets, terms, phrases())
                result, events = reuse_memory(manifest, targets, load(args.memory), terms)
                dump(args.output, result)
                dump(Path(args.output).with_suffix(".reuse.json"), events)
        return 0
    except (ContractError, KeyError, TypeError, ValueError, OSError) as exc:
        print(f"Localization BLOCK: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
