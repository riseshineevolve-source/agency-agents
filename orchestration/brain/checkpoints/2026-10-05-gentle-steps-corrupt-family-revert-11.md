# Gentle Steps EN app — corrupt Christmas runtime regression repaired checkpoint 11

Date: 2026-10-05
Status: broken Christmas-family promotion reverted; exact-head CI re-running; owner-approved source bytes still gated

## Exact app state
- repository: `riseshineevolve-source/RISE.SHINE.EVOLVE`
- branch: `gentle-steps/app-en-full24-purple-gold`
- exact HEAD: `98c351050ecc99b9d3a5674528fee1629ba3b738`
- HEAD message: `Revert corrupt Christmas Family runtime asset promotion`
- compared with last known-green source tree `192fd304b59232b2bc48deb4babd9e89d6da032b`: 2 commits ahead / 0 behind / zero file differences

## Reproducible regression found and repaired
A later commit `4a167f1a22d623a02d69e511b896fcaa86d61038` attempted to promote Christmas Family V1 into runtime.

Exact-head English App run `37376521208` / #132 failed in `Validate full 24-day English app` with:
- `FAIL: owner-approved Christmas family runtime SHA mismatch`
- `FAIL: Christmas family manifest runtime SHA mismatch`
- Advent date-lock boundary logic still PASS

The committed `brand/generated/family-clean.webp` was proven corrupt/truncated:
- Git blob: `7094e13e68bc0c00a512f275f6e6af37a61d0b2d`
- packaged APK asset size: 11,310 bytes
- actual SHA-256: `2c8785afdf445b435223e3a8ad242f3ce48bb8082f0b348b4d7b42e1dcc06abf`
- manifest/test expected SHA-256: `53079c49cf04d51d7dc7f7429665f308695c1226aa3326e442c3c41d8711c17b`
- WebP header reports 640x640 but Pillow, ImageMagick and ffmpeg all fail to decode it as a complete valid image.

Repair commit `98c351050ecc99b9d3a5674528fee1629ba3b738` restores only the seven files changed by the broken promotion to their exact prior known-green blobs. No force update and no unrelated lane changes were made.

## Evidence from broken promotion head
- English App: run `37376521208` / #132 — FAILURE as above
- SEO Validation: run `37376521177` / #1014 — SUCCESS
- Android Build: run `37376521480` / #86 — SUCCESS
- Android artifact: `11372550035`
  - artifact ZIP digest: `sha256:5f86b84f1986afa02534d0d769b198e299d68b58ead559fbaea3506f1255e7a9`
  - debug APK SHA-256: `a019ea0ee2284d4f20cdb8811c0c4bcda09ad7d6fc576317ca8d3dad5e4796d3`
  - unsigned AAB SHA-256: `c8623904d78693caef831ed0bca4603957a2730a8fb95dad977bf4890cd75acb`
- Android high audit gate passed; no breaking `npm audit fix --force` was applied.

## Fresh repair-head CI
Push-triggered runs started for `98c351050ecc99b9d3a5674528fee1629ba3b738`:
- English App `37379079280` / #133 — queued at checkpoint time
- Android Build `37379079282` / #87 — in progress at checkpoint time
- SEO Validation `37379079286` / #1015 — in progress at checkpoint time

Because the repair head has zero file differences from previously green source tree `192fd304...`, it restores the prior source state, but exact-head workflow completion must still be checked on the next verification.

## Christmas Family V1 source gate
Owner lock remains `gentle-steps-app/brand/concepts/HAPPY_MAKERS_CHRISTMAS_FAMILY_V1_LOCK.json`.
Exact source file id remains `file_00000000689881f4a1ed4b9ba414ce08`.

Fresh raw-file materialization in this run still fails with:
`This Project file does not have an authorized raw-byte materialization path.`

Therefore:
- do not redraw;
- do not reconstruct from preview pixels;
- do not silently substitute a lookalike;
- do not retry the corrupt/truncated runtime asset.

## Readiness
READY FOR INTERNAL TESTING: NO.

Remaining material repository-side gap:
- obtain an authorized complete byte path for the exact owner-approved Christmas Family V1, derive valid deterministic production WebP family/cameo assets, record hashes, then refresh Home/Family/Day visual proof and exact-head CI.

Genuine owner/device/external gates remain:
- real-device Android smoke
- TalkBack / physical assistive-technology verification
- real local-notification delivery + tap + cold-start verification
- final package ID
- final production icon/splash approval
- signing
- Play Console / pricing / regions / monetization
- privacy / Data Safety / legal declarations
- Play upload/publication

## Next safe action
1. Verify all three repair-head workflows to completion.
2. If repair head is green, stay on that baseline.
3. Retry only the authorized exact owner-approved source path when it materially changes; do not invent visual work.
