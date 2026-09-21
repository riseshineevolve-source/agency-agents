"""Deterministic invariants; language heuristics produce review items, not rewrites."""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
import re
import unicodedata

from .contracts import require, review_valid, validate_manifest, STATUSES
from .io import ContractError, digest

TOKEN_RE = re.compile(r"\$\{[A-Za-z_]\w*\}|\{\{\s*[A-Za-z_]\w*(?:\.\w+)*\s*\}\}|\{(?:[A-Za-z_]\w*|\d+)(?:![rsa])?(?::[^{}]+)?\}|%(?:\d+\$|\([A-Za-z_]\w*\))?[-+#0 ]*\d*(?:\.\d+)?[sdif]", re.UNICODE)
NUMBER_RE = re.compile(r"(?<![\w])\d+(?:[.,]\d+)?(?![\w])")
COORD_RE = re.compile(r"\b[A-Z]{1,2}[1-9][0-9]*\b")
CODE_RE = re.compile(r"`([^`\n]+)`|\b[A-Z]+(?:[_-][A-Z0-9]+)+\b")
URL_RE = re.compile(r"https?://[^\s<>\]\)\"']+|\]\(([^\s)]+)\)")


def norm(text):
    return " ".join(unicodedata.normalize("NFC", text).split()).casefold()


def occurrences(text, phrase):
    return len(re.findall(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", text, re.IGNORECASE))


def placeholders(text):
    tokens = Counter(TOKEN_RE.findall(text))
    residue = TOKEN_RE.sub("", text).replace("%%", "")
    # Complex ICU and unmatched interpolation syntax must go through i18n QA.
    malformed = any(c in residue for c in "{}") or bool(re.search(r"%(?:\d+\$|\([\w]+\)|[A-Za-z])", residue))
    return tokens, malformed


class Markup(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tokens, self.stack, self.invalid = [], [], False

    def handle_starttag(self, tag, attrs):
        # Visible title/alt can translate. All other attributes are structural.
        protected = sorted((k, v) for k, v in attrs if k not in {"title", "alt", "aria-label"})
        self.tokens.append((tag, tuple(protected)))
        if tag not in {"br", "hr", "img", "input", "meta", "link", "wbr", "area", "base", "col", "embed", "param", "source", "track"}:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        previous = len(self.stack)
        self.handle_starttag(tag, attrs)
        self.stack = self.stack[:previous]

    def handle_endtag(self, tag):
        self.tokens.append(("/" + tag, ()))
        if not self.stack or self.stack.pop() != tag:
            self.invalid = True


def markup(text):
    parser = Markup()
    parser.feed(text)
    parser.close()
    # Detect incomplete tags without treating normal comparison operators as HTML.
    dangling = bool(re.search(r"</?[A-Za-z][^>]*$", text))
    return parser.tokens, parser.invalid or bool(parser.stack) or dangling


def links(text):
    return Counter(m.group(1) or m.group(0) for m in URL_RE.finditer(text))


def load_terms(catalog):
    require(catalog.get("version") == 1, "Unsupported terminology catalog")
    ids, keys = {}, {}
    for term in catalog["terms"]:
        tid = term["id"]
        require(tid not in ids, f"Duplicate terminology ID: {tid}")
        require(term.get("state") in {"locked", "provisional", "owner_gate", "contextual"}, f"Unknown term lock: {tid}")
        require(term.get("mode") in {"translate", "never_translate", "transcreation_only", "identity"}, f"Unknown term mode: {tid}")
        require(bool(term.get("source")) and bool(term.get("provenance")) and bool(term.get("rationale")), f"Incomplete terminology traceability: {tid}")
        require(isinstance(term.get("targets"), list), f"Invalid targets: {tid}")
        require(bool(term["targets"]) or term["state"] == "owner_gate", f"Term needs a target: {tid}")
        for scope in term["products"]:
            key = (scope, norm(term["source"]))
            require(key not in keys, f"Conflicting source terminology: {key}")
            keys[key] = term
        ids[tid] = term
    for (scope, source), term in keys.items():
        global_term = keys.get(("*", source))
        if scope != "*" and global_term:
            require(term["targets"] == global_term["targets"], f"Global/product terminology conflict: {term['id']}")
    return ids


def fit_issues(segment, text):
    budget = segment.get("fit_budget")
    if budget is None:
        return [("fit_risks", "review", "No measured fit budget; real surface review remains open")]
    issues = []
    candidates = [text] + budget.get("approved_line_breaks", [])
    for candidate in candidates[1:]:
        if norm(candidate) != norm(text):
            issues.append(("fit_risks", "error", "Approved line break changes text or diacritics"))
    def within(candidate):
        lines = candidate.splitlines() or [""]
        return (("max_chars" not in budget or len(candidate.replace("\n", " ")) <= budget["max_chars"])
                and ("max_lines" not in budget or len(lines) <= budget["max_lines"])
                and ("max_line_chars" not in budget or max(map(len, lines)) <= budget["max_line_chars"]))
    if not any(within(c) for c in candidates if norm(c) == norm(text)):
        issues.append(("fit_risks", "review", "Overflow against declared character/line budget; preserve meaning and body typography"))
    if budget.get("requires_real_surface", True):
        issues.append(("fit_risks", "review", "Real designed surface proof required; character counts cannot close this gate"))
    return issues


def language_issues(text, content_type, phrases):
    issues = []
    for phrase in phrases:
        if norm(phrase) in norm(text):
            issues.append(("translationese_warnings", "review", f"Review contextual language signal: {phrase}"))
    patterns = [
        (r"\b\w+\(-?aś\)|\bgotowy/gotowa\b|\bKapitan\(a\)", "Mechanical gender notation"),
        (r"\b(?:połączenie rodzinne|dzielona pauza|dokona[jć] wyboru|kliknij tutaj, aby)\b", "Possible English calque or stiff UI wording"),
        (r"\b(?:serduszko|chwileczk[aię]|rączk[aię]|zadank[oa])\b", "Check unnecessary diminutive against character voice"),
        (r"\b(?:celebrujcie wspólne chwile|magiczna podróż|wyjątkowa więź)\b", "Check generic warmth against source meaning"),
    ]
    if content_type in {"child_address", "cta", "ui"}:
        patterns.append((r"\b\w+(?:łeś|łaś|łbyś|łabyś)\b", "Gendered direct address; check audience intent"))
    for pattern, message in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(("translationese_warnings", "review", message))
    if unicodedata.normalize("NFC", text) != text:
        issues.append(("translationese_warnings", "review", "Normalize Unicode to NFC while retaining Polish diacritics"))
    return issues


def check_segment(segment, target, catalog, product, phrases):
    issues = []
    def add(category, message, severity="error"):
        issues.append((category, severity, message))
    source, text = segment["source_text"], target["target_text"]
    identity_source = source
    for mapping in segment.get("identity_mappings", []):
        source_count = occurrences(source, mapping["source"])
        target_count = sum(occurrences(text, form) for form in mapping["target_forms"])
        if source_count != target_count:
            add("protected_token_failures", f"Scoped alias identity changed: {mapping['source']}")
        identity_source = re.sub(r"\b" + re.escape(mapping["source"]) + r"\b", lambda _: mapping["target_forms"][0], identity_source, flags=re.I)
    if target.get("source_sha256") != segment["source_sha256"] or target.get("review_status") == "stale":
        add("stale_translations", "Translation references a different source hash or is marked stale")
    if not text.strip():
        add("untranslated_segments", "Target text is missing")
        return issues
    if target.get("review_status") == "untranslated":
        add("untranslated_segments", "Target still has untranslated status")
    matching = []
    for term in catalog.values():
        if product not in term["products"] and "*" not in term["products"]:
            continue
        explicit = term["id"] in segment.get("term_ids", [])
        whole = norm(source) in {norm(term["source"]), *(norm(x) for x in term.get("source_forms", []))}
        embedded = term["mode"] in {"never_translate", "identity"} and any(occurrences(identity_source, form) for form in [term["source"]] + term.get("source_forms", []))
        if term["mode"] in {"never_translate", "identity"} and not embedded and any(occurrences(text, form) for form in term["targets"]):
            add("protected_token_failures", f"Introduced identity/token absent from source: {term['id']}")
        if explicit or whole or embedded:
            matching.append(term)
            if term["state"] != "locked":
                add("terminology_violations", f"Term {term['id']} is {term['state']}; its approval gate remains open", "review")
            if term["targets"] and (whole or explicit) and norm(text) not in {norm(x) for x in term["targets"]}:
                add("terminology_violations", f"Target drifts from canonical term {term['id']}")
            if embedded:
                source_count = sum(occurrences(identity_source, f) for f in [term["source"]] + term.get("source_forms", []))
                target_count = sum(occurrences(text, f) for f in term["targets"])
                if source_count != target_count:
                    add("protected_token_failures", f"Identity/token count changed: {term['id']}")
    for tid in segment.get("term_ids", []):
        if tid not in catalog or catalog[tid] not in matching:
            add("terminology_violations", f"Unknown or out-of-scope term reference: {tid}")
    if norm(source) == norm(text) and not any(t["mode"] in {"never_translate", "identity"} for t in matching):
        add("untranslated_segments", "Target equals source without a protected-term exemption")
    for token in segment["protected_tokens"]:
        if source.count(token) != text.count(token):
            add("protected_token_failures", f"Protected token changed: {token}")
    sp, sm = placeholders(source)
    tp, tm = placeholders(text)
    if sp != tp:
        add("placeholder_parity", "Placeholder names, types or multiplicity changed")
    if sm or tm:
        add("placeholder_parity", "Malformed or unsupported interpolation syntax; explicit i18n review required")
    sh, si = markup(source)
    th, ti = markup(text)
    if sh != th or si or ti or links(source) != links(text):
        add("protected_token_failures", "Malformed/changed links, HTML structure, anchors or protected attributes")
    if re.search(r"\]\([^)]*$", text) or text.count("[") != text.count("]"):
        add("protected_token_failures", "Malformed Markdown link/label delimiters")
    a, b = TOKEN_RE.sub("", source), TOKEN_RE.sub("", text)
    for mapping in segment["number_mappings"]:
        if a.count(mapping["source"]) != b.count(mapping["target"]):
            add("number_coordinate_logic_failures", "Explicit bilingual number mapping changed")
        a, b = a.replace(mapping["source"], ""), b.replace(mapping["target"], "")
    if Counter(NUMBER_RE.findall(a)) != Counter(NUMBER_RE.findall(b)):
        add("number_coordinate_logic_failures", "Numeric values or multiplicity changed (written forms need an explicit mapping)")
    if Counter(COORD_RE.findall(source)) != Counter(COORD_RE.findall(text)):
        add("number_coordinate_logic_failures", "Coordinate/code identity changed")
    if Counter(CODE_RE.findall(source)) != Counter(CODE_RE.findall(text)):
        add("protected_token_failures", "Code strings changed")
    if target.get("logic_atoms", []) != segment["logic_atoms"]:
        add("number_coordinate_logic_failures", "Logic atoms or answer identities changed")
    for atom in segment["logic_atoms"]:
        if norm(atom["target_anchor"]) not in norm(text):
            add("number_coordinate_logic_failures", f"Missing {atom['kind']} anchor for {atom['value']}")
    if segment["logic_sensitive"]:
        en_neg = len(re.findall(r"\b(?:not|never|no|neither|without)\b|n't\b", source, re.I))
        pl_neg = len(re.findall(r"\b(?:nie|nigdy|żaden|żadna|żadne|bez|ani)\b", text, re.I))
        if bool(en_neg) != bool(pl_neg):
            add("number_coordinate_logic_failures", "Negation presence changed; bilingual logic review required")
        # These operators must be explicitly represented even if source/target atom
        # lists happen to agree. Anchors remain bounded lexical checks, not a solver.
        for pattern, kind in [(r"\brow\b", "row"), (r"\bcolumn\b", "column"), (r"\bexactly\b", "exactly"), (r"\bat least\b", "at_least"), (r"\bat most\b", "at_most"), (r"\bbefore\b|\bafter\b", "order"), (r"\bnorth\b", "north_of"), (r"\bsouth\b", "south_of"), (r"\beast\b", "east_of"), (r"\bwest\b", "west_of")]:
            if re.search(pattern, source, re.I) and kind not in {a["kind"] for a in segment["logic_atoms"]}:
                add("number_coordinate_logic_failures", f"Source operator lacks a declared {kind} atom")
    if segment["semantic_risk"] or segment["logic_sensitive"] or segment["character_sensitive"]:
        if not review_valid(segment, target):
            add("semantic_review_queue", "Bilingual QA needed for this exact source, target and policy hash", "review")
    if target.get("review_status") in {"approved", "locked"} and not review_valid(segment, target):
        add("semantic_review_queue", "Approval is absent or stale for current text/policy", "error")
    issues.extend(fit_issues(segment, text))
    issues.extend(language_issues(text, segment["content_type"], phrases))
    return issues


CATEGORIES = ("source_coverage", "untranslated_segments", "stale_translations", "terminology_violations", "protected_token_failures", "number_coordinate_logic_failures", "placeholder_parity", "fit_risks", "translationese_warnings", "semantic_review_queue")


def qa(manifest, targets, terms, phrases=()):
    validate_manifest(manifest)
    catalog = load_terms(terms)
    require(isinstance(targets, dict) and targets.get("version") == 1, "Unsupported target payload")
    issues, by_id = [], {}
    def issue(sid, category, severity, message):
        issues.append({"segment_id": sid, "category": category, "severity": severity, "message": message})
    if targets.get("product") != manifest["product"] or targets.get("contract_sha256") != manifest["contract_sha256"]:
        issue("*", "stale_translations", "error", "Target product/source contract does not match")
    require(isinstance(targets.get("segments"), list), "Target segments must be a list")
    for t in targets["segments"]:
        require(isinstance(t, dict) and isinstance(t.get("id"), str), "Invalid target segment")
        require(isinstance(t.get("target_text"), str) and t.get("review_status") in STATUSES, f"Invalid target text/status: {t['id']}")
        allowed = {"id", "target_text", "source_sha256", "review_status", "logic_atoms", "semantic_review", "reuse_provenance"}
        if set(t) - allowed:
            issue(t["id"], "protected_token_failures", "error", "Target attempts to override source metadata or contains unsupported fields")
        if t["id"] in by_id:
            issue(t["id"], "source_coverage", "error", "Duplicated target/clue ID")
        by_id[t["id"]] = t
    expected = {s["id"] for s in manifest["segments"]}
    for sid in sorted(set(by_id) - expected):
        issue(sid, "source_coverage", "error", "Extra target key/ID")
    passed_ids, approved_ids = set(), set()
    for s in sorted(manifest["segments"], key=lambda s: s["id"]):
        t = by_id.get(s["id"])
        if t is None:
            issue(s["id"], "source_coverage", "error", "Missing target/clue ID")
            continue
        found = check_segment(s, t, catalog, manifest["product"], phrases)
        for category, severity, message in found:
            issue(s["id"], category, severity, message)
        if not any(severity == "error" for _, severity, _ in found):
            passed_ids.add(s["id"])
        if t["review_status"] in {"approved", "locked"} and review_valid(s, t) and not any(sev == "error" for _, sev, _ in found):
            approved_ids.add(s["id"])
    issues.sort(key=lambda i: (i["segment_id"], i["category"], i["message"]))
    errors = sum(i["severity"] == "error" for i in issues)
    reviews = sum(i["severity"] == "review" for i in issues)
    failed_ids = {i["segment_id"] for i in issues if i["severity"] == "error"}
    passed = 0 if "*" in failed_ids else len(passed_ids - failed_ids)
    approved = 0 if "*" in failed_ids else len(approved_ids - failed_ids)
    return {
        "format": "rse-localization-qa-v1", "product": manifest["product"],
        "source_revision": manifest["source_revision"], "contract_sha256": manifest["contract_sha256"],
        "status": "BLOCK" if errors else "REVIEW" if reviews else "PASS",
        "counts": {"source_segments": len(expected), "mapped_segments": len(expected & set(by_id)),
                   "deterministic_pass": passed, "approved_language": approved, "errors": errors, "review_items": reviews},
        "categories": {c: sum(i["category"] == c for i in issues) for c in CATEGORIES}, "issues": issues,
        "limits": "Deterministic gates do not prove semantic equivalence, layout fit, solvability or publication readiness.",
    }


def markdown_report(report):
    lines = ["# Localization QA", "", f"Status: **{report['status']}**", "", "| Metric | Count |", "|---|---:|"]
    for key, value in report["counts"].items():
        lines.append(f"| {key} | {value} |")
    lines += ["", "| Segment | Category | Severity | Detail |", "|---|---|---|---|"]
    for i in report["issues"]:
        lines.append("| " + " | ".join(str(i[k]).replace("|", "\\|").replace("\n", " ") for k in ("segment_id", "category", "severity", "message")) + " |")
    lines += ["", report["limits"], ""]
    return "\n".join(lines)


def aggregate_reports(reports):
    require(bool(reports), "Cannot aggregate an empty QA suite")
    require(all(r.get("format") == "rse-localization-qa-v1" for r in reports), "Mixed/unsupported QA report formats")
    issues = []
    for report in reports:
        for item in report["issues"]:
            issues.append({**item, "segment_id": report.get("fixture", report["product"]) + ":" + item["segment_id"], "product": report["product"]})
    counts = {key: sum(report["counts"][key] for report in reports) for key in reports[0]["counts"]}
    return {"format":"rse-localization-qa-v1", "product":"*", "source_revision":"multiple source snapshots", "contract_sha256":digest([r["contract_sha256"] for r in reports]),
            "status":"BLOCK" if counts["errors"] else "REVIEW" if counts["review_items"] else "PASS", "counts":counts,
            "categories":{c:sum(r["categories"][c] for r in reports) for c in CATEGORIES}, "issues":sorted(issues,key=lambda i:(i["segment_id"],i["category"],i["message"])),
            "reports":reports, "limits":"Aggregate counts cover these supplied scopes only. Deterministic PASS does not prove semantic equivalence or real surface fit."}
