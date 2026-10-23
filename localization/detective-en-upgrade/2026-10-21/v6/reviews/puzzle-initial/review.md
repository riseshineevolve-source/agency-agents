# Independent initial mechanics review for Detective EN V6

Scope: owner-authorized corrections to Cases 02/03/07/10/15/20 only. This is a mechanics/source-dependency review, not review of a final V6 candidate (root has not yet supplied that candidate/hash). Root remains sole candidate writer. No product art, renderer, source, old report, or candidate was modified.

Original authority: `upload/DETECTIVE_ACADEMY_EN_20261021_225P.pdf`, SHA256 `9db84d4f138cbbde8eb1f4a0f783f4d126c639120a11cabb65fc00711b9f05a0`. Baseline candidate V5 SHA256 `9ebae1eabafe2f5ed92c38c2ad7b858a9c85d573b5a7e92c4fb08f1c5810a978`.

## Independently enumerated repair models

`independent-enumeration.py` is a new backtracking implementation. It uses prior source-pixel room/object transcriptions, does not call old solvers, and never restricts domains with printed expected solutions. Expected rosters are compared only after full enumeration. Full roster uniqueness, not merely requested-contact stability, is checked.

Nine tested models all yield exactly ONE complete assignment, each identical to the intended printed roster:

- Case02 outer GRID corner and shared-edge beside, with/without same-room restriction.
- Case07 explicit C2 distance anchor and all visible wheeled-case candidates A1/D1/D6, shared-edge beside, with/without same-room restriction.
- Case10 visible wheeled robot arm at B6 instead of charging pod, all other beside relationships shared-edge, with/without same-room restriction.
- Case15 shared-edge beside within SAME ROOM and NE offsets independently positive.
- Case20 explicit lower-row Sid, lower-row/right-column Pax, touching-diagonal Luca/Asa, with either E7-only or both E7/F7 corrected to usable bunks.

Results and full placements are in `independent-results.json`.

## Exact proposed local rule text

Place a local rule in each repaired map's instruction box, rather than silently changing the whole book:

> In this case, “beside” means one square up, down, left or right, in the same room. Diagonal squares and squares across a wall do not count.

This works for Cases02/07/10/15 and preserves the sole intended roster in all independently tested cases. Do not apply this definition to “diagonally next to”, which is a distinct relationship, or to all other map cases without separately reviewing their constraints.

For Cases07/10 distance:

> Count grid steps by adding the row difference and the column difference. This measures position on the grid, not a walking route through doors.

For Case15 direction:

> North-east means at least one row higher and at least one column to the right. The two distances do not have to be equal.

## Case02

- `page020.block08`: **03\nRook was in a corner of the whole grid, directly beside a teacher’s desk.\n**
- `page020.block04`: add local beside rule. Optional marker-led key avoids confusion between usable desk chairs and blocked teacher desks: empty floor/white-circle furniture usable, black-square objects blocked.
- Dependency closure: clue p20, map21, hints152/161/170, solution181/map182. Existing hint statements and solution placements remain true. If desired, `page161.block08` can say “outer-grid-corner/desk clues” but this is not required for correctness.
- Unique roster: NovaB3, DaxD2, RookA6, AtlasF4, IvyC5, MaxE1. Answer DaxD2.

## Case07

- `page042.block08` + `page042.block09`: **03\nWilla was exactly 2 grid steps from the metal frame at C2. Add the row difference and the column difference.\n** (split according to stable-ID/layout contract).
- This is an EXPLICIT OWNER-AUTHORIZED REPAIR choosing a new precise anchor. Never claim source pixels identified C2 as the old “stage range marker”.
- `page042.block10`: **04\nZoe was against an outer wall and directly beside a wheeled equipment case.\n**
- All three visible cases A1/D1/D6 are admitted. No need to identify D6 in the clue or reveal ZoeC6.
- `page042.block04`: add local beside rule, remove obsolete “range” vocabulary and use actual objects: wheeled equipment cases, metal stage frame, light strips, palms, pianos, washers. Marker-led key also valid. Old “buffet” is not visually an independently identified item.
- `page190.block11`: replace “beside the costume cart” with “beside a wheeled equipment case” (same C6 position, same plot).
- Hints153/162/171 contain no stage-range/charging terminology and stay true. Map43/solved191 need no geometric change if text expressly identifies frameC2.
- Unique roster: BlazeA3, IndigoD2, WillaB1, ZoeC6, RocketE5, GrayF4. Answer ZoeC6.

## Case10

- `page054.block08`: **03\nWyatt was in column B, directly beside the wheeled robot arm.\n**
- Visible robot arm is B6. This is visually distinct from the standing robot A5 and tall circle-marked boxes A4/B3. No witness coordinate is given away. If layout uses object labels, “ROBOT ARM” at B6 could reinforce the referent, but text plus visibly unique object is sufficient for this model.
- `page054.block03` or `page054.block04`: add local beside rule. Marker-led key can eliminate legacy cryopod/charging-pod vocabulary. Keep all other referenced demo-seat, coolant-tank, console, parts-crate identities intact or label them visibly.
- `page154.block07` HINT1 MUST change: **Wyatt has the tightest starting clue: column B plus the wheeled robot arm.\n**
- Hints163/172, solution194/map195 and narrative54 parent remain valid. No new alias/charging reference should remain for this clue.
- Unique roster: EmberD5, NicoF6, WyattB7, FinnA2, BeckC1, VeraG4, DashE3. Answer EmberD5.

## Case15

- `page074.block04`: add local beside rule and explicit north-east definition above, applying to BOTH Harper and Piper.
- `page074.block07`: **01\nHarper was north-east of Cruz.\n** is sufficient with rule box; retaining existing expanded wording also works, provided unequal positive offsets remain permitted.
- `page074.block08`: Piper NE Duke stays true under same definition.
- `page074.block10`: **04\nCruz was directly beside a camp cot in the same room.\n**
- `page074.block12`: **06\nInez shared a room with a cot but was not directly beside that cot.\n**. Root should decide whether redundant local-rule repetition merits space; current statement is semantically adequate once rule box exists.
- Natural same-room restriction excludes CruzB7 across wall from cotC7 and CruzB3 diagonally across wall from cotC4.
- Hints155/164/173, solution202/map203 unchanged positions remain valid.
- Unique roster: HarperD2, PiperF4, DukeE5, CruzC3, JettG7, InezB6, MiloA1. Answer HarperD2.

## Case20

- Authorize all same visible bunk shapes E5/E7/F7 as **usable cadet bunks**, with white-circle markers; E7/F7 black markers need correction in map97 and solvedmap211. Both newly usable E7/F7 still give exactly ONE intended roster. This is more coherent than arbitrarily treating identical F7 as a blocked sleep pod.
- `page096.block03`: explicitly identify cadet bunks E5/E7/F7 as usable (or a small visual object key). D1 is the different capsule silhouette and remains blocked sleep pod. No reason to change existing room geometry, furniture, or witness positions.
- `page096.block05`: **01\nSid was in a lower row than Pax.\n**. “South of” must not imply same column, because global distinct-column rule forbids that.
- `page096.block06`: **02\nPax was in a lower row and a column to the right of Mara.\n**. Better rule-box wording can add: “The row and column distances do not have to be equal.” An exact45-degree diagonal is incorrect for intended D4→F5.
- `page096.block07`: **03\nLuca was one row and one column away from Asa.\n** or retain “diagonally next to” with same explicit definition. This is a coordinate relationship and CAN cross a room boundary; do not impose Case15 same-room beside rule here.
- `page165.block11` HINT2 currently says “north/south chain”; optional align to “lower-row relationships”, while names and reasoning stay true.
- Solution210 and solved211 expected roster unchanged. New art does not change Case26 empty-room initials: SupplyRoom already contains SidE7 in intended roster, and F7 being usable introduces no new witness placement.
- Unique roster: MaraD4, AsaB2, LucaA1, TobyC6, PaxF5, SidE7, DemiG3. Answer PaxF5.

## Case03

Owner specifically removes captions' numbers and chronology: `page024.block04` **PHOTO A\n**, `page025.block04` **PHOTO B\n**. Preserve internal photograph labels017/071 as one of ten differences, solution183 and subsequent archive trail. The chapter headers already say PHOTOA/PHOTOB; shorter black-bar labels remain useful if visually desired. No earlier/later/current/archived wording should remain in either PHOTOA/B caption.

## Limits / next review

This review confirms corrected mechanics models and dependency IDs, not final candidate language or map-patch pixels. Once root has exact V6 candidate/hash, check actual changed wording against these model definitions, source-preservation allowlist and diagrams. Confirm that actual white circles replace E7/F7 on both unsolved and solved artwork, with no other art changes.
