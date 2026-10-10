# RSE Premium Book Autonomous Upgrade / Native Re-authoring — Master New-Chat Prompt V2

Use this prompt in a brand-new ChatGPT conversation together with the base manuscript file(s).

---

Take over **RSE Premium Book Autonomous Content Upgrade** for this book.

Your job is to take the uploaded manuscript from its current state to the strongest possible **final premium content candidate**, with durable GitHub state, controlled multi-agent collaboration, regression protection, full reader testing and final downloadable files.

Do NOT stop after diagnosis.
Do NOT ask the owner to approve ordinary editorial decisions.
Do NOT rewrite the whole book every time one section is weak.
Do NOT lose strong existing content.
Do NOT treat "different" as "better".
Do NOT claim publication readiness until the exact content has passed the required content, layout and proof gates.

GitHub becomes source of truth as soon as durable project state is created.

Start from:

`riseshineevolve-source/agency-agents/orchestration/bootstrap/PREMIUM_BOOK_CONTENT_UPGRADE_BOOTSTRAP.md`

Then read, in order:

1. `orchestration/architecture/RSE_PREMIUM_BOOK_CONTENT_UPGRADE_PROTOCOL_V1.md`
2. `strategy/runbooks/scenario-premium-book-content-upgrade.md`
3. `orchestration/architecture/RSE_BOOK_AGENT_V3.md`
4. `orchestration/architecture/RSE_BOOK_MAP_CONTRACT_V1.md`
5. all project-specific canonical source / voice / mechanics / owner-lock files if they already exist.

Later durable GitHub state beats chat memory.

# OWNER INPUT

I am uploading the initial/base manuscript file(s).

**BOOK / PROJECT NAME:** [fill in]

**TARGET LANGUAGE:** [fill in]

**SOURCE LANGUAGE:** [fill in if different]

**BOOK CHARACTER / TYPE:** [for example narrative adventure / family activity book / detective puzzle book / workbook / calendar / nonfiction / hybrid]

**TARGET AUDIENCE / AGE:** [fill in]

**DESIRED STYLE / VOICE / REGISTER:** [fill in]

**INTENDED EXPERIENCE:** [for example 10 minutes per day / bedtime read / puzzle session / chapter-based reading]

**PUBLICATION SURFACE:** [book / KDP / app / both / unknown]

**ROUTE:** choose exactly one:

- **ROUTE A — SAME_LANGUAGE_PREMIUM_UPGRADE**  
  The manuscript already exists in the target language. Upgrade it to a final premium version while preserving everything that already works.

- **ROUTE B — CROSS_LANGUAGE_NATIVE_REAUTHORING**  
  The manuscript exists in another language. Do NOT translate sentence by sentence. Treat the source as authority for meaning, facts, function, characters, mechanics, chronology, safety, consent, claim strength and required structure, but create the target-language edition essentially from scratch so it reads as if it had originally been written in the target language.

**OWNER LOCKS / THINGS THAT MUST NOT CHANGE:** [optional]

**THINGS I ESPECIALLY LIKE AND WANT PRESERVED:** [optional]

**THINGS I DISLIKE / WANT REMOVED:** [optional]

**OTHER EXISTING VERSIONS / OWNER-CORRECTED FILES:** [upload if they exist]

If an optional input is missing, infer a provisional answer from the manuscript where safe. Do not stop ordinary execution for missing non-critical metadata.

# PRIMARY OBJECTIVE

Produce a book that is materially better than the starting manuscript as a whole and in every part that genuinely needs improvement.

The final book must be:
- logically coherent;
- structurally strong;
- natural in the target language;
- premium in written register;
- interesting and emotionally credible;
- appropriate to the target age/audience;
- free from filler and repeated function;
- consistent in facts, chronology, characters, terminology and voice;
- mechanically complete where activities/games/puzzles exist;
- safe and consent-aware;
- strong as a whole reader experience;
- protected against regression;
- ready for owner read as one exact immutable candidate.

The governing rule is:

**KEEP beats rewrite.**

A strong existing line or section is an asset.
Protect it.

# AUTONOMOUS EXECUTION MODE

After the initial input, continue autonomously through the process.

Do not ask the owner to approve:
- grammar fixes;
- obvious logic fixes;
- removal of repetition;
- instruction clarification;
- small natural-language repairs;
- safe local humor improvements;
- standard regression fixes.

Stop only for a genuine OWNER_GATE:
- title/brand choice;
- unresolved source conflict that changes meaning;
- legal/compliance decision;
- major character/product identity change;
- a redesign with two legitimately different strategic directions and no clear winner;
- final content approval;
- physical/Previewer proof;
- publication/release authorization.

You may give short progress checkpoints, but do not turn the workflow into dozens of approval messages.

# PHASE 0 — DURABLE INTAKE

Before substantive editing:

1. Verify repository and current `main`.
2. Create or use one dedicated non-main working branch for this book.
3. Establish **one-writer-per-surface ownership**.
4. Save the uploaded source manuscript into durable project truth.
5. Record exact file path + hash.
6. Never edit the only copy.
7. Create:
   - `SOURCE_MANIFEST`
   - immutable `ORIGINAL_BASELINE`
   - separate `WORKING_MASTER`
   - `CHECKPOINTS/`
8. Record Route A or Route B.
9. Record target language, audience, book type, voice, experience length and owner locks.

If GitHub/write tools fail:
**STOP EDITING THAT SURFACE.**
The last durable checkpoint remains authoritative.
Do not accumulate invisible chat-only changes.

# PHASE 1 — SOURCE CONVERGENCE / BEST-OF

If more than one manuscript/version exists:

1. Inventory every version.
2. Hash every file.
3. Identify which is structurally newest.
4. Compare materially different sections by stable segment/function.
5. Preserve earlier owner-approved or demonstrably stronger material.
6. Build:
   - `SOURCE_VERSION_INVENTORY`
   - `SOURCE_CONVERGENCE_REPORT`
   - `GOLDEN_KEEP_REGISTRY`

The newest file does NOT automatically win.

Examples of GOLDEN_KEEP:
- a stronger joke from an older version;
- a clearer game mechanic;
- a better character line;
- an already-fixed logic issue;
- owner-approved wording;
- a stronger ending;
- accepted terminology.

Approval inheritance rule:

**Previously approved or clearly excellent content stays KEEP/LOCKED until a concrete documented defect reopens it.**

# PHASE 2 — BUILD THE BOOK CONTROL MAP

Assign stable IDs to every meaningful unit.

Examples:
- D01.ZWOLNIJ
- D01.GRAMY
- D01.MIEDZY_NAMI
- CH03.SCENE04
- CASE04.CLUE02
- INTRO.PARA05
- BACKMATTER.LETTER

Build `CONTENT_MAP` containing, as applicable:
- segment ID;
- function;
- audience;
- speaker/character;
- voice target;
- emotional job;
- humor job;
- facts;
- mechanics;
- safety/consent;
- dependencies;
- recurrence;
- word/density budget;
- current hash;
- status: KEEP / FIX / BLOCK / OWNER_GATE / APPROVED / FROZEN.

Also create:
- `IMMUTABLE_FACTS`
- `GLOSSARY / TERMINOLOGY`
- `CHARACTER_VOICE_BIBLE`
- `ACTIVITY_MECHANICS_MAP` for games/activities;
- `PUZZLE_TRUTH_MAP` for puzzle/detective books;
- chronology/setup/payoff map for narrative books.

# PHASE 3 — FREEZE VOICE AND AUDIENCE RULES

Create a target-language/style profile.

Define:
- age/readability;
- warmth;
- humor type;
- premium book register;
- desired rhythm;
- forbidden tone;
- character-specific voices;
- cultural fit;
- emotional-pressure limits;
- examples of excellent lines;
- examples of rejected lines.

For child/family books explicitly test:
- anti-cringe;
- no baby language;
- no adult fake-teen slang;
- no school-workshop voice;
- no corporate coaching;
- no therapy/mindfulness clichés unless intentionally part of the book;
- no forced vulnerability;
- no compulsory apology/gratitude/disclosure;
- humor must never mock a sincere answer, affection, apology, refusal or safety.

# PHASE 4 — ROUTE-SPECIFIC WRITING

## ROUTE A — SAME-LANGUAGE PREMIUM UPGRADE

Work directly in the current language.

Improve only where needed:
- clarity;
- logic;
- structure;
- naturalness;
- pacing;
- humor;
- voice;
- mechanics;
- reader experience;
- progression;
- proof.

Preserve strong existing text.

## ROUTE B — CROSS-LANGUAGE NATIVE RE-AUTHORING

Do NOT write from sentence-level source syntax.

Mandatory order:

1. **Source Function Analyst** reads the source.
2. Create a wording-free functional brief per segment.
3. Hide sentence-level source wording from the target writer where practical.
4. **Native Target-Language Writer / Book Co-Author** writes from function, meaning, audience, culture and voice.
5. **Natural Language / Usage / Idiom Editor** checks real native usage.
6. **Book Register Editor** checks polished written-book language.
7. **Audience / Family Ear Reviewer** checks how it sounds to the intended reader.
8. **Cultural Localizer** intervenes only where real cultural distance exists.
9. **Transcreator** handles humor, idiom, rhythm and emotional mechanisms only where needed.
10. **Logic / Continuity Editor** checks the target book as an independent book.
11. Mechanics/puzzle/safety reviewers test actual usability.
12. Only then reopen the original source.
13. **Meaning Guardian + Bilingual QA** verify facts, function, chronology, mechanics, safety, consent and claim strength.
14. **Proofreader** works last.

Test question:

**"Does this read like a premium book genuinely written from the beginning in the target language while preserving the product truth?"**

Not:

**"Is this a faithful sentence-by-sentence translation?"**

# PHASE 5 — FIRST FULL-BOOK DIAGNOSTIC

Before broad rewriting, run one independent diagnostic board.

Minimum reviewer board:

1. **Reader Experience / Family Ear Reviewer**
2. **Natural Language Editor**
3. **Book Register Editor**
4. **Logic / Continuity Editor**
5. **Structure / Arc Reviewer**
6. **Repetition / Function Distribution Reviewer**
7. **Humor / Character Voice Reviewer**
8. **Mechanics / Activity / Puzzle Reviewer** if applicable
9. **Safety / Consent / Emotional Pressure Reviewer** if applicable
10. **Proofreader / technical-language scan**
11. **Source Fidelity / Meaning Guardian** for Route B
12. **Genre specialist** where needed: game designer, puzzle validator, narratologist, subject expert.

Every reviewer works independently first.

They return:
- KEEP
- FIX
- BLOCK
- OWNER_GATE

with evidence.

They do NOT rewrite the whole manuscript.

# PHASE 6 — ISSUE LEDGER + FUNCTION DISTRIBUTION

Create `ISSUE_LEDGER`.

Every issue records:
- issue ID;
- segment ID;
- severity;
- exact problem;
- reader impact;
- proposed direction;
- dependencies/neighbors;
- required reviewers;
- status.

Prioritize:
1. truth / safety / mechanics;
2. logic / continuity;
3. reader confusion;
4. structure / progression;
5. repeated function/mechanic;
6. audience mismatch;
7. unnatural language/register;
8. humor/voice;
9. proofing;
10. optional polish.

Also build `FUNCTION_DISTRIBUTION`.

Check repeated PURPOSE, not only repeated wording.

Examples:
- several different prompts that all ask for gratitude;
- several games using the same memory-chain mechanic;
- repeated body resets;
- repeated endings;
- too many reflective tasks late in the book.

A book can have zero repeated sentences and still feel repetitive.

# PHASE 7 — EDITOR-IN-CHIEF SYNTHESIS

Use this permanent collaboration law:

**MANY INDEPENDENT REVIEWERS → ONE EDITOR-IN-CHIEF → ONE CONTROLLED WRITER → INDEPENDENT VALIDATION**

Never run serial whole-book rewriting:
Writer A -> Writer B -> Writer C.

That causes semantic drift.

The Editor-in-Chief:
- compares findings;
- resolves disagreements;
- protects GOLDEN_KEEP;
- rejects unnecessary rewrites;
- groups related defects into bounded slices;
- selects the smallest sufficient scope.

Decision precedence:
1. explicit owner lock;
2. immutable truth / safety / mechanics / law;
3. product brief + audience/style profile;
4. GOLDEN_KEEP / previously approved material;
5. reader/logic/usability evidence;
6. style preference.

# PHASE 8 — SURGICAL EDIT LOOP

For every coherent defect cluster:

1. Save durable pre-edit snapshot.
2. Record base hash.
3. Declare exact `allowed_changed_segments`.
4. Declare protected segments.
5. Declare dependency closure.
6. Run only relevant reviewers on that scope.
7. Editor-in-Chief selects exact change direction.
8. Exactly ONE writer applies the patch.
9. Compute actual changed segment IDs.
10. Compare with allowlist.
11. Compare protected hashes.
12. Run regression.
13. Review changed scope + declared dependencies only.
14. Checkpoint only after PASS.

If actual diff exceeds scope:

**FAIL CLOSED → revert → narrow scope → reapply.**

Never accept accidental collateral drift because it "also looks better".

# PHASE 9 — COMPETITIVE REDESIGN FOR WEAK CORE ELEMENTS

Do not insert the first redesign idea into the manuscript.

Trigger this protocol when:
- a core game/activity fails;
- opening is weak;
- finale is weak;
- a major chapter/case is boring;
- a key mechanic is repetitive;
- an important character/scene does not land.

Run a concept competition:

1. Generate 3–5 genuinely different candidate concepts.
2. Keep them OUTSIDE the working master.
3. Score them independently using a 100-point rubric relevant to the product.

Typical rubric:
- reader wants to do/read it;
- clarity;
- emotional/entertainment payoff;
- fit with audience;
- fit with book arc;
- uniqueness vs other sections;
- mechanics/usability;
- 2-person / small-group support where relevant;
- safety/inclusion;
- cultural/local fit;
- time/effort cost.

4. Compare candidates against the CURRENT VERSION too.
5. A redesign wins only if it is clearly materially better.
6. If no candidate clearly wins:
   **KEEP CURRENT.**
7. Only the winning concept enters a new surgical edit slice.

# PHASE 10 — REQUIRED SPECIALIST ROUTING

Use only agents relevant to the defect.

Default RSE pool:

**Meaning / source**
- Source Function Analyst
- Meaning Guardian
- Bilingual QA
- factual/domain expert

**Primary writing**
- Native-language Writer / Book Co-Author
- Polish Native Family Writer for Polish family content
- Narrative Designer / Narratologist for story books

**Language**
- Natural Language Editor
- Usage / Idiom Editor
- Book Register Editor
- Proofreader last

**Reader**
- Family Ear Reviewer
- child/teen reader lens
- adult-reader lens when adults participate

**Creative**
- Transcreator
- Character Voice Reviewer
- Cultural Localizer

**Mechanics**
- Activity Instruction Completeness Reviewer
- Game Designer
- Puzzle/Logic Validator
- Safety/Consent Reviewer

**Experience / behaviour**
- Organizational Psychologist only as a lens for cooperation, psychological pressure and group dynamics
- Personal Growth Mentor only as a lens for agency, usefulness and behavior transfer
- Breath/Reset specialist for body/breath exercises

Do not let psychologists/mentors become the book's writer unless the product is explicitly a psychology/coaching book.

# PHASE 11 — UNIT / DAY / CHAPTER TESTING

Every sequential unit must be tested individually.

For each day/chapter/case/lesson record:

- does it start clearly?
- can the reader execute it without guessing?
- how long does it take?
- is the experience satisfying?
- does it work for the promised group size?
- does it work for 2 people if promised?
- for family/group books: test 2, 3, 4 and 5+ where mechanics materially differ;
- is any person forced into spotlight, touch, eye contact or disclosure?
- does humor help rather than interrupt?
- is it too childish / too adult / too complex?
- does it feel weaker than neighboring units?
- does it earn its place?

Create a `UNIT_EXPERIENCE_MATRIX`.

For time-based books, estimate:
- reading/setup time;
- activity/game time;
- conversation/reflection time;
- transitions;
- likely total.

Flag only meaningful violations.
Do not destroy strong content to hit a stopwatch mechanically.

# PHASE 12 — PROGRESSION / ARC TEST

Test the book as a journey, not only as isolated units.

Check:
- opening power;
- early ease;
- middle-book sag;
- increasing richness or challenge;
- intentional breathing-space days;
- emotional depth;
- variety;
- callbacks;
- payoff;
- final-week/act escalation;
- ending/finale strength.

Do NOT require every unit to be harder than the previous one.

Prefer a wave:
**BUILD → BREATHE → BUILD → PEAK → CLOSE**

For calendars/programs, the final days must feel more earned, richer or more meaningful than the opening.

For narrative/puzzle books, setups must pay off.

# PHASE 13 — MILESTONE WHOLE-BOOK AUDITS

Do NOT reread the whole book after every local patch.

Run full-book audits only at these gates:

### FULL AUDIT 1 — Initial Diagnostic
Before major editing.

### FULL AUDIT 2 — Post-Structural / Post-Redesign Audit
After major changes to structure, function distribution, major games/chapters/cases.

### FULL AUDIT 3 — Owner-Read Candidate Audit
When all known material FIX/BLOCK items are closed.

### FULL AUDIT 4 — Fresh-Eyes Publish-Gate Audit
A NEW independent pass after the candidate appears finished.

This last pass is mandatory.

The fresh-eyes board must again inspect:
- family/reader reality;
- logic;
- natural language;
- book register;
- humor;
- mechanics;
- unit-by-unit experience;
- promised duration;
- 2/3/4+ variants where relevant;
- progression;
- finale;
- safety/consent;
- proof.

If the fresh-eyes audit finds only bounded defects:
patch only those bounded segments and rerun exact-diff.

If it finds no material defect:
**STOP CREATIVE REWRITING.**

# PHASE 14 — FINAL TEST BATTERY

Before declaring final content candidate, run the following **12 universal final gates**:

1. **Source/coverage gate**
2. **Natural-language gate**
3. **Premium book-register gate**
4. **Logic/continuity gate**
5. **Structure/arc/progression gate**
6. **Reader-experience/engagement gate**
7. **Repetition/function-distribution gate**
8. **Audience/age/anti-cringe gate**
9. **Humor/character-voice gate**
10. **Proofreading/typography gate**
11. **Density/time/readability gate**
12. **Fresh-eyes publish-gate audit**

Then run applicable product modules:

### Activity / game / family book: +4 mandatory gates
13. **Instruction completeness gate**
14. **2/3/4/5+ group-size gate**
15. **Safety/consent/agency gate**
16. **Per-unit real-use/time simulation gate**

### Puzzle / detective book: +4 mandatory gates
13. clue completeness;
14. single-solution / solvability test;
15. answer/solution consistency;
16. clue-story integration.

### Narrative book: +4 mandatory gates
13. character continuity;
14. chronology;
15. setup/payoff;
16. scene/chapter pacing.

### Route B localization: +3 mandatory gates
17. meaning/function fidelity;
18. bilingual fact/mechanics backcheck;
19. native-target-language authenticity independent of source syntax.

A gate is PASS only if it was actually run.
Use NOT RUN / PENDING otherwise.

# PHASE 15 — GOLDEN KEEP + REGRESSION

Every significant bug fixed becomes a regression-test candidate.

Regression protects:
- accepted intent;
- truth;
- mechanics;
- safety;
- character voice;
- owner locks;
- GOLDEN_KEEP.

Regression must NOT blindly protect stale wording.

If CI fails because it expects an older weaker line:
1. determine whether content regressed or the test is obsolete;
2. never restore weaker text only to make CI green;
3. update the test only after the new behavior passes appropriate review;
4. checkpoint the new accepted lock.

# PHASE 16 — FINAL CANDIDATE CREATION

When:
- BLOCK = 0;
- material FIX = 0;
- material REDESIGN = 0;
- all required gates PASS;
- fresh-eyes publish audit finds no material defect;
- previous frozen versions remain intact;

then create:

**OWNER_READ_CANDIDATE**

Requirements:
- immutable exact file;
- exact Git/GitHub blob/hash;
- manifest points to that exact candidate;
- final QA receipt;
- final issue ledger;
- no internal metadata inside reader-facing pages.

Do not call it final merely because the working master looks good.
The exact candidate identity matters.

# PHASE 17 — FINAL FILES FOR THE OWNER

Automatically generate from the exact candidate:

1. **Final editable source**
   - Markdown or native text master.

2. **DOCX**
   - clean editable owner version;
   - correct headings and paragraphs;
   - no internal QA metadata on reader pages.

3. **PDF**
   - clean owner-read PDF;
   - each chapter/day begins cleanly where appropriate;
   - readable typography;
   - inspect/render the PDF after generation;
   - verify no clipping, broken characters, orphaned headings or overflow.

The PDF/DOCX must come from the SAME exact candidate.
Do not generate them from an older working file.

Deliver direct download links to the owner.

# PHASE 18 — OWNER APPROVAL AND CONTENT FREEZE

After the owner approves the exact candidate:

state becomes:

**CONTENT_APPROVED**

Then create:
- `CONTENT_FREEZE_MANIFEST`
- exact frozen hash
- content lock.

State becomes:

**FROZEN_CONTENT**

After FROZEN_CONTENT:
- renderer cannot rewrite text;
- layout cannot rewrite text;
- image agent cannot rewrite text;
- Book Agent cannot silently improve wording.

If later one sentence must change:
unlock only that segment + dependency closure.
No global unfreeze.

# PHASE 19 — BOOK PRODUCTION / PRINT GATES

Only after FROZEN_CONTENT:

`FROZEN_CONTENT
→ BOOK_MAP
→ LOCK GRAPH
→ TEMPLATE / ASSET SLOTS
→ DETERMINISTIC PAGE BUILD
→ PDF
→ VISUAL QA
→ PREFLIGHT
→ TARGET-PLATFORM PREVIEWER
→ PHYSICAL PROOF IF REQUIRED
→ PRINT_READY
→ RELEASE_AUTHORIZED`

Text-final is NOT the same as print-ready.
Print-ready is NOT the same as release-authorized.

# FINAL STOP CONDITION

Stop creative editing when:

- every required source unit is accounted for;
- BLOCK = 0;
- material FIX = 0;
- material REDESIGN = 0;
- facts/meaning/mechanics correct;
- safety/consent correct;
- logic/continuity PASS;
- progression/arc PASS;
- repetition/function distribution PASS;
- natural language PASS;
- premium book register PASS;
- audience/anti-cringe PASS;
- humor/voice PASS;
- all unit mechanics work;
- promised group sizes work;
- time/experience promise is credible;
- finale/ending PASS;
- proofreading PASS;
- fresh-eyes publish-gate PASS;
- exact immutable candidate exists;
- previous frozen versions are untouched;
- owner-only choices are isolated.

When these conditions are true:

**STOP REWRITING.**

Do not manufacture new changes to show activity.

# FINAL OWNER REPORT

Do not send a long stream of intermediate editorial choices.

At the end, give the owner one concise final report containing:

1. selected route;
2. source/baseline identities;
3. versions converged;
4. key GOLDEN_KEEP protections;
5. major upgrades completed;
6. agent/reviewer board used;
7. all final test gates and PASS/NOT RUN status;
8. remaining owner gates only;
9. exact candidate path/hash;
10. links to final PDF and DOCX/source file.

If a genuine owner decision was unavoidable earlier, isolate it clearly and ask only that decision.

The intended experience is:

**UPLOAD BASE MANUSCRIPT + FILL IN INTAKE → SYSTEM RUNS AUTONOMOUSLY → USER RECEIVES ONE PREMIUM FINAL CANDIDATE + PDF/DOCX + QA RECEIPT**

not:

**UPLOAD MANUSCRIPT → DOZENS OF MANUAL CHAT ITERATIONS → RISK LOSING GOOD CONTENT.**

---