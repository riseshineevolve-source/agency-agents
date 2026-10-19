# Detective Academy PL — V04 R8 exact-source recovery and Book Factory handoff

Status: **SOURCE INTEGRITY PASS / NOT PRINT READY**
Checked: 2026-10-19
Writer: Polish Localization Engine
Scope: localization metadata and proof handoff only. Full manuscript, illustrations, editorial proofs and owner artwork remain in their authoritative private storage. **Do not use stale V03 REV6 as the current working master.**

## Current newest verified private Library snapshot

Location: /RSE/Detective Academy/PL Versions/V04/

The latest complete available PL editorial family is V04 **R8**, uploaded 2026-10-15 around 18:26 UTC. Unlike the visible public GitHub V04 branch, which contains only a bounded opening pages 03–10, the **private Library R8 is a full text edition**. All these primary bytes were independently fetched and SHA-256-verified:

| Exact Library filename | SHA256 | Result |
|---|---|---|
| DETECTIVE_ACADEMY_PL_V04_R8_NATIVE_READER.md | d547b13c953346b35b8b7910fd94a4819ba680319deede73e5bfdfe41ae148a3 | PASS |
| DETECTIVE_ACADEMY_PL_V04_R8_NATIVE_MASTER.md | 4fdc20d499edb430af322315bdaa21f4502fbe9cbb62ac0c8fab01cc82deefa7 | PASS |
| V04_R8_SEJF_PODPOWIEDZI_90.md | a260d3be8f6589b2ee4dc94284164a4694843768ab7ada6e772df4df8c9082e3 | PASS |
| V04_R8_AKTA_ROZWIAZAN_30.md | b50a54f696e4076344b7ec672378977710d21b148b63b1b0b9aaf7968d9adba3 | PASS |
| DETECTIVE_ACADEMY_PL_V04_R8_READER_OWNER_PROOF_NOT_PRINT_READY.pdf | f6020ebd9485f0ce4b74e9642aedb9f4342a7a132b662c8ee7df4ede73e9658f | PASS; text proof only |
| DETECTIVE_ACADEMY_PL_V04_R8_MASTER_OWNER_PROOF_NOT_PRINT_READY.pdf | 7a04e74b73a8f17cdb99d71ad62df16d211e5fa091072bc1712950dd0749e7c7 | PASS; text proof only |
| V04_R8_INDEPENDENT_TEXT_AND_PUZZLE_QA.json | fd67b04cb5643c1ddc24a34f94356ca8ff6fcb38c53f414ee8b290d6a6591326 | PASS |

The three substantive Markdown parts (Reader, 90 hints, 30 solutions) are each **exact full substrings of the R8 Master**. No new copy or changes to locked puzzle truth made in this recovery.

## Bounded tests and independent evidence

- Historical V04 R8 QA receipt: **59 / 59 assertions PASS**. This includes 30-case reader, 90 hints/3 per case, 30 solutions, Case05 unique 6-symbol answer among all 720 permutations, Case03 017/071 + exactly 10 visual differences as written, Case12 ELIPSA G2, Case14 4 min vs 2, Case21 B-D-A-C, Case26 14 map references, Case28 Rule Zero, Case29 D3, Case30 four earned fields.
- Independent 2026-10-19 hash/structure inspection: 7/7 primary artifact SHA-256 checks PASS; reader 30 ordered cases, hints 30 ordered cases/90 levels, solutions 30 ordered cases; no banned reader-facing **drużyn***; no unused reserve **ZANTA**; exact master component containment PASS.
- Final Room Zero **FOUR original plain black 0-marked materials**, per newer V04 owner production truth. Older V03 SIX-mark expansion proposal is SUPERSEDED for current final R8; do not reintroduce it. This is different from Case05 **six SYMBOLS**, which remains a separate unchanged local puzzle mechanic.
- FINAL70 book-wide naming approval remains: old owner-locked 40 + NEW30 exact assignment; ZYRA assigned, ZANTA unused reserve. See V02_FINAL70_ASSIGNMENT.md and 2026-10-13 NEW30 owner decision. Do not invent or reassign aliases.
- Source convergence: original 2026-10-08 EN V10 freeze applied to its explicitly named Polish source; V03/V04 were subsequently developed from the V12-family owner direction. A future switch to **newest EN print source** is NOT automatic, and requires exact owner-frozen source/hash parity check with current Book Factory.

## Two documentation issues, NOT text-source defects

Existing R8 manifest's recorded SHA-256 values for its **own manifest** and for **V04_R8_OWNER_HANDOFF.md** do not match the independently fetched bytes. Do not edit historical R8 files in place or declare the seven substantive hashes invalid. Archive a new self-consistent external receipt if the handoff needs to be repackaged.

## Actual PDF inspection — new regression finding

- Reader owner-read PDF: **59** pages; US Letter **612 x 792 pt**, no empty/footer-only pages detected.
- Master owner-read PDF: **80** pages; US Letter **612 x 792 pt**; **page 80 contains only the page number "80"**, despite historical QA recording no empty pages.
- Both PDFs: **ZERO embedded illustration image objects**, so neither is the intended illustrated Book Factory/KDP interior. They are text proofs (WeasyPrint-generated).
- Action: a final producer must reject footer-only pages as empty and render the actual designed map/photo/Comms layouts; DO NOT patch/reflow the locked R8 manuscript to cover a text-only PDF pagination defect.

## Explicit external handoff: Detective Book Factory sole layout writer

Feed exact R8 text, hints, solutions and current officially owner-approved image/map manifest into **the existing Book Factory**, with no competing localization page compositor. Verification focus:

1. **Case03:** two real print photos A=017, B=071, exactly 10 visually provable differences, no fake eleventh difference.
2. **Case12:** exact witness/identity visual map confirms ELIPSA at G2; labels fit and preserve reader solvability.
3. **Case21:** four printed fragment shapes/contents actually assemble in the solution order B–D–A–C; no replacement props.
4. **Case26:** all 14 exact Room/old maps and baked captions match printed page and the English phrase CHECK THE OLD MAP; no superficial overlay translations.
5. **Case27:** two source maps overlay correctly to produce the intended proof; no guessed pixel geometry.
6. **Final 0 truth:** four marked records, not six; Case05 six symbols must not be conflated.
7. **Reader-facing Polish:** independent real family 8–12 read-aloud, narrative/character register, every diagram/label translated where appropriate, enough pencil space, no overflows or clipped diacritics at physical US Letter print scale.
8. **Publication gates:** complete KDP interior/cover, physical print proof, owner visual/content approval, explicit CONTENT_FROZEN / PRINT_READY and release authorization.

Do not claim any of these external proofs passed based on textual QA.

## Next safe task

Production/Design (Book Factory): obtain the exact Library R8 artifacts and current owner-approved print templates/assets. Render a single physical PL candidate and inspect only changed or blocked pages; report actual PDF SHA/page count and real visual QA. The Localization Engine remains the **only writer for Polish language changes**; any proven text defect is a bounded source-hash-specific surgical patch with new revision R9, never silent edits to immutable R8. Avoid mass retranslation or invented aliases.

## Control-plane boundary

Only localization-owned checkpoint metadata is written here. No English detective source, product renderer, website, consumer app, marketing master, artwork, puzzle coordinates, or other lane mailboxes were edited by this handoff.
