# Slice 010 Pre-Edit Scope

Base master: WORKING_MASTER_V9_TEXT_PUZZLES_A.txt
Base blob: 9dfb24eb9bc4a70f4120a0a8c635c9f23372d1e5

Allowed changed segments:
- D25.GLITCH_PUZZLE
- D27.GLITCH_PUZZLE
- D28.GLITCH_PUZZLE
- D30.GLITCH_PUZZLE
- D31.GLITCH_PUZZLE

Protected:
- every other master segment
- all daily quote tails

Dependencies to update after the patch:
- PUZZLE_TRUTH_REGISTRY.json
- PUZZLE_COMPLETENESS_MATRIX.md

Review packet:
reviews/SLICE_010_PUZZLE_REDESIGN_B_REVIEW_BOARD.md

Any change outside this scope fails closed.
