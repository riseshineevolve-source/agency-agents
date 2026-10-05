# Slice 012 Review Board — Remaining Deterministic Visual Puzzle Specs

Date: 2026-10-05
Scope: D17, D18, D20, D21, D23 and D24 Glitch & Puzzle segments only.

## Puzzle / print-mechanics reviewer
- D17 Coin Triangle needs exact starting coordinates and exact three moved coins.
- D18 Word Search needs a real grid, target locations and no accidental second copies.
- D20 Impossible Object needs deterministic vector geometry and an observation question with one truth.
- D21 current "remove 3 lines" has no starting diagram. Replace it with a precise 2×2 matchstick-grid challenge.
- D23 Hidden Star needs exact field size and exact hidden-star location.
- D24 Maze needs exact cell geometry, one entry, one center goal and one valid route.

## Teen-ear reviewer
Instructions should fit one scan. No puzzle should rely on the renderer to invent clues later.

## Editor-in-Chief synthesis
Only the six Glitch & Puzzle segments may change.
Every other master segment and all quote tails remain protected.

## Pre-edit scope lock
Base master: `WORKING_MASTER_V11_PUZZLE_SPECS_C.txt`
Base blob: `fde03e476770eeed8210b3e17dc8d11372de8218`

Allowed changed segments:
- D17.GLITCH_PUZZLE
- D18.GLITCH_PUZZLE
- D20.GLITCH_PUZZLE
- D21.GLITCH_PUZZLE
- D23.GLITCH_PUZZLE
- D24.GLITCH_PUZZLE

Required dependency updates:
- PUZZLE_TRUTH_REGISTRY.json
- PUZZLE_COMPLETENESS_MATRIX.md

Any other master-text change rejects the slice.
