# RSE Premium Book Content Upgrade Protocol v1

Status: CANONICAL ARCHITECTURE CANDIDATE / REQUIRED PRE-FROZEN-CONTENT STAGE  
Date: 2026-10-05  
Owner: Central RSE Technical Orchestrator  
Applies to: every RSE book, workbook, family calendar, activity book, narrative book and book-like fixed/flow content product before FROZEN_CONTENT.

## 0. Purpose

This protocol defines the repeatable RSE process for taking an initial manuscript in any language and upgrading it into a premium final content master without losing meaning, mechanics, safety, character identity, already-strong passages or previously approved work.

It exists to prevent the failure mode where:
- one local fix causes unrelated sections to drift;
- multiple agents serially rewrite one another;
- good copy is lost because every pass starts from scratch;
- a later language edit silently changes logic, numbers, activity rules or safety;
- the whole book must be reread after every tiny change;
- layout pressure causes meaning to be deleted;
- the renderer becomes an accidental copywriter;
- chat memory becomes more authoritative than durable source files.

The governing principle is:

**Improve only what is demonstrably weak. Preserve everything already strong. Change scope must be explicit, reviewable and mechanically enforced.**

The content lifecycle is:

INITIAL MANUSCRIPT
-> SOURCE SNAPSHOT
-> CONTENT MAP
-> IMMUTABLE TRUTH + VOICE LOCKS
-> FULL DIAGNOSTIC AUDIT
-> PRIORITIZED ISSUE LEDGER
-> BOUNDED MULTI-AGENT UPGRADE SLICES
-> REGRESSION + ISOLATION QA
-> FULL-BOOK ARC AUDIT
-> OWNER-READ CANDIDATE
-> REAL-SURFACE FIT
-> FINAL PROOF
-> FROZEN_CONTENT
-> RSE BOOK AGENT / BOOK MAP / PRODUCTION

This protocol ends at FROZEN_CONTENT. The existing RSE Book Agent v3 then owns deterministic page production.

---

# A-Z EXECUTION MAP

## A. Accept the manuscript and define the exact edition

Before anyone edits text, record:
- book ID;
- edition/language;
- source language;
- target language if different;
- audience and age range;
- format: narrative / activity / workbook / calendar / puzzle / hybrid;
- expected reading/playing duration where relevant;
- owner goal for the upgrade;
- current status: raw draft / edited draft / previous edition / translated draft / published edition;
- publication constraints;
- legal or factual risk areas;
- explicit owner gates.

Do not begin with "make it better".
Convert that into measurable editorial goals.

Example goals:
- natural native-language prose;
- premium book register;
- age 8–12 without baby tone;
- sharper character humor;
- fewer repeated activity mechanics;
- zero coaching/mindfulness cliché;
- exact preservation of puzzle truth;
- ten-minute family experience;
- stronger final arc;
- no forced emotional disclosure.

Deliverable:
- CONTENT_UPGRADE_BRIEF.md

## B. Baseline freeze before editing

Create an immutable baseline of the exact manuscript being improved.

Required:
- exact file/path;
- Git blob SHA or SHA-256;
- date/revision;
- source provenance;
- prior owner-approved sections or locked pages;
- known exclusions.

Never edit the only copy.

Create:
- ORIGINAL_BASELINE
- WORKING_MASTER
- CHECKPOINT directory

If a previous accepted version must remain safe, freeze its hash permanently.

Rule:
**Version N is never overwritten to create Version N+1.**

This is the same rule used successfully in Gentle Steps PL: frozen Version 1 remained untouched while Version 2 evolved independently.

## C. Create stable segment IDs

Do not manage a book only as pages or paragraphs.

Every independently reviewable content unit gets a stable ID.

Examples:
- D01.ZWOLNIJ
- D01.GRAMY
- D01.MIEDZY_NAMI
- CH03.SCENE04
- CASE12.CLUE03
- INTRO.PARA07
- HM.DILO.COMMENT.014
- BACKMATTER.LETTER.P02

IDs must survive wording changes.

The segment ID is the unit of:
- review;
- patching;
- hashing;
- QA;
- issue tracking;
- approval;
- change control.

This is what makes local improvements possible without rereading the entire book after every edit.

## D. Decompose the book into a Content Map

Create a machine-readable CONTENT_MAP.json or equivalent table.

Each segment should record at least:
- segment_id;
- section/chapter/day/page role;
- audience;
- content type;
- current text hash;
- function;
- immutable facts;
- mechanics if applicable;
- safety/consent boundaries;
- character/speaker;
- voice target;
- emotional job;
- humor job;
- recurrence/dependencies;
- word count or length budget;
- status: DRAFT / KEEP / FIX / BLOCK / APPROVED / FROZEN;
- owner gate if any.

For activity books also record:
- starting position;
- who starts;
- turn order;
- timing/counts;
- reset/error rules;
- variants;
- two-person/small-group behavior;
- stopping condition.

For narrative books also record:
- chronology;
- character knowledge;
- setup/payoff links;
- callbacks;
- unresolved threads.

This Content Map becomes the editorial equivalent of the physical Book Map.

## E. Extract immutable truth before style work

Separate what may be creatively improved from what must not drift.

Immutable truth includes as applicable:
- facts;
- numbers;
- dates;
- names;
- chronology;
- character relationships;
- plot outcomes;
- puzzle answers;
- activity mechanics;
- timing/counts;
- consent;
- safety;
- claim strength;
- legal meaning;
- product promises;
- recurring in-world terminology.

Create:
- IMMUTABLE_FACTS.json or .md
- GLOSSARY / TERMINOLOGY
- CHARACTER_VOICE_BIBLE.md
- ACTIVITY_MECHANICS_MAP.json when needed

No stylistic agent may silently change immutable truth.

## F. Freeze the product voice and audience test

Define the voice before iterative editing.

At minimum:
- age/readability;
- warmth level;
- humor type;
- formality/book register;
- forbidden registers;
- character-specific voices;
- cultural fit;
- emotional pressure limits;
- examples of accepted lines;
- examples of rejected lines.

For family/child books include:
- anti-cringe test;
- no forced youth slang;
- no therapy/workshop voice unless explicitly intended;
- no baby language for older children;
- no fake inspirational uplift;
- no forced vulnerability.

For localization, define whether the target should feel:
1. controlled/source-led localization; or
2. native re-authoring from function.

If native re-authoring is selected, sentence-level source wording is not the writing model. Function and truth are.

## G. Global diagnostic audit before rewriting

Run one full-book diagnostic pass before making broad changes.

The purpose is to find defects, not rewrite the book.

Use independent lenses:
- reader experience;
- language/naturalness;
- book register;
- logic/continuity;
- structure/arc;
- repetition;
- mechanics/comprehension;
- safety/consent;
- character voice;
- humor;
- age fit;
- emotional pressure;
- factual/semantic fidelity;
- layout-density risk.

Every finding must be classified:
- BLOCK: unsafe, false, contradictory, impossible or semantically wrong;
- FIX: materially weak/correctable;
- KEEP: already strong;
- OWNER_GATE: requires taste/brand/legal decision.

Never create a rewrite task for a KEEP segment.

## H. Build the Issue Ledger

Convert the audit into a durable ISSUE_LEDGER.json / .md.

Every issue gets:
- issue_id;
- segment_id;
- defect class;
- severity;
- evidence;
- reason it matters to the reader;
- proposed direction;
- dependencies/neighbors to recheck;
- required reviewer roles;
- status.

Prioritize in this order:
1. meaning/safety/mechanics;
2. logic/continuity;
3. reader confusion;
4. repetition/filler;
5. audience/age mismatch;
6. unnatural language/register;
7. weak humor/voice;
8. micro-proofing;
9. optional polish.

This prevents spending time perfecting jokes while a game is still logically broken.

## I. Identify book-wide function repetition

Before replacing individual sections, inspect the Content Map for duplicated jobs.

Examples:
- five conversation prompts all asking for appreciation;
- four games using the same cumulative-memory loop;
- multiple resets using the same face/jaw relaxation;
- repeated "what did this month teach us?" reflection;
- too many late-book gratitude exercises;
- the same December-chaos paragraph opening multiple days.

Flag repeated function, not only repeated wording.

A book can have zero duplicate sentences and still feel repetitive.

Create a FUNCTION_DISTRIBUTION table:
- segment;
- function;
- mechanic;
- emotional job;
- social job;
- intensity;
- novelty.

Use it to rebalance the arc.

## J. Choose the smallest useful slice

Do not launch a whole-book rewrite.

A slice contains only the segments needed to close one coherent defect cluster.

Good slice examples:
- three weak conversation prompts;
- one game plus its instruction completeness;
- one character's humor lines;
- one repeated reset family;
- one chapter continuity issue;
- one final-act reflection cluster.

Bad slice:
- "rewrite Days 1–24";
- "make the whole book funnier";
- "polish everything".

Before writing, declare the exact allowlist of segment IDs.

## K. Keep one writer, many reviewers

This is a permanent RSE collaboration rule.

**Many agents may independently review the same bounded scope. Only one controlled writer applies the final patch.**

Do not run:
Writer A -> Writer B rewrites A -> Writer C rewrites B -> Writer D rewrites C.

That creates semantic drift and destroys strong lines.

Instead run:
BASE
-> parallel/independent specialist reviews
-> orchestrator synthesis
-> ONE writer patch
-> independent validation

The orchestrator/editor-in-chief decides:
- KEEP;
- accept patch;
- reject patch;
- request a narrower revision.

Review agents return targeted findings or candidate lines. They do not take ownership of the whole manuscript.

## L. Route agents by defect type

Use all needed agents, but only where their expertise is relevant.

Universal editorial board:

**Source / meaning**
- Localization Source Function Analyst when cross-language;
- Localization Meaning Guardian;
- factual/domain specialist as needed.

**Primary writing**
- Native-language writer / Book Co-Author;
- Polish Native Family Writer for Polish family material;
- Narrative Designer / Narratologist for story architecture.

**Language**
- Natural Language Editor;
- Usage/Idiom Editor;
- Book Register Editor;
- Proofreader only at the end.

**Reader/audience**
- Family Ear Reviewer;
- child/teen audience reviewer;
- Psychologist only for pressure, consent, disclosure and relational risk, not as a creative owner.

**Creative**
- Transcreator for humor, idiom and emotional mechanism;
- Cultural Localizer only where cultural distance exists;
- character voice reviewer.

**Mechanics**
- Activity Instruction Completeness Reviewer;
- Game Designer;
- puzzle/logic validator;
- safety reviewer.

**Structure**
- Logic Editor;
- Continuity/Narrative reviewer;
- repetition/function-distribution reviewer.

Language-specific projects should instantiate equivalent native-language roles.

Do not send every segment through every creative agent. Route efficiently from the Issue Ledger.

## M. Make KEEP the default

A segment is not improved merely because it is different.

A replacement is accepted only if it is materially better on the defined criteria.

KEEP wins when:
- meaning is correct;
- reader understands it;
- language is natural;
- voice fits;
- mechanics work;
- it is not repetitive in the book arc;
- it is age-right;
- it is safe;
- it already has good rhythm/humor.

Do not rewrite good copy to make an agent look productive.

"Different" is not a quality metric.

## N. Native re-authoring route for localization

When source language differs from target language and the target should feel natively authored:

1. Source Function Analyst sees the source.
2. It creates a wording-free functional brief.
3. Native target-language writer writes from function, truth and voice, not source syntax.
4. Native usage/idiom gate.
5. Book register gate.
6. Product-specific creative pass.
7. Mechanics/safety completeness.
8. Family/audience ear test.
9. Only then reopen source for bilingual fidelity backcheck.

This prevents translationese.

Do not use creative re-authoring for legal/privacy/regulatory text.

## O. One surgical patch at a time

Before each patch:
- identify latest safe base snapshot;
- record base hash;
- declare exact allowed_changed_segments;
- mark protected regions;
- define expected dependency closure.

After patch:
- compute actual changed segments;
- compare with allowlist;
- fail if scope is broader;
- compare protected hashes;
- run required reviewers only on changed scope plus declared neighbors.

If the actual diff exceeds expected scope:
**FAIL CLOSED.**

Do not "just inspect and accept" accidental drift.

## P. Protect neighbors and dependencies explicitly

A local edit may have legitimate dependencies.

Examples:
- changing a recurring label affects all occurrences;
- changing a character catchphrase affects voice consistency;
- changing a clue affects solution text;
- changing a family activity mechanic affects safety instructions;
- changing a chapter fact affects later callbacks.

The orchestrator must calculate expected dependency closure before editing.

If a neighbor must change, add it to the allowlist first.

No surprise dependency expansion after the edit.

## Q. Run specialist review in layers

Recommended order for an edited segment:

1. Meaning/fact/mechanics lock.
2. Native language/usage.
3. Book register.
4. Audience/family ear.
5. Creative/humor/voice where needed.
6. Logic/continuity.
7. Instruction completeness or puzzle validation.
8. Safety/consent.
9. Bilingual fidelity if applicable.
10. Proofreading.
11. Surface-fit check.

Do not proofread copy that is still being structurally rewritten.

Do not let proofreader changes reopen creative decisions.

## R. Regression test after every meaningful slice

Every slice must prove both:
1. intended improvement occurred;
2. unrelated content did not change.

Minimum automated checks:
- structure counts;
- stable segment IDs;
- unique headings where required;
- immutable facts;
- protected phrases/locks;
- no forbidden regressions;
- frozen prior version hash;
- exact changed-segment set;
- source/candidate hashes;
- mechanics/safety assertions;
- terminology consistency.

Project-specific tests should encode defects previously found so they cannot silently return.

Every bug worth fixing is a candidate regression test.

## S. Save a durable checkpoint only after PASS

A checkpoint must include:
- timestamp;
- branch/commit;
- working master path;
- master blob/hash;
- base snapshot path/hash;
- changed segment IDs;
- reason for change;
- reviewers used;
- QA result;
- density/surface notes;
- remaining issues;
- owner gates.

Do not move the safe baseline forward on a failed slice.

If tools fail during write:
- keep the last durable checkpoint authoritative;
- do not claim uncommitted changes as progress;
- do not continue stacking edits in chat memory.

## T. Recheck only the affected closure after local edits

This is how RSE avoids rereading the full book after every sentence.

After one bounded patch, recheck:
- changed segments;
- explicit neighboring/dependent segments;
- global invariants/tests.

Do NOT reread all chapters every time.

Full-book review happens only at milestone gates:
1. initial diagnostic;
2. after major structural/function changes;
3. owner-read candidate;
4. final proof/freeze.

This is the core efficiency gain.

## U. Run milestone whole-book arc audits

At milestone gates, read the complete book as a reader, not as isolated units.

Evaluate:
- opening power;
- pacing;
- escalation/de-escalation;
- variation of mechanics/functions;
- repetition;
- emotional load;
- character voice distribution;
- joke density and quality;
- clarity;
- section transitions;
- middle-book sag;
- ending strength;
- payoff of earlier setups;
- whether late sections turn into a worksheet/reflection marathon.

Do not automatically edit findings. Put them into the Issue Ledger first.

## V. Validate real reader usability

For activity/family books verify:
- a family can perform the activity from the page alone;
- no missing starter/order/count;
- two-person/small-group variants work where required;
- optionality is clear;
- safety/consent is explicit;
- no forced disclosure;
- adult and child can participate on equal footing where intended;
- setup burden matches product promise;
- timing claim is plausible.

For narrative books verify:
- no unexplained knowledge;
- no name drift;
- no broken timeline;
- no missing setup/payoff;
- no contradictory motivations.

Human playtest/read-aloud evidence is stronger than editorial assumption when available.

## W. Test the real surface without sacrificing meaning

After language master quality is high, test the exact candidate in the real book template.

Check:
- overflow;
- font size;
- hierarchy;
- widows/orphans;
- scan speed;
- callout size;
- instruction readability;
- page-turn logic;
- dense pages;
- accessibility/contrast where relevant.

If content does not fit, use this order:
1. approved layout variant;
2. harmless copy tightening;
3. approved split;
4. exception/owner gate.

Never remove:
- safety;
- consent;
- mechanics;
- required facts;
- puzzle truth;
simply to fit a page.

Layout is not authorized to rewrite FROZEN_CONTENT.

## X. Build the Owner-Read Candidate

When no known substantive content defect remains:
- copy exact current master to an immutable owner-read candidate;
- record its hash;
- run full structural scan;
- run final multi-agent review;
- generate clean review PDF;
- clearly separate internal metadata from reader-facing text;
- list open owner decisions only.

Owner review should focus on:
- taste/brand choices;
- title;
- recurring labels;
- final emotional tone;
- unresolved legitimate alternatives.

Do not make the owner rereview unchanged material because of unrelated technical changes.

## Y. Freeze content with an explicit manifest

After owner approval and final QA, create CONTENT_FREEZE_MANIFEST.json.

It records:
- book/edition;
- exact premium master path;
- master hash;
- Content Map hash;
- glossary/voice hashes;
- frozen segment IDs;
- unresolved approved exceptions;
- QA receipts;
- owner approval reference;
- date;
- status FROZEN_CONTENT.

After FROZEN_CONTENT:
- renderer cannot rewrite copy;
- asset generation cannot rewrite copy;
- layout cannot rewrite copy;
- Book Agent cannot "improve" prose during build.

Any later copy change requires an unlock record:
- target segment;
- reason;
- old hash;
- proposed new hash;
- dependency closure;
- re-review scope.

No global unfreeze.

## Z. Hand off to RSE Book Agent v3

Only now enter physical production.

The handoff is:

FROZEN_CONTENT
-> BOOK_MAP.json
-> LOCK GRAPH
-> TEMPLATE/ASSET SLOTS
-> DETERMINISTIC PAGE BUILD
-> PAGE CACHE
-> PDF ASSEMBLY
-> VISUAL/PREFLIGHT QA
-> EXCEPTION-ONLY OWNER REVIEW
-> RELEASE

Book Agent v3 must consume exact frozen content hashes.

If a page does not fit, production raises an exception.
It does not silently rewrite the manuscript.

---

# MULTI-AGENT COLLABORATION CONTRACT

## Editor-in-chief / Orchestrator

Owns:
- source of truth;
- current safe baseline;
- Content Map;
- Issue Ledger;
- agent routing;
- patch allowlist;
- dependency closure;
- acceptance/rejection;
- checkpoint;
- final status.

It does not accept "agent consensus" blindly.
It compares recommendations against locks and product goals.

## Review agents

Review agents:
- receive bounded scope;
- identify specific defects;
- return KEEP/FIX/BLOCK;
- provide evidence;
- may propose targeted wording.

They do not:
- overwrite the whole manuscript;
- expand scope without escalation;
- silently change facts/mechanics;
- erase accepted voice;
- reformat unrelated sections.

## Writer agent

Exactly one writer applies one accepted patch set to the bounded scope.

The writer receives:
- current text;
- approved findings;
- immutable constraints;
- allowed segment IDs;
- voice/reader target.

The writer must not "clean up" neighboring copy opportunistically.

## Validator agents

Validators compare the patch against:
- baseline;
- immutable truth;
- mechanics;
- safety;
- target language;
- dependency closure.

Validators do not reopen style simply because they prefer another phrasing.

---

# REQUIRED ARTIFACT SET

Every serious RSE book upgrade should leave:

1. CONTENT_UPGRADE_BRIEF.md
2. SOURCE_MANIFEST.json
3. ORIGINAL_BASELINE / immutable source snapshot
4. CONTENT_MAP.json
5. IMMUTABLE_FACTS.json or equivalent
6. CHARACTER_VOICE_BIBLE.md when recurring characters exist
7. TERMINOLOGY / glossary
8. ISSUE_LEDGER.json
9. EDIT_GUARD.json
10. regression tests
11. checkpoints/
12. MULTI_AGENT_QA.md
13. REAL_SURFACE_FIT_REPORT.md
14. OWNER_READ_CANDIDATE
15. OWNER_READ.pdf
16. CONTENT_FREEZE_MANIFEST.json
17. final handoff to BOOK_MAP.json

A chat message is not a substitute for any of these artifacts.

---

# EDIT_GUARD MINIMUM CONTRACT

A reusable edit guard should contain:

    {
      "base_snapshot_path": "...",
      "current_master_path": "...",
      "allowed_changed_segments": ["CH03.SCENE04"],
      "require_exact_changed_set": true,
      "protected_regions": ["PREAMBLE", "BACK_MATTER"],
      "frozen_prior_version_sha": "...",
      "expected_dependencies": [],
      "rules": [
        "unallowlisted content must remain byte-identical",
        "scope expansion requires guard update before editing",
        "failed regression does not advance the baseline"
      ]
    }

For a prepared-but-not-yet-written patch, subset mode may be temporarily allowed.
Immediately after the patch, restore exact-set enforcement.

---

# CONTENT MAP MINIMUM CONTRACT

Recommended per-segment fields:

    {
      "segment_id": "D14.MIEDZY_NAMI",
      "role": "family_conversation",
      "function": "discover family influence and shared habits",
      "speaker": null,
      "immutable_facts": [],
      "mechanics": [],
      "safety": [],
      "voice": "warm, specific, non-coaching",
      "audience": "family_8_12_plus",
      "dependencies": [],
      "status": "APPROVED",
      "content_sha256": "..."
    }

Project-specific fields may be added, but stable IDs and function are mandatory.

---

# ACCEPTANCE TEST FOR EVERY PROPOSED REWRITE

Accept only when all are true:

1. It fixes a documented problem.
2. It is materially better than the current line.
3. Meaning/facts/mechanics are preserved.
4. Safety/consent are preserved or improved.
5. It sounds native in the target language.
6. It fits the intended book register.
7. It fits audience age and emotional maturity.
8. It does not create a new repetition elsewhere.
9. Character voice remains distinct.
10. It does not increase layout pressure without reason.
11. Actual diff stays inside declared scope.
12. Regression tests pass.

If the answer to "is it clearly better?" is no:
**KEEP.**

---

# FULL-BOOK DEFINITION OF DONE

Content is ready for FROZEN_CONTENT only when:

- source/structure coverage is complete;
- all BLOCK issues are closed;
- all material FIX issues are closed;
- no known semantic drift;
- no broken facts/numbers/mechanics;
- no unresolved safety/consent defects;
- logic and continuity pass;
- repetition/function-distribution pass;
- character voice pass;
- audience/anti-cringe pass;
- natural language pass;
- book-register pass;
- humor performs its intended function;
- proofreading pass;
- real-surface fit is acceptable or has an approved exception;
- owner-read candidate hash is fixed;
- owner-only decisions are explicitly resolved or isolated;
- frozen previous versions remain unchanged;
- exact candidate QA status is recorded honestly;
- final content hash is written to CONTENT_FREEZE_MANIFEST.

Do not claim PASS if exact-head CI or a required review did not run.
Use NOT RUN / PENDING rather than inventing evidence.

---

# FAILURE AND ROLLBACK RULES

## If a patch causes collateral drift
Reject it.
Restore base snapshot.
Narrow scope.
Reapply only the intended patch.

## If two agents disagree
Do not merge both versions.
Return to immutable function + product brief.
Editor-in-chief selects one direction or escalates to owner if it is a genuine taste/brand decision.

## If tool/GitHub write fails
Stop accumulating invisible edits.
Last durable checkpoint remains authoritative.
Retry later from durable state.

## If layout does not fit
Do not delete meaning reflexively.
Use approved layout variants first.

## If a full-book audit finds no substantive defect
Stop rewriting.
Move to owner-read/freeze.
"More changes" is not the goal.

---

# EFFICIENCY RULES

1. Full-book audit is diagnostic, not a rewrite command.
2. Local patch -> local re-review + global invariants.
3. Reuse accepted copy; do not regenerate it.
4. Route specialists only to relevant defects.
5. Run expensive whole-book review only at milestones.
6. Encode recurring defects as automated regressions.
7. Keep issue severity explicit.
8. Maintain one canonical working master.
9. Never edit from chat memory when durable source exists.
10. Owner reviews exceptions and genuine decisions, not unchanged content.

---

# RSE GOLDEN PRINCIPLES

1. **Source of truth beats chat memory.**
2. **Function and truth before style.**
3. **KEEP beats rewrite.**
4. **One writer, many independent reviewers.**
5. **No whole-book rewrite to fix a local problem.**
6. **Every edit has an allowlist and a baseline.**
7. **No silent dependency expansion.**
8. **Every meaningful defect becomes a regression candidate.**
9. **Safety, consent, mechanics and facts are never sacrificed for brevity or layout.**
10. **Full-book rereads happen at milestone gates, not after every patch.**
11. **FROZEN_CONTENT is a real technical lock, not a conversational promise.**
12. **Production/layout cannot rewrite locked copy.**
13. **Do not manufacture work after the manuscript is excellent.**
14. **Claim only QA that actually ran.**
15. **The final goal is reader value, not agent activity.**

---

# GENTLE STEPS LEARNINGS PROMOTED TO UNIVERSAL RSE RULES

The following lessons from the Gentle Steps V2 upgrade are now universal:

- preserve a frozen earlier version before deep upgrading;
- create a separate evolving version rather than overwriting history;
- real audience situations are stronger than generic coaching framing;
- repeated function matters more than repeated words;
- humor should be brief, character-specific and situation-specific;
- vulnerable prompts require optionality and must not force disclosure or forgiveness;
- activity variants must actually work for 2, 3, 4 and larger groups when promised;
- consent/no-touch alternatives are first-class mechanics, not footnotes;
- a technically correct instruction can still be unusable if a family has to infer a missing step;
- age fit must include an anti-cringe test, not only reading level;
- "natural" does not mean chatty; final copy still needs premium written-book register;
- mindfulness/wellness framing should be replaced by ordinary concrete actions when that better fits the audience;
- late-book reflection can become repetitive even when every prompt is individually good;
- density is a watchlist, not permission to cut safety or mechanics;
- once a good section is stable, freeze it and stop touching it;
- final owner-read should be generated from an exact candidate hash;
- content finalization and page production are separate systems.

This protocol is the mandatory editorial front-end to RSE Book Agent v3 for any manuscript that is not already owner-approved FROZEN_CONTENT.
