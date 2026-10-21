#!/usr/bin/env python3
"""Prepare, guard and export RSE PL/EN language work. Prose is written by the RSE language skill."""
from __future__ import annotations
import argparse
import copy
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$")
TOKENS = re.compile(r"\{\{[^{}]+\}\}|\{[A-Za-z_][A-Za-z0-9_.]*\}|%\([^)]+\)[sd]|%[sd]|https?://[^\s<>\]\)]+")
NUMBERS = re.compile(r"(?<!\w)\d+(?:[.,:]\d+)*(?!\w)")
STAGES = ["native_language", "meaning", "audience", "logic"]
BRIEF_FIELDS = ["function", "reader_action", "immutable_facts", "mechanics", "safety_consent", "chronology", "character_voice", "emotional_job", "humor_job", "dependencies"]
FORBIDDEN = {"source_text", "source_sentence", "source_excerpt", "source_copy", "literal_translation", "target_text", "draft", "english_copy", "polish_copy"}

class Block(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise Block(message)


def hash_bytes(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value):
    return hash_bytes(canonical(value))


def pairs(items):
    result = {}
    for key, value in items:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=pairs)


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def safe_new_file(path, data):
    path = Path(path)
    require(not path.exists(), f"Refusing to overwrite: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)


def strings(value, pointer=""):
    if isinstance(value, str):
        if value.strip():
            yield pointer, value
    elif isinstance(value, dict):
        for key, child in value.items():
            escaped = key.replace("~", "~0").replace("/", "~1")
            yield from strings(child, pointer + "/" + escaped)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from strings(child, pointer + "/" + str(index))


def paragraphs(text, prefix):
    for index, match in enumerate(re.finditer(r"\S[\s\S]*?(?=\n[ \t]*\n|\Z)", text), 1):
        yield f"{prefix}/paragraph/{index}", match.group().strip()


def extract(source):
    suffix = source.suffix.lower()
    if suffix == ".json":
        value = load(source)
        if isinstance(value, dict) and isinstance(value.get("segments"), list):
            specs = value["segments"]
            require(specs and all(isinstance(s, dict) and isinstance(s.get("text"), str) and s["text"].strip() for s in specs), "Structured segments need nonempty text")
            ids = [s.get("id") for s in specs]
            require(all(isinstance(sid, str) and ID.fullmatch(sid) for sid in ids) and len(ids) == len(set(ids)), "Invalid/duplicate structured source IDs")
            return [(f"/segments/{i}/text", s["text"]) for i, s in enumerate(specs)], {"kind": "json", "document": value, "segment_specs": specs}
        return list(strings(value)), {"kind": "json", "document": value}
    if suffix == ".docx":
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        ptag = "{" + ns["w"] + "}p"
        def own_text(node, root=True):
            if node.tag == ptag and not root:
                return ""
            kind = node.tag.rsplit("}", 1)[-1]
            if kind == "t":
                return node.text or ""
            if kind in {"tab", "br", "cr"}:
                return "\t" if kind == "tab" else "\n"
            return "".join(own_text(child, False) for child in node)
        segments = []
        with zipfile.ZipFile(source) as archive:
            names = ["word/document.xml"] + sorted(name for name in archive.namelist()
                    if re.fullmatch(r"word/(?:header\d*|footer\d*|footnotes|endnotes)\.xml", name))
            for name in names:
                document = ET.fromstring(archive.read(name))
                for index, paragraph in enumerate(document.iter(ptag), 1):
                    text = own_text(paragraph)
                    if text.strip():
                        segments.append((f"docx/{name}/paragraph/{index}", text))
        return segments, {"kind": "docx", "parts": names, "note": "Text from body/tables/textboxes, headers, footers and notes. Images, fields, reading order and tracked changes need source audit; comments are editorial metadata."}
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader
            pages = [page.extract_text() or "" for page in PdfReader(source).pages]
        except ImportError:
            require(shutil.which("pdftotext"), "PDF extraction needs pypdf or pdftotext")
            process = subprocess.run(["pdftotext", "-layout", str(source), "-"], capture_output=True, check=True)
            pages = process.stdout.decode("utf-8").split("\f")
        result = []
        for index, page in enumerate(pages, 1):
            result.extend(paragraphs(page, f"pdf/page/{index}"))
        return result, {"kind": "pdf", "note": "Extracted text only; visual/OCR completeness and reading order require review."}
    require(suffix in {".md", ".txt", ".markdown"}, "Supported sources: MD, TXT, JSON, DOCX, PDF")
    return list(paragraphs(source.read_text(encoding="utf-8-sig"), "text")), {"kind": "text"}


def language(text):
    words = Counter(re.findall(r"[^\W\d_]+", text.lower()))
    pl = sum(words[w] for w in "jest się nie na że jak dla to z w do i oraz przez was razem coś macie chwilę".split())
    en = sum(words[w] for w in "the a an is are and with your you to of for this that together do not".split())
    pl += 2 * sum(1 for c in text.lower() if c in "ąćęłńóśźż")
    require(max(pl, en) >= 3 and abs(pl-en) >= 2, "Source language is ambiguous; supply --from pl or --from en")
    return "pl" if pl > en else "en"


def get_profile(project, override=None):
    path = Path(override) if override else ROOT / "tools/rse-language/profiles" / (project + ".json")
    if not path.exists():
        require(project == "generic" and override is None, f"Missing project profile: {path}")
        return {"project": project, "languages": {"pl": {}, "en": {}}}
    value = load(path)
    require(isinstance(value, dict) and value.get("project") == project, "Project/profile mismatch")
    require(isinstance(value.get("languages"), dict), "Profile needs languages")
    return value


def required_locks(profile, original, source_lang, target_lang):
    target = profile["languages"].get(target_lang, {})
    result = list(target.get("required_strings", []))
    for lock in profile.get("locks", []):
        before, after = lock.get(source_lang), lock.get(target_lang)
        if before and before in original and after:
            result.append(after)
    require(all(isinstance(item, str) and item for item in result), "Invalid profile required strings")
    return list(dict.fromkeys(result))


def lock_counts(profile, original, source_lang, target_lang):
    counts = {text: 1 for text in profile["languages"].get(target_lang, {}).get("required_strings", [])}
    for lock in profile.get("locks", []):
        before, after = lock.get(source_lang), lock.get(target_lang)
        if before and after and before in original:
            counts[after] = max(counts.get(after, 0), original.count(before))
    return counts


def freeze_check(project, source_sha, receipt):
    require(isinstance(receipt, dict), "Detective production requires --freeze with current exact source authority")
    require(receipt.get("project") == project and receipt.get("approved") is True, "Detective freeze is not explicitly approved for this project")
    require(receipt.get("source_sha256") == source_sha, "Detective freeze source hash mismatch")
    require(isinstance(receipt.get("reference"), str) and receipt["reference"].strip(), "Detective freeze needs an owner reference")


def prepare(args):
    source = Path(args.source).resolve()
    require(source.is_file(), "Source file does not exist")
    destination = Path(args.output).resolve()
    require(not destination.exists(), "Run directory already exists; resume it instead of overwriting")
    require(destination != source and source not in destination.parents, "Run cannot replace or be inside the source file")
    raw = source.read_bytes()
    source_sha = hash_bytes(raw)
    units, adapter = extract(source)
    require(units, "Source has no extractable text; OCR/source audit required")
    original = "\n\n".join(text for _, text in units)
    source_lang = args.source_language if args.source_language != "auto" else language(original)
    mode = args.mode if args.mode != "auto" else ("upgrade" if source_lang == args.to else "localize")
    require((source_lang == args.to) == (mode == "upgrade"), "Use upgrade for the same language, localize for a different language")
    profile = get_profile(args.project, args.profile)
    freeze = load(args.freeze) if args.freeze else None
    if args.project == "detective-academy" and (mode == "localize" or args.scope == "full_book"):
        freeze_check(args.project, source_sha, freeze)
    segments = []
    for index, (locator, text) in enumerate(units, 1):
        spec = adapter.get("segment_specs", [{}] * len(units))[index - 1]
        tokens = TOKENS.findall(text) + spec.get("protected_tokens", [])
        for pattern in profile.get("protect_patterns", []):
            tokens.extend(match.group(0) for match in re.finditer(pattern, text))
        require(all(isinstance(t, str) and t and t in text for t in tokens), "Protected tokens must exist in the source segment")
        segments.append({"id": spec.get("id", f"s{index:04d}"), "locator": locator, "source_text": text,
                         "source_sha256": hash_bytes(text.encode()), "protected_tokens": list(dict.fromkeys(tokens)),
                         "numbers": NUMBERS.findall(text), "protected_numbers": spec.get("protected_numbers", []),
                         "protected": spec.get("protected", False)})
    manifest = {"format": "rse-language-run-v1", "source_path": str(source), "source_sha256": source_sha,
                "source_snapshot": "source" + source.suffix.lower(), "source_language": source_lang,
                "target_language": args.to, "mode": mode, "scope": args.scope, "project": args.project,
                "profile": profile, "adapter": adapter, "freeze": freeze, "segments": segments,
                "required_strings": required_locks(profile, original, source_lang, args.to),
                "required_string_counts": lock_counts(profile, original, source_lang, args.to),
                "preserve_numbers": args.preserve_numbers,
                "default_status": "PREMIUM_WORKING", "print_ready": False, "release_authorized": False}
    manifest["manifest_sha256"] = digest(manifest)
    candidate = {"format": "rse-language-candidate-v1", "language": args.to,
                 "run_sha256": manifest["manifest_sha256"],
                 "segments": [{"id": s["id"], "text": s["source_text"] if mode == "upgrade" else ""} for s in segments]}
    brief = {"format": "rse-language-brief-v1", "run_sha256": manifest["manifest_sha256"],
             "units": [{"id": s["id"], "locator": s["locator"], **{field: "" for field in BRIEF_FIELDS}} for s in segments]}
    packet = {"format": "rse-language-writer-packet-v1", "status": "FUNCTION_BRIEF_REQUIRED",
              "target_language": args.to, "source_visibility": "functional_brief_only" if mode == "localize" else "same_language_baseline",
              "run_sha256": manifest["manifest_sha256"], "units": [{"id": s["id"]} for s in segments],
              "instruction": "Fill and validate functional-brief.json using packet before drafting. The CLI does not generate prose."}
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".rse-language-", dir=destination.parent))
    try:
        (staging / manifest["source_snapshot"]).write_bytes(raw)
        save(staging / "run.json", manifest)
        save(staging / "candidate.json", candidate)
        save(staging / "functional-brief.json", brief)
        save(staging / "writer-packet.json", packet)
        save(staging / "issue-ledger.json", {"run_sha256": manifest["manifest_sha256"], "issues": [], "diagnostic": "NOT_RUN"})
        save(staging / "change-scope.json", {"run_sha256": manifest["manifest_sha256"], "allowed_changed_segments": [], "protected_segments": [], "reason": "Declare before meaningful edits"})
        (staging / "SOURCE_AND_WORKFLOW.md").write_text(
            "# Source and workflow\n\nSource is immutable. The skill performs diagnosis, KEEP/FIX selection, native writing and independent review.\n"
            "Declare change-scope.json before editing; every changed segment must be allowed and have a reason.\n"
            "For localization fill functional-brief.json then run packet. Give only the resulting packet to the first target-language writer.\n"
            "Run check on the candidate. Machine PASS does not prove semantic fidelity, language quality, layout or release approval.\n", encoding="utf-8")
        staging.rename(destination)
    except BaseException:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    return {"status": "PREPARED", "run": str(destination), "source_sha256": source_sha, "segments": len(segments), "mode": mode, "language_review": "NOT_RUN"}


def run_load(directory):
    directory = Path(directory).resolve()
    run = load(directory / "run.json")
    require(isinstance(run, dict) and run.get("format") == "rse-language-run-v1", "Unknown run format")
    require(run.get("manifest_sha256") == digest({key: value for key, value in run.items() if key != "manifest_sha256"}), "Run manifest changed")
    snapshot = directory / run["source_snapshot"]
    require(snapshot.parent == directory, "Invalid source snapshot path")
    require(hash_bytes(snapshot.read_bytes()) == run["source_sha256"], "Immutable source snapshot changed")
    original = Path(run["source_path"])
    require(original.is_file() and hash_bytes(original.read_bytes()) == run["source_sha256"], "Current original source changed or is unavailable")
    source_ids = [s["id"] for s in run["segments"]]
    require(source_ids and len(source_ids) == len(set(source_ids)) and all(ID.fullmatch(s) for s in source_ids), "Invalid source IDs")
    for segment in run["segments"]:
        require(hash_bytes(segment["source_text"].encode()) == segment["source_sha256"], "Source segment changed")
    return directory, run


def walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_keys(child)


def validate_brief(run, brief):
    require(isinstance(brief, dict) and brief.get("format") == "rse-language-brief-v1" and brief.get("run_sha256") == run["manifest_sha256"], "Brief belongs to another source/run")
    require(set(brief) <= {"format", "run_sha256", "units"}, "Unknown brief fields could leak source wording")
    require(not (FORBIDDEN & set(walk_keys(brief))), "Brief contains source wording/draft keys")
    units = brief.get("units", [])
    expected = [s["id"] for s in run["segments"]]
    require(isinstance(units, list) and all(isinstance(u, dict) for u in units) and [u.get("id") for u in units] == expected, "Brief IDs must cover source in order")
    for unit, source in zip(units, run["segments"]):
        require(set(unit) <= {"id", "locator", *BRIEF_FIELDS}, "Unknown brief unit fields could leak source wording")
        require(unit.get("locator") == source["locator"], "Brief source locator mismatch")
        for field in BRIEF_FIELDS:
            require(isinstance(unit.get(field), (str, list, dict)) and bool(unit[field]), f"Brief needs {field} for {unit['id']}; use explicit none where inapplicable")
        if run["mode"] == "localize":
            source_words = re.findall(r"\w+", source["source_text"].lower())
            brief_text = " ".join(re.findall(r"\w+", json.dumps({k: unit[k] for k in BRIEF_FIELDS}, ensure_ascii=False).lower()))
            require(not any(" ".join(source_words[i:i+8]) in brief_text for i in range(max(0, len(source_words)-7))), "Brief repeats sentence-level source wording; summarize function instead")
    return units


def build_packet(run, brief):
    units = validate_brief(run, brief)
    return {"format": "rse-language-writer-packet-v1", "status": "READY_FOR_NATIVE_WRITER",
            "run_sha256": run["manifest_sha256"], "brief_sha256": digest(brief), "target_language": run["target_language"],
            "source_visibility": "functional_brief_only", "required_strings": run["required_strings"],
            "required_string_counts": run["required_string_counts"],
            "profile": run["profile"]["languages"].get(run["target_language"], {}),
            "voice": run["profile"].get("voice", {}).get(run["target_language"], ""), "units": units,
            "segment_constraints": [{"id": s["id"], "protected_tokens": s["protected_tokens"],
                "protected_numbers": s["numbers"] if run.get("preserve_numbers") else s.get("protected_numbers", [])} for s in run["segments"]],
            "instruction": "Write from function and immutable truth. Preserve mechanics, consent and claim strength. Reopen original only for final bilingual backcheck."}


def packet(args):
    directory, run = run_load(args.run)
    result = build_packet(run, load(args.brief))
    data = json.dumps(result, ensure_ascii=False, indent=2).encode() + b"\n"
    sidecar = str(args.output) + ".receipt.json"
    require(not Path(args.output).exists() and not Path(sidecar).exists(), "Packet or receipt output already exists")
    safe_new_file(args.output, data)
    receipt = {"format": "rse-language-packet-receipt-v1", "run_sha256": run["manifest_sha256"], "packet_sha256": hash_bytes(data), "brief_sha256": result["brief_sha256"]}
    try:
        safe_new_file(sidecar, json.dumps(receipt, ensure_ascii=False, indent=2).encode() + b"\n")
    except BaseException:
        Path(args.output).unlink(missing_ok=True)
        raise
    return {"status": result["status"], "packet": str(Path(args.output).resolve()), **receipt}


def packet_check(run, candidate, path):
    if run["mode"] != "localize":
        return
    require(path, "Localization requires --packet from the completed functional brief")
    payload = load(path)
    require(isinstance(payload, dict), "Invalid writer packet")
    receipt = load(str(path) + ".receipt.json")
    sha = hash_bytes(Path(path).read_bytes())
    require(isinstance(receipt, dict) and receipt.get("format") == "rse-language-packet-receipt-v1" and receipt.get("run_sha256") == run["manifest_sha256"], "Packet receipt belongs to another source/run")
    require(receipt.get("packet_sha256") == sha, "Writer packet changed after validation")
    brief = {"format": "rse-language-brief-v1", "run_sha256": run["manifest_sha256"], "units": payload.get("units")}
    expected = build_packet(run, brief)
    require(payload == expected and receipt.get("brief_sha256") == expected["brief_sha256"], "Packet/functional-brief contract changed")
    require(candidate.get("writer_packet_sha256") == sha, "Candidate is not bound to the validated writer packet")


def candidate_check(directory, run, candidate):
    require(isinstance(candidate, dict) and candidate.get("format") == "rse-language-candidate-v1", "Unknown candidate format")
    require(candidate.get("run_sha256") == run["manifest_sha256"], "Candidate belongs to a different run")
    require(candidate.get("language") == run["target_language"], "Candidate target language mismatch")
    units = candidate.get("segments")
    require(isinstance(units, list) and all(isinstance(s, dict) for s in units), "Candidate segments must be a list of objects")
    actual = [s.get("id") for s in units]
    expected = [s["id"] for s in run["segments"]]
    require(all(isinstance(sid, str) and ID.fullmatch(sid) for sid in actual), "Invalid candidate ID")
    require(len(actual) == len(set(actual)), "Duplicate candidate IDs")
    require(actual == expected, "Candidate must cover every source ID exactly once in source order")
    scope = load(directory / "change-scope.json")
    require(isinstance(scope, dict) and scope.get("run_sha256") == run["manifest_sha256"], "Change scope is stale")
    allowed, protected = scope.get("allowed_changed_segments", []), scope.get("protected_segments", [])
    require(isinstance(allowed, list) and isinstance(protected, list), "Invalid change scope")
    require(set(allowed) <= set(expected) and set(protected) <= set(expected), "Unknown scope IDs")
    require(not set(allowed) & set(protected), "Allowed/protected scope overlaps")
    changes = []
    for source, target in zip(run["segments"], units):
        text = target.get("text")
        require(isinstance(text, str) and text.strip(), f"Empty/missing target: {source['id']}")
        changed = text != source["source_text"]
        if changed:
            changes.append(source["id"])
            require(source["id"] in allowed and isinstance(scope.get("reason"), str) and scope["reason"].strip(), f"Undeclared change: {source['id']}")
        if source.get("protected") or source["id"] in protected:
            require(not changed, f"Protected region changed: {source['id']}")
        for token in source["protected_tokens"]:
            require(text.count(token) == source["source_text"].count(token), f"Protected token changed: {source['id']}: {token}")
        if run.get("preserve_numbers"):
            require(Counter(NUMBERS.findall(text)) == Counter(source["numbers"]), f"Number drift: {source['id']}")
        for token in source.get("protected_numbers", []):
            require(isinstance(token, str) and Counter(NUMBERS.findall(text))[token] == Counter(source["numbers"])[token] > 0, f"Declared number drift: {source['id']}")
    all_text = "\n\n".join(s["text"] for s in units)
    for lock in run["required_strings"]:
        require(all_text.count(lock) == run["required_string_counts"][lock], f"Owner lock missing/changed/duplicated: {lock}")
    for forbidden in run["profile"]["languages"].get(run["target_language"], {}).get("forbidden_strings", []):
        require(forbidden not in all_text, f"Forbidden/stale string: {forbidden}")
    if run["project"] == "detective-academy" and (run["mode"] == "localize" or run["scope"] == "full_book"):
        freeze_check(run["project"], run["source_sha256"], run["freeze"])
    return changes


def review_check(run, candidate_sha, reviews):
    require(isinstance(reviews, dict) and reviews.get("candidate_sha256") == candidate_sha, "Review bundle is stale for candidate bytes")
    receipts = reviews.get("reviews", [])
    require(isinstance(receipts, list) and all(isinstance(r, dict) for r in receipts), "Reviews must be a list of objects")
    names = [r.get("stage") for r in receipts]
    require(len(names) == len(set(names)), "Duplicate review stages")
    stages = run["profile"]["languages"].get(run["target_language"], {}).get("required_review_stages", STAGES)
    require(stages and all(isinstance(s, str) and s for s in stages), "No valid review stages configured")
    by_stage = {r["stage"]: r for r in receipts}
    for stage in stages:
        require(stage in by_stage, f"Missing specialist review: {stage}")
        review = by_stage[stage]
        require(review.get("candidate_sha256") == candidate_sha, f"Stale review: {stage}")
        require(review.get("status") == "PASS", f"Specialist review has unresolved issues: {stage}")
        require(isinstance(review.get("reviewer"), str) and review["reviewer"].strip(), f"Review lacks identity: {stage}")
        require(isinstance(review.get("evidence"), str) and review["evidence"].strip(), f"Review lacks evidence: {stage}")
    return list(stages)


def check(args):
    directory, run = run_load(args.run)
    candidate_path = Path(args.candidate).resolve()
    candidate = load(candidate_path)
    changes = candidate_check(directory, run, candidate)
    packet_check(run, candidate, args.packet)
    candidate_sha = hash_bytes(candidate_path.read_bytes())
    stages = review_check(run, candidate_sha, load(args.reviews)) if args.reviews else []
    result = {"status": "OWNER_READ_CANDIDATE" if stages else "LANGUAGE_REVIEW_REQUIRED",
              "deterministic_qa": "PASS", "candidate_sha256": candidate_sha, "changed_segments": changes,
              "specialist_reviews": stages or "NOT_RUN", "surface_fit": "NOT_RUN",
              "owner_approval": "NOT_GRANTED", "print_ready": False, "release_authorized": False}
    if args.output:
        safe_new_file(args.output, json.dumps(result, ensure_ascii=False, indent=2).encode() + b"\n")
    return result


def export(args):
    directory, run = run_load(args.run)
    candidate = load(args.candidate)
    candidate_check(directory, run, candidate)
    packet_check(run, candidate, args.packet)
    output = Path(args.output).resolve()
    protected_paths = {Path(run["source_path"]).resolve(), directory / "run.json", directory / run["source_snapshot"]}
    require(output not in protected_paths, "Cannot export over provenance/source")
    if run["adapter"]["kind"] == "json":
        value = copy.deepcopy(run["adapter"]["document"])
        for source, target in zip(run["segments"], candidate["segments"]):
            if source["locator"] == "":
                value = target["text"]
                continue
            parts = [p.replace("~1", "/").replace("~0", "~") for p in source["locator"].split("/")[1:]]
            node = value
            for part in parts[:-1]:
                node = node[int(part)] if isinstance(node, list) else node[part]
            key = int(parts[-1]) if isinstance(node, list) else parts[-1]
            node[key] = target["text"]
        if isinstance(value, dict) and "segment_specs" in run["adapter"] and value.get("language") == run["source_language"]:
            value["language"] = run["target_language"]
        data = json.dumps(value, ensure_ascii=False, indent=2).encode() + b"\n"
    else:
        data = ("\n\n".join(s["text"] for s in candidate["segments"]) + "\n").encode()
    safe_new_file(output, data)
    return {"status": "WORKING_EXPORT", "output": str(output), "sha256": hash_bytes(data), "print_ready": False, "release_authorized": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    cmd = sub.add_parser("prepare")
    cmd.add_argument("--source", required=True)
    cmd.add_argument("--to", choices=["pl", "en"], required=True)
    cmd.add_argument("--from", dest="source_language", choices=["pl", "en", "auto"], default="auto")
    cmd.add_argument("--mode", choices=["auto", "upgrade", "localize"], default="auto")
    cmd.add_argument("--project", choices=["gentle-steps", "detective-academy", "generic"], default="generic")
    cmd.add_argument("--scope", choices=["bounded", "full_book"], default="full_book")
    cmd.add_argument("--profile")
    cmd.add_argument("--freeze")
    cmd.add_argument("--preserve-numbers", action="store_true")
    cmd.add_argument("--output", required=True)
    cmd = sub.add_parser("packet")
    for option in ["run", "brief", "output"]:
        cmd.add_argument("--" + option, required=True)
    cmd = sub.add_parser("check")
    for option in ["run", "candidate"]:
        cmd.add_argument("--" + option, required=True)
    cmd.add_argument("--reviews")
    cmd.add_argument("--packet", help="Validated writer packet required for cross-language candidates")
    cmd.add_argument("--output")
    cmd = sub.add_parser("export")
    for option in ["run", "candidate", "output"]:
        cmd.add_argument("--" + option, required=True)
    cmd.add_argument("--packet", help="Validated writer packet required for cross-language candidates")
    args = parser.parse_args(argv)
    try:
        result = {"prepare": prepare, "packet": packet, "check": check, "export": export}[args.command](args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (Block, OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError, zipfile.BadZipFile, ET.ParseError, re.error) as exc:
        print(json.dumps({"status": "BLOCK", "reason": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
