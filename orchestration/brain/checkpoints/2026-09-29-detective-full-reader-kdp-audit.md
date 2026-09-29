# Detective Academy Book 1 EN — Full 181-page reader + KDP audit

Date: 2026-09-29
Authority: Central RSE Technical Orchestrator
Artifact reviewed:
`HMDA_Book1_EN_FINAL_VISUAL_POLISH_OWNER_REVIEW_2026-09-29.pdf`

Artifact SHA-256:
`4d50a3f5af30a19acadfbec6e0d0d907d60efcacd47da7db90812c8e8f8756d1`

Artifact pages: 181
QA JSON status: PASS
Canonical V3 source commit:
`e8e97f5738f9e37887b7b788cd67161bbd3c9bf3`
Canonical V3 blob:
`c10c6d20456d75df6e952f9d2d3e1d9a6637b221`

Status:
**FULL READER AUDIT COMPLETE / BLOCKED ON BOUNDED FINAL FIXES / EN NOT FROZEN**

## What passes

- Current final V3 story copy is present; 714/714 checked fragments in supplied QA.
- 15/15 spatial cases remain unique-solution according to supplied QA.
- Spatial Witness Board LEFT -> Live Case Map RIGHT parity is correct for all 15 cases.
- Correct V3 reader-facing Witness Board copy is printed; raw Shigai victim/thief wording no longer leaks.
- Case 03 has correct Photo A/B facing spread and exactly ten tracker marks.
- Case 06 includes Uma incident bridge + restored Roman-spoon humor.
- Happy Makers normal-case chats are single-flow COMMS panels.
- Evidence Grid signature motif is now coherent and modern.
- Room Zero debrief has reader-facing headings and COMMS panels.
- Case21 -> Case26 -> Case27 -> Rule Zero -> D3 -> Case30 causal chain is intact.
- Bibi trainee-route-note reveal and Archive File 001 triangle callback are intact.
- Reverse Hint Vault/Solutions are physically reversed and legible after rotating the book.
- Page size is Letter, PDF unencrypted, no XFA; gutter/margin geometry passed local audit.

## Reader/puzzle blockers that QA did not catch

1. **Case 11 page 47** prints literal HTML `<br/>` in records. Convert to real line breaks.
2. **Case 09 page 41** gives away the visual-classification puzzle by labeling evidence as `plain Academy 0`, `striped circle`, `ring with pointer`, `no Academy mark`. Render record labels + actual symbol samples without answer labels.
3. **Case 26 page 100** says “write one letter in each of the 14 boxes above,” but no 14 boxes are printed. Add 14 case-indexed letter boxes.
4. **Case 27 page 102** old/current plans do not visibly show the promised old-only sealed room. Make the old plan contain the extra enclosed room while the aligned current plan shows the modern Archive wall/no room; preserve C1/F3/A5 anchors.
5. **Case 28 pages 104-105** instruct the reader to sort cards into three printed zones, but FACT / THEORY / UNSUPPORTED ASSUMPTION zones are absent. Add actual sort zones/assignment surface and make missing-word recovery visually earned.
6. **Case 30 page 113** says DETECTIVE = name from Detective ID, but solution uses OFFICIAL CALL SIGN. Change prompt to the OFFICIAL CALL SIGN from the Recruit Credential. Prefer six visible CODE slots.
7. **Case 08 page 39 / solution** references a route crossing a wall, but the printed evidence does not visibly show route geometry/wall crossing. Either draw the route/wall relation or remove unsupported wall-crossing claim; preserve only evidence the reader can prove.
8. **Case 21 page 81** leaks production edge labels (`zigzag-2 / curve-1`, etc.). Remove debug terminology; the child should match physical tear shapes.

## Narrative/fair-play fixes

9. **Case 01 -> Case 02:** the message to the Case01 intake contact is sent, then the story says “before the reply comes back”; the reply never returns later. Add one bounded closure sentence before Trophy Hall interrupts, confirming no courier / printer released the envelope, without solving Room Zero.
10. **Case 16 page 64:** Evidence 07 explicitly eliminates 1998 and 2008, effectively solving the year. Remove that line; let the child combine printed ranges and dates.
11. **Archive File 001 image page 121:** image contains `BLACKWOOD ACADEMY EST. 1912`, an institution not introduced anywhere in Book 1. Unless this is an explicit Book 2 canon reveal, replace that embedded branding with canon-consistent Old/Detective Academy wording. Do not change the intended missing-person/photo hook.
12. **Fair-play 0 motif:** prior files mostly tell rather than visually seed the plain 0. Where feasible, place the small plain 0 visually on the earlier relevant record/tag/envelope surfaces so Case09 becomes a real callback rather than a labeled classification exercise.

## Lower-priority reader polish

- Case08 route labels are the only detected used text below 8pt (~7.5pt); enlarge to ~9-10pt.
- Repeated Witness Board instruction can be shortened after the first spatial case if desired, but keep enough standalone usability.
- Evidence Grid parity pages are now attractive but numerous; keep parity, avoid turning them into padding.
- Front-matter Happy Makers chats (pages 4 and 9) remain plain bullets rather than COMMS panels; optional consistency fix.
- Field Certification is clear but visually modest for the reward beat; optional subtle seal/hook/grid treatment.

## KDP-specific technical fixes before Previewer

- Case03 Photo A/B effective print resolution was measured at ~209 DPI. Page3 squad image ~293 DPI. KDP recommends images at least 300 DPI. Use higher-resolution source or deterministic print derivative/upscale without changing composition/art.
- Signature grid/vector strokes include ~0.22pt lines. KDP submission guidance says lines should be at least 0.75pt / 0.3mm. Raise signature/functional grid and line-art strokes to print-safe width where appropriate.
- Manuscript has 181 pages. KDP rounds odd page counts up to an even number, so production/spine calculation is effectively 182 pages. Prefer an intentional final p182 rather than relying on an automatically inserted blank.
- Used Arial/Arial Bold are embedded; an unused Helvetica resource remains unembedded. Strip the unused resource for a cleaner final file if practical.
- Current inner-content distance is >= ~45pt / 0.625in, so the 151-300-page KDP 0.5in minimum gutter requirement is met.
- Reverse upside-down Hint/Solution design is acceptable as a puzzle-book treatment; preserve.

## Next action

Do not reopen story architecture or redesign the book.

Apply only the bounded fixes above to the current 181-page working tree, preserving all current V3 text except the explicitly listed micro-corrections. Then:
1. rerun all existing V3/reader/unique-solution/parity/hash/reverse audits;
2. render every page;
3. human visual review of every contact sheet + enlarged changed pages;
4. KDP Previewer;
5. representative physical proof;
6. explicit owner EN freeze;
7. final cover/spine based on frozen even KDP page count;
8. owner-controlled publication.

No merge, EN freeze or KDP publication is authorized by this checkpoint.
