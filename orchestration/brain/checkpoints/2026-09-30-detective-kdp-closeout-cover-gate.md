# Detective Academy — KDP closeout + cover gate — 2026-09-30

Authority: Central portfolio checkpoint only. Detective production surfaces remain delegated/read-only for Central.

## Current exact interior truth
- Repo: riseshineevolve-source/RISE.SHINE.EVOLVE
- PR #571 branch: feature/detective-book-factory
- Head: cf4d47369e8eff45187a79d95082cd66404ce997
- Canonical V3 blob: a85a5941852930f6b88711af26b16ea1651d2fbc
- Exact KDP candidate: HMDA_Book1_EN_KDP_INTERIOR_FINAL.pdf
- SHA-256: 3f70d96cca6e6d6945533d82b90a11addf286884b0dad24feb0e0a8bad8ab189
- Pages: 180
- Content/layout: READ-ONLY
- EN: NOT FROZEN
- KDP Previewer: NOT YET PASSED; external owner action.

## Bounded transparency closeout
The current 180-page candidate still has Evidence Grid stroke transparency on 50 pages: white grid strokes using /CA 0.13 or /CA 0.25. This is not an image soft-mask problem.

Authorized closeout only:
- replace those translucent white grid strokes at source-renderer level with equivalent opaque gray strokes;
- clip to the same rounded black panel;
- preserve 0.85 pt grid geometry;
- require zero transparency objects afterward;
- rerun deterministic QA plus full visual regression.

No broad creative/text/layout reopening.

## Locked front-cover truth
- File: OSTATECZNA OKLADKA ROOM ZERO.png
- SHA-256: 2570df512f3883663aca1c4e5359ba12aa0489276f484b86ac5623ab037429a9
- Dimensions: 1086 x 1448 px
- Visually immutable.

Central checked the accessible ChatGPT Library and found nine copies of OSTATECZNA OKLADKA ROOM ZERO*.png. All nine are byte-identical, 1086 x 1448 px, and match the locked SHA. No higher-resolution locked-equivalent derivative was found in the accessible Library or default-branch GitHub search.

If no higher-resolution locked-equivalent derivative is surfaced by the delegated closeout worker, only deterministic non-generative upscale plus bounded crop/clip is authorized. For the front panel including outside/top/bottom bleed, target 8.625 x 11.25 in. Because the source is exact 3:4, it can be scaled to 8.625 x 11.5 in and center-clipped 0.125 in top and bottom without horizontal stretch. At 300 dpi this is approximately 2588 x 3450 px before clip and 2588 x 3375 px after clip. Keep the full wrap as exact PDF geometry rather than rasterizing the entire wrap.

Confirmed 180-page black-ink/white-paper geometry:
- spine: 0.40536 in
- full wrap incl. bleed: 17.65536 x 11.25 in

## Documentation drift / blocker
Canonical agency-agents cover docs correctly lock the front SHA, but the KDP release package still contains historical 146-page passages. The cover/A+ lock also contains a newer recruitment lock that explicitly supersedes older wording still repeated later in the same file. These stale passages must not drive the final wrap.

Repository search found no canonical Detective QR destination. Do not invent a URL or turn a placeholder into a live QR.

## Next gate
Dedicated Detective closeout writer -> bounded transparency rebuild -> zero-transparency verification -> full visual regression -> owner KDP Previewer. Full wrap uses the locked front plus current 180-page geometry. No main merge, EN freeze, publication, production deploy, paid activation or owner-art mutation is authorized.
