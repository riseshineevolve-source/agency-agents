# HMDA V7 Final Review — Issue Ledger

Mode: FINDINGS ONLY  
Master edited: NO

Severity:
- BLOCK = cannot certify/freeze accurately
- HIGH = material story/logic/experience issue
- MEDIUM = meaningful quality improvement
- LOW = polish
- KEEP = explicitly protect

## BLOCK

### FR-BLOCK-01 — Owner-read artifact is not exact canonical V7
The downloadable V7 PDF/TXT generated earlier contains stale text that differs from canonical GitHub V7.
Examples: stale Case01 hints/solution; stale Case21 chat; stale page-9 language.
Impact: owner could approve a different manuscript from the canonical master.
Decision required later: regenerate owner-read artifact only after final fixes, from exact candidate hash.

### FR-BLOCK-02 — Case03 final exact-ten visual is unresolved
The story, hints and delayed callbacks require one exact final A/B pair. Current experimental images are not approved.
Required locked visual facts include:
- 017 / 071;
- a tread/shoeprint element usable as a Case24 resemblance callback;
- a triangle-pattern difference usable as the post-Book1 Archive File 001 callback;
- exactly ten unambiguous differences at print size.
Impact: Case03, Case24 visual callback, Case06 routing payoff and Book2 stinger cannot all be certified until this closes.

### FR-BLOCK-03 — Case03 Hint/Solution package cannot be certified before final art
Hints and solutions currently name specific differences. Any visual redesign makes them potentially stale.
Required later: derive final solution crop/labels from the exact locked A/B, not from prose memory.

## HIGH

### FR-HIGH-01 — Badge / envelope / credential canon is not converged
Current opening: black envelope containing blank Recruit Credential.
Case01 title: THE BADGE THAT ARRIVED BEFORE THE MAIL.
Later Room Zero thread: recruit badge record.
Case09 Level3: opening badge.
Impact: a child can reasonably ask where the badge came from.
Direction later: either visibly establish a badge in opening canon or rename/reword all stale badge references.

### FR-HIGH-02 — Case02 Happy Makers chat contradicts revised story state
Cup is already back. Chat says "Trophy rescue kit" and "before you rescue the trophy."
Impact: dialogue no longer reacts to the actual scene.

### FR-HIGH-03 — Case02 local mystery overpromises "who returned the Cup?"
Puzzle finds Max's companion and narrows a time window, not the person who physically returned the Cup.
Impact: title/hook may create a question Book1 never closes.
Direction later: either explicitly close the return or clearly frame the case as an undocumented-return-window mystery.

### FR-HIGH-04 — Case03 photo anomaly has no Book1 explanation
Two files are described as copies of the same photograph but contain ten differences.
Impact: this is too large an anomaly to read as ordinary file noise. If intentional, it should remain explicitly unresolved; otherwise it feels like a dropped mystery.

### FR-HIGH-05 — Contact-case consequence chain is incomplete
Reader-facing story does not clearly cash the witness follow-up in several cases:
- 13 camera,
- 17 ticket,
- 19 scanner,
- 20 paint,
- 22 instrument cases.
Impact: puzzle can feel like an isolated worksheet even when Solution Files claim it mattered.

### FR-HIGH-06 — Case17 belonging regression
At MASTER rank: station worker asks "You're detectives, right?" and Mimi answers "Working on it."
Impact: reader had already become an expected member of the team; this line resets the emotional arc.

### FR-HIGH-07 — Case18 title and dramatic question mismatch
Title says THE SEVEN-MINUTE ALIBI, but story mainly tests whether 0:07 is meaningful.
No clear person's alibi is established.
Impact: title promises a different local mystery.

### FR-HIGH-08 — Case05 immediate reward is incomplete
Six-symbol code opens access to an old sealed envelope, but the envelope itself is not meaningfully opened/explained at that moment.
Impact: strong puzzle has a weaker immediate payoff than expected.

### FR-HIGH-09 — Final Hook06 / badge rack lacks fair-play seed
Finale says it is "the same one from intake" and references an empty hook, but current opening does not clearly establish the portable rack with five occupied hooks + Hook06.
Impact: emotionally strong certification detail risks feeling invented at climax.

### FR-HIGH-10 — Final panel field labels do not match inputs
ROOM actually wants coordinate D3.
DETECTIVE actually wants Official Call Sign.
Impact: a grand-final interface should become clearer, not need semantic exceptions.

### FR-HIGH-11 — Finale difficulty does not match rank promise
Locked spatial grades show Case29 boss = 8.2 while Cases13 and23 = 8.4.
Case30 is mainly retrieval.
Impact: Grand Master / Grand Final is narratively grander, not mechanically hardest.

### FR-HIGH-12 — Difficulty progression is non-monotonic
Case13 expert 8.4 -> Case15 hard 6.7.
Impact: rank progression FIELD AGENT -> MASTER does not map cleanly to challenge growth.

### FR-HIGH-13 — Finale explanation is too long before certification
The Room Zero explanation is logically coherent but lengthy and recap-heavy.
Impact: reveal energy may peak, then sag before the badge/certification reward.

### FR-HIGH-14 — Map preservation payoff is underused
Page11 explicitly tells reader not to erase final placements. Later story sometimes frames keeping whole maps as a new/special choice.
Impact: misses a powerful "this is why we told you to keep them" payoff.

## MEDIUM

### FR-MED-01 — Spatial companion mechanic fatigue
15/30 cases are spatial and most prefinal spatial cases ask for a same-room/area contact.
Case26 justifies the repetition, but the middle/late experience can still feel mechanically samey.

### FR-MED-02 — Case28 missing-word task is too telegraphed for FINAL rank
ZERO ______. NOTICE FIRST. THEORIZE SECOND. strongly suggests ASSUMPTIONS.
The sort is the real puzzle; missing-word field adds little final-stage difficulty.

### FR-MED-03 — Case26 navigation burden is production-critical
Fourteen old maps must be reopened in case order.
Without excellent page navigation / lookup UX, a brilliant meta puzzle can become tedious flipping.

### FR-MED-04 — Case27 needs real print usability test
Overlay logic is machine-sound, but physical usability must prove a child can align/compare the plans in a paper book.

### FR-MED-05 — Opening-to-first-puzzle latency
Current intro occupies roughly 15 pages before Case01.
Not automatically wrong, but must be tested with a fresh child reader for skip/abandon risk.

### FR-MED-06 — Dense intro prose for low end of 8-12
Case04 is the strongest flag; Cases07,12,14,17,22 also carry comparatively dense causal sentences.
Direction later: split syntax, not ideas.

### FR-MED-07 — Humor pattern repetition
Frequent structure: Alio/Dilo proposes dramatic idea -> Luli/Mimi corrects.
Risk: reader predicts punchline before it lands.

### FR-MED-08 — Nini has less decisive investigative agency
Nini is warm/useful but less often the person whose observation changes the route of investigation.

### FR-MED-09 — Case22 humor weaker than baseline quality
"case is closed / instrument case" pun feels more generic than the book's best character humor.

### FR-MED-10 — Some Solution WHY IT MATTERS lines outpace main-story causality
Back matter sometimes tells a clearer consequence than the reader-facing next scene shows.

### FR-MED-11 — Case03-to-Case24 tread callback must remain resemblance, not identity
Current concept correctly says resemblance is not proof. Final art/copy must not accidentally imply same shoe/person.

### FR-MED-12 — Book2 stinger quality depends on exact seed
Triangle callback is excellent only if triangle difference is unmistakably present in the final Case03 evidence and was not retrofitted after the fact.

## QA / TEST COVERAGE FINDINGS

### FR-QA-01 — Spatial uniqueness PASS
All 15 locked spatial cases: exhaustive independent unique solution PASS in current Book Factory validation.

### FR-QA-02 — Case01 uniqueness and clue necessity PASS
Current six clues: one solution KNOX D2.
Ablation: removing any one clue produces multiple solutions.

### FR-QA-03 — Case05 unique solution PASS; one redundant clue
Unique code:
BALL -> STAR -> BOLT -> HEART -> KEY -> MOON.
Removing "KEY is not first or last" still leaves one solution.
This clue is not needed for uniqueness.

### FR-QA-04 — Spatial clue minimality is untested
Current machine suite proves unique final solution, not whether each individual clue is necessary.
Status: TEST COVERAGE GAP, not puzzle failure.

### FR-QA-05 — Visual/physical puzzle truth needs rendered-asset QA
Cases 03,09,11,14,16,21,24,27,28 cannot be certified solely from text/answer declarations; final evidence surfaces must match solution truth.

## KEEP REGISTRY

Protect unless a concrete defect requires a bounded change:
- Page03 black-envelope hook.
- Recruit Credential agency.
- Five field detectives + Bibi mentor.
- Mimi phone payoff into Case11.
- 017/071 -> Heritage.
- Case08 route continuation.
- Case09 Bibi "remember vs know."
- Case14 wrong memory != lie.
- Case16 Bibi photograph and hat.
- Case18 false 0:07 and Dilo correction.
- Case21 printer cough / torn-note suspense.
- Case24 mud beats arrow.
- Case25 Archive Restoration parcel -> overlay tools.
- Case26 14 maps -> CHECK THE OLD MAP.
- Rule Zero exact meaning.
- Case29 D3.
- Bibi route-note authorship.
- Field Slot06 certification.
- Book2 triangle callback concept, subject to visual seed lock.

## Overall gate

CONTENT_APPROVED: NO  
FROZEN_CONTENT: NO  
PRINT_READY: NO

Recommended later implementation style:
bounded patches by issue cluster, then dependency-closure QA; no global rewrite.
