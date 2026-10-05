# Paste-Ready Prompt — RSE Premium Book Creation / Upgrade

Use this prompt in a brand-new ChatGPT conversation together with the base manuscript file(s).

---

Take over **RSE Premium Book Content Upgrade** execution.

GitHub is source of truth after durable state is created. Start from:

`riseshineevolve-source/agency-agents/orchestration/bootstrap/PREMIUM_BOOK_CONTENT_UPGRADE_BOOTSTRAP.md`

Then read, in order:

1. `orchestration/architecture/RSE_PREMIUM_BOOK_CONTENT_UPGRADE_PROTOCOL_V1.md`
2. `strategy/runbooks/scenario-premium-book-content-upgrade.md`
3. `orchestration/architecture/RSE_BOOK_AGENT_V3.md`
4. `orchestration/architecture/RSE_BOOK_MAP_CONTRACT_V1.md`

Do not reconstruct project truth from old chat memory when durable GitHub state exists.

## INPUT I AM PROVIDING NOW

I am uploading the initial/base manuscript file(s).

**BOOK / PROJECT NAME:** [fill in]

**TARGET LANGUAGE:** [fill in]

**BOOK CHARACTER / TYPE:** [for example: narrative adventure / family activity book / detective puzzle book / workbook / Christmas calendar / educational nonfiction / other]

**TARGET AUDIENCE / AGE:** [fill in]

**DESIRED STYLE / VOICE / REGISTER:** [fill in — describe how it should feel to the reader]

**ROUTE:** choose exactly one:

- **ROUTE A — SAME_LANGUAGE_PREMIUM_UPGRADE**  
  The book already exists in the target language. Upgrade the content to a final premium version.

- **ROUTE B — CROSS_LANGUAGE_NATIVE_REAUTHORING**  
  The book exists in another language. Do NOT translate it sentence by sentence. Use the original-language book only as authority for content, function, facts, characters, mechanics, chronology, safety, claim strength and required structure. Create the target-language edition essentially from scratch so it reads as if it had originally been written in the target language.

**OPTIONAL OWNER LOCKS / THINGS THAT MUST NOT CHANGE:** [fill in if relevant]

**OPTIONAL THINGS I ESPECIALLY LIKE AND WANT PRESERVED:** [fill in if relevant]

**OPTIONAL THINGS I DISLIKE / WANT REMOVED:** [fill in if relevant]

**OTHER EXISTING VERSIONS / CORRECTED FILES:** [upload them too if they exist]

## YOUR JOB

Take the manuscript from the uploaded base material to a **super-final premium content master**, not merely a corrected draft.

The target is a book that is:
- logically coherent;
- structurally strong;
- clear;
- natural in the target language;
- appropriate to the audience;
- premium in written register;
- interesting throughout;
- free of filler and unnecessary repetition;
- consistent in characters, facts, terminology and tone;
- safe and mechanically complete where activities/puzzles are involved;
- strong as a whole reader experience, not only sentence by sentence.

Preserve everything already excellent.

**KEEP beats rewrite.**

Do not rewrite for novelty.

## FIRST RUN — BEFORE EDITING

1. Verify/create the dedicated working branch/surface. Never edit main directly.
2. Save/hash the uploaded base manuscript into durable project truth.
3. If multiple versions exist, inventory ALL of them first.
4. Do a best-of/source-convergence pass before new writing.
5. Create a `GOLDEN_KEEP_REGISTRY` for owner-approved or demonstrably stronger existing passages so they are not lost.
6. Create immutable baseline and separate working master.
7. Record the target-language/style profile and selected Route A/B.
8. Assign stable segment IDs.
9. Build `CONTENT_MAP`.
10. Extract immutable facts, mechanics/puzzle truth, safety/consent, glossary, character voice and dependencies.
11. Run one complete diagnostic audit of the whole book WITHOUT automatically rewriting everything.
12. Create `ISSUE_LEDGER` with each finding classified as:
   - KEEP
   - FIX
   - BLOCK
   - OWNER_GATE
13. Build a function/repetition map so you detect repeated PURPOSE/MECHANIC, not only repeated words.
14. Choose the highest-value bounded slice.

## SOURCE-CONVERGENCE RULE

If several near-final versions exist, do not simply choose the newest file.

Compare them by stable segment/function.

Preserve:
- earlier owner-approved text;
- stronger jokes;
- clearer mechanics;
- better natural-language passages;
- already-fixed logic;
- accepted terminology.

A newer file does not automatically supersede a better earlier passage.

Previously approved strong content inherits KEEP status unless a specific documented defect justifies reopening it.

## ROUTE A — SAME-LANGUAGE UPGRADE

Improve the existing target-language book directly.

Audit:
- reader experience;
- natural language;
- premium book register;
- logic;
- continuity;
- structure/arc;
- repetition/function distribution;
- clarity;
- age fit;
- anti-cringe;
- humor;
- character voice;
- mechanics;
- safety/consent;
- proof;
- density/surface pressure.

Preserve facts, mechanics, puzzle truth, safety, approved voice and strong existing text.

## ROUTE B — NATIVE RE-AUTHORING IN A NEW LANGUAGE

Do NOT produce a literal translation.

Mandatory sequence:

1. **Source Function Analyst** reads the original.
2. Produce a wording-free functional brief by segment.
3. Create a writer packet that does NOT expose sentence-level original wording where practical.
4. **Native target-language writer** writes each segment from function, meaning, reader, culture and desired style.
5. **Target-language Usage/Idiom/Natural Language Editor** checks real native usage.
6. **Book Register Editor** checks premium written-book language.
7. **Audience / Family Ear / age-fit reviewer** checks how it sounds to the intended reader.
8. **Cultural Localizer** adapts only where cultural distance matters.
9. **Transcreator** handles humor/wordplay/emotional mechanism only where needed.
10. **Logic/Continuity Editor** checks the whole system/story.
11. **Mechanics / Instruction / Puzzle / Safety reviewers** verify exact usability and truth.
12. Only then reopen the original source.
13. **Meaning Guardian + Bilingual QA** verify that facts, function, mechanics, chronology, safety, consent and claim strength were not lost or invented.
14. **Proofreader** works last.

Do not make the target text look artificially parallel to the source.

The test is not: "Is this a good translation?"
The test is: "Does this read like a premium book genuinely written from the beginning in the target language while preserving the original product truth?"

## MULTI-AGENT COLLABORATION

Use all relevant specialist agents, but do NOT let them serially rewrite the whole manuscript.

Permanent rule:

**Many independent reviewers. One controlled writer.**

First-pass reviewers independently return:
- KEEP
- FIX
- BLOCK
- OWNER_GATE
with evidence.

Then the orchestrator/editor-in-chief synthesizes decisions.

Exactly ONE writer applies the accepted patch to the declared scope.

Reviewers/validators then compare the patch against the baseline.

Do not allow parallel writers on the same canonical master.

## SURGICAL CHANGE CONTROL — MANDATORY

Before every meaningful edit:

1. Freeze a durable pre-edit snapshot.
2. Record base hash.
3. Declare exact `allowed_changed_segments`.
4. Declare protected regions.
5. Declare expected dependency closure.
6. Edit ONLY that scope.

After editing:

1. Compute actual changed segment IDs.
2. Verify actual changed scope matches the allowlist.
3. Verify protected content is byte-for-byte unchanged where required.
4. Verify frozen previous versions remain unchanged.
5. Run regression and relevant specialist QA.
6. Checkpoint only after PASS.

If unrelated text changed:
**FAIL CLOSED → revert → narrow patch → reapply.**

Never regenerate an entire chapter/day/book to fix one line unless a documented structural defect genuinely requires that scope.

## DO NOT LOSE GOOD CONTENT

Do not "clean up" neighboring passages opportunistically.

Do not replace a strong line because another line nearby is weak.

Do not accept a rewrite merely because it is different.

Every proposed rewrite must answer:
**What documented problem does this fix, and is it materially better?**

If the answer is unclear:
**KEEP.**

## RE-REVIEW SCOPE

After a local patch, do NOT reread the whole book.

Recheck:
- changed segments;
- declared dependencies/neighbors;
- global invariants/regression tests.

Run full-book audits only at milestone gates:
1. initial diagnostic;
2. after major structural/function changes;
3. before owner-read candidate;
4. before final freeze.

This is mandatory for efficiency and regression control.

## REGRESSION TEST RULE

Regression tests protect approved INTENT, MECHANICS, LOGIC and LOCKS.

If a test fails because it still expects an older weaker line:
- determine whether the manuscript or the test is wrong;
- never restore inferior wording just to make CI green;
- update the regression only after the new wording/behavior has been validated and accepted;
- checkpoint the new lock.

## FULL-BOOK PREMIUM AUDIT

At milestone gates read the book as an actual target reader.

Check:
- opening power;
- clarity;
- pacing;
- middle-book sag;
- escalation/de-escalation;
- variety;
- repeated functions/mechanics;
- filler;
- logic;
- callbacks/payoffs;
- character consistency;
- joke quality and distribution;
- emotional pressure;
- reader fatigue;
- late-book reflection overload;
- ending strength;
- whether every section earns its place.

Do not automatically rewrite every finding. Put defects into the Issue Ledger first.

## ACTIVITY / PUZZLE COMPLETENESS

Where relevant verify:
- who starts;
- how starter is chosen;
- order/direction;
- exact counts/timing;
- reset/error rules;
- rounds;
- optional/advanced variants;
- 2-person/small-group behavior;
- ending condition;
- safety;
- consent;
- no-touch alternative if appropriate;
- exact puzzle/clue/answer truth.

Clarity outranks brevity.

Never cut mechanics, safety or consent just to make text shorter or fit a page.

## CHILD / FAMILY / TEEN FIT WHERE RELEVANT

Use an anti-cringe test.

Reject:
- baby language for older children;
- fake youth slang;
- school-workshop voice;
- corporate coaching language;
- therapy/mindfulness clichés where not intended;
- forced vulnerability;
- compulsory apology/gratitude/disclosure;
- humor that mocks a vulnerable answer, affection, apology or safety.

Humor should be brief, situational and voice-specific.

## REAL-SURFACE FIT

Only after the content is strong, test the **exact candidate hash** in the real intended template/surface.

Record that hash in `REAL_SURFACE_FIT_REPORT`.

A template proof for an older candidate cannot approve a newer text.

If text does not fit:
1. approved layout variant;
2. harmless tightening;
3. approved split;
4. exception/owner gate.

Layout is not authorized to rewrite protected meaning, mechanics or safety.

## FINALIZATION STATES

Keep these states separate:

`DRAFT → PREMIUM_WORKING → OWNER_READ_CANDIDATE → CONTENT_APPROVED → FROZEN_CONTENT → PRINT_READY → RELEASE_AUTHORIZED`

Do not call text "print-ready" or "KDP-ready" merely because the content is excellent.

### OWNER_READ_CANDIDATE
Create one immutable exact-hash candidate.
Run final multi-agent full-book audit.
Generate a clean owner-read PDF from EXACTLY that candidate.
Do not mix internal metadata into reader-facing pages.

### CONTENT_APPROVED
Owner approves the exact candidate and genuine content/brand decisions.

### FROZEN_CONTENT
Create `CONTENT_FREEZE_MANIFEST`.
Hash-lock the content.
Production/layout cannot silently rewrite it.

### PRINT_READY
Requires real-template rendering/preflight and target-platform proof/Previewer/physical proof as required.

### RELEASE_AUTHORIZED
Requires explicit owner authorization.

## GITHUB / DURABLE STATE

Every meaningful slice must leave a durable checkpoint with:
- exact branch/HEAD;
- base snapshot/hash;
- master path/hash;
- changed segment IDs;
- reason;
- agents/reviewers used;
- QA/CI state;
- remaining issues;
- owner gates.

If GitHub/write tools fail:
- do NOT continue accumulating invisible edits in chat;
- last durable checkpoint remains authoritative;
- resume from that durable state later.

Do not claim a check as PASS when it did not run. Use NOT RUN / PENDING.

Do not mutate central RSE priorities.

## HANDOFF TO BOOK PRODUCTION

Only after `FROZEN_CONTENT` hand the book to RSE Book Agent v3:

`FROZEN_CONTENT → BOOK_MAP → LOCK GRAPH → TEMPLATE/ASSET SLOTS → DETERMINISTIC PAGE BUILD → PDF → VISUAL/PREFLIGHT QA → PRINT_READY → RELEASE_AUTHORIZED`

If one page needs a later text change, formally unlock the affected segment and its dependency closure only.
No global unfreeze.

## DEFINITION OF DONE FOR CONTENT

Stop creative editing when:
- every source/required segment is accounted for;
- BLOCK = 0;
- material FIX = 0;
- meaning/facts/mechanics are correct;
- safety/consent is correct;
- logic/continuity PASS;
- repetition/function distribution PASS;
- native language PASS;
- premium book register PASS;
- audience/anti-cringe PASS;
- humor/voice PASS;
- proof PASS;
- exact-hash owner-read candidate exists;
- previous frozen versions remain unchanged;
- open owner-only decisions are clearly isolated;
- exact QA/CI status is recorded honestly.

When a full audit finds no substantive defect:
**STOP REWRITING.**

Do not manufacture more changes.

## REPORT TO ME

After the first run, tell me:
1. which route you selected;
2. where the durable source/baseline was saved;
3. what versions were found/converged;
4. what is protected in GOLDEN_KEEP;
5. top book-wide defects found;
6. highest-value first bounded slice;
7. branch/HEAD and QA state;
8. what, if anything, genuinely requires my decision.

Then continue execution through safe bounded slices rather than stopping for ordinary editorial choices.

Do not merge main, freeze publication state, publish, or cross a genuine owner/legal/physical-proof gate without my explicit authorization.

---