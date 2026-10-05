# HMDA V7 — Puzzle / Hint / Solution Final QA Review

Mode: REVIEW ONLY
Scope: puzzle truth, uniqueness, clue necessity, hint scaffolding, solution consistency, final difficulty.

## A. Machine-backed puzzle truth

Current RSE Book Factory v2 source validation proves:
- 15/15 locked spatial cases independently solve to exactly one solution;
- source geometry is preserved;
- blocked/occupiable semantics are preserved;
- witness count/name/order is locked;
- answer identity and coordinate match source;
- Case26 extraction uses exactly 14 selected spatial maps and spells CHECKTHEOLDMAP;
- Case01 is excluded from the 14-map extraction;
- Case29 is excluded from the 14-map extraction and instead supplies D3.

Spatial cases:
02,04,06,07,10,12,13,15,17,19,20,22,23,25,29.

## B. Case01 independent exhaustive test

Current V7 clues:
1. QUILL B1.
2. PIP row 3.
3. MORSE column C.
4. all helpers use distinct row and distinct column.
5. PIP is left of QUILL.
6. MORSE is in a lower row than KNOX.

Exhaustive result:
- QUILL B1
- PIP A3
- MORSE C4
- KNOX D2
- solution count: 1

Clue ablation:
- remove clue1 -> multiple solutions
- remove clue2 -> multiple solutions
- remove clue3 -> multiple solutions
- remove clue4 -> multiple solutions
- remove clue5 -> multiple solutions
- remove clue6 -> multiple solutions

Result: all six current Case01 clues are mechanically necessary.

## C. Case05 independent exhaustive test

Symbols:
BALL, STAR, BOLT, HEART, KEY, MOON.

Constraints:
1. STAR immediately before BOLT.
2. BALL before STAR.
3. HEART after BOLT.
4. KEY not first or last.
5. MOON after KEY.
6. exactly one symbol between HEART and MOON.

Unique solution:
BALL -> STAR -> BOLT -> HEART -> KEY -> MOON.

Ablation solution counts:
- remove 1 -> 19
- remove 2 -> 5
- remove 3 -> 3
- remove 4 -> 1
- remove 5 -> 2
- remove 6 -> 6

Finding:
Constraint 4 is redundant for uniqueness.
This is not a broken puzzle, but it fails the owner's desired "every clue earns its place" standard.

## D. Non-spatial logic evidence

Existing publication logic validation already established forced answers for unchanged mechanics:
- 08 Route C
- 09 true Academy mark classification
- 11 record D outside timeline
- 14 Noah timing impossibility
- 16 Old Academy Annex / 2002
- 18 A -> B -> C -> D
- 21 B -> D -> A -> C / THE ANSWER IS IN WHAT YOU LEAVE EMPTY
- 24 EAST PATH -> WEST GATE
- 26 CHECK THE OLD MAP
- 27 sealed room behind Archive wall
- 28 ASSUMPTIONS / fact-theory-assumption sort
- 30 four prior-answer inputs

Final rendered evidence still has to be checked for cases whose logic depends on visible art/pieces/layout.

## E. Case03 exact-ten dependency

Current V7 Solution Files name ten differences.

The book also requires three long-range functions:
1. 017 / 071 -> Case06.
2. tread/shoeprint resemblance -> Case24 reasoning lesson.
3. triangle-pattern difference -> post-Book1 Archive File001.

Because final Photo A/B is not locked, Case03 status is:
ASSET BLOCK / SOLUTION NOT CERTIFIABLE.

Hard later rule:
The solution page must be generated from / verified against the exact final A/B, not from a remembered list.

## F. Hint ladder audit

Overall:
- Level1 generally points to the best starting observation.
- Level2 narrows domains/logic.
- Level3 gives the strongest nudge and often nearly exposes the answer.
This matches the intended three-level contract.

Known issues:
- Any Case03 hint referring to exact image regions is provisional until art lock.
- Final owner artifact must use canonical Case01 hints matching V7 clues.
- Page references must be generated from final pagination, not inherited historical numbers.

## G. Solution-file audit

Strengths:
- solutions explain reasoning;
- WHY IT MATTERS usually reconnects puzzle to story;
- false lead Case18 is explicitly rejected rather than secretly reused;
- spatial companions are described as leads/contacts, not guilt.

Finding:
For Cases 13/17/19/20/22, WHY IT MATTERS sometimes describes a useful next interview more clearly than the main story actually shows. This is a story-flow issue, not an answer-key error.

## H. Final challenge audit

Narrative escalation: PASS / strong.
Mechanical monotonicity: FAIL / needs review.

Reasons:
- Case13 spatial grade 8.4 appears before Case15 grade6.7.
- Boss29 grade8.2 is below Cases13 and23 at8.4.
- Case28 missing word is heavily telegraphed.
- Case30 is primarily prior-answer retrieval.

The final sequence can still be excellent, but GRAND MASTER / GRAND FINAL currently describes narrative importance more accurately than raw puzzle difficulty.

## I. Required QA before FROZEN_CONTENT

1. clue-ablation test for every spatial case;
2. exact final Case03 A/B + solution lock;
3. rendered witness-board answer-name audit;
4. rendered hint/solution cross-check;
5. physical print test for Case26 navigation;
6. physical usability proof for Case27 overlay;
7. difficulty/progression decision for Cases13/15/29/30;
8. exact owner-read PDF regenerated from final candidate hash.

Current status:
CONTENT_APPROVED: NO
FROZEN_CONTENT: NO
