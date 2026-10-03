# World 01 — permanent Android identity checkpoint

Date: 2026-10-01
Status: **PERMANENT APP ID LOCKED / ANDROID CI GREEN / OWNER DEVICE + STORE GATES REMAIN**

## Current application truth

Repository: `riseshineevolve-source/spark-joy-fam`

Release-hardening PR #3 was merged to `main`, followed by PR #4 locking the
permanent series-level Android identity.

PR #4 merge commit:

`b5abbdba08b899e5f953f40808e4f624fa10f8e7`

Permanent Android application ID:

`com.riseshineevolve.levelupyourbrain`

Current visible application name remains:

`Level Up Your Brain: World 01`

The package ID intentionally does not contain `world01`, so future World 02
content can remain within the same Google Play application identity.

## Exact verification

Exact package-ID implementation SHA:

`a8bd793a6c621683db0d37a61e2c3cbe75efde73`

GitHub Actions workflow:
- World 01 Android #78
- run ID: `36830395296`
- conclusion: **SUCCESS**

Passed on the exact code head:
- `npm ci`;
- unit/runtime tests;
- TypeScript;
- production lint;
- fail-closed release contract;
- production dependency audit;
- offline web build;
- no-remote-font gate;
- Capacitor Android generation/sync;
- Android privacy/transport hardening;
- Android 16 / target API 36 verification;
- Android lint/unit tests;
- debug APK build;
- unsigned release AAB build;
- artifact upload.

GitHub artifact:
- ID: `11146843823`
- digest: `sha256:a16c6f48d8b96a57a084c211bc601a9426ec775bce6969df6f45d4a0144e761c`

Locally materialized build hashes from that artifact:
- debug APK SHA-256: `5c8f41034574003e25f9faffa9a482e247d82d94ffac5a66c222159fc3cce5ff`
- unsigned release AAB SHA-256: `cd2e5ebb348d3854bc886182de7282c803a3f7c1448d8430d725dff7ec46fd14`

## Store/device preparation

Durable release handoffs now exist in the app repository:
- `release/WORLD01_DEVICE_QA.md`
- `release/WORLD01_PLAY_ASSETS.md`

Google Play visual work remains an owner visual gate. Do not substitute generic
Capacitor/Lovable icon art.

## Remaining genuine gates

1. real-device QA (visual, Back, TalkBack, font scaling, offline/restart);
2. final launcher/adaptive icon, monochrome icon, splash and Play visual assets;
3. production signing / Play App Signing;
4. privacy, target-audience, Data Safety and content-rating owner/legal inputs;
5. pricing/monetization decision, if any;
6. explicit owner approval before Google Play upload/publication.

The permanent package-ID gate is closed.
No Google Play upload or publication was performed.
