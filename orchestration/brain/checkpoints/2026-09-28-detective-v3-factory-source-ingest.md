# Detective Academy V3 — Book Factory Source Ingest Checkpoint

Date: 2026-09-28  
Owner directive: V3 final text is authorized for production integration; English is **NOT FROZEN**.

## Canonical text authority

- Source: `orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`
- Final-text commit: `6c2e21a24d760218923cfd8d47655a3cbf72c575`
- Git blob: `f6e16e99084562ddf56825ccc7bfdd12baad0656`
- Version family remains **V3**. Do not create V4 for this integration.

## Durable factory progress

Repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`  
Branch: `feature/detective-book-factory`

The exact canonical V3 text is now stored byte-for-byte in the factory:

`tools/detective-book-factory/content/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Commits:
- `9a67c95451450f38cf56cec6a3ed154153db23bd` — exact V3 source ingest;
- `02e9ad7d5fde98980f77730dbc3a2e5a0d724dfe` — fail-closed V3 source verifier;
- `03ca0eebc9137ee74dca12e3b836b230aeffe477` — verifier aligned to canonical Case 21 arrow notation;
- `337e9d7caf3fee4e8cba92dc9f53c213668a648d` — branch-local ingest checkpoint;
- `ccb8e43ee21692d5ac1f013f17aabc26dc554bfd` — lossless machine-readable V3 final-text contract builder.

Direct branch read verifies the ingested factory file has Git blob
`f6e16e99084562ddf56825ccc7bfdd12baad0656`, exactly matching the owner-authorized source.

## Verified V3 source invariants

Bounded source verification confirms:
- 30 main cases in order;
- 30 Hint Vault entries at each of Levels 1, 2 and 3;
- 30 Solution Files;
- Case 03 exact-ten contract;
- Case 05 six-symbol answer `BALL -> STAR -> BOLT -> HEART -> KEY -> MOON`;
- Case 21 `B → D → A → C` and `THE ANSWER IS IN WHAT YOU LEAVE EMPTY`;
- Case 26 extraction set exactly Cases 02, 04, 06, 07, 10, 12, 13, 15, 17, 19, 20, 22, 23 and 25;
- Case 01 excluded from the Case 26 extraction set;
- Case 01 support copy uses QUILL / MORSE / PIP / KNOX;
- Rule Zero remains `ZERO ASSUMPTIONS. NOTICE FIRST. THEORIZE SECOND.`;
- Case 29 access coordinate remains `D3`;
- Book 2 hook remains `ARCHIVE FILE 001 // STILL OPEN`.

## Current factory verification

At factory head `ccb8e43ee21692d5ac1f013f17aabc26dc554bfd`:
- Build Detective Academy PDF run #181 / `36443670848`: **PASS**
- SEO Validation run #734 / `36443670874`: **PASS**

These runs prove the source-ingest commits do not break the existing historical
factory pipeline. They do **not** prove that historical V4/V4.1 reader copy has
been replaced in rendered output.

## Renderer integration findings

The historical renderer still contains production-incompatible assumptions for
the current V3 authority, including:
- a hard-coded four-slot Case 05 code renderer;
- historical Case 03 three-difference fallback surfaces;
- early reader-facing Field Slot 06 / "Detective Six" presentation in historical layers;
- fixed 145/146-page assumptions in V4.1 finalization.

Those surfaces must be adapted or bypassed by the V3 production integration.
Do not force V3 back into the old fixed page count.

The current historical V4.1 owner-visual gate also names three assets in code,
while the central production contract requires the exact four-file packet:
`case03_photo_A.png`, `case03_photo_B.png`, `case03_solution.png`,
`book2_archive_photo.png`.

## Write/tool gate encountered

A direct workflow edit to run the new V3 verifier in
`.github/workflows/build-detective-book.yml`, and subsequent bounded attempts
to wire V3 into existing renderer source, were blocked before mutation by the
GitHub/OpenAI write-safety gate. No workflow or existing renderer file was
silently changed.

## Next safe slice

1. Wire the lossless V3 text contract into a V3 production renderer path without
   restoring historical V4/V4.1 reader prose.
2. Generalize Case 05 to six slots/six symbols.
3. Enforce Case 01 reader aliases QUILL / MORSE / PIP / KNOX at the evidence surface.
4. Require the exact four-file owner visual packet and hydrate the locked
   Witness Boards/maps/Case03/archive/finale evidence from source.
5. Run answer-name/clue/coordinate/Case03/Case05/Case26/RoomZero regressions.
6. Render with actual page count, reflow/add pages before cutting approved text.
7. Run deterministic KDP preflight plus full human visual audit.
8. Representative physical proof and explicit owner EN freeze remain mandatory.

No main merge, KDP upload/publication, price change, locked-cover change or EN
freeze is authorized by this checkpoint.
