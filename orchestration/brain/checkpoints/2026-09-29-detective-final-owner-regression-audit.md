# Detective Academy Book 1 EN — Final owner regression audit of 180-page bounded build

Date: 2026-09-29
Authority: Central RSE Technical Orchestrator
Artifact:
`HMDA_Book1_EN_FINAL_BOUNDED_READER_KDP_OWNER_REVIEW_2026-09-29.pdf`

Verified SHA-256:
`5212f7c3ebc4c5228516c18c31be84a54eaf0d147a1e439150225b4f5192aa22`

Pages: 180
Status:
**FULL 180-PAGE HUMAN/READER AUDIT COMPLETE / FOUR READER BLOCKERS + ONE KDP ORIENTATION BLOCKER REMAIN / EN NOT FROZEN**

## Audit method

- independently verified SHA;
- rendered all 180 physical pages;
- visually inspected all 9 main contact sheets;
- rotated pages 121-180 upright and visually inspected all reverse Hint/Solution contact sheets;
- enlarged critical puzzle/finale pages;
- independently checked PDF preflight, page size, font resources, image DPI, vector line widths, minimum text size and grayscale image pixels;
- reread the main 30-case chain + Hint Vault + Solution Files for reader solvability and cause/effect continuity.

## What passes

- 180 even pages, Letter 612x792 pt;
- openable, unencrypted, no XFA;
- min effective embedded-image DPI ~312.768;
- all embedded RGB images are pixel-grayscale (R=G=B);
- minimum detected vector line width 0.85 pt;
- used Arial / Arial Bold embedded;
- smallest detected text span 8 pt; normal reader copy larger;
- inner text/image margin ~45 pt / 0.625 in, above KDP 151-300-page 0.5 in minimum;
- current V3 story, Room Zero chain, Case03, Case05, Case21, Case26, Rule Zero, D3, Bibi reveal and Archive File 001 callback remain intact;
- Case09 symbol evidence no longer semantically prints the answer;
- Case11 HTML/debug leak removed;
- Case16 explicit answer-giving Evidence 07 removed;
- Case21 debug tear names removed;
- Case26 has 14 case-indexed extraction boxes;
- Case27 old-only room vs current Archive wall is visually present;
- Case28 has visible FACT/THEORY/UNSUPPORTED ASSUMPTION sorting zones;
- Case30 asks for OFFICIAL CALL SIGN and has six code slots;
- fair-play 0 tags are visually seeded on Case02/04/05;
- Archive File 001 image now uses OLD ACADEMY rather than Blackwood;
- reverse Hint Vault/Solutions are legible when book is rotated.

## Four remaining reader blockers

### 1. Case01 is not fully solvable from the printed candidate set
Page 13 names QUILL, PIP and MORSE but never prints KNOX as the fourth helper candidate. The solution/hint require KNOX.

Fix:
add an explicit visible helper roster on the Case01 intake board:
`QUILL / PIP / MORSE / KNOX`
without adding a direct Knox placement clue.
Optional aligned fair-play seed: add `RECRUIT BADGE RECORD 0` to the Case01 file/intake surface so the four Case09 records have all been visibly seen earlier.

### 2. Case Wall page 9 is functionally too small and contains an unused decorative zone
The current page has small write-in zones, but later explicit saves require:
- MATCHING MARKS: one 0 + four record names;
- MESSAGES/RULES: RULE 0 FIRST; THE ANSWER IS IN WHAT YOU LEAVE EMPTY; CHECK THE OLD MAP; ZERO ASSUMPTIONS. NOTICE FIRST. THEORIZE SECOND.;
- CODES/COORDINATES: six-symbol code + D3;
- OPEN QUESTIONS: initial system question + Bibi recognition note.
The FALSE LEADS zone is never explicitly used.

Fix:
keep Case Wall physically on page 9, remove FALSE LEADS, and reallocate the abundant unused lower-page space so an 8-12-year-old can write all required saved items at normal handwriting size. MESSAGES/RULES must be the largest zone.

### 3. Case08 still claims a wall-based route failure that the reader cannot prove
Case08 story/rules still say one route attempts/crosses a wall, but page39 provides no route geometry demonstrating a wall crossing. Current solution correctly eliminates A by closed Paint Corridor and B by locked Staff Stairs.

Fix preferred:
remove the unsupported wall-specific claim from story/rules/WHY IT MATTERS and keep the puzzle based on the two printed hard restrictions:
A = closed Paint Corridor;
B = locked Staff Stairs;
C = valid open route.
Preserve humor without requiring unseen geometry.

### 4. Case24 asks for FROM/TO locations that are absent from its evidence
Page93 shows Print1-4 and mud values, but no EAST PATH / WEST GATE endpoint labels. The Solution File expects EAST PATH -> WEST GATE.

Fix:
label the two ends of the printed four-print sequence:
left / Print1 end = EAST PATH
right / Print4 end = WEST GATE
(or draw a minimal path strip with those endpoints).
Do not state the direction; mud fading must still determine it.

## KDP orientation blocker discovered in full audit

The current reverse Hint Vault / Solution Files use full-page 180-degree rotation on physical pages 121-180, including headers and page numbers.

Current official KDP paperback guidance says all pages and content must use the same orientation. It allows *some* upside-down text only when the rest of the page remains right-side up (example: upside-down riddle answers on an otherwise upright page).

Therefore the current full-page reverse section is a material KDP compliance risk and must not be represented as publication-safe before KDP Previewer.

Safest production fix:
- keep pages 121-180 physically upright;
- preserve the STOP // HINT VAULT divider and back-of-book anti-peek structure;
- retain the same Hint Vault levels, Solution Files, maps and copy;
- do not rotate full page content.

Alternative only if owner explicitly accepts risk:
- test current orientation in KDP Previewer before changing it, but do not freeze/publish unless Previewer and proof both accept it.

## Low-risk final technical cleanup while rebuilding

- remove unused unembedded Helvetica PDF resource if practical;
- update PDF metadata title away from “V3 Interior Proof” to final Book 1 title/owner-review designation;
- preserve >=300 effective DPI and >=0.75pt functional/signature line widths;
- preserve 180 even page count unless the bounded fixes naturally require another even count;
- no new creative redesign.

## Gate

Do NOT move to EN freeze or publication yet. Resolve the four reader blockers and the reverse-section KDP orientation risk before treating the interior as KDP-ready.
After only these four reader fixes:
1. rebuild with exact same private inputs;
2. deterministic QA/regression;
3. Central rechecks Case01, page9, Case08, Case24 plus whole-artifact contact sheets;
4. if clean -> KDP Previewer;
5. representative physical proof;
6. explicit owner EN freeze;
7. final spine/cover;
8. owner-controlled publication.

No merge, EN freeze or publication authorized here.
