# Interactive Book Factory — World 01 published-source graph checkpoint

Date: 2026-09-30
Status: LOCAL SOURCE-PROVEN CANDIDATE PASS / REMOTE CI PENDING AT CHECKPOINT

## Branch and custody

- Execution branch: `codex/interactive-book-world01-level1-graph-20260930`
- Isolated checkout: dedicated Git worktree, not the historical pilot checkout.
- Current-main base fetched for this run: `6beda0188c3dcca897cbf2468c995b356260e112`.
- Historical pilot source: `codex/interactive-book-world01-pilot` at `7795e6933c39f4f126666ad712c690ccd418f048`.
- Pilot files were ported as commit `0ab47536fb47f6d34a8d162f26a1fb3a82a70ffe`; main's portfolio registry remained the base and only its Interactive Book Factory block was updated afterward.
- Canonical source: private published 108-page World 01 paperback, 14,523,549 bytes, SHA-256 `adf9d384985ec7ad0fb1d7f9f6c3d46189592a171474c38ee93ac35bb808c549`.
- `spark-joy-fam/src/data/storyContent.ts` Git blob `377463e1853743f82d4d3bca5ce89b6e5b05b210` was read-only comparison evidence.

## Contract and coverage

The active bounded contract is `orchestration/architecture/RSE_INTERACTIVE_BOOK_CONTENT_GRAPH_V1.md`. The older v0 validators, synthetic fixtures, and three-opener pilot remain labeled legacy and continue to pass. The v1 candidate has three independent English source graphs, with Polish planned but unavailable. Every substantive printed block has a stable language-neutral node ID, source page/block ID, exact printed copy fields, speaker when applicable, and one printed-order successor. Transitions are display traversal only; no new game mechanics or puzzle scoring were inferred.

| Mission | Printed pages | Blocks/nodes | Opener | Narrative dialogue | System logs | Console | Quest | Science | Secret code |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 — The After-School Crash | 15–22 (8/8) | 26/26 | 1 | 10 | 8 | 3 | 2 | 1 | 1 |
| 2 — The Ice Cream Tragedy | 23–32 (10/10) | 32/32 | 1 | 15 | 9 | 3 | 2 | 1 | 1 |
| 3 — The Invisible XP | 33–41 (9/9) | 30/30 | 1 | 12 | 10 | 3 | 2 | 1 | 1 |
| **Total** | **15–41 (27/27)** | **88/88** | **3** | **37** | **27** | **9** | **6** | **3** | **3** |

These counts cover substantive text blocks, including printed headings, speaker labels, system-log labels, and instructional labels. Repeated page furniture (`SYSTEM: ONLINE`, `LVL_INDEX`), decorative marks, and artwork remain outside the semantic graph. This is not a page-design or artwork parity certificate.

## Source and derivative findings

The private PDF was rendered page by page and cross-checked against text extraction. The v1 validator checks pack fields against locked page evidence and, in private-PDF mode, checks binary identity, page count, and each field's claimed page. Level 2 has three documented extraction-order anomalies where fragment checks reconstruct the visually verified field. The app derivative has material omissions, speaker changes, block splits/merges, order changes, app-only subtitle/glitch copy, and stripped punctuation. Detailed dispositions are in `orchestration/content-sources/WORLD01_LEVEL1_APP_DIVERGENCES_2026-09-30.md` and `WORLD01_LEVEL2_3_APP_DIVERGENCES_2026-09-30.md`. No app-only copy entered the graph.

## Verification

- All three candidate packs validate with the private canonical PDF.
- 31 graph tests pass locally, including positive coverage and negative copy, speaker, order, page, source-hash, locale, hidden-field, and transition cases; private-PDF tamper cases run locally.
- Historical synthetic/v0 validator, 12 v0 negative cases, pilot candidate/provenance verifier, and 12 pilot provenance mutation cases pass locally.
- The updated GitHub workflow rebuilds the three packs, rejects generated drift, validates all three against locked evidence, and runs the 31-case graph suite. Private-PDF checks are local because the PDF is not committed to CI.

## Boundaries and next slice

No deployment, backend, pricing, merge to main, or publication was performed. No Polish copy is marked ready. The next source slice is World 01 Level 4, published pages 42–50, beginning with its opener and continuing through printed narrative, console, Quest, and secret-code blocks under the same source-graph gate.
