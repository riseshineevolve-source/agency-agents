# Polish Localization Engine — current-main reconciliation checkpoint

Status: **DRAFT PR #13 REFRESHED IN ISOLATED WORKTREE / EN NOT FROZEN / NO MERGE**
Date of refresh: 2026-09-29/30. The original checkout at `147f160c1e5b5df8cd930d817bf42a64cc85af82` was not reset, cleaned, rebased, stashed or edited.

## Git provenance

| Ref at refresh | Exact SHA |
| --- | --- |
| Durable remote PR #13 head before refresh | `ca9df86a3154f5776dd3ef2e2889d1e6fff3f438` |
| Live `origin/main` fetched before reconciliation | `6beda0188c3dcca897cbf2468c995b356260e112` |
| Pre-merge merge base | `ff091c9d591431b3513546cf8ad68b25cc79b1d2` |
| Conflict-free normal merge of current main | `e2fac5ee735543c71f34f5a2ca54b0b4ae010196` |

Before the merge the PR branch was **4 commits ahead / 119 behind** live main. There were 57 PR-side paths and 61 main-side paths changed since the merge base, with **zero overlapping paths**. A normal non-force merge succeeded with no conflict. It brought current-main portfolio/orchestration and Detective V3 truth into the PR branch without editing those files. The final checkpoint commit follows this merge; its exact pushed SHA and current-head CI belong in PR #13 and the handoff report.

## Verification and review debt

Local Polish regression on the merged branch: terminology documentation check PASS; 59 localization contract/adversarial tests PASS (including four V3 guard tests); five backcheck tests PASS; seven fixture sets PASS. Fixture proof covers 31 bilingual segments, zero deterministic errors, zero stale translations and **34 review items**. The 34 classify as:

- Detective calibration: 19 missing measured real-surface fit budgets.
- Gentle Steps Christmas: three calibration fit budgets, four Week 1 real-template heading proofs, three provisional term approvals.
- Project Unstoppable: five web/app fit budgets.

No item is a deterministic defect or demonstrably stale on current evidence; safe automated reduction is therefore **zero**. These open gates retain their severity. No proxy count or candidate wording is promoted to print-layout or language PASS. Repository consistency checks and exact-head PR CI remain required at push; historical `ca9df86...` checks are not current-head evidence.

## Detective V3 pre-freeze handoff

Canonical candidate text is Git blob `a85a5941852930f6b88711af26b16ea1651d2fbc` at `orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`; raw SHA-256 is `1af8564985d382f2a6ed3154798e9a4f5e201fa5726ca1478015d774682f5ac0`. The [readiness package](DETECTIVE_PL_PREFREEZE_READINESS_2026-09-29.md) inventories its 30 cases, 90 hints, 30 solutions, new recurring surfaces, meta callbacks, protected puzzle truth, source/raster hydration gap, provisional terminology and pending freeze receipt. The guard checks bytes and structure; the existing Book Factory YAML gate still requires explicit owner freeze, final structured source hash, ALL-15 evidence and frozen aliases before a full-book source plan can be generated.

English remains **NOT FROZEN**. No full Detective Polish translation, English freeze, final term auto-approval, main merge, publication or print-layout PASS is authorized by this checkpoint. After the owner freeze, reconcile final composed source plus assets/renderer literals to V3, pass the frozen receipt and existing `detective-prepare` guard, annotate logic and measured fit, then begin bounded mission-complete translation and real-template QA.
