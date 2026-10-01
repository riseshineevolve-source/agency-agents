# World 02 — canonical source vs legacy app audit

Date: 2026-10-01  
Status: **AUDIT COMPLETE / REBUILD FROM PUBLISHED SOURCE / NO LEGACY COPY PROMOTION**

## Canonical source

Canonical print authority is already recovered in:

`orchestration/content-sources/level-up-your-brain-world-02.yml`

Published paperback:
- file: `paperback 10 STORIES WORLD 02 FINAL standard(1).pdf`
- ISBN: `9798249971823`
- pages: **104**
- bytes: **66,576,954**
- SHA-256: `e94d2937cc459a5c7c3c5968c64ba39f2a03702f929488e42b00b5db3f9f7f76`
- role: `published_print_interior_master`
- source authority: final page images/layout

Separate recovered sources remain secondary:
- ebook PDF SHA-256 `24c93e3f041571cf106783e3a1700b5208e16bb4828baa413593816aa14edf34`
- extracted text DOC SHA-256 `07cdb5db20f4c60e9eb499595084c705b090f881f7c498b34736998d55a17a7b`

The extracted DOC is useful for text work but does not outrank the final paperback page images.

## Published level map

| Level | Source page start | Published title | Published key / skill |
|---|---:|---|---|
| 11 | 13 | The Daily Habit Loop | DISCIPLINE & AUTOMATION |
| 12 | 22 | The Nightly Reboot | REST |
| 13 | 30 | The Glitchy Wi-Fi | LISTENING |
| 14 | 38 | The Teflon Shield | RESILIENCE |
| 15 | 47 | The Spaceship Mutiny | CONTRIBUTION |
| 16 | 55 | The 6 and 9 Mystery | PERSPECTIVE |
| 17 | 64 | The Mental Spam | CRITICAL THINKING |
| 18 | 72 | The Pixel Zombie | BALANCE |
| 19 | 79 | The Pivot Dance | FLEXIBILITY |
| 20 | 86 | The Reality Glitch | TRUTH DETECTOR |

Published endgame / post-mission material begins at page 93 and continues through page 104.

Approximate mission page spans from the final PDF:
- L11: pp. 13–21
- L12: pp. 22–29
- L13: pp. 30–37
- L14: pp. 38–46
- L15: pp. 47–54
- L16: pp. 55–63
- L17: pp. 64–71
- L18: pp. 72–78
- L19: pp. 79–85
- L20: pp. 86–92
- endgame / special codes / loadout / bonus: pp. 93–104

## Current application repository

Repository: `riseshineevolve-source/spark-joy-fam`  
Current production main baseline is the completed World 01 Android rebuild.

World 01 merge commit:
`8e05b34ca4a8990635a4bf1c581e46ab41e48d1a`

Current production entry:
- `src/App.tsx` imports only `@/world01/World01App`
- World 01 canonical content lives in ten source-proven packs under `src/content/world01/`
- World 01 runtime is offline-first, device-local progress, no required auth/paywall
- Capacitor 8 / Android API 36 path exists

There is currently:
- **no** `src/content/world02/`
- **no** production `src/world02/` runtime
- **no** World 02 production entry path

Therefore World 02 is not currently a release candidate app.

## Legacy World 02 content found in the repository

Historical file:
`src/data/storyContent.ts`

Current blob:
`377463e1853743f82d4d3bca5ce89b6e5b05b210`

This file contains ten historical World 02 records (Levels 11–20), but the current World 01 README explicitly treats the legacy story-content layer as historical comparison material, not production source.

### Source-vs-legacy comparison

| Level | Published paperback | Legacy app | Result |
|---|---|---|---|
| 11 | The Daily Habit Loop / DISCIPLINE & AUTOMATION | The Daily Habit Loop / DISCIPLINE | **PARTIAL CONFLICT** — title aligns, key is incomplete and body is not source-verified |
| 12 | The Nightly Reboot / REST | The Nightly Reboot / REST | **TITLE/KEY ALIGN** — full body still unverified |
| 13 | The Glitchy Wi-Fi / LISTENING | The Glitchy Wi-Fi / LISTENING | **TITLE/KEY ALIGN** — full body still unverified |
| 14 | The Teflon Shield / RESILIENCE | The Teflon Shield / RESILIENCE | **TITLE/KEY ALIGN** — full body still unverified |
| 15 | The Spaceship Mutiny / CONTRIBUTION | The Spaceship Mutiny / CONTRIBUTION | **TITLE/KEY ALIGN** — full body still unverified |
| 16 | The 6 and 9 Mystery / PERSPECTIVE | The Worry Tornado / COURAGE | **HARD CONFLICT** |
| 17 | The Mental Spam / CRITICAL THINKING | The Apology Glitch / HONESTY | **HARD CONFLICT** |
| 18 | The Pixel Zombie / BALANCE | The Gratitude Hack / GRATITUDE | **HARD CONFLICT** |
| 19 | The Pivot Dance / FLEXIBILITY | The Battery Swap / EMPATHY | **HARD CONFLICT** |
| 20 | The Reality Glitch / TRUTH DETECTOR | The Dream Team Finale / UNITY | **HARD CONFLICT** |

The divergence is not a minor wording drift. Levels 16–20 are different missions with different titles, keys and story concepts.

### Audit decision

**Do not repair or extend the legacy World 02 data. Do not selectively reuse Levels 11–15 simply because their titles match.**

All ten World 02 missions must be re-extracted from the published paperback and placed into source-proven content packs. The legacy data can remain only as comparison evidence.

Reason:
1. the published paperback is already the locked canonical source;
2. Level 11 already demonstrates a source-key mismatch;
3. Levels 16–20 demonstrate wholesale story drift;
4. title alignment is not evidence that dialogue, science, quest, secret code or order are identical;
5. the proven World 01 rebuild already established the correct pattern: source graph first, runtime second.

## Required World 02 rebuild architecture

Reuse the World 01 production contract, not the old Lovable product shell.

Expected content direction:
- language-neutral stable IDs;
- canonical EN packs for Levels 11–20;
- explicit paperback SHA/source-page provenance;
- separate localized copy when PL is later authorized;
- source-aware node types for opener, dialogue, system log, Neuro Console, quest, secret family code, inventory/system notes and endgame;
- offline-first installed content;
- local progress by default;
- no account requirement merely to read;
- no client-side premium entitlement invention;
- no XP/reward mechanic unless source-proven;
- unsupported/missing node types fail closed.

The first implementation should preserve the current Level numbering **11–20** rather than renumbering World 02 to 1–10.

## Endgame / special material

Pages 93–104 are product content, not disposable appendix.

They include:
- Mission Accomplished / endgame protocol;
- NEVER FIGHT SOLO / squad handover;
- special emergency codes;
- Ultimate Loadout / Keys & Family Codes;
- create-your-own family code;
- bonus hacks;
- Learning Hub return/unlock pages.

These must be represented deliberately in the World 02 source graph/endgame. Do not silently copy the World 01 endgame or invent a generic completion screen.

## Science / wellbeing editorial boundary

The paperback contains neuroscience, neurodiversity, nervous-system, screen-balance, emotional-regulation and online-information claims. Source fidelity means the app must not silently rewrite these as stronger claims.

Before public release, run a separate factual/safety editorial review of source claims. That review may recommend calibrated wording, but it must be tracked as an editorial change against source rather than silently altering source extraction.

This audit does not independently validate the medical/scientific truth of every claim; it identifies that such a release review is required.

## Reuse boundary from World 01

World 01 proves:
- source-derived typed content packs;
- offline-first runtime;
- device-local progress;
- source-aware rendering;
- reduced-motion/safe-area handling;
- Capacitor 8 / API 36 Android path;
- deterministic content tests.

World 02 should reuse that architecture.

Avoid a broad factory rewrite before Level 11 exists. Extract only the reusable runtime pieces needed by the first real World 02 mission, then expand mission-by-mission.

## Audit conclusion

**AUDIT COMPLETE.**

Repository-side truth:
- canonical source recovered and hashed;
- 10 published mission boundaries known;
- current legacy-app conflicts identified;
- no production World 02 pack/runtime currently exists;
- correct rebuild path is unambiguous;
- World 01 is the implementation baseline.

Next safe implementation slice:
1. create World 02 source receipt/evidence manifest from the canonical PDF;
2. build **Level 11** as the first complete source-proven World 02 pack;
3. validate it through the reusable content graph/runtime;
4. only then scale Levels 12–20 in bounded source-proven batches.

No deployment, Play publication, pricing, backend creation or source-copy invention is authorized by this audit.
