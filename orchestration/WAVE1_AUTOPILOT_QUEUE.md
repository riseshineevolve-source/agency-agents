# RSE Wave 1 Autopilot Queue

Updated: 2026-09-18
Rule: advance the highest-value safe task in each lane without owner interruption; stop only at OWNER GATE, dedicated-execution boundary, external configuration/device gate, or unrecoverable blocker.

| Lane | Project | Autonomy | Current state / next safe work | Stop gate |
|---|---|---|---|---|
| A | RSE Core / AI Discovery | AUTO + VERIFY | 4/4 C1 guides indexed; app pages remain crawled-not-indexed on old crawl dates; seniors discovered-not-indexed; monitor recrawl/public-search propagation without creating C2 content | Bing evidence requires GSC Wizard Bing API key; material public-content/business decision remains owner-gated |
| B | Polish Localization Engine | AUTO + VERIFY through calibration | Round 2 PASS; Round 3 bilingual/surface PASS; Day 11 full pilot PASS; Days 05/20/25 bounded batch PASS; regression validator + CI + segmented scale-out plan added | explicit owner authorization before starting the full 244-page segmented Polish production run |
| C1 | Detective Academy | AUTO + VERIFY below visual gate | production manifest locked to 15 spatial modules; Book Factory remains code-driven; geometry/solution logic preserved | spatial-map visual standard approval before mass conversion |
| C2 | Optical Animals | AUTO for inventory/tooling | 12 approved visuals, 8 unresolved; manifest/tooling remains source-of-truth | final 20 artwork/species roster is owner-gated |
| D1 | Happy Me | AUTO + VERIFY below external release gate | source/CI machine gates passed; no source-only queue remains | Supabase/Play signing external configuration + real-device/internal-track verification |
| D2 | Senior / Hello Today | dedicated chat + central sync | Phase 14H open PR #77: paired Child Device + 6+ UX boundary; Child Mode still production-disabled | dedicated execution + Play/Firebase/Integrity, Families/legal/Data Safety and real-device gates |
| D3 | Mind Bloom | dedicated chat + central sync | Draft PR #2 on `feature/personal-chief-of-staff-foundation`; CI #42 PASS; active slice Phase 1G-B People Memory | dedicated execution owner; protect local People work and reconcile reviewed Supabase migrations before merge |
| E | Opinie | GitHub dev with synthetic fixtures; production local-only | bootstrap spec ready; target repo `opinie-offline-workbench` not yet created; real case data remains forbidden remotely | current GitHub connector cannot create repositories; confidential data and final expert conclusions remain hard owner/local gates |

## Consumption priority when Codex allowance is scarce

1. Release/blocker code work that cannot be done deterministically.
2. Detective Book Factory or Happy Me implementation requiring repository reasoning.
3. Polish Engine implementation only after a concrete failed regression or after owner authorizes segmented scale-out.
4. Tooling for Optical Animals only when it removes repeated manual work.
5. Never spend Codex allowance merely to generate status summaries, repeat audits, rewrite settled documentation, or wake Wave 2/Gifts.

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
