# Happy Makers Detective Academy — pl-PL Segmentation Contract

Status: **PRE-FREEZE PRODUCTION CONTRACT / NO FULL-BOOK TRANSLATION YET**  
Locale: `pl-PL`  
Product: *Happy Makers Detective Academy: The Mystery of Room Zero*  
Purpose: make the English-freeze -> Polish-production handoff deterministic without translating an unfrozen source.

## Gate

Full-book Polish localization starts only after the canonical English master is explicitly frozen. ALL-15 spatial validation is already a prerequisite and must remain green. Until English freeze, this contract, glossary/calibration, validators and bounded synthetic/accepted fixtures may advance; real full-book segment translation may not.

## Core invariant

**Native Polish wording may change. Puzzle truth may not.**

The child must still be the missing detective, the book itself must still function as evidence, the 30 missions must still form one book-long mystery, solved cases may still matter later, the Hint Vault must remain confidence-building, and the Polish edition must feel like a premium detective-series object rather than a worksheet.

## Stable source-segment identity

Every reader-facing English segment entering localization receives an immutable ID before translation:

`HMDA.<mission-or-system>.<surface>.<ordinal>`

Examples of ID shape only:
- `HMDA.SYSTEM.OPENING.001`
- `HMDA.M07.WITNESS.003`
- `HMDA.M07.HINT.002`
- `HMDA.M07.SOLUTION.004`

IDs identify source meaning, not page number. A layout reflow must not silently create a new semantic segment. If English meaning changes after freeze, bump the source revision and invalidate the affected Polish segment for re-review.

Minimum manifest fields:
- `segment_id`
- `source_revision`
- `mission_id` or `SYSTEM`
- `surface_type`
- `risk_class`
- `source_text`
- `protected_tokens`
- `logic_atoms` where applicable
- `recurrence_key` where applicable
- `fit_class`
- `pl_status`

Allowed `pl_status` before translation: `UNTRANSLATED` only.

## Risk classes

### L0 — protected token / non-localizable

Do not translate or mutate unless separately approved:
- immutable IDs;
- coordinates and grid references;
- deterministic adventure aliases unless a documented pronunciation/readability exception is approved;
- Rise.Shine.Evolve.;
- Happy Makers;
- machine/control tokens not intended for readers.

Any L0 mutation is `BLOCK`.

### L1 — logic-locked

Translate conservatively and validate proposition-by-proposition:
- witness statements and clues;
- map instructions;
- answer/verdict statements;
- solution reasoning;
- Hint Vault steps when they encode deduction;
- ROOM / ZONE labels where semantics affect solving;
- callbacks carrying book-long mystery logic.

Every L1 segment requires `logic_atoms`.

### L2 — recurrence-locked microcopy

Translate through the Detective glossary/profile, not stylistic variation:
- Akademia Detektywów;
- TABLICA ZEZNAŃ;
- MAPA ŚLEDZTWA;
- TWOJE ZADANIE;
- ZEZNANIA ŚWIADKÓW;
- SEJF PODPOWIEDZI;
- ZASADA ZERO;
- WERDYKT;
- WSPÓŁRZĘDNA;
- POKÓJ ZERO while its surface lock remains provisional.

A real fit conflict is escalated; it is not solved by silently inventing a synonym.

### L3 — voice / transcreation

Function-first native Polish:
- case hooks;
- Happy Makers banter;
- emotional encouragement;
- dossier flavor text;
- rank flavor;
- marketing-safe in-book recruitment copy.

L3 may move culturally, but may not introduce new clues, remove evidence, spoil callbacks, strengthen claims, or collapse distinct character voices into generic banter.

## Logic-atom contract

For each L1 segment, record only the semantic operators actually present. Typical atoms:
- `IDENTITY(person/object)`
- `ROW(n)`
- `COLUMN(letter)`
- `COORDINATE(cell)`
- `ROOM(name)` / `ZONE(name)`
- `NEGATION(predicate)`
- `EXACTLY(n)` / `AT_LEAST(n)` / `AT_MOST(n)`
- `NORTH_OF(x)` / `SOUTH_OF(x)` / `EAST_OF(x)` / `WEST_OF(x)`
- `ADJACENT_TO(x)` / `DIAGONAL_TO(x)`
- `SAME_ROOM_AS(x)` / `DIFFERENT_ROOM_FROM(x)`
- ordinal/order relation when present;
- answer identity and required reasoning dependency.

The Polish line passes only when the same atom set is preserved. Naturalness never authorizes changing `exactly one` into `one`, `beside` into `same room`, a negation into uncertainty, or a coordinate into an approximate place.

## Segmentation boundaries

Do not split these across independent translation units:
- one clue sentence plus its logically necessary qualifier;
- a name/alias and the predicate that identifies that person;
- a Hint Vault level whose meaning depends on the preceding sentence;
- a solution step whose pronoun would become ambiguous when isolated;
- a callback phrase whose recurrence is intentional.

Do split decorative prose from logic-bearing text when the same visual card contains both. This allows native Polish transcreation without contaminating the clue proposition.

Mission-level production batches remain atomic for QA: one mission may contain many segment IDs, but it cannot be signed off from fragments translated by unrelated passes.

## Gender-neutral child address

Direct reader address must avoid mechanical double forms and unnecessary gender marking.

Prefer:
- imperative verbs (`Sprawdź`, `Zaznacz`, `Porównaj`);
- impersonal recruitment phrasing (`W Akademii brakuje tylko Ciebie`);
- neutral level/badge names (`POZIOM: TEREN` rather than gendered agent titles);
- second-person constructions that are naturally gender-neutral in Polish.

Reject patterns such as `gotowy/gotowa`, `detektyw/detektywka` used as forced direct-address pairs, `zrobiłeś(-aś)` and similar mechanical notation.

Character gender in story/clues remains whatever the source establishes; the neutrality rule applies to the child reader, not to erasing character identity.

## Native-Polish rule

The final Polish segment must sound authored in Polish, not translated from English.

Avoid:
- English noun stacks;
- literal gerund/instruction syntax;
- repeated `Twoim zadaniem jest...` when a direct instruction is more natural;
- stiff schoolbook reasoning (`na podstawie powyższych przesłanek należy...`);
- decorative slang or Poland-specific references added only to make text look localized;
- TikTok/internet imitation that will age quickly.

Logic-first rewrite sequence for L1:
1. write the literal proposition in plain Polish;
2. compare logic atoms to source;
3. rewrite naturally for ages roughly 8–12;
4. compare atoms again;
5. check recurrence terminology;
6. check surface fit without removing meaning.

## Fit classes

Fit class is assigned from the final English surface before Polish generation:

- `F0_FREEFLOW` — paragraph/page can reflow substantially;
- `F1_CARD` — bounded card; line breaks may change, text may not be omitted;
- `F2_LABEL` — compact recurring label; glossary lock + typography first;
- `F3_MAP` — map/diagram label; preserve geometry/readability and exact semantic reference;
- `F4_BADGE` — very compact rank/status surface; use approved short form only;
- `F5_FIXED_ART` — text baked into an asset; requires explicit replacement/render path, never hidden overflow.

Fit resolution order:
1. natural shorter Polish with identical meaning;
2. reflow/line-break adjustment;
3. surface/layout adjustment;
4. only then escalate a glossary conflict.

Never shrink reader-facing type into illegibility and never delete a clue for fit.

## Spoiler / callback handling

Segments connected to Room Zero or the second-use-clue mechanic receive `meta_sensitive: true` in the extraction manifest.

Rules:
- preserve recurrence and ambiguity exactly where intentional;
- do not explain a callback earlier than English source does;
- never insert the protected `CHECK THE OLD MAP` meta content into public marketing or explanatory translator notes;
- translator/editor notes for meta-sensitive segments must remain internal and separate from reader-facing text.

## Recurrence handling

Use `recurrence_key` for phrases whose consistency is part of the product experience, for example Rule Zero, Hint Vault labels, recurring dossier labels, rank names and deliberate callbacks.

When one approved Polish recurrence changes, every segment sharing the same key must be revalidated in one migration. No ad-hoc variation for style.

## Production sequence after English freeze

Executable entry point and exact commands:
[Detective PL execution checkpoint](DETECTIVE_PL_EXECUTION_CHECKPOINT.md).
Current glossary/identity locks are owned by
[engine/terminology.json](engine/terminology.json); older examples in this contract
describe intent rather than a second editable terminology authority.

1. hash/identify the frozen English source and record its revision;
2. extract all reader-facing segments and protected tokens;
3. classify L0-L3 + fit class;
4. assign logic atoms to every L1 segment;
5. validate 100% segmentation coverage before translating;
6. translate in bounded mission-complete batches;
7. run bilingual logic QA + native Polish edit;
8. run deterministic terminology/gender/English-leak regression;
9. render real Polish surfaces and resolve fit without semantic loss;
10. re-run all 15 spatial cases against identical solution truth;
11. whole-book recurrence/voice/spoiler pass;
12. Polish KDP PDF preflight.

## Pre-freeze definition of DONE

This preparation slice is complete when:
- the segmentation ID/risk/fit contracts are durable;
- Detective recurring terms are defined in the profile/calibration corpus;
- gender-neutral reader-address rules are explicit;
- logic atoms cover spatial operators needed by the accepted Detective fixture;
- full-book translation remains blocked until English freeze;
- no real Detective source segment has been translated merely to create activity.

This file does not authorize KDP publication, pricing, cover decisions or full-book Polish production before the English freeze.
