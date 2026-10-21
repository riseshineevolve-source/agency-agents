# Source comparison and protected mechanics

The explicitly authorized current source is `upload/DETECTIVE_ACADEMY_EN_20261021_225P.pdf`, SHA-256 `9db84d4f138cbbde8eb1f4a0f783f4d126c639120a11cabb65fc00711b9f05a0`, 225 physical pages. The 115-page V10 source is comparison evidence only. This audit does not grant a content freeze or print approval.

Both complete text extractions were read. Current raster pages 1–18 were recovered through OCR and then independently visually transcribed by the voice reviewer in `frontmatter-verified.json`. Every current puzzle/evidence page was rendered and visually inspected, including the paired Case03 photographs. No map or puzzle was modified. The original PDF is the immutable authority for all figure pixels and page geometry.

## Material version differences

| Function | V10 physical pages | Current physical pages | Current authority to preserve |
|---|---:|---:|---|
| Front matter | 1–19 | 1–15 | Shorter designed text, including changed orientation and different Case Wall dialogue. Current p6 calls the team six detectives; character bios and finale distinguish five field detectives and archive mentor Bibi. |
| Case01 | 20–22 | 16–18 | Title changed from THE ENVELOPE THAT ARRIVED BEFORE THE MAIL to THE ENVELOPE THAT WAS NEVER DELIVERED. QUILL's old fixed B1 clue becomes row1; a separate KNOX columnD clue replaces the redundant distinct-row/column clue. Same final placements and KNOX D2 answer. Current hints and solution explain the revised deduction. |
| Case03 | 25–26, 88 | 22–26, 183–184 | Entire ten-difference inventory was redesigned. The 017/071 reference remains; the other current locations are centre cushion, shield rim, ring award, phone base, recorder front, pen, right crystal, piano pedals and shelf camera. Current piano pedals are A2/B3; V10 was A3/B2. |
| Trophy/Heritage continuity | 27, 31 | 27, 36 | Current prose explicitly identifies 017 as current Trophy Hall reference and 071 as an older linked Heritage intake file; it is not a typo. |
| Local case follow-up | 29 onward | 30 onward | Current transitions often name the earned companion instead of a generic follow-up; preserve who provides each answer. |
| Case12 | 41, 43, 97 | 60, 65, 197 | Current text distinguishes access-like words from an ordinary rehearsal cue and explicitly closes the password-leak question. |
| Case24 callback | 60 | 112 | V10 linked the tread to a Case03 shoeprint difference. Current Case03 has no shoeprint difference; current Case24 removes that obsolete callback. Never restore it. |
| Case26 | 62–64 | 120–124 | The same fourteen selected maps, Case01 exclusion, retained placements and CHECK THE OLD MAP extraction survive. Current evidence list is on p123. |
| Final panel | 70–72, 84, 115 | 137–143, 159, 168, 177, 225 | RULE WORD replaces the ambiguous V10 METHOD label. It still means ASSUMPTIONS, not the whole rule sentence. Other inputs remain D3, the six-symbol code and the reader's existing call sign. |
| Route explanation | 71–72 | 140–143 | Current wording explicitly limits the system to marking/matching/routing/verifying real cases and reopening archived material; it cannot create cases, select a suspect or solve the investigation. |
| Archive hook | 75 | 146–147 | V10 revealed a matching triangular award mark as Case03 difference8. Current difference8 is a crystal, so current hook uses the 017/071 archive trail instead. The new file's triangular symbol remains, but no matching mark in the photographs is claimed. |
| Navigation | various | 148–149 | A current physical index maps every case to story/board/puzzle, all three hints and its solution. There are 30 solution texts and 16 solution-map plates. |

## Verified mechanics inventory

`truth-and-mechanics-lock.json` records all 30 cases, their objectives/evidence/solution locators, exact solution text and answer strings, all 107 placements from the 16 solution maps, the four controlled plain-zero records, current Case03 differences, all numeric mini-puzzle data, the fourteen empty-room initials and the finale dependency graph. `source-page-map.json` covers every physical page exactly once. `intake.json` is the original text-block baseline; `intake-v2.json` adds visually verified front matter without changing existing pp19+ IDs.

The six-symbol puzzle was independently enumerated across all 720 permutations: exactly one sequence satisfies its six clues, BALL–STAR–BOLT–HEART–KEY–MOON. Clock conversion and route arithmetic were checked against printed evidence. This audit does not claim an independent exhaustive constraint solve of every illustrated map; all map geometry and printed solution placements remain protected.

## Confirmed source defects and narrow repair boundaries

- **p80:** The narrative promises Bibi's younger handwriting and then leaves the body blank. The heading contains RULE0FIRST, and p82 supplies the line later; p81 asks the reader to copy it immediately. The exact locked line `RULE 0 FIRST` may be added after the existing colon.
- **p9 / p143:** The current recruit page omits the earlier five-badge rack and empty-hook06 setup retained in V10, while p143 still calls back to the rack the reader supposedly saw. A bounded narrative setup repair is appropriate; the recruit form stays unchanged.
- **p122 / p123:** The instruction says the selected cases are listed on this page; the list actually appears on the following evidence page.
- **p131:** The current RuleZero evidence page has no Case Wall save instruction, though later retrieval expects the earned rule. Add an instruction outside the puzzle artwork, on the preceding narrative/instruction page, preserving the exact rule and destination.
- **p158:** Hint1 retains a production note that final pagination is assigned only after layout despite the completed physical index. Only that production aside may be removed; actual hints and case numbers stay protected.
- **p6:** Six detectives compresses five field detectives plus Bibi's separate archive-mentor role. The finale depends on five active field detectives, Bibi as mentor and the reader earning field position06. Clarify the introduction without adding a seventh existing field member.

The current p11 map introduction has less explicit legend prose than V10, but actual puzzle legends still display usable-floor circles, blocked-object squares, walls and doorways. Do not silently import the V10 prose or change the current legends.

No English-to-Polish translation, source-art change, content approval, publishing or release action was performed.
