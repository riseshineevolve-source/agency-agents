# Interactive Book source graph contract v1

Status: ACTIVE BOUNDED CANDIDATE / PUBLISHED WORLD 01 LEVELS 1–4
Date: 2026-09-30

## Authority and scope

The published 108-page World 01 paperback identified by SHA-256
`adf9d384985ec7ad0fb1d7f9f6c3d46189592a171474c38ee93ac35bb808c549`
is canonical product-copy evidence. The private PDF is not committed. The locked
page evidence at `orchestration/content-sources/world01-level{1,2,3,4}-page-evidence.json`
records visual, block-by-block transcriptions of pages 15–50. The four source
graphs at `orchestration/content-packs/world01/level{1,2,3,4}.en.candidate.json`
are generated from their corresponding ledgers. A validator checks every graph
field against the ledger; with
`--pdf`, it also checks the private binary identity, page count, and each text
field on its claimed PDF page. CI can check the locked ledger and generation,
but cannot independently authenticate the private PDF.

The four packs contain 123 substantive printed content blocks across 36 pages:
Level 1 has 26 blocks on pages 15–22, Level 2 has 32 on pages 23–32,
Level 3 has 30 on pages 33–41, and Level 4 has 35 on pages 42–50. Together
these are four openers, 90 narrative blocks (52 dialogue + 38 system logs),
one printed inventory block, 12 Neuro Console files, eight Quest blocks, four
science blocks, and four secret-code blocks. The repeated `SYSTEM: ONLINE` and `LVL_INDEX`
page furniture, decorative bullets, and artwork are outside the semantic graph.
The page number and printed speaker/system-log labels are retained. This is
100% coverage of Levels 1–4 substantive text blocks, not a digital reproduction
of its page design or artwork.

## Pack shape

`schema_version` and `minimum_runtime_contract` are `1.0.0`. Each envelope has
one `mission_id`, English canonical and supported locale, and a planned but
unavailable Polish locale. `product_id` and `content_pack_id` isolate the book.
`source` records the PDF hash, size, page count, mission page range, and evidence path.
Every node has a language-neutral `node_id`, one-based `sequence`, `node_type`,
optional `subtype` and `speaker_id`, a single `next_id` or terminal `null`, and
provenance with source ID/hash, printed page, and evidence block ID. The
`localized_copy` array holds exactly one English field map per node. Labels,
dialogue, narration, console, quest, and secret-code wording remain exactly as
visually transcribed, including punctuation and the published page-22 quote
asymmetry.

The edge sequence follows the printed visual reading order. It establishes a
display traversal only. Level 4 introduces the source-derived `inventory` node
type solely to preserve the printed `// FILE: INVENTORY / ITEM ACQUIRED` block;
it does not grant or calculate an in-app item. The published Quest prompts and
secret code are text;
the graph adds no scoring, answer checking, puzzle resolution, gates, reward
calculation, account state, entitlement, or backend semantics. There are no
new game mechanics.

## Fail-closed rules

- Unknown envelope/node/provenance/copy fields fail, including hidden access or
  billing fields.
- Every printed block has one node and one English copy record in source order;
  extra or missing nodes/copy fail.
- Type, subtype, speaker, page, source identity, field names, and field values
  must match the locked evidence exactly.
- IDs and next edges form one stable, linear traversal per mission. Reordered or
  branching content fails.
- Unsupported or fabricated localized copy fails. `pl-PL` is planned only.
- A local private-PDF verification is required to claim PDF-authenticated
  provenance; ordinary CI validates the checked-in evidence boundary.

## Legacy boundary

`RSE_INTERACTIVE_BOOK_CONTENT_CONTRACT_V0.md` and the two historical v0
validators/fixtures remain for compatibility and pilot regression. The
`mission-openers.en.candidate.json` pack is an earlier, limited candidate
with three openers. It is not a complete mission and is not merged into this
v1 graph. New real content slices use this v1 source-graph contract until an
explicit contract revision is made.

## Verification

Run `python scripts/build-world01-graph.py <level>` for levels 1, 2, 3, and 4,
`python scripts/validate-interactive-book-graph.py <pack>`, and
`python scripts/test-interactive-book-graph.py`. For private source custody,
run `python scripts/validate-interactive-book-graph.py <pack> --pdf <published-pdf>`
and set `WORLD01_CANONICAL_PDF` when running the tests. The validator uses
`pypdf` only for the private-PDF mode.
