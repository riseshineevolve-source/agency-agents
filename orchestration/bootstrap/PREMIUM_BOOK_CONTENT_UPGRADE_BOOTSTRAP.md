# RSE Premium Book Content Upgrade — New-Chat Execution Bootstrap

Status: CANONICAL BOOTSTRAP CANDIDATE  
Date: 2026-10-05  
Scope: manuscript/content creation and premium upgrading before FROZEN_CONTENT.

## Purpose

Use this bootstrap when a new chat starts with an initial manuscript and the owner wants either:

- **ROUTE A — SAME_LANGUAGE_PREMIUM_UPGRADE**  
  Improve and upgrade the book in its current/target language.

- **ROUTE B — CROSS_LANGUAGE_NATIVE_REAUTHORING**  
  Use the original-language manuscript as source authority for content, function, facts, mechanics and story truth, but create the target-language edition from scratch as native writing. This is NOT literal or sentence-by-sentence translation.

This bootstrap is designed so the new chat does not need access to an earlier conversation.

## Source of truth

GitHub is source of truth once durable state exists.

Repository:
`riseshineevolve-source/agency-agents`

Read in this order:

1. `orchestration/architecture/RSE_PREMIUM_BOOK_CONTENT_UPGRADE_PROTOCOL_V1.md`
2. `strategy/runbooks/scenario-premium-book-content-upgrade.md`
3. `orchestration/architecture/RSE_BOOK_AGENT_V3.md`
4. `orchestration/architecture/RSE_BOOK_MAP_CONTRACT_V1.md`
5. project-specific canonical source/voice/mechanics/owner-lock files if they already exist.

Later durable GitHub state beats chat memory.

## Required owner input at the start

The user should upload the initial/base manuscript file(s) and provide:

1. **Target language**
2. **Book character/type**
3. **Target audience / age range**
4. **Desired style / voice / register**
5. **Route**
   - A = SAME_LANGUAGE_PREMIUM_UPGRADE
   - B = CROSS_LANGUAGE_NATIVE_REAUTHORING

Strongly useful optional input:
- title/brand direction;
- examples of passages/style the owner likes;
- passages or patterns the owner dislikes;
- non-negotiable characters/facts/mechanics/terms;
- other near-final versions or corrected files;
- what is already owner-approved;
- intended publication surface/trim if known.

Do not block ordinary work merely because optional fields are missing. Mark non-critical inferred values as provisional. Stop only for genuine owner decisions that materially affect meaning, brand, legal status, safety or product identity.

## First-run actions

Before substantive rewriting:

1. Verify repository and current main state.
2. Create/use one dedicated non-main working branch for this book/content lane.
3. Establish one-writer-per-surface ownership.
4. Save/hash the uploaded source into durable project truth before editing.
5. Inventory every existing manuscript/version if more than one exists.
6. Build SOURCE_VERSION_INVENTORY.
7. Run source convergence/best-of comparison.
8. Build GOLDEN_KEEP_REGISTRY for already approved or demonstrably stronger fragments.
9. Create immutable baseline + separate WORKING_MASTER.
10. Record TARGET_LANGUAGE_AND_STYLE_PROFILE and selected Route A/B.
11. Build stable segment IDs and CONTENT_MAP.
12. Extract IMMUTABLE_FACTS / mechanics / glossary / character voice.
13. Run one full diagnostic audit without rewriting everything.
14. Create ISSUE_LEDGER with KEEP / FIX / BLOCK / OWNER_GATE.
15. Choose the highest-value bounded slice and begin surgical execution.

## Route A contract — same-language premium upgrade

Work directly in the target language.

Improve:
- reader experience;
- naturalness;
- premium written register;
- structure/arc;
- repetition/function distribution;
- logic/continuity;
- mechanics;
- safety/consent;
- age fit;
- humor;
- character voice;
- clarity;
- proof.

Preserve:
- immutable facts;
- mechanics/puzzle truth unless a documented defect explicitly authorizes change;
- safety/consent;
- already strong and owner-approved text;
- current voice locks;
- valid recurring terminology.

Do not rewrite strong text for novelty.

## Route B contract — cross-language native re-authoring

The source-language manuscript is authority for:
- meaning;
- function;
- facts;
- chronology;
- character roles;
- activity/puzzle mechanics;
- safety/consent;
- claim strength;
- product promises;
- required structure unless explicitly reopened.

It is NOT wording authority.

Mandatory order:

1. Source Function Analyst reads source.
2. Produce wording-free functional brief by stable segment ID.
3. Create target-language writer packet without sentence-level source wording.
4. Native target-language writer authors from function, reader, culture and style.
5. Native Usage/Idiom/Natural Language review.
6. Premium Book Register review.
7. Audience/Family Ear / age-fit review.
8. Cultural Localizer where cultural distance exists.
9. Transcreator only where humor/emotional mechanism requires it.
10. Logic/continuity review.
11. Mechanics/instruction/puzzle/safety review.
12. Reopen original source.
13. Meaning Guardian + Bilingual QA compare function/truth.
14. Proofreader last.

Never "fix" a native target sentence merely to make it look structurally parallel to the source.

Legal/privacy/regulatory passages do not use creative re-authoring.

## Multi-agent collaboration law

Many agents may review. One writer patches.

Reviewers first return independent:
- KEEP
- FIX
- BLOCK
- OWNER_GATE

They provide evidence and targeted suggestions.

They do not serially rewrite the whole manuscript.

The orchestrator/editor-in-chief:
- synthesizes reviews;
- protects locks;
- decides what is actually worth changing;
- declares exact segment allowlist;
- routes one writer;
- validates diff;
- advances baseline only after PASS.

One canonical master has one writer at a time.

## Surgical change-control law

Before every meaningful patch:
- durable base snapshot;
- base hash;
- exact allowed_changed_segments;
- protected regions;
- expected dependency closure.

After patch:
- compute actual changed segments;
- compare with allowlist;
- compare protected hashes;
- run relevant regression tests;
- fail closed on collateral drift.

Do not re-review the entire book after a local patch.

Re-review:
- changed segment;
- explicit dependency/neighbor closure;
- global invariants.

Full-book reads happen only at milestone gates.

## Regression law

Regression tests protect accepted intent, logic, mechanics and owner locks.

If CI protects stale weaker wording:
- determine whether content or test is wrong;
- do not revert a genuine improvement just to make CI green;
- update the test only after the new version is explicitly validated and checkpointed.

## Milestone full-book review

Run full reader/arc audit:
1. after initial diagnostic;
2. after major structural/function-distribution changes;
3. before OWNER_READ_CANDIDATE;
4. before final freeze.

Audit as a reader:
- opening;
- pacing;
- middle-book sag;
- repetition of function;
- logic;
- clarity;
- emotional load;
- humor;
- voice distribution;
- ending;
- payoff;
- age fit;
- usability.

Findings enter ISSUE_LEDGER first. They do not trigger automatic rewrite.

## Finalization ladder

Use explicit states:

DRAFT
-> PREMIUM_WORKING
-> OWNER_READ_CANDIDATE
-> CONTENT_APPROVED
-> FROZEN_CONTENT
-> PRINT_READY
-> RELEASE_AUTHORIZED

Never collapse these states.

OWNER_READ_CANDIDATE:
- substantive content defects closed;
- exact candidate hash;
- full multi-agent QA;
- clean owner-read PDF from exact candidate.

CONTENT_APPROVED:
- owner accepts the exact candidate and owner-only content decisions.

FROZEN_CONTENT:
- create CONTENT_FREEZE_MANIFEST;
- hash-lock content;
- renderer/layout/assets may not rewrite copy.

PRINT_READY:
- exact frozen content passes real-template fit, render/preflight, target-platform preview and required physical proof.

RELEASE_AUTHORIZED:
- explicit owner authorization to publish/release.

## Final handoff to Book Agent

Only after FROZEN_CONTENT:

FROZEN_CONTENT
-> BOOK_MAP
-> LOCK GRAPH
-> TEMPLATES / ASSET SLOTS
-> DETERMINISTIC PAGE BUILD
-> QA
-> PRINT/PREVIEWER PROOF
-> PRINT_READY
-> RELEASE_AUTHORIZED

If layout does not fit, Book Agent raises an exception.
It does not silently rewrite frozen text.

## Required reporting after each bounded run

Report only durable truth:
- exact branch/HEAD;
- working master path/hash;
- base snapshot;
- changed segment IDs;
- why they changed;
- reviewer roles used;
- regression/CI state;
- what remains;
- exact owner gate, if any.

Never claim PASS for a check that did not run.

## Stop conditions

Do not stop for ordinary editorial decisions resolved by the protocol.

Stop only when:
- genuine owner brand/taste decision is required;
- changing meaning/mechanics/safety requires owner decision;
- legal/compliance gate;
- source ambiguity cannot be resolved from canonical material;
- publication/print/release authorization;
- required external/physical proof.

If a full audit finds no substantive defect:
stop rewriting and move to owner-read/freeze.

## Central RSE safety

Do not:
- mutate central RSE priorities;
- merge main without authorization;
- publish;
- claim print/KDP readiness without real proof;
- start a competing writer lane;
- bypass failed durable writes;
- use chat memory as source of truth after GitHub state exists.
