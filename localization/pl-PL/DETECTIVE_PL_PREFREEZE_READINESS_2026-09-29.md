# Detective Academy pl-PL — V3 pre-freeze readiness

Status: **SOURCE INVENTORIED; EN NOT FROZEN; FULL-BOOK PL TRANSLATION BLOCKED**
Authority for candidate text: `orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md` at Git blob `a85a5941852930f6b88711af26b16ea1651d2fbc` and raw SHA-256 `1af8564985d382f2a6ed3154798e9a4f5e201fa5726ca1478015d774682f5ac0`. This is a **text-only candidate**, not a frozen rendered or composed master. Current-main handoffs describe a 180-page owner-review candidate; page count and print fit are not established by this Markdown inventory.

## Verified candidate inventory

The byte-bound guard verifies 30 ordered reader cases, one six-part apparatus per case, three Hint Vault levels with 30 entries each, 30 Solution Files, and the ordered Case Wall, Room Zero explanation, Field Certification, archive hook and non-reader editorial appendix boundaries. Run:

```sh
python scripts/localization-engine.py detective-v3-guard --receipt localization/pl-PL/engine/detective-freeze.example.json
```

The result `PREFREEZE_SOURCE_VERIFIED` proves only bytes and structural coverage. It does not establish reader-facing completeness of hydrated evidence, puzzle solvability, semantic translation quality, real-template fit, physical proof or English freeze. The V3 editorial locks expressly say that locked Witness Boards, map clues, photo evidence and other puzzle payloads are **not** fully re-transcribed in the prose master; the renderer must hydrate exact source/raster elements. The final localization inventory must include those elements, renderer literals, asset labels and actual designed surfaces. Do not use the Markdown headings alone as a full-book extraction manifest.

## Terminology decisions needed from this V3

The canonical `engine/terminology.json` remains the sole approved term source. Existing locks cover `Detective Academy`, `case`, `case file`, `Your Objective`, `Evidence`, `Your Verdict`, `Hint Vault`, `Rule Zero`, `coordinate`, `Witness Board` and the zero-assumptions motto. `Room Zero` and rank wording remain **provisional**. V3 introduces or materially changes the following reader-visible surfaces, which require owner/editor review and measured fit before being added as locked Polish terms:

| V3 source surface | Current decision required |
| --- | --- |
| `Recruit Credential`, `Official Call Sign`, `Field Certification`, `Certified Field Detective` | Distinguish the intake card, child-selected call sign and earned final certificate. Existing `Detective Certificate` wording does not silently cover all four. |
| `Case Wall`, `CASE WALL -> PAGE 9`, its four zones | Approve one recurring wall label and four zone labels; preserve the instruction that only explicit save prompts go there. Page 9 is layout-dependent after freeze. |
| `Investigation Rules`, `Happy Makers Chat`, `Puzzle / Evidence Surface`, `Make the Call` | Lock the final six-part case rhythm alongside existing `case file`, `Your Objective` and `Your Verdict`; do not infer a synonym from older calibration labels. |
| `Solution Files`, `WHY IT MATTERS`, three Hint Vault level labels, `STOP // HINT VAULT` | Keep hints, answer files, dividers and payoff notes distinct; review compact fit on real back-of-book surfaces. |
| `Archive File 001`, `Black Envelope`, plain `0` mark, `Rule Zero` | Preserve distinct narrative roles and timing. The mark is a route tag, not a fabricated clue or a reason for the incidents. |
| `FOLLOW THE EVIDENCE. DO NOT GUESS.` | V3 differs from the currently locked `DON'T GUESS` wording; resolve the English/Polish recurrence intentionally after freeze, without changing the current lock now. |

No target wording is accepted by this inventory. Do not auto-accept provisional ranks, `Room Zero` or any new heading merely because a candidate phrase appears in V3.

## Segmentation and truth requirements

- Use stable `HMDA.<mission-or-system>.<surface>.<ordinal>` IDs tied to frozen source meaning, never page numbers. Inventory front matter, 30 main cases, Room Zero interludes, explanation, certification, archive hook, 90 hint entries, 30 solutions and all reader-visible hydrated/raster/renderer text. Keep editorial appendices internal and explicitly excluded with reasons.
- For every case, keep the six-part case rhythm and one mission-complete QA batch. Separate decorative voice from logic-bearing evidence, while keeping each clue with its qualifier and each solution dependency with its antecedent. The `CASE WALL -> PAGE 9` instruction and later retrieval form one recurrence chain.
- Mark Room Zero, Rule Zero, the 0 mark, the Case 21 note/handwriting, Case 25 parcel-to-overlay payoff, Case 27 old-plan anchor/margin note, Case 28 damaged rule and A–F sort, Case 29 empty-room message and Case 30 four-field finale as `meta_sensitive`. Preserve the difference between `ROOM` and `ZONE`, exact coordinates, witness identity, order, counts, negation and answer names.
- Keep hint levels and Solution Files separate from ordinary reader case pages. Ordinary verdicts stay unconfirmed in the main story; the explanation and final closure occur only at their earned points. Internal translator notes may contain spoiler logic; reader/marketing copy may not expose it early.
- Resolve the V3 editorial appendix's remaining references to `upside-down` Hint Vault/Solution Files against the current-main final microfix handoff's **upright** production direction before freezing the render contract. No Polish layout orientation decision follows from this text-only inventory.
- Classify F0–F5 from the **final English designed surfaces**. Missing measurements remain review items. Preserve protected IDs and source/raster assets. Re-run the ALL-15 spatial truth check after localized hydration and render; the text guard is not a puzzle solver.

## Owner freeze and source receipt

The tracked [V3 receipt template](engine/detective-freeze.example.json) records candidate Git blob and raw SHA-256, but keeps owner instruction, final structured source hash, ALL-15 evidence and alias hash **PENDING**. Copy it to a private receipt only after the owner explicitly says `FREEZE EN INTERIOR`. Record the actual owner evidence, final source revision, raw SHA-256 of the frozen Book Factory composed source, ALL-15 PASS evidence and canonical alias digest. Then run:

```sh
python scripts/localization-engine.py detective-v3-guard --receipt PRIVATE_FREEZE_RECEIPT.json --frozen-source PRIVATE_FROZEN_MASTER.yml --aliases PRIVATE_FROZEN_RUNTIME.json
python scripts/localization-engine.py detective-prepare --source PRIVATE_FROZEN_MASTER.yml --freeze PRIVATE_FREEZE_RECEIPT.json --aliases PRIVATE_FROZEN_RUNTIME.json --output build/detective-pl/source-plan.json
```

The first command fails if the canonical V3 bytes, case/hint/solution structure, final structured source bytes, owner evidence, ALL-15 evidence or alias snapshot differ from the receipt. The second runs the existing Book Factory YAML schema guard and generates an **untranslated** source plan. Before `extract`, reconcile the frozen composed source, hydrated assets and renderer literals to the canonical text and extend classification for any new fields; unknown fields block. Only then annotate logic atoms and measured fit, achieve full reader-facing coverage, and start bounded mission-complete PL production under the [execution checkpoint](DETECTIVE_PL_EXECUTION_CHECKPOINT.md). Any owner-frozen text blob other than V3 requires a deliberate receipt/test migration and new review, never a silent source swap.
