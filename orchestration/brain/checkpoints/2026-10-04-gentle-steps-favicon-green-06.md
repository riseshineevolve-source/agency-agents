# Gentle Steps EN app — exact-head green checkpoint 06

Date: 2026-10-04
Status: bounded PWA polish landed and exact-head validation green

## Exact app state
- branch: `gentle-steps/app-en-full24-purple-gold`
- HEAD: `262a4b19e9b65044e453619a0f8371610a50182c`
- net runtime change in this closing slice: explicit SVG favicon link using the existing provisional purple/gold app icon; analytics consent include remains unchanged to preserve the central validator contract

## Exact-head validation
- Gentle Steps English App run `37174328114`: SUCCESS
- SEO Validation run `37174328131`: SUCCESS
- Gentle Steps Android Build run `37174328167`: SUCCESS
- English visual proof artifact `11291994373`, digest `sha256:88c2cd1d7a9d0d05ef24f116c56ae187e95ec57912a6c0733456a0526a4a4171`
- English Lighthouse artifact `11292029264`, digest `sha256:303e6d545e24faedfdb518c194cee85d1cea6667a52dc79140c8d470481230a6`
- Android pre-Play artifact `11292712885`, digest `sha256:3911981f342da5720e865cc1dadc1ec31a640048e9ba06133d11a8e4b22bb2e6`
- SEO Lighthouse artifact `11292925239`, digest `sha256:f27ab230c1e6bef82089fec90561f3ce09dde07c346aede275d2ffcd6fd43ada`
- SEO status artifact `11292368629`, digest `sha256:f75b1ffd0cbb5a3a3fe775acc66ce8097a14b3019e59e5d9cbb70075a1df3719`
- native dependency audit step: SUCCESS
- SDK 36 / debug APK / unsigned AAB build step: SUCCESS

## Repair note
A first attempt to defer the central analytics-consent script caused SEO Validation to fail because the repository validator requires the exact canonical include form. That change was fully reverted before this checkpoint. The final favicon-only head above is green across all exact-head workflows.

## Remaining repository-side gaps
1. `preview=1` is still URL-only in `gentle-steps-app/app.js`; the lock requires local/test-only behavior. Two bounded source-write repair paths for this specific change were rejected before branch mutation in this run; do not broaden the change.
2. Christmas Family V1 is owner-locked, but the locked source image has no authorized raw-byte materialization path in this scheduled environment. Runtime generated family assets therefore remain the older cover/portrait set. Do not redraw or substitute lookalikes.
3. The current Android splash is the provisional deterministic purple/gold city/star composition generated from `brand/splash-mark.svg`; it still lacks the owner-approved Christmas Family V1 identity required by the latest product lock.
4. Long-day proof still uses fixed viewport captures for Day 22 / Day 23 / Day 24 rather than true bottom/full-page evidence.

## Positive visual/platform facts
- provisional app icon source complies with current lock: purple/gold, festive, no green-dominant treatment, no laurel/Roman branch, no crowded five-face composition
- full EN validator, current mobile proof render, Lighthouse steps, SEO pipeline, dependency audit and Android build are green on the exact HEAD above

READY FOR INTERNAL TESTING: NO.

Next safe actions: keep the exact-head green baseline stable; on a later run apply the smallest test-only preview guard if source mutation is accepted, strengthen long-day bottom proof without speculative refactors, and promote Christmas Family V1 only when the exact owner-approved raster bytes become programmatically available.
