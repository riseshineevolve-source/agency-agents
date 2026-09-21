# Production localization infrastructure

The single terminology authority is [terminology.json](terminology.json). The
top-level accepted terminology document is generated from it. Existing fixture
text remains historical evidence, not a second editable glossary. JSON is UTF-8,
human readable and Git-friendly. All source/target approvals are scoped; no tool
translates new product copy or grants an owner freeze.

Install and verify from the repository root:

```sh
python -m pip install -r scripts/localization/requirements.txt
python scripts/localization-engine.py terms-doc --check
python scripts/test-localization-engine.py
python scripts/test-localization-fixtures.py
```

The fixture command runs the seven original regression fixtures, preserves the
five Detective anchor groups, and produces bilingual packages for existing
Detective, Gentle Steps and Project Unstoppable source/target pairs. Historical
book passages without verbatim English remain target-only regression evidence;
their source coverage is not invented. Outputs go into ignored
`build/localization-proof/`, including one aggregate report, per-product JSON and
Markdown reports, candidate packages and approved language memory. CI stores this
bounded evidence as an artifact. Full private books must stay outside tracked
files and outside public CI artifacts.

## Source and target contract

`inventory` lists every JSON/YAML leaf using RFC 6901 paths. `extract` requires an
explicit plan classifying every source string as localized, protected, or excluded
with a reason. Keys are never translation candidates. Non-string leaves are
protected automatically. Duplicate keys, source paths and segment IDs fail closed.
YAML uses a safe loader; ISO date scalars retain their spelling as strings.
Use string mapping keys; non-string YAML keys require an explicit source-format
conversion before ingestion. This is a structured-source packager, not a PDF OCR
or arbitrary HTML crawler.

```sh
python scripts/localization-engine.py inventory --source source.yml --output build/inventory.json
python scripts/localization-engine.py extract --source source.yml --plan plan.json --revision SOURCE_COMMIT_OR_HASH --output build/product-pl
```

Plan shape (the text already resides in `source.yml`; no target copy is invented):

```json
{
  "version": 1,
  "product": "project-unstoppable",
  "adapter": "app",
  "scope": "bounded",
  "segments": [{
    "id": "PU-HERO-002",
    "source_path": "/store/badge",
    "content_type": "ui",
    "surface_type": "badge",
    "logic_sensitive": false,
    "character_sensitive": false,
    "semantic_risk": true,
    "term_ids": ["ui.coming-soon-google-play"],
    "fit_budget": {"max_chars": 30, "max_lines": 2, "requires_real_surface": true}
  }],
  "protected_paths": ["/store/url", "/store/id"],
  "excluded_paths": {"/internal_note": "Internal production metadata"}
}
```

Each source segment contains product context through its manifest, source file,
revision, exact EN text and SHA-256, stable ID and source path, content/surface
type, explicit logic/name sensitivity, optional fit budget, protected tokens,
terminology references, number mappings and logic atoms. Target records contain
only the stable ID, source text hash, PL text, review status, copied logic atoms,
review evidence and optional reuse provenance. They cannot override source paths,
answers, keys, budgets or protection policy. A source contract hash includes the
complete source document and policy. Hashes detect drift, not malicious forgery.

Allowed surfaces: heading, subtitle, button, badge, clue_card, map_label,
app_control, body_block, callout, cover_copy, back_cover_copy, short_label.
Review states: untranslated, draft, review_required, approved, locked, stale.

For a logic-sensitive segment, supply bilingual atoms using the kinds defined in
`scripts/localization/contracts.py`. Each records `kind`, immutable `value`,
`source_anchor`, and `target_anchor`. Numeric spelling changes such as source `2`
to Polish `drugim` require a narrow `number_mappings` entry with source/target spans
and a rationale. Do not blanket-exempt numbers. Automatic checks compare numeric
and coordinate multiplicity, code strings, protected names/declensions, negation,
declared operators and answer identities, placeholders, markup and links.

Regex and copied atoms do not establish semantic equivalence. Logic, character
and other semantic-risk segments stay in bilingual review. A completed language
review has `status: pass`, a named `reviewer` or durable existing QA reference,
`source_sha256`, `target_sha256`, and `policy_sha256` (from
`segment_policy_hash`). Never stamp this record merely because scripts pass.
Changing text or policy invalidates that review. The approved-fixture importer
only binds reviews already present in the accepted calibration documents.

## QA and surface adapters

```sh
python scripts/localization-engine.py qa --manifest build/product-pl/source-manifest.json --targets build/product-pl/targets.pl-PL.json --output build/product-pl/qa.json
python scripts/localization-engine.py export --manifest build/product-pl/source-manifest.json --targets build/product-pl/targets.pl-PL.json --output build/product-pl/candidate-package.json
```

All five adapters (`book`, `puzzle`, `app`, `web`, `structured`) reconstruct the
original source-shaped payload by replacing only selected values. Book/puzzle
packages retain bilingual records, stable clue IDs, source answer/coordinate
data and fit/risk reports. App exports preserve nested keys and interpolation.
Web exports preserve URLs, anchors and structured metadata while allowing visible
copy to change. A URL migration requires an explicitly revised source contract;
the target payload cannot silently supply a link map. No deployer is provided.

Candidate exports require zero deterministic errors and retain open review items.
`--release` additionally requires all language approvals and a PASS report; it
does not authorize publishing. A pending real-surface requirement blocks release.
Simple braces, mustache, JS interpolation and common printf placeholders are
supported with exact name/type/multiplicity parity. Complex ICU syntax fails
closed for an explicit i18n integration; it is not silently parsed as simple text.

QA reports have one `rse-localization-qa-v1` format, source coverage, untranslated
and stale targets, terminology, tokens, numbers/logic, placeholders, fit risks,
conservative language warnings, semantic review queue and separate deterministic
pass versus approved-language counts. QA exit 1 means BLOCK; exit 0 means the
deterministic checks passed, so inspect the PASS/REVIEW status before promotion.
Language heuristics flag suspicious phrasing without rewriting accepted copy.

## Approved reuse

```sh
python scripts/localization-engine.py tm-build --manifest build/product-pl/source-manifest.json --targets build/product-pl/targets.pl-PL.json --output build/product-pl/memory.json
python scripts/localization-engine.py tm-reuse --manifest build/new-source/source-manifest.json --targets build/new-source/targets.pl-PL.json --memory build/product-pl/memory.json --output build/new-source/reused.pl-PL.json
```

Memory holds only reviewed approved/locked language, keyed by product and stable
segment ID. Exact source text, policy and terminology hashes must match. A new
file revision can reuse an unchanged segment; even a one-character text change
invalidates reuse. Existing edits are retained; stale targets lose approval.
Conflicting entries fail, and every reuse records its prior revision and contract.
There is no fuzzy matching or external SaaS. Store approved memory with its
product's appropriate access controls; generated full manuscripts are private.

## Real-template fit

Character and line budgets detect pressure; they never prove rendered fit.
Approved line-break candidates must preserve words and Polish diacritics. Nothing
automatically shortens copy or shrinks body type. Missing budgets remain review
items. The four Gentle Steps headings and line breaks are in
[gentle-steps-fit.json](gentle-steps-fit.json).

```sh
python scripts/localization-engine.py fit-request --output build/gentle-fit/request.json
python scripts/localization-engine.py fit-proof --evidence REAL_EVIDENCE_DIR/evidence.json --output build/gentle-fit/result.json
```

Without evidence, `fit-proof` returns BLOCK (exit 2). The existing renderer must
render pages 25, 26, 35, 38 on the actual template and write
`rse-real-template-fit-evidence-v1`: request `spec_sha256`, `surface_kind:
actual_template`, `renderer`, `renderer_revision`, `reviewer`, template
`{path, sha256}`, and exactly four `pages`. Each page records `source_pdf_page`,
the exact approved `heading`, its canonical JSON `heading_sha256`, `render:
{path, sha256}`, source/rendered `body_font_pt` and `body_leading_pt`, and `review`
with the rendered file hash plus true `no_clipping`, `no_collisions`,
`diacritics_correct`, `print_scale_reviewed`, `heading_legible`, and
`tracking_acceptable`. Artifact hashes use raw bytes; text/spec hashes use
canonical JSON via `localization.io.digest`. Artifact paths are relative to the
evidence directory and cannot escape it. This verifies evidence integrity and
review completeness; visual truth relies on the named print-scale reviewer.

No actual Gentle Steps renderer is present in this repository. Do not replace it
with an estimated font box or proxy page. The one-command proof verifier is ready;
connecting a genuine renderer is the remaining surface-dependent step.
