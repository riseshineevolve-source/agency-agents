# Case 07 — unresolved source anchor

This is an additional source-figure gate for the existing Book Factory handoff. The current V5 manuscript is unchanged: SHA256 `9ebae1eabafe2f5ed92c38c2ad7b858a9c85d573b5a7e92c4fb08f1c5810a978`. Original owner225PDF SHA256 `9db84d4f138cbbde8eb1f4a0f783f4d126c639120a11cabb65fc00711b9f05a0` is the authority. Historical editions do not supply missing evidence.

## Reproducible conflict

Source folio 42, `page042.block08`–`page042.block09`, says Willa is two grid steps from the **stage range marker**, with row difference plus column difference. On the actual map, folio 43, neither the room labels nor the key identifies that marker. A1, D1 and D6 show similar road cases/carts. C2 shows a wheeled metal rack/crate-like silhouette. C1 and C4 show light strips. None carries a range-marker label.

Two independent visual reviews agree that the referent cannot be selected from the visible source. The root solver's anchor simulations are diagnostics, not source validation:

| Assumed anchor | Complete placements, shared-edge “beside” | Result |
| --- | ---: | --- |
| D1 | 3 | More than one answer/roster |
| C2 | 1 | Matches printed roster |
| C1 | 1 | Different roster, same Zoe C6 answer |
| C4 | 1 | Different answer |

The fact that C2 reproduces the printed roster does **not** independently establish that C2 is the intended marker. Using the solution to identify it would be circular.

## Bounded resolution contract

The source/art owner must identify the intended anchor from authoritative editable source or an explicit source-side correction. The product writer can then make that anchor visibly unambiguous in the map or its source-approved clue. Record the actual coordinate, approved object/label, affected source IDs and destination slot, and before/after hashes. Re-run the literal puzzle enumeration against that correction and independently check the new figure. Preserve the intended witness roster only when supported by that evidence.

No proposed coordinate has been applied. Do not silently rename C2, choose D1, import an old-edition symbol, or change the protected clue to force the answer. Continue unaffected import/layout work. This gate is separate from Case03's caption chronology and from the outstanding V5 import/render receipts.

Evidence: `geometry-audit/case07-anchor-review.json`, `root-map-grids-06-07.json`, `solve-root-maps-06-07.py`, `root-map-results-06-07.json`, and `root-solver-independent-review.json`. No receiving chat acknowledgment is claimed.
