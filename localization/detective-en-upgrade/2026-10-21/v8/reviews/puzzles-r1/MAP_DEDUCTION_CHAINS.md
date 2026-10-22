# Independently checked map deduction chains

Reviewed baseline candidate SHA256: `df4b39f8793de32ace25998ae2986dfb708ad08a5bb80b6f0b8c0eecef49eeb1`.

These notes are grounded in the actual V7 unsolved figures, not inferred from printed solution coordinates. The independent solver finds exactly one FULL assignment for each of the 16 maps. Some later puzzles require testing a small number of combinations; a short printed explanation should say what is being tested instead of merely saying a person “resolves to” a square. Rows/columns are never reused. The exactly-one-companion condition is a solving constraint.

## Case 01 — Knox D2

Quill and Pip occupy rows 1 and 3. Morse and Knox reserve columns C and D, leaving A/B for Pip and Quill. Pip is left of Quill, so Pip=A3 and Quill=B1. Morse and Knox must take rows 2/4. Morse is lower, so Morse=C4 and Knox=D2. D2 lies in Delivery.

## Case 02 — Dax D2

Nova=B3. Of Display Room squares in column D, D1 is blocked by the globe, so Dax=D2. Rook's whole-grid corner plus same-room teacher-desk adjacency leaves A6. In Equipment Room, F5 and F6 are blocked, so Atlas=F4. Ivy's desk-chair choices are A6/C5/F1: A6 is Rook's column/row and F1 is Atlas's column, leaving C5. The last row is 1 and last column E, so Max=E1. Max and Dax are the two Display Room occupants.

## Case 04 — Zuri F4

Echo=A2. The Pickup Tent has only F4 in row 4; the Packing Room has only C5 in row 5. Briar can stand at C2 or D3 beside the ring-toss stand in the same room. Column C is Clover's, so Briar=D3. Kai's Kitchen choices A5/B5/B6 lose column A to Echo and row 5 to Clover; Kai=B6. Pixel is in the Pickup Tent by the objective, and the unused row/column intersect at E1. Its other occupant is Zuri.

## Case 06 — Arlo D2

Scout=E3. D2 is the only clear Foyer square in row 2. Wren's same-room bench beside the skeleton is C4 (the bench at C5 is across a room boundary). Hugo's Dinosaur Gallery squares beside a display case are A4/A6; Wren has row 4, so Hugo=A6. Vale's Gallery choices beside the statue are F3/F5; Scout has row 3, so Vale=F5. Uma takes the last row/column intersection B1. Arlo is the sole other person in Uma's Foyer.

## Case 07 — Zoe C6

Rocket=E5. Blaze is alone in Rehearsal, so Indigo must be in Dressing and Willa cannot use B3. Willa's clear two-step squares from C2 are A2/B1/B3/E2; column E is already used. Zoe's outer-wall squares beside the wheeled cases are A2/B1/C6. If Zoe takes A2 or B1, the remaining Dressing placements cannot give Indigo a separate row and column. Hence Zoe=C6. Blaze and Willa must use A/B, so Indigo=D2. Row 2 is now used, forcing Willa=B1. The last two people use A/F and rows 3/4: Gray must be F4 in Prop Room to have Zoe as the one companion; Blaze is A3.

## Case 10 — Ember D5

Wyatt=B7: B5 is blocked and B7 is the usable Robotics square directly beside the arm at B6. Ember can use D4/D5, reserving column D. Nico can use F4/F6, reserving F. Beck's outer-wall crate choices C1/D1 therefore reduce to C1. After deleting used rows/columns, the only person who can fill row 3 is Dash (E3/G3), and the only person who can fill row 5 is Ember, so Ember=D5. Finn's G4 choice would leave both Vera and Nico needing row 6; Finn must use row 2. If Nico=F4, Dash=E3 would share Assembly with two people, while Dash=G3 would have no Demo companion. Thus Nico=F6; Vera=G4, Dash=E3, Finn=A2. Assembly contains Dash and Ember.

## Case 12 — Nell G2

Cove=B7. With seven people in seven different rows, third from the south means Iris is in row 5. Kira is alone in Bird Room, so Eli must use Green Room and Sage must use Rehearsal. Kira cannot use rows 5/7, so uses row 6. Eli cannot then use Green Room row 6 or Iris's row 5, leaving F4; Nell therefore cannot use column F and is G2. The remaining rows force Sage into row 3 and Winter into row 1. Winter must share an area with exactly one person: row-1 Training Room would leave Winter alone, so Winter=D1 in Stage Wing with Nell. That reserves D; Kira=E6, Sage=C3 and Iris=A5.

## Case 13 — Bodhi B7

Moxie=C5/D5. The westward chain requires Bodhi in B6/B7/C6/C7, with Willow further north and west. Test Skye's usable Ranger squares with Juno's touching-corner clue. C6 leaves no room/row for Eden or Bodhi; D4 leaves every diagonal blocked or in Moxie's row/column; D3 forces Juno/Eden west of F/G, leaving those columns unfillable. Thus Skye=E4. Juno=D3 would likewise leave no F/G square for Eden's same room, so Juno=F3 and Eden=G2. The remaining chain has only eight complete row/column arrangements before using Remy's companion clue; seven leave Remy alone or with two other people. The valid one is Moxie=C5, Willow=A1, Bodhi=B7, Remy=D6. B7 and D6 are both Research Lab.

A useful printed final check is: Bodhi=B6 would leave Remy=D7 alone in Research; Bodhi=B7 puts both Bodhi and Remy in Research. Moxie=D5 never supplies Remy exactly one companion.

## Case 15 — Harper D2

The two 'above and right' links, cot clues and Welcome-only condition leave column A for Milo. In Equipment Room Milo would have no possible companion, so Milo=A1 in Games Cabin. Column G must go to Jett: the only other usable G square outside Jett's solo room is G1, and row 1 is used. Column F must go to Harper or Piper; the available square is F4. Test these two cases together with the cot neighbours. Harper=F4 forces Cruz=D7, and the remaining rows leave Jett needing blocked G2. Thus Piper=F4. Cruz cannot use B4/D4 (row 4 used) or D7 (again no row for Jett), leaving C3. Harper must then be D2: E2 is blocked and F/G are used. Duke cannot use C5/D5 because C/D are used, so Duke=E5. Inez=B6 and Jett=G7 finish the roster. Milo's one Games Cabin companion is Harper.

## Case 17 — Axel E3

Koa's Waiting Lounge choices F6/G6 reduce to F6 because Luna reserves column G; Luna then is G7. Sunny's benches reduce to C2/D5; Mika's Ticket Office squares reduce to B4/B5. Axel is in row 3. Otis cannot use the Baggage Platform: its usable squares lose rows 6/7 and column B to the placements already reserved. Otis therefore joins Mika in Ticket Office. Reed cannot join those two and still have exactly one companion, and cannot join the two Waiting Lounge occupants. The only possible pair is Reed with Axel in Main Corridor. Sunny must therefore be D5, leaving Mika=B4. Of the remaining columns A/C/E, Reed can use only C2 in the corridor; Otis=A1 and Axel=E3 follow.

## Case 19 — Mack A7

Theo's seven-step squares from E6 are A3/B2/C1. Kian's Study Hall choices are F3/F4. Test these small anchors with Avery's two-row gap, Mack's south-west relation and the exactly-one-Archive condition. A3 gives no complete distinct-row/column placement. Both surviving combinations put Kian=F4, Avery=E5 and Ollie=D3. The two candidate finishes are:

| Theo | Dex (same room) | Mack | Sasha | Sasha's companion count |
|---|---|---|---|---:|
| B2 | A1 | C7 | G6 | 0 |
| C1 | G2 | A7 | B6 | 1 |

The first finish leaves Sasha alone in Service Corridor. The second gives Sasha=B6 and Mack=A7 in Returns Hall. This uses the full companion condition, rather than selecting a preferred-looking answer.

## Case 20 — Pax F5

Mara=D4/E4. Asa must occupy another Main Studio square, with a usable touching diagonal for Luca. Compare those candidates with the rows below Mara needed by Pax and Sid, and Toby's solo Workshop condition. The complete row/column restrictions eliminate Mara=E4 and Asa=E3, leaving Mara=D4 and Asa=B2. Luca is then A1/A3. The remaining top-row and third-row placements plus Demi's companion condition force Luca=A1 and Demi=G3; Demi's Safety Station must have exactly one other person. Pax can then be E5/F5 and Sid E7/F7. Only F5 is in Safety Station, so Pax=F5; Sid=E7. Toby uses C6, since rows 5/7 have been used. All three bunks E5/E7/F7 are usable during these tests; none is silently blocked.

## Case 22 — Cody C4

Wes must be in a room containing lockers but outside all same-room adjacent squares. His usable choices are B2/C3/D3/D7/E7/F4/F5/F6/G5. Gia's seven-step choices from the piano A7 are B1/C2/D3/E4/F5/G6. For each, test Cody's diagonal and the Lex–Imani diagonal together with Imani/Nia sharing and the exactly-one-Practice rule. Eleven complete distinct-row/column placements remain before Zara's one-companion condition; ten put Zara alone or with too many people. The only valid finish has Wes=D3, Cody=C4, Gia=B1, Lex=E6, Imani=F7, Nia=G5 and Zara=A2. Cody and Zara are the two Rehearsal Room occupants.

For explanation improvement, show at least one failed test rather than just stating Wes=D3: Wes=C3 can yield Cody=D4 and Zara=A2, but D4 is Green Room and Zara is alone in Rehearsal. A coordinate next to the right room is not enough.

## Case 23 — Rae F6

Vivi's seven-step candidates from the gondola A6 are C1/E3/G5/G7, none in Snack Stand. Therefore Pia is in Snack Stand (B2/B3/C3), and the bench witness must be Ozzy=A3. Pia=B2 after row 3 is used. Mae shares Ozzy's Balloon Corner; combining Cora north-east of Mae and Rae two columns east of Cora leaves Mae=C5/D5 and Cora=D1/E1. Cora uses row 1 and Mae row 5, so Vivi=G7. Rae cannot use column G and must be F6, forcing Cora=D1 and Mae=C5. Jude is the unused intersection E4. E4 and F6 are Prize Tent.

## Case 25 — Casey D5

Casey's Lobby/column clue gives D4/D5. Wynn's Laundry stools are A5/C5/B7; compare each with Tate's touching diagonal, rejecting blocked or reused rows/columns. Gabe and Rio occupy consecutive columns/rows with Rio north-west, and Sol must be north-east of Gabe. These relationships permit only six complete distinct-row/column arrangements before Nori's companion condition. Five leave Nori alone or with the wrong number of people. The valid arrangement is Wynn=B7, Tate=C6, Rio=E2, Gabe=F3, Sol=G1, Casey=D5 and Nori=A4. Nori and Casey are the two Lobby occupants.

Useful failed tests: Casey=D4, Wynn=B7, Tate=C6, Rio=E2, Gabe=F3, Sol=G1 would place Nori=A5 in Laundry with both Wynn and Tate. Casey=D5, Tate=A6, Wynn=B7, Gabe=F4, Rio=E3, Sol=G1 would put Nori=C2 alone in Parcel Room.

## Case 29 — Vega D3

The Mavis–Vega–Cato chain needs three increasing rows. Cato must be north-east of a Control Room occupant; the earlier Control possibilities and blocked I3 cannot fit the chain. Thus Cato=I4 and Ren=H5. Wade's same-room desk neighbours are D7/F7/G6. Testing Jules's touching diagonal with Bryn in Jules's room eliminates G6 and leaves Jules=E8; Bryn must use row 9. For Wade=D7, the remaining combinations put Seth alone, so Wade=F7. Column F is then used and Bryn=G9. The unused rows are 1/2/3/6 and columns A/B/C/D. If Seth used row 6, he would be alone in Map Room. Therefore Poppy takes row 6: C6 is the Training square, forcing Mavis=A2 in the same room. Vega's north-west chain then leaves B3/D3. Vega=B3 would leave Seth=D1 alone in Equipment; Vega=D3 leaves Seth=B1 with exactly one other Equipment occupant. Thus Vega=D3 is the access coordinate.

## Limits of these notes

Cases 13/15/19/22/25/29 include explicit candidate testing. The machine receipt contains all complete assignments and traceable input domains; no claim is made that the shorter prose independently lists every rejected intermediate branch. Use the solver receipt to verify uniqueness, and use the prose plus selected failed branches to teach the method. The canonical printed solution text has not been edited by this reviewer.
