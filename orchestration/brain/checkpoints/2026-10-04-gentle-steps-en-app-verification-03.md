# Gentle Steps EN app — verification checkpoint 03

Date: 2026-10-04
Authority: dedicated Gentle Steps execution lane
Status: EXACT-HEAD CI GREEN / CURRENT PROOF REVIEWED / CHRISTMAS FAMILY V1 PROMOTION STILL OPEN

## GitHub truth

App repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`
Branch: `gentle-steps/app-en-full24-purple-gold`
HEAD: `6ae46c35906158323c2a435f4954ab15bfc581c0`

Branch compare against that SHA is identical: ahead 0, behind 0.

## Exact-head validation

- Gentle Steps English App run `37155578470`: SUCCESS
- Gentle Steps Android Build run `37155578417`: SUCCESS
- SEO Validation run `37155578412`: SUCCESS

Visual proof artifact:
- id `11286096075`
- digest `sha256:851b90d4f2a5d4e9f76a1505d885b9d350992f05931916b32cb91d41f63c9857`

Lighthouse artifact:
- id `11285781679`
- digest `sha256:ee57fe562db5e42231276ef9cf06bf67a0e9568f6dded2a853f03ae9b4f9eac0`

## Proof review

Home, Family, Day 01, Day 12, Day 22, Day 23 and Day 24 have no obvious horizontal overflow or sticky-action obstruction in the current deterministic captures.

Current Home/Family/day cameos still use the pre-Christmas-V1 generated family assets, so this is not final visual identity proof.

Day 22/23 captures are 390x1600 viewport captures, not full-page evidence. Final release proof must cover the complete scrollable content for Days 22, 23 and 24.

## Lighthouse

Home: Performance 100 / Accessibility 100 / Best Practices 96 / SEO 100; FCP 1.0s, LCP 1.7s, TBT 0ms, CLS 0.

Day 22: Performance 100 / Accessibility 100 / Best Practices 96 / SEO 100; FCP 0.9s, LCP 1.4s, TBT 0ms, CLS 0.

The earlier calendar accessible-name mismatch is no longer reported. Remaining browser-console issue is favicon.ico 404.

## Remaining repository-side work

1. Promote exact owner-approved Christmas Family V1 assets without redraw.
2. Run fresh Home / Family / Day 01 / 12 / 22 / 23 / 24 proof after promotion.
3. Add full-scroll proof for Days 22 / 23 / 24.
4. Close favicon 404.
5. Re-run exact-head CI, Lighthouse, dependency audit and Android packaging after those changes.

READY FOR INTERNAL TESTING: NO.

Owner/device/Play/legal gates remain unchanged.
