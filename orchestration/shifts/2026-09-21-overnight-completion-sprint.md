# RSE Overnight Completion Sprint — 2026-09-21 -> 2026-09-22

Window: 2026-09-21 21:15 -> 2026-09-22 08:15 Europe/Warsaw
Mode: high-intensity parallel completion sprint
Owner intent: use available Codex capacity aggressively on real DONE milestones, not status/audit churn.

## Parallel-writer rule

Run at most one writer per repository/worktree.

Approved concurrent lanes:
1. Detective Academy — repo RISE.SHINE.EVOLVE / feature/detective-book-factory
2. Polish Localization Engine — repo agency-agents / rse/polish-localization-engine-v1
3. Senior / Hello Today — repo hello-today-android. / phase14h-paired-child-device-6plus or current successor branch
4. Optical Animals tooling — its dedicated/local checkout only; preserve approved art and inspect remote before push

Do NOT run a second writer in any of these worktrees.

## Lane 1 — Detective Academy

Current state:
- owner-review V2 in progress
- current remote owner-review base head: 71baf0cc164b69ada78e4ce615783b344a0b3371
- approved owner asset is now present locally at assets/images/Happy Makers detectives.png
- EN is NOT frozen
- Polish full-book translation remains blocked until explicit owner freeze

Overnight target:
- detect newly present squad asset
- update canonical sync mapping
- finish all-15 V2 regeneration
- complete global typography / opening / writing surfaces / verdict / map readability / Witness Board / naming application / drift audit
- generate HMDA_Book1_EN_OwnerReview_v2.pdf + full contact sheets + preflight
- commit/push coherent checkpoint
- stop at owner visual approval; do not freeze/publish/price

## Lane 2 — Polish Localization Engine

Current branch:
rse/polish-localization-engine-v1

Current durable state:
- reconciled with main at 10b8189
- PR #6 mergeable
- regression PASS across 7 accepted fixtures / 37,159 candidate chars
- Gentle Steps source-side spot-check PASS
- Detective profile/calibration/logic preservation active
- Detective full-book scale-out owner-frozen until EN source freeze

Overnight target:
- finish reusable pl-PL production infrastructure needed by current RSE products
- harden deterministic source segmentation, provenance/backcheck, terminology locks, designed-surface budgets, app/UI/book/PDF adapters and regression reporting
- advance Gentle Steps only below real-template gate; never fake template evidence
- prepare exact zero-discovery handoff for full Detective PL immediately after EN freeze
- do not start full Detective translation

## Lane 3 — Senior / Hello Today

Current PR #77:
- head 618063ebde6980f5c7cbcc9c9b5f11d44bf6f027
- mergeable
- Phase 14H source/CI baseline green
- Child Mode remains production-disabled
- external Play/Firebase/Integrity/Families/legal/Data Safety/real-device gates remain

Overnight target:
- exhaust only concrete repository-side release-hardening work tied directly to existing external gates
- improve deterministic local verification / release evidence / config fail-closed tooling / reproducible release packet where a real gap exists
- do not invent new features or cross legal/device/production gates
- if current repo genuinely has no safe source work, stop early with evidence rather than burn quota

## Lane 4 — Optical Animals tooling

Current:
- 12 approved visuals protected
- 8 owner-gated final selections
- local hardening commit 5e69b43 exists
- dedicated target repo status must be verified before push

Overnight target:
- inspect git remote and preserve local 5e69b43
- if canonical remote is safe/confirmed, publish durable tooling checkpoint
- continue deterministic assembly/preflight/release-manifest tooling only
- no artwork regeneration, promotion or final-20 owner decisions
- build as much reproducible KDP assembly automation as possible below visual gate

## Deliberately parked

Happy Me:
- machine/source release gates already green
- target Supabase production project remains external/owner gate
- release packet explicitly says no new source-only task should be invented without code/config changes
- do not spend overnight Codex capacity here

Mind Bloom:
- Private V1 frozen
- no overnight spend

Marketing:
- separate dedicated execution chat
- no parallel Codex writer from central sprint unless specifically requested

## Morning success criteria

By 08:15:
- Detective V2 either ready for owner visual review or stopped only on a concrete owner asset/visual gate
- Polish Engine materially closer to production-scale reuse, with all work durable
- Senior either gains a real release-hardening milestone or proves all remaining work is external
- Optical tooling gains a durable reproducible release milestone without touching art decisions
- no duplicate writers, no unnecessary CI, no owner gates crossed
