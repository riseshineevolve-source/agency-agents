# Interactive Book Factory — World 01 Levels 1–4 source-graph checkpoint

Date: 2026-09-30
Status: **LEVEL 4 SOURCE-PROVEN CANDIDATE PASS / PR CI GREEN / OWNER INTEGRATION GATE**

## Execution boundary

- Dedicated branch: `codex/interactive-book-world01-level1-graph-20260930`.
- Bootstrap authority: `orchestration/bootstrap/WORLD01_EXECUTION_BOOTSTRAP.md` on current `main`.
- This slice continued the prior Levels 1–3 checkpoint with exactly one next published-source mission: Level 4 / Mission 4, pages 42–50.
- Central `orchestration/brain/PROGRAM_REGISTRY.yml` was restored byte-for-byte from current `main`; this lane does not propose a central RSE priority change.
- No deployment, pricing, backend creation, publication, or main-branch merge was performed.

## Canonical source custody

Canonical published source remains the private 108-page paperback:

- filename: `10 STORIES WORLD 01 FINAL paperback.pdf`
- bytes: `14,523,549`
- custody SHA-256: `adf9d384985ec7ad0fb1d7f9f6c3d46189592a171474c38ee93ac35bb808c549`

For this Level 4 slice, pages 42–50 were visually inspected from the exact Project/Library PDF record with the matching filename, byte size, and page count, with parsed text used only as a cross-check. Raw-byte materialization was unavailable in the current tool surface, so this execution did **not** re-run the optional `--pdf` binary-hash/page-text verifier for Level 4. CI therefore proves the checked-in locked-evidence boundary, not a fresh private-binary hash authentication.

The app derivative `spark-joy-fam/src/data/storyContent.ts`, Git blob
`377463e1853743f82d4d3bca5ce89b6e5b05b210`, remained read-only comparison evidence.

## Level 4 coverage

Level 4 / **The Spy Who Was Bored** is represented by 35 printed blocks across all nine pages 42–50:

| Type | Nodes |
|---|---:|
| opener | 1 |
| dialogue | 15 |
| system log | 11 |
| inventory | 1 |
| Neuro Console | 3 |
| Quest | 2 |
| science | 1 |
| secret code | 1 |
| **Total** | **35** |

Page inventory is exactly: 42:1, 43:5, 44:5, 45:6, 46:6, 47:5, 48:3, 49:3, 50:1.

The page-47 `// FILE: INVENTORY / ITEM ACQUIRED` block required one reusable contract extension: source-derived node type `inventory`. It preserves the printed block only. It adds no item grant, reward, scoring, unlock, entitlement, or other game/runtime mechanic.

Durable artifacts:

- `orchestration/content-sources/world01-level4-page-evidence.json`
- `orchestration/content-packs/world01/level4.en.candidate.json`
- `orchestration/content-sources/WORLD01_LEVEL4_APP_DIVERGENCES_2026-09-30.md`
- `orchestration/architecture/RSE_INTERACTIVE_BOOK_CONTENT_GRAPH_V1.md`
- `scripts/build-world01-graph.py`
- `scripts/validate-interactive-book-graph.py`
- `scripts/test-interactive-book-graph.py`
- `.github/workflows/interactive-book-contract.yml`

## Printed source vs app derivative

Material Level 4 derivative divergences were documented and excluded from canonical copy, including:

- app-only subtitle;
- merged/reordered page-43 system logs;
- missing `Dilo sat up straighter.` on page 45;
- abridged Alio dialogue on page 45;
- three omitted page-46 printed system logs;
- page-47 dialogue/log order drift;
- flattened inventory semantics;
- app em dash where print uses a hyphen on page 48;
- stripped printed quotation marks on page 50.

No app-only copy entered the source graph.

## Deterministic verification

Draft PR: **#16 — World 01 source graph through Level 4**

PR merge test checkout: `dbce19d9944513ea1bfd71c84bb60b0bff05bfab`.

Interactive Book Contract run **36745982903**: **PASS**.

The CI job:

- passed the legacy synthetic v0 fixture and 12 fail-closed classes;
- passed the bounded opener provenance candidate and 12 provenance/parity mutations;
- rebuilt Levels 1, 2, 3, and 4 and found zero generated drift;
- validated Level 1: 26 nodes, pages 15–22;
- validated Level 2: 32 nodes, pages 23–32;
- validated Level 3: 30 nodes, pages 33–41;
- validated Level 4: 35 nodes, pages 42–50, including one `inventory` node;
- ran **41 graph tests: OK, 4 skipped**. The four skips are the private-PDF tamper tests, intentionally unavailable in CI.

All PR workflows observed for the checkpoint head completed successfully:

- Interactive Book Contract;
- RSE Technical Orchestrator validation;
- RSE portfolio guardrails;
- RSE AI Agency validation;
- Check Runbooks Consistency;
- Check Hermes Config Rewrite;
- Check Divisions Consistency;
- Check Tools Consistency;
- Test Installer.

## Cumulative graph state

Levels 1–4 now cover published pages 15–50: **123 substantive nodes across 36 pages**.

Cumulative types:

- 4 openers;
- 52 dialogue blocks;
- 38 system logs;
- 1 inventory block;
- 12 Neuro Console files;
- 8 Quest blocks;
- 4 science blocks;
- 4 secret-code blocks.

English is source-proven. `pl-PL` remains planned but unsupported.

## Real owner gate

The bounded source slice is closed and green. The remaining integration action is an owner/central decision on **draft PR #16**: merge/reconcile this delegated World 01 source-graph lane into current `main`, or keep it isolated for further delegated source extraction.

No merge is performed automatically because it crosses from the delegated execution lane into central durable truth. No product conversion/deployment/backend/pricing/publication action is authorized by this checkpoint.
