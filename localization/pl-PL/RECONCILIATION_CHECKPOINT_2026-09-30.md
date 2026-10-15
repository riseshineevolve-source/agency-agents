# Polish Localization Engine — bounded execution checkpoint 2026-09-30

Status: **BOUNDED SLICE IMPLEMENTED / CURRENT-MAIN RECONCILED / OWNER GATES OPEN / NO MAIN MERGE**

This checkpoint records the dedicated Polish Localization execution slice requested on 2026-09-30. Central RSE priorities were not changed.

## Git provenance

| Item | Exact state |
|---|---|
| PR #13 branch before this slice | `07f5324b3e02993886fcb94d84e8bc70d11b6c20` |
| live `main` reconciled | `dc49a7020375e38aa8a4205d836c90a12303adbc` |
| pre-sync relation | localization branch 6 commits ahead / 29 behind; common merge base `6beda0188c3dcca897cbf2468c995b356260e112` |
| changed-path overlap | **0** |
| sync mechanism | PR #15, `main → codex/polish-engine-main-reconcile` |
| sync merge commit | `75d7f43d17188c2f2b971c241fda273f8ff18fb8` |
| implementation head before this checkpoint file | `74fa699e2b7756f4a50f2d6858f0cc68d218d915` |

The sync changed only the localization execution branch. `main` was not mutated.

## Gentle Steps — owner re-authoring direction operationalized

Owner direction from `orchestration/quick-desk/inbox/2026-09-30-gentle-steps-pl-reauthoring.md` is now converted into a project-specific execution profile:

`localization/pl-PL/GENTLE_STEPS_PL_REAUTHORING_PROFILE.md`

Locked workflow:
1. extract immutable function/mechanics;
2. write native Polish from the functional brief rather than sentence-level English;
3. Polish family-language edit;
4. humor + character-voice pass;
5. anti-coaching / anti-translationese pass;
6. bilingual factual/mechanical backcheck;
7. read-aloud + real-surface QA.

Existing Gentle Steps Polish calibration copy was **not deleted**. It is preserved as historical QA/reference evidence.

The two historical Gentle Steps golden fixtures now carry explicit `REFERENCE ONLY` supersession banners.

### Real-template fit safety

`localization/pl-PL/engine/gentle-steps-fit.json` is now:
- `copy_authority: REFERENCE_ONLY`;
- limited to historical Week 1 geometry calibration;
- explicitly unable to approve production Polish copy.

The fit engine now returns:
- `REFERENCE_PASS` when the historical exact headings genuinely pass real-template evidence;
- `BLOCK` when evidence is incomplete/stale/proxy/typographically changed;
- never production `PASS` for the superseded copy.

The CLI treats `REFERENCE_PASS` as non-release success by returning a non-zero status, so old copy cannot silently close a production gate.

A new exact-text fit spec is required after native Polish re-authoring.

## Detective Academy — current V3 receipt refreshed, full PL still blocked

Current V3 candidate:
- source-lock revision: `e136e94402c8f870f3d9221b7047c1406cbec813`;
- Git blob: `8685f8e561d0bfb3837445b72b4d6f799a9a48f2`;
- raw SHA-256: `a74bd490e454394ac3c9cb39507278d36d0e7ed6542d1b84a47d2a7ba6b1a0ae`.

The tracked Detective pre-freeze receipt and readiness package now bind this current source instead of the older V3 bytes.

No full Detective Polish translation was started.

The pre-freeze guard still protects:
- 30 ordered reader cases;
- six-part case apparatus;
- 90 Hint Vault entries;
- 30 Solution Files;
- ordered system/meta sections.

The current V3 text appendix still contains legacy `upside-down` orientation wording while the production handoff requires upright Hint/Solution pages. Localization does not choose between them; final EN render truth must reconcile this before freeze.

## CI / verification contract

All implementation changes are committed to the PR #13 branch. Exact-head GitHub CI must be evaluated on the final checkpoint head; historical green runs are not sufficient. The authoritative exact-head CI result belongs in PR #13 after workflows finish.

No failing gate may be weakened merely to make CI green.

## Real owner gates reached

### Gentle Steps
Production language cannot be globally locked until owner resolves the voice-defining brand choices:
- final Polish product title;
- the three recurring daily labels currently provisional (`Mindful Moment`, `Fun Spark`, `Family Connection`);
- any editorial/safety trade-off surfaced by re-authoring;
- final visual/editorial approval of the complete Polish proof.

### Detective Academy
Full Polish production remains blocked until:
- exact hydrated EN interior is final;
- KDP/preflight + representative physical proof pass;
- explicit owner instruction `FREEZE EN INTERIOR`;
- final structured source hash, ALL-15 evidence and frozen aliases are recorded.

## Explicit non-actions

This slice did **not**:
- change central RSE priorities;
- merge PR #13 into `main`;
- publish or deploy any product;
- approve old Gentle Steps copy as production;
- lock Gentle Steps title/recurring labels;
- freeze Detective English;
- start full Detective Polish translation.
