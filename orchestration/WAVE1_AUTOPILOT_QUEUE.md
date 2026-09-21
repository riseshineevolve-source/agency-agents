# RSE Wave 1 Autopilot Queue

Updated: 2026-09-21
Rule: advance the highest-value safe task in each lane without owner interruption; stop only at OWNER GATE, dedicated-execution boundary, external configuration/device gate, or unrecoverable blocker.

Canonical precedence: `orchestration/brain/RSE_BRAIN_MASTER.md` + `orchestration/brain/PROGRAM_REGISTRY.yml` + latest `RSE_BRAIN_CHECKPOINT.yml` override stale lane notes here.

## Commercial priority stack — Q4 2026

Canonical source: `orchestration/brain/COMMERCIAL_PRIORITY_STACK.md`

1. **Detective Academy -> KDP**
2. **Mind Bloom -> Private DONE / frozen**
3. **24 Gentle Steps to Christmas**
4. **Optical Animals**
5. **Consumer App Factory / Google Play apps**
6. Senior / Happy Me / Opinie / AI Discovery continue safely in parallel below gates.

Revenue rule: do not wait for Google Play/DUNS when a quality-gated KDP product can ship independently.


| Lane | Project | Autonomy | Current state / next safe work | Stop gate |
|---|---|---|---|---|
| A | RSE Core / AI Discovery | AUTO + VERIFY | Indexing tracker is 7/10 indexed; all 4 C1 guides remain indexed. Adventure and Unstoppable remain crawled-not-indexed; Seniors remains unknown to Google. Continue measurement/recrawl evidence only; C2 content remains unauthorized. | Material public-content/business decisions and C2 expansion remain owner-gated. |
| B | Polish Localization Engine | AUTO + VERIFY through calibration | Calibration is green through controlled representative batches; Gentle Steps Week 1 text/source QA passes, but real-template layout fit remains pending. Do not start full-book production. | Explicit owner authorization before full segmented Polish production; real-template layout gate where required. |
| C1 | Detective Academy | AUTO + VERIFY through final interior / preflight | **ALL-15 = 15/15 PASS REMOTE** at `da0b5b1`; canonical 30-mission master integration PASS and 15 paired spreads generated. Final PDF is blocked only because local `assets/production` has not been populated. Run the existing `scripts/sync_brand_assets.py`, which maps canonical `assets/images` character/group art into the required production filenames, then render final interior and run strict KDP preflight. No owner asset-selection gate is required for this existing canonical mapping. | KDP upload/publication, pricing, final cover and physical proof remain owner-only gates. |
| C2 | Optical Animals | AUTO for inventory/tooling | 12 approved visuals protected, 8 unresolved. Dedicated target repo still does not exist as of 2026-09-21. Maintain manifest/preflight safeguards only; no art promotion, replacement or roster changes automatically. | Final 20 artwork/species roster is owner-gated. |
| D1 | Happy Me | AUTO + VERIFY below external release gate | Machine/source gates are green and external release gate packet exists. Target Supabase project is INACTIVE; do not restore silently. | Supabase activation/billing, Play signing, real-device/internal-track verification and commercial/publication decisions. |
| D2 | Senior / Hello Today | CENTRAL EXECUTION | Phase 14H source/CI baseline is green; production Child Mode remains OFF. Only fix newly verified source/CI blockers below external/legal/device gates. | Play/Firebase/Integrity, Families/legal/Data Safety, production Child Mode and real-device/human gates. |
| D3 | Mind Bloom | FROZEN / VERIFY ONLY | Private V1 Source Release Candidate is PASS; current head `bec72d0` has Mind Bloom CI #81 SUCCESS. Do not continue feature development or provider work merely because budget exists. | Reopen only for a reproducible Private V1 blocker or explicit owner decision on POST-V1 provider/commercial work. |
| D4 | Marketing Autopilot | DEDICATED EXECUTION + central sync | Dedicated marketing chat owns implementation. Central lane maintains durable architecture/status and verifies shared dependencies only when needed. | Paid marketing activation, spend/budget decisions and dedicated execution boundary. |
| E | Opinie | GitHub dev with synthetic fixtures; production local-only | Synthetic workbench CI green; deterministic provenance/review packet and explicit human review transitions pass. Dedicated target repo still does not exist as of 2026-09-21. Preserve the current human-gated boundary; do not invent speculative workflow states. | Confidential data, real case cloud use, automatic final expert conclusion and release remain hard owner/local gates. |

## LOCAL_PRIVATE companion lanes

These lanes may run only when their current conversation attachments/local working files are actually available. They never become remote portfolio source-of-truth.

| Project | Safe work | Hard boundary |
|---|---|---|
| Domowe Finanse 2026 | Local code/debug/hardening with synthetic fixtures; preserve business rules and layout. | Never send real workbook data, names, amounts, descriptions or derived private outputs to GitHub/web/connectors. Skip the lane if local files are unavailable. |
| Smart CV Tailor / CV | Local renderer/import/matching/QA hardening; preserve approved Standard CV + ATS contract and truth/evidence lock. | Never send CV/Experience Database/contact/application content or derived private outputs to GitHub/web/connectors. Skip the lane if local files are unavailable. |

## Consumption priority when Codex allowance is scarce

1. Detective Book Factory release/blocker work required to reach ALL-15, final interior and KDP preflight.
2. Polish Localization Engine work that prepares Detective PL without translating a moving English master; after EN freeze, Detective PL becomes the next commercial sprint.
3. 24 Gentle Steps work that preserves the Christmas seasonal window, especially source/layout/localization blockers.
4. Optical tooling that removes repeated manual work without touching approved art; final visual promotion remains owner-gated.
5. Consumer App Factory / Google Play work only when it is high-value and not blocked by Google/DUNS/external setup.
6. Senior / Happy Me / Opinie / AI Discovery continue below gates; prioritize concrete blockers, not speculative scope.
7. Mind Bloom consumes no Codex by default while Private V1 is frozen; use it only for a reproducible release blocker or explicit owner reopen.
8. Never spend Codex allowance merely to generate status summaries, repeat audits, rewrite settled documentation, or wake Wave 2/Gifts.

## Work bundling rule

Prefer one well-scoped Codex task that contains:
- exact source-of-truth pointers,
- one milestone,
- permitted files/surfaces,
- tests to run,
- owner gates,
- required checkpoint output.

Do not create a series of tiny sessions for steps that can be executed and verified together.

## Idle-lane rule

A lane may be intentionally idle when:
- it is waiting at an OWNER GATE,
- it is waiting for external account/device configuration,
- required assets exist only on the local machine and are not currently connected,
- another dedicated execution chat owns the shared dependency,
- additional work would only create speculative scope.

Idle is better than burning Codex on invented work.
