# Detective Academy — Modern Props V4 Hydration Gate

Date: 2026-09-25  
Status: ACTIVE BOUNDED OWNER VISUAL GATE  
Authority: Central RSE Technical Orchestrator  
Canonical precedence: live repository state > this checkpoint > chat history.

## Codex candidate V4 evidence supplied by owner

This evidence is from the local Codex modern-props worktree and is **not yet canonical production source**.

- local Codex head reported: `295d648a1c0a18570c4703a563f6ee2e096ed8a8`
- candidate V4 ZIP SHA-256: `0e63a781276c3752a2d8d9b45fc1773e1ed0a46f5c6940b15fcf20e529f5d308`
- classification: **22 CLEAR / 1 BORDERLINE / 0 REMAKE**
- only remaining visual blocker: `hydration_station`
- HMDA_02 render: PASS
- HMDA_13 render: PASS
- HMDA_29 render: PASS except hydration-station recognizability
- structural fingerprints HMDA_02 / 13 / 29: PASS, zero locked-field differences
- Room Zero meta: PASS
- CHECK THE OLD MAP: PASS
- clue-critical collaborative desk: PASS
- clue-critical mentor workstation + separate TEACHER'S DESK label: PASS
- exam bench: CLEAR
- seating-family distinctness: PASS

The existing hydration station rendered at approximately 47 x 153 px at 300 dpi and approximately 23 x 76 px on the 50% sheet, so it read first as a slim appliance rather than an unmistakable bottle-refill station.

## New hydration candidate

Central chat prepared exactly one replacement candidate and renamed it:

`hydration_station.png`

Source file characteristics:
- PNG RGBA
- 1024 x 1536 px
- alpha bbox approximately 951 x 1511 px
- alpha-bbox aspect ratio approximately 0.629
- SHA-256: `a91f9c1126463ed134ac0f64760bf60ba51b9b934be6b8b25e4f8c85f78f383d`

If the renderer remains height-limited near 153 px, this aspect ratio should yield roughly 96 px rendered width, inside the intended approx. 85–100 x 150 px visual target.

This is still a **candidate**, not owner-approved production art.

## Next safe execution

1. Replace only the candidate `hydration_station.png` in the pilot-only candidate route.
2. Do not change D9 geometry, footprint, runtime, clue logic, map logic or any other prop.
3. Run HMDA_29-only 100% + 50% print recognizability gate first.
4. If hydration station = CLEAR, rerun the existing HMDA_02 / HMDA_13 / HMDA_29 V4 owner gate.
5. Required target: **23 CLEAR / 0 BORDERLINE / 0 REMAKE** with all structural/meta checks still PASS.
6. Return owner review packet; do not set production `owner_approved=true` automatically.
7. After explicit owner approval, register exact 23 asset hashes and preserve fail-closed validation.
8. Only then scale the approved external prop pack to all 15 locked spatial modules.
9. Re-run all-15 structural/solver/print QA before integrating into the final book artifact.

## Forbidden

- no regeneration of the other 22 CLEAR assets
- no footprint enlargement
- no geometry movement
- no clue/story/answer change
- no production manifest promotion before owner approval
- no all-15 scaleout before the 23/23 owner gate passes
- no merge / English freeze / KDP publication from this checkpoint alone


## Hydration gate result — candidate 2

Codex reported on 2026-09-25:

- local head unchanged: `295d648a1c0a18570c4703a563f6ee2e096ed8a8`
- candidate hydration SHA: `69da989e57f0ecdd1432282c41850061f67fa292b4e4707d2e5bae7e96735c97`
- rendered bbox: **102 x 153 px**
- clipping / overlaps: NO / NO
- 100%: BORDERLINE
- 50%: BORDERLINE
- HMDA_29 structural/render geometry: PASS
- final classification remains **22 CLEAR / 1 BORDERLINE / 0 REMAKE**
- Room Zero meta and CHECK THE OLD MAP: PASS
- no three-pilot rerun or production promotion occurred.

Conclusion: renderer footprint/scale is no longer the blocker. Further photorealistic machine variants are rejected as an inefficient direction.

### Final correction strategy

One last art correction may change only the visual language of `hydration_station.png`:

- map-scale, high-contrast, illustrated-realistic rather than photorealistic product render;
- squat/wide bottle-refill silhouette;
- bottle body must consume roughly 40–50% of sprite width;
- oversized recognizable loop/handle;
- large central refill nozzle;
- thick solid stream that survives reduction;
- wide tray/basin;
- simplify decorative housing aggressively;
- no text/logo;
- no footprint/geometry/runtime change.

Gate policy:
- if actual 100% print scale becomes CLEAR and 50% remains only BORDERLINE, do not automatically restart art; surface it as owner acceptance because 50% is a stress-test, not the physical book scale;
- if 100% remains BORDERLINE, stop visual regeneration and use a minimal separately rendered non-clue label only if owner approves that exception rather than blocking the entire book on repeated art generation.

No other prop may be reopened.


## Final pilot presentation gate — READY FOR OWNER APPROVAL

Owner supplied Codex result on 2026-09-25:

- local modern-props head: `7ad9454356f087e6f09da7f70ac4f545f94b3204`
- hydration occurrences in locked 15-case runtime: **1 — HMDA_29:D9**
- hydration asset SHA-256: `69da989e57f0ecdd1432282c41850061f67fa292b4e4707d2e5bae7e96735c97`
- hydration rendered bbox: **102 x 153 px**
- WATER REFILL label: Arial Bold, 6 pt at 300 dpi, directly below art inside D9
- HMDA_29 map context at 100%: **CLEAR**
- 50% stress test: **ACCEPTABLE**
- final prop status: **22 STANDALONE CLEAR / 1 CONTEXT_CLEAR_WITH_LABEL / 0 REMAKE**
- structural fingerprints HMDA_02 / 13 / 29: PASS / PASS / PASS, zero locked-field differences
- Room Zero meta: PASS
- CHECK THE OLD MAP: PASS
- print scale: PASS, grayscale, 8.5 x 11 in, 300 dpi
- collaborative_desk / mentor_workstation / TEACHER'S DESK behavior preserved
- exam_bench CLEAR
- seating distinctness PASS

The pilot-only reproducible gate was saved in a local Codex commit. No owner_approved flags, all-15 scaleout, push, merge or English freeze occurred.

### Next owner gate

The prop system is now technically ready for **explicit owner visual approval** of:
- the 22 standalone-clear assets,
- the single hydration presentation exception `WATER REFILL` at HMDA_29:D9,
- the exact candidate asset hashes from the final owner packet.

After explicit owner approval, the next authorized bounded execution is:
**register exact hashes + production owner-approved manifest state -> all-15 scaleout -> all-15 deterministic structural/solution/meta/print QA -> owner review packet.**

Do not reopen the 23 prop designs during all-15 scaleout unless a concrete map-context collision or clue/semantic regression is proven.
