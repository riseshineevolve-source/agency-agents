# Scenario: Polish Localization (pl-PL)

## Trigger
Use when the user provides a URL, PDF, manuscript, UI strings or text and asks for a native Polish edition/localization.

## Goal
Produce publication-ready Polish that preserves source truth and function while reading as originally written for Poland.

## Route selection before Phase 0

Choose one of two explicit modes:

### A. Controlled localization/transcreation
Use the existing Phase 0–9 flow when the Polish edition should remain recognisably source-led at sentence/segment level.

### B. Native re-authoring from function
Use when the owner says the Polish product should feel written from scratch for Poland and English should be a reference for function/truth rather than wording.

For Route B:

1. Capture source bytes/revision with `reauthor-init`.
2. Localization Source Function Analyst creates a wording-free `rse-functional-brief-v1`.
3. Generate `reauthor-writer-packet`; the packet must contain no sentence-level English source copy.
4. Polish Native Family Writer writes the first Polish version from the brief only.
5. Polish Cultural Localizer + Polish Transcreator + Polish Family Ear Reviewer + Polish Natural Language Editor improve cultural reality, humor/character, credibility and anti-coaching naturalness.
6. Only then generate `reauthor-backcheck-packet` and re-open the English source for Meaning Guardian/Bilingual QA.
7. Logic, proof and real-surface QA follow.
8. `reauthor-final-gate` returns `READY_FOR_OWNER_GATE` until all product-specific owner decisions are explicitly approved for the exact candidate hash.

Never use Route B for legal/privacy/regulatory text.

## Phase 0: Intake and structure
1. Identify input type and scope.
2. Capture source snapshot/version.
3. Map pages/sections/screens/paragraphs.
4. Assign stable segment IDs.
5. Extract names, terminology, facts, numbers, product claims, character profiles and non-translatable tokens.

Deliverables:
- structure map
- source manifest
- glossary seed
- immutable facts list

## Phase 1: Classification
Classify each segment as factual, educational, narrative, dialogue, humor, pun, marketing, CTA, UI, legal/privacy or SEO.

Flag:
- `transcreation_required`
- `cultural_review_required`
- `legal_review_required`
- `i18n_review_required`
- `narrative_continuity_required`

## Phase 2: Semantic draft
Polish Semantic Translator creates meaning-safe draft and semantic record. Do not optimize for cleverness yet.

## Phase 3: Selective creative localization
Use Polish Transcreator only for segments where literal rendering would lose effect. Use Polish Cultural Localizer only when cultural distance matters.

For narrative/books, invoke Narratologist/Narrative Designer/Book Co-Author only for continuity, voice or story-specific problems.

## Phase 4: Meaning gate
Localization Meaning Guardian compares source and current Polish. Resolve all semantic BLOCK/FIX items before natural-language polish.

## Phase 5: Native Polish edit
Polish Natural Language Editor removes translationese, synthetic phrasing and unnatural rhythm while preserving the semantic lock.

## Phase 6: Logic and continuity
Polish Logic Editor checks flow, references, chronology, callbacks and terminology. For books, include cross-chapter continuity.

## Phase 7: Proof
Polish Proofreader handles grammar, spelling, punctuation and typography only.

## Phase 8: Surface checks
Website/UI:
- labels/buttons fit
- variables/placeholders preserved
- pluralization/declension
- responsive layout pressure
- meta/alt/schema localized
- SEO uses Polish search intent

PDF/book:
- page/block mapping preserved
- headings/callouts/dialogue/exercises/captions accounted for
- layout pressure logged
- no text silently omitted to fit

Legal/privacy:
- creative agents excluded
- legal/compliance review required

## Phase 9: Final bilingual QA
Bilingual Localization QA returns PASS/FIX/BLOCK per reviewed scope.

## Change protocol
Maintain a canonical target. Agents patch by segment ID. Never serially rewrite the whole artifact unless restructuring is explicitly required.

## Website golden test: RSE Learning Hub
Use `https://rise-shine-evolve-learning-hub.com/` as the first integrated test because it contains brand marketing, humor, gaming metaphors, parent/child copy, character copy, UI labels, GIFTS microcopy, SEO material and legal/privacy surfaces.

Before publishing a localized site, crawl/inspect all reachable first-party pages and interactive copy, not only visible homepage paragraphs.

## Definition of done
- source coverage complete
- no semantic drift
- Polish reads natively
- humor/wordplay function preserved where applicable
- cultural references work in Poland
- voice and character continuity stable
- grammar/typography clean
- UI/PDF constraints checked
- SEO localized by Polish intent
- legal copy reviewed on conservative route
- final QA = PASS
