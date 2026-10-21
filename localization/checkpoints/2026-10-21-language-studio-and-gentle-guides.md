# Polish Localization Engine: Language Studio and Gentle Steps V3

Date: 2026-10-21
Writer scope: localization tooling/candidates and own mailbox only.
Branch: `codex/polish-engine-language-studio-20261021`
PR: https://github.com/riseshineevolve-source/agency-agents/pull/40
Base main: `4b123f5ccdb77f7a8e4390624f7466d16ba665a6`
Initial implementation commit: `547518585b2d8c598f93f55f0dc72d61d2d8e71e`.
Final checkpoint commit is the commit containing this file; inspect PR current head.

## Source and preservation

Read current Universe Map, chat registry, autonomy protocol, lane bootstrap and
own/dependency mailboxes. Latest explicit owner locks override stale PDF labels.
The uploaded premium-content prompt is stored byte-exact under
`tools/rse-language/source/` with a SHA-256 manifest. Its proposed three premium
bootstrap/protocol/runbook paths were absent from main; this checkpoint does not
claim those absent files were read. Book Agent v3 and Book Map contracts exist.

PL Gentle Steps R6 was read from pinned engine snapshot
`8b484a528cd2ef85d23d5efc5c5c341a2fd02985`. Exact Git blob:
`896cf92bf6ed126ef62e623fd9cac640270e853f`. SHA-256:
`68ad0a94b7cb4713c825fe1c6af4507eac5c982cb3b0054000d18ddeaf0457b3`.
A temporary local extra final newline from hydration was removed only after the
Git blob matched. No source prose changed. The existing 24-day book/app masters,
website, Book Factory and Detective PL R8 were not edited.

## Reusable tool

`$rse-language` accepts short PL/EN translation/authoring or same-language upgrade
requests. Repo skill: `.agents/skills/rse-language/SKILL.md`; Python facade:
`scripts/rse-language.py`; profiles/guide: `tools/rse-language/`.
The installed skill was saved with Git; current saved revision is recorded in
the mailbox. The calling assistant writes/reviews prose. The CLI needs no API
key and does not pretend to generate a book by itself.

The facade protects exact snapshots, stable IDs, scoped changes, tokens, optional
number invariants and product strings. Cross-language authoring requires a
complete validated functional brief, packet/receipt and candidate packet hash.
Specialist reviews bind raw candidate bytes. Existing engine remains intact; no
blind merge from diverged old engine branches was performed.

## Four Gentle Steps articles

Canonical localizations: `localization/campaigns/gentle-steps/2026-10-21/v3`.
Unchanged V2 baselines, attachment/source hashes, editorial receipt and final
candidate hashes are retained alongside them. PL/EN are sibling campaigns.
Article 1 uses Day19 pause, Day10 game, Day07 question; article 2 uses Day21 pause,
Day22 game, Day14 question. No full day is exposed. Actual final reread found no
material language/meaning defects. CTA destinations remain the sole website
writer's responsibility. No current sale/edition availability is invented.

Deliverable: `RSE_GENTLE_STEPS_ARTICLES_PL_EN_V3_20261021.zip`, SHA-256
`807ec7d52fbb4e9876ae49ef8c9be057873394b90a72dffbc22a0926829cab2f`.
Saved file identity: `libfile_8e6a48cd11c48191bbc1ec7b5c4922c6`.
Owner editorial approval and publication remain open.

## Validation

- New facade: 31/31 regression tests PASS locally after the final source-issue guard.
- Existing engine: 59/59 tests PASS on byte-verified hydrated snapshot `8b484a5`; its scripts were not changed.
- Skill metadata/frontmatter validation: PASS; installed skill push `423eb90` succeeded.
- Real transfer trial: actual source-isolated writer, four actual final stage reviews; final strengthened check = OWNER_GATE for three source-clarity defects, deterministic QA PASS.
- Hosted CI: no workflow runs returned for initial implementation commit `5475185`; final exact-head CI must be inspected separately and is not claimed PASS.
- Four campaign candidates: source/day coverage, exact final hashes, language/meaning review PASS; owner publication approval not granted.

The isolated trial used a wording-free packet, fresh writer and three independent
reviewers covering four stages. A real collocation defect was repaired by the
sole writer; final reviews were bound to the new hash. It also surfaced original
source-game ambiguities. These were preserved and flagged instead of inventing
rules or claiming a complete playable-game proof. The final tool check after
issue-ledger enforcement is recorded with the trial evidence. This fixture is
not a new RSE product or owner-facing production gate.

## Consumer handoff and remaining gates

Website consumes V3 only after owner editorial approval, resolving an actual
preview/product route and verifying live title, formats and language routing.
The supplied wrap reference opens locally and still contains abcabc placeholders;
this is an observation about that attached reference, not the current production
wrap. Gentle Steps retains its real-template/device/release gates.

Detective PL retains the verified complete R8 and FINAL70/four-zero decisions.
Designed R8 proof remains authorized. Do not start competing translation.
Migration to a later evolving EN master needs explicit exact-source freeze.

Main was not merged. No product publication, release, source freeze or owner
approval was granted by this work. A mailbox update is a durable handoff, not
evidence that another chat woke or acknowledged it.
