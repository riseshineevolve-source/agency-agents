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

Start from:
`orchestration/bootstrap/PREMIUM_BOOK_CONTENT_UPGRADE_BOOTSTRAP.md`

Then read:
1. `orchestration/architecture/RSE_PREMIUM_BOOK_CONTENT_UPGRADE_PROTOCOL_V1.md`
2. `orchestration/architecture/RSE_BOOK_AGENT_V3.md`
3. `orchestration/architecture/RSE_BOOK_MAP_CONTRACT_V1.md`
4. project-specific source/voice/mechanics locks.

The paste-ready new-chat template is:
`orchestration/templates/RSE_PREMIUM_BOOK_UPGRADE_NEW_CHAT_PROMPT.md`.

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

## Intake and route selection

At the start the owner uploads the base manuscript and specifies:
- target language;
- book character/type;
- target audience/age;
- desired style/voice/register;
- Route A SAME_LANGUAGE_PREMIUM_UPGRADE or Route B CROSS_LANGUAGE_NATIVE_REAUTHORING.

If multiple existing versions are provided or found, source convergence + GOLDEN_KEEP happens before new writing.

## Execution loop

1. Select and record Route A/B.
2. Inventory/converge all source versions and preserve GOLDEN_KEEP.
3. Freeze source/baseline and hashes.
4. Build/update Content Map and immutable truth.
5. Run one full diagnostic audit.
6. Convert findings into Issue Ledger with KEEP/FIX/BLOCK/OWNER_GATE.
7. Select the highest-value bounded slice.
8. Declare exact editable segment IDs and expected dependencies.
9. Run relevant independent specialist reviewers.
10. Orchestrator synthesizes decisions.
11. One writer applies the smallest accepted patch.
12. Run isolation diff + regression tests.
13. Review changed scope plus declared neighbors only.
14. Checkpoint only after PASS.
15. Repeat until no substantive FIX/BLOCK remains.
16. Run milestone whole-book arc audit.
17. Create exact-hash owner-read candidate and review PDF.
18. Owner content review -> CONTENT_APPROVED.
19. Perform exact-hash real-surface fit without deleting protected meaning.
20. Resolve/isolate owner gates.
21. Create CONTENT_FREEZE_MANIFEST and set FROZEN_CONTENT.
22. Hand frozen hashes to Book Agent v3 / BOOK_MAP.
23. Keep PRINT_READY and RELEASE_AUTHORIZED as later distinct production/owner states.

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
- target-language/style profile + route;
- source-version inventory/convergence report when applicable;
- GOLDEN_KEEP registry;
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
