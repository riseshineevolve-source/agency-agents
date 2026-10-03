# World 01 — complete published mission graph + Android handoff checkpoint

Date: 2026-09-30
Status: **PUBLISHED MISSIONS 1–10 SOURCE GRAPH MERGED / ANDROID RUNTIME IN EXECUTION**

## Canonical source

Owner-supplied file: `10 STORIES WORLD 01 FINAL paperback(3).pdf`

- pages: 108
- bytes: 14,523,549
- SHA-256: `adf9d384985ec7ad0fb1d7f9f6c3d46189592a171474c38ee93ac35bb808c549`

The uploaded file was independently hashed in the execution environment and
matches the existing World 01 custody hash exactly.

## Published mission graph

PR #17 in `riseshineevolve-source/agency-agents` was merged as
`bad6e94cbadfe49f08046ed29f61b84339b76dfc`.

World 01 mission content is now covered from printed pages 15–99:

- 10 missions
- 85 mission pages
- 282 source-proven semantic nodes
- English source-proven
- pl-PL planned but not marked ready
- source-only structures preserved, including Level 4 inventory, Level 5 Wizard
  Breathing Box exercise, and SYSTEM NOTE / SYSTEM TIP blocks in later levels.

The historical Lovable `spark-joy-fam/src/data/storyContent.ts` derivative was
audited as comparison material only. Levels 5–10 contain material story/key/
objective divergences, so it is not canonical copy.

## Android handoff

Execution continues in private repo `riseshineevolve-source/spark-joy-fam`
on branch `codex/world01-android-runtime-v1-20260930`, draft PR #1.

The production entry path is being replaced with:

- bundled canonical World 01 content packs;
- offline-first reading;
- no mandatory account/paywall to read;
- local device progress;
- source-aware rendering;
- Capacitor 8 native Android wrapper;
- Android 16 / API 36 CI validation for current Google Play requirements.

The legacy Lovable runtime remains historical comparison material and is not the
source of truth for product copy.

## Remaining real release gates

The current code/runtime work does not authorize Play publication. Final release
still requires:

1. green Android CI with APK/AAB build;
2. real-device UX/accessibility QA;
3. final app icon / splash / store visual approval;
4. confirmation of permanent Android application ID before first Play publish;
5. production signing key / Play App Signing path;
6. Play Console Data Safety and privacy declarations based on the actual final
   data behavior;
7. pricing / billing decision if monetization is enabled;
8. explicit owner publication approval.
