# Scenario: Premium Book Content Upgrade

## Trigger

Use whenever an RSE book/manuscript exists but its content is not yet explicitly owner-approved and hash-locked as FROZEN_CONTENT.

Applies to:
- new manuscripts;
- revised editions;
- translated/localized editions;
- activity books;
- family calendars;
- workbooks;
- puzzle books;
- narrative books;
- substantial copy upgrades before KDP/app production.

## Mandatory authority

Read first:
1. `orchestration/architecture/RSE_PREMIUM_BOOK_CONTENT_UPGRADE_PROTOCOL_V1.md`
2. `orchestration/architecture/RSE_BOOK_AGENT_V3.md`
3. project-specific source/voice/mechanics locks.

## Goal

Turn the current manuscript into one premium, native, coherent, mechanically correct, regression-protected content master and freeze it before page production.

## Operating law

- durable source beats chat memory;
- KEEP beats rewrite;
- many reviewers, one controlled writer;
- edit by stable segment ID;
- every patch has a base snapshot and allowlist;
- unscoped drift fails closed;
- facts/mechanics/safety/consent cannot be traded for style or fit;
- local edit -> local review + global invariants;
- full-book reread only at milestone gates;
- production never rewrites FROZEN_CONTENT.

## Execution loop

1. Freeze source/baseline and hashes.
2. Build/update Content Map and immutable truth.
3. Run one full diagnostic audit.
4. Convert findings into Issue Ledger with KEEP/FIX/BLOCK/OWNER_GATE.
5. Select the highest-value bounded slice.
6. Declare exact editable segment IDs and expected dependencies.
7. Run relevant independent specialist reviewers.
8. Orchestrator synthesizes decisions.
9. One writer applies the smallest accepted patch.
10. Run isolation diff + regression tests.
11. Review changed scope plus declared neighbors only.
12. Checkpoint only after PASS.
13. Repeat until no substantive FIX/BLOCK remains.
14. Run milestone whole-book arc audit.
15. Create exact-hash owner-read candidate and review PDF.
16. Perform real-surface fit without deleting protected meaning.
17. Resolve/isolate owner gates.
18. Create CONTENT_FREEZE_MANIFEST and set FROZEN_CONTENT.
19. Hand frozen hashes to Book Agent v3 / BOOK_MAP.

## Required specialist routing

Use only relevant roles for the current issue. Typical pool:
- source/function analyst;
- native-language writer / Book Co-Author;
- family/audience ear reviewer;
- natural language / usage editor;
- book register editor;
- transcreator / character voice reviewer;
- logic/continuity editor;
- activity instruction reviewer / game designer;
- safety/consent reviewer;
- meaning guardian;
- bilingual QA where applicable;
- proofreader last.

Do not chain agents as successive whole-document rewriters.

## Stop condition

Stop creative editing when a full audit finds no substantive defect and remaining items are owner decisions, real-surface/physical proof, freeze or publication gates.

Do not manufacture additional rewrites after the manuscript is excellent.

## Required final artifacts

- premium master;
- Content Map;
- immutable facts/voice/glossary locks;
- Issue Ledger with all material defects closed;
- edit guard;
- regression evidence;
- multi-agent QA receipt;
- owner-read candidate + PDF;
- real-surface fit report;
- CONTENT_FREEZE_MANIFEST;
- final frozen content hash.

Only then continue into deterministic book production.
