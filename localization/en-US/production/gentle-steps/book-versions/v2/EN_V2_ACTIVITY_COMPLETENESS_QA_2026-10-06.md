# Gentle Steps EN V2 — Activity Instruction Completeness QA

Date: 2026-10-06

## Status

**FIX — bounded mechanical clarity only**

No game redesign is required.

## Findings

### D01.PLAY
Round 2 must explicitly guarantee that the starter also receives one positive sentence.
Fix: route the final catch back to the starter.

### D02.PLAY
Uses clockwise order without explicitly forming a circle.
Fix: add circle setup.

### D03.PLAY
Uses clockwise order without explicitly forming a circle.
Fix: add circle setup.

### D11.PLAY
Uses "person on the starter's left" without explicit circle setup.
Fix: add circle setup.

### D12.PLAY
Uses "person to the right" without explicit circle setup.
Fix: add circle setup.

### D13.PLAY
Expert chooses next player but does not explicitly prevent repeats before everyone has a turn.
Fix: choose someone who has not gone yet; continue until everyone who wants a turn has gone.

### D19.PLAY
"Next person clockwise" is unnecessary because the game does not require a circle.
Fix: choose another guesser; continue until everyone has had a turn.

### D21.PLAY
Uses "person to their right" without explicit seating arrangement.
Fix: sit in a circle or around a table.

### D22.PLAY
"Next person clockwise" is unnecessary because no circle is established.
Fix: another person becomes guesser; continue until everyone who wants a turn has gone.

### D23.PLAY
Alternation is clear, but the group order is implicit.
Fix: establish a circle and say continue around it while alternating.

## Already PASS

- all 24 games have START;
- all 24 games have explicit two-person handling;
- D09 scales to 2/3/4/5+;
- D15 handles a three-person group;
- D17 odd group has explicit reuse of one player;
- D18 has explicit 3-person rotation and safe-space handling;
- D24 works for two and group play;
- no elimination mechanics;
- opt-in / pass rules remain intact.

No other game needs a mechanical rewrite.
