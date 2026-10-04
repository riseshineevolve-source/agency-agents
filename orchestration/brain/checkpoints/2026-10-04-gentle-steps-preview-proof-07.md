# Gentle Steps EN app — preview/proof hardening checkpoint 07

Date: 2026-10-04
Status: exact-head green; preview gate and long-day proof fixed; Christmas derivative quarantined

## Exact app state
- branch: `gentle-steps/app-en-full24-purple-gold`
- exact HEAD: `444d619c43ccd73472109991bc1ecbd3fb0f4b01`
- branch HEAD verified exact after all source mutations in this slice

## Material verified deltas
1. `preview=1` is now test-only:
   - accepted only on loopback hosts `127.0.0.1`, `localhost`, `::1`
   - explicitly blocked in native Capacitor runtime
   - local CI proof continues to work
2. Long-day proof strengthened:
   - Day 22 / 23 / 24 now render as 390x5000 evidence
   - exact-head screenshots were inspected and include Family Connection, day navigation, and the final completion action
   - no clipping or action-button obstruction was observed in these captures
3. Christmas Family V1 derivative gate discovered and contained:
   - repo file `gentle-steps-app/brand/generated/happy-makers-christmas-v1.webp`
   - Git blob `490b194071c644b8db34f7d11efecba86ae2cb22`
   - dimensions: 640x128
   - exact-head browser QA renders the derivative as an empty cream strip, so it is not a valid runtime family asset
   - it is now marked `QUARANTINED_DO_NOT_USE_RUNTIME` in `brand/generated/manifest.json`
   - service worker cache was bumped to v9 and no longer precaches this unusable derivative
   - owner-approved source file `file_00000000689881f4a1ed4b9ba414ce08` still has no authorized raw-byte materialization path
   - do not infer character mapping, redraw, or silently substitute
4. QA brand preview now surfaces this Christmas asset gate explicitly.

## Exact-head validation
- Gentle Steps English App run `37192786924`: SUCCESS
- SEO Validation run `37192786882`: SUCCESS
- Gentle Steps Android Build run `37192786899`: SUCCESS
- visual proof artifact `11299876022`, digest `sha256:8e1df653640ddd48d98d935c7c846dd562c46607332eae4981adfa8d5d41713d`
- English Lighthouse artifact `11300175427`, digest `sha256:cf627c956e6e063a9a9edec2a27e5f73410adf3f0a0cb4b7ea6714d88fd73875`
- SEO Lighthouse artifact `11299936114`, digest `sha256:067c4f6d536a91bd4962d14295ae64f83de6e21f9a2870a82e297f129492d88b`
- SEO status artifact `11299592450`, digest `sha256:0bd466d4c6b9b1d3331735392fa22a09c5dfe712c33d906abd5852841028acef`
- Android pre-Play artifact `11300016084`, digest `sha256:4190a8723df69df085d081374bc2fb7a101fde9f8514c0200dc3ba413a2e2531`
- Home Lighthouse: Performance 100 / Accessibility 100 / Best Practices 100 / SEO 100; LCP 1.7 s; TBT 0 ms; CLS 0
- Day 22 Lighthouse: Performance 100 / Accessibility 100 / Best Practices 100 / SEO 100; LCP 1.4 s; TBT 0 ms; CLS 0
- native dependency audit step: SUCCESS
- SDK 36 / lintDebug / debug APK / unsigned AAB build: SUCCESS
- debug APK SHA-256: `4efed24f8fab3d5d13f41d49c04e506b36d9902b2af1734a3ed7ddaa2ca605ce`
- unsigned AAB SHA-256: `fcbaafa30f613e031f41ae2cac9255d930c9bab33fde449d097bf4c452de2418`

## Remaining repository-side gap
The only material source-side blocker is the Christmas Happy-Makers production identity. Home / Family / daily cameos must not be switched until valid exact owner-approved source bytes are available. The currently committed 640x128 derivative is unusable and quarantined.

## External/owner gates
- real-device Android smoke
- TalkBack
- real notification delivery/tap/cold-start verification
- final package ID
- final Play icon/splash approval
- signing
- monetization / regions
- privacy / Data Safety / legal declarations
- Play upload / publication

READY FOR INTERNAL TESTING: NO.

Next safe action: keep the exact-head green baseline stable. On future runs, first re-check whether the exact owner-approved Christmas source can be materialized. If not, verify current truth and do not manufacture replacement work.
