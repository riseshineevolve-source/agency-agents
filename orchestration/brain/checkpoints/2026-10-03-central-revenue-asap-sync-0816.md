# Central revenue-ASAP sync — 2026-10-03 08:16 Europe/Warsaw

Status: VERIFIED / CENTRAL CHECKPOINT ONLY / NO PRODUCT-LANE MUTATION

## Source-of-truth snapshot
- agency-agents main: `c12e5fec42deffe3b8d6892f1c12023a09a9b88f`
- Detective First18 agency branch: `execution/detective-first18-20261002@487ea222257dd0f0c1b9798880b1861142617281`
- Detective First18 factory branch: `execution/detective-first18-20261002@9db186446e2ed321adada80ec025e5c18a1a472c`
- Detective factory base: `feature/detective-book-factory@e6a531bc6f26b7cafc4fa73b1af5ee549d1c4283`
- Gentle Steps app delegated branch: `gentle-steps/app-en-full24-purple-gold@494a9652c6edf96faf151d75b2753b6e2754fff3`
- Marketing delegated reconciliation branch: `marketing/reconcile-2026-10-02-1624@411f8f768d57b8e9c2352afeb016872d2246389f`

## Material reconciliation
Fresh read of delegated Marketing checkpoint `marketing/DETECTIVE_STATIC_LOCK_REAUDIT_2026-10-02.md` resolves the front-cover identity direction for current marketing/cover work:
- current final cover: `Akademia Detektywów_ Tajemnica Pokoju Zero.png`
- SHA-256: `935cdf705c4107a3139cd55e8f639eaae5c0959631b1f28ebc359376cd9b77ad`
- old Oct-1/Sept-25 cover SHA `2570df512f3883663aca1c4e5359ba12aa0489276f484b86ac5623ab037429a9` is explicitly marked NOT CURRENT / RETIRED in that delegated re-audit.

This matches the newer main-file `marketing/DETECTIVE_FINAL_CHARACTER_LOCK_2026-10-02.md`, which is OWNER LOCKED and names the same current final cover SHA.

## Remaining Detective packaging blocker
The ambiguity is no longer which newer cover Marketing considers current. The unresolved release-package issue is that main `marketing/DETECTIVE_ACADEMY_KDP_RELEASE_PACKAGE.md` and `marketing/DETECTIVE_ACADEMY_COVER_A_PLUS_VISUAL_LOCK.md` still carry stale 2026-09-25 cover/page-count wording. Central will not edit those delegated Marketing surfaces while Marketing ownership is active.

Final wrap generation therefore remains blocked until:
1. the current final interior/page count is owner-approved after the First18 gate and full-book scaleout;
2. the delegated Marketing/KDP release package is reconciled to the current locked cover SHA and final page count;
3. transparency-safe final interior and full visual regression pass;
4. real KDP Previewer + physical proof are completed by owner.

## Current highest-value gate
Detective First18 remains NOT OWNER-FROZEN. Case 02+ stays READ-ONLY. H01/H02/H03 owner decisions remain the next product gate.

No merge to main, EN freeze, publication/upload, production deploy, spend, paid activation, secrets/signing keys, art mutation, or delegated-lane write occurred.
