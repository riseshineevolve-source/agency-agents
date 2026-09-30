# RSE Brain Master

Status: CANONICAL
Rebuilt: 2026-09-18
Last reconciled: 2026-09-26
Primary durable repo: `riseshineevolve-source/agency-agents`

## 1. Operating model

Rise.Shine.Evolve. is managed as a portfolio, not as a pile of chats.

Central RSE Orchestrator owns:
- portfolio sequencing,
- dependencies,
- durable decisions,
- recovery,
- AI Discovery,
- brand/business coordination,
- Polish Localization Engine,
- Detective Academy,
- Happy Me coordination,
- Optical Animals coordination,
- Senior / Hello Today portfolio coordination (read-only while the delegated worker is active),
- Mind Bloom Assistant portfolio/privacy coordination (read-only while the delegated worker is active),
- marketing architecture,
- content-source recovery.

Dedicated execution ownership is now split to increase parallel throughput while preserving one writer per surface:

- **Central RSE Orchestrator (this chat):** portfolio coordination + Detective Academy + Polish Localization + Optical Animals + cross-project decisions.
- **Happy Me delegated execution chat:** Happy Me Adventures only. Canonical handoff: `orchestration/handoffs/HAPPY_ME_DELEGATED_EXECUTION_HANDOFF.md`.
- **Senior / Mind Bloom delegated execution chat:** Senior / Hello Today active repository-side product/content completion + Mind Bloom bounded PRIVATE SINGLE-OWNER DEPLOYMENT / PRIVACY COMPLETION. Canonical handoff: `orchestration/handoffs/SENIOR_MIND_BLOOM_DELEGATED_EXECUTION_HANDOFF.md`. Central must not write either delegated repository while that worker is active.
- **Marketing Autopilot:** remains a separate dedicated marketing execution stream.

The Central RSE Orchestrator remains the only chat allowed to mutate central portfolio priorities, RSE Brain, Commercial Priority Stack and cross-project sequencing.

Delegated chats must checkpoint inside their project repositories and report meaningful milestones/blockers back to Central; they must not edit the same project branch/worktree in parallel with another chat.

Mind Bloom Private V1 remains source-RC PASS and ordinary feature development remains frozen. Owner decision 2026-09-25 explicitly reopened only a bounded PRIVATE SINGLE-OWNER DEPLOYMENT / PRIVACY COMPLETION lane under the delegated Senior/Mind Bloom worker. Provider/OAuth Phase 2B remains owner-gated and inactive; private-data boundaries are non-negotiable.

Opinie uses a special split model:
- sanitized code + synthetic fixtures may be developed in GitHub,
- real case files, archives, embeddings, evidence and outputs remain local/offline.

## 2. Non-negotiable workflow

`CURRENT TRUTH -> PLAN -> IMPLEMENT -> VERIFY -> CHECKPOINT -> NEXT GATE`

Do not run parallel writers over the same product surface.

Default agent routing:
- CORE first,
- specialists only where they add unique expertise,
- default max ~4 active roles,
- deterministic checks before expensive agent/Codex work.

## Commercial priority stack — Q4 2026

Canonical priority file: `orchestration/brain/COMMERCIAL_PRIORITY_STACK.md`
Portfolio completion snapshot: `orchestration/brain/PORTFOLIO_COMPLETION_SNAPSHOT.md` (working estimate only; live repo facts override)

Owner-locked order:
1. **Detective Academy EN -> KDP** — primary revenue lane; do not wait for Google Play/DUNS.
2. **Detective Academy PL -> KDP Poland** — immediate second commercial edition after explicit English-source freeze.
3. **Optical Animals** — giftable KDP lane; owner reports 19/20 illustrations ready. Finish final art plus exact-source seek-and-find identity pipeline; never substitute invented lookalikes.
4. **24 Gentle Steps to Christmas** — seasonal Q4 lane, explicitly sequenced after Optical Animals.
5. **Consumer App Factory / Google Play apps** — strategic, but below shippable KDP revenue while Google/DUNS gates remain.
6. **Senior / Happy Me / Opinie / AI Discovery / Website** — continue safely in parallel below their gates.

Frozen/non-active commercial lane: **Mind Bloom Private V1** — source release candidate PASS / feature development frozen; future provider or commercial work is a separate owner-gated decision.

Operational sequence: **Detective EN KDP -> Detective PL KDP -> Optical Animals gift lane -> Gentle Steps seasonal lane -> Google Play acceleration when external gates clear.**

## 3. Global product/business sequence

### A. Current production baseline
Protect already-shipped cleanup and current app direction.

### B. Business + brand master strategy
Unify positioning, customer, offer architecture, brand architecture and website strategy.

### C. Change filter
Every meaningful proposal becomes:
- ACCEPT,
- HOLD,
- REJECT,
- OWNER GATE.

### D. English master
Approved strategy/copy/product architecture lands in English first.

### E. AI Discovery reconciliation
Canonical product/entity truth, schema, sitemap, intent content, feeds, evals and search monitoring must describe the current English reality.

### F. English freeze
Stable English becomes canonical source.

### G. Polish transcreation
Polish Localization Engine localizes stable source, not a moving target.

### H. Polish discovery layer
Polish search intent, structured content and local cultural/search behavior are handled after localization.

## 4. Brand foundation

Master brand: **Rise.Shine.Evolve.**

Current architecture:
- Master brand: Rise.Shine.Evolve.
- Audience gateways: Kids & Families / Teens / Adults / Seniors.
- Character IP: The Happy Makers, primarily Kids & Families.
- Product worlds may differ visually while sharing RSE DNA.
- Free layer: GIFTS / Tiny Tools / Product Finder.
- Commerce: Amazon KDP / Google Play / future verified channels.

Important correction from older work:
The Happy Makers are NOT forced as the visual/character layer for every RSE audience. Senior App can belong to RSE without adopting the kids' universe.

Current strategic territory:
- **Real-life skills, made playable.**
- family variant: **Family growth, made playable.**

Desired post-contact feeling:
**"OK. We've got a next move."**

Brand personality:
- Playful
- Clever
- Warm
- Practical
- Brave

Current buyer focus:
parents/caregivers of children roughly 6–10.

Child user principle:
the child should not feel "fixed"; experiences should offer agency, humor, discovery, challenge and choice.

Voice:
- kids: fun, clear, intelligent, never babyish,
- teens: dry wit, concise, no forced coolness,
- parents: warm, practical, zero parent guilt,
- adults: less gaming vocabulary, intelligent partner tone.

Ownable language candidates already developed:
- Made for the messy Tuesday.
- One small move. Real-life level-up.
- Same team. Next move.
- Less lecture. More doing.
- Rise. Shine. Evolve. Repeat.

## 5. Business / Revenue Engine

Working program: **RSE CORE Revenue Engine v1**

Primary objective:
`DISCOVERY -> USEFUL FREE EXPERIENCE -> IDENTIFIED LEAD -> TRUST/NURTURE -> GOOGLE PLAY APP -> ACTIVATION -> VALUE -> PURCHASE -> REVIEW/REFERRAL -> NEXT PRODUCT`

Current positioning lock used in the Revenue Engine:
**More useful than a printable. More playful than a parenting course. Far lighter than therapy.**

Safety interpretation:
this communicates low-friction practical usefulness. It must never imply diagnosis, treatment, or replacement of therapy/professional care.

Current strategic locks:
- Rise.Shine.Evolve. is the umbrella brand.
- Happy Makers are the primary consumer IP for the children's ecosystem.
- Primary v1 audience is parents/caregivers of children about 6–10.
- Primary product focus is the Happy Me / Happy Makers ecosystem.
- Apps are moving to Google Play.
- Project Unstoppable is secondary/future teen focus.
- Adults is future path.
- Seniors is a separate path after Adults.
- GIFTS are acquisition/product-demonstration assets, not a disconnected product line.
- Existing books remain revenue/acquisition assets.
- No new RSE product lines during CORE Revenue Engine v1 without owner approval.
- No subscription model without owner approval.
- No broad opportunistic redesign/refactor.

First funnel concept:
`SEARCH/SOCIAL/AMAZON/AI -> RSE CONTENT -> HAPPY MAKERS GIFT -> EMAIL CAPTURE -> INSTANT USEFUL RESULT -> NURTURE -> HAPPY ME GOOGLE PLAY -> ACTIVATION -> VALUE -> REVIEW/REFERRAL -> NEXT PRODUCT`

Event schema concept includes:
landing_view, gift_view, gift_started, gift_completed, lead_capture_started, lead_captured, email_clicked, app_store_clicked, app onboarding/mission events, day-3/day-7/day-30 return, purchase/refund, review and referral events.

## 6. AI Discovery / Commerce

Architecture:
**ONE canonical product + entity truth layer, multiple platform adapters.**

Target platforms:
- ChatGPT/OpenAI Search & Shopping,
- Google Search / AI Overviews / AI Mode,
- Bing/Copilot,
- Claude Search,
- Perplexity.

Never create five independent truths or duplicate AI-specific product pages.

Current app truth:
- old PWA/browser/Paddle/SaaS/12-month model is SUPERSEDED,
- current direction is Android / Google Play,
- use Coming Soon until real store URLs/prices/dates exist,
- Seniors is present after Adults.

AI Discovery principles:
- OAI-SearchBot discovery is distinct from GPTBot training policy.
- Google/Gemini uses normal search fundamentals; no separate "Gemini SEO" system.
- Bing uses sitemap + IndexNow + Bing Webmaster / AI Performance when available.
- Claude-SearchBot / Claude-User discovery must not be accidentally blocked.
- Perplexity commerce is an adapter, not source of truth.
- structured data must match visible content.
- never fabricate price, availability, ratings, reviews, identifiers, launch dates or medical/scientific claims.
- no mass AI SEO page generation.

Current measurement state is tracked in the central project registry and issue #584. As of 2026-09-24, fresh GSC Wizard inspection is blocked by `payment_required`; no paid monitoring service may be restored automatically, and C2 content remains unauthorized until fresh evidence justifies it.

## 7. RSE Consumer Platform + Bilingual App Factory

Target public-app architecture:
- one shared RSE Consumer identity/data platform for ordinary public consumer apps where justified;
- World 01 is the intended first real factory pilot after source approval;
- World 02 and 24 Gentle Steps to Christmas should reuse the same proven runtime/content contract;
- English + Polish live in one product/runtime by default, with language-neutral content IDs;
- offline-first for core content where feasible;
- guest-first allowed where account creation is not genuinely required;
- no new Supabase/Firebase project merely because a new app exists.

Identity and paid access are deliberately separate:
- authentication answers **who is this account?**
- entitlement answers **which exact product/content may this account access?**
- one RSE login never implies ownership of every RSE app;
- product access is keyed by account + product and must fail closed when the matching server-authoritative entitlement is absent;
- client-only premium flags are forbidden.

Current durable contracts:
- `orchestration/architecture/RSE_CONSUMER_PLATFORM_APP_FACTORY.md`
- `orchestration/architecture/RSE_CONSUMER_SYNTHETIC_DATA_CONTRACT_V0.md`
- `orchestration/architecture/RSE_CONSUMER_ENTITLEMENT_MODEL_V0.md`
- `orchestration/architecture/RSE_INTERACTIVE_BOOK_CONTENT_CONTRACT_V0.md`
- `orchestration/architecture/RSE_CONSUMER_SUPABASE_EPHEMERAL_SQL_CHECKPOINT.md`
- `orchestration/architecture/RSE_CONSUMER_SUPABASE_ADVANCED_GATES_CHECKPOINT.md`
- `orchestration/architecture/RSE_CONSUMER_EPHEMERAL_CANDIDATE_CHECKPOINT.md`

Current verification state:
- the synthetic PostgreSQL 16 base RLS harness is green;
- the advanced Gate A-H harness is green on CI run `35541200417` at head `9baf778da210b4c354dcb10e19d452f9524df8e6`;
- the candidate migration contract and deterministic schema/policy drift gate are complete; hardened drift-guard CI run `35655936834` is green, with candidate branch checkpoint head `40dcb3f12c8f8b80a54924b48e8c9e17c53ccf64`;
- in the advanced model, browser/mobile authenticated roles cannot directly mutate protected progress/sync state;
- the atomic sync primitive is `SECURITY INVOKER`, executable only by a synthetic trusted-server role and accepts no client premium/entitlement claim;
- this remains synthetic/local/CI architecture only: no live Supabase project has been created or modified and no production deployment is authorized;
- no further Consumer Platform repository-side slice is selected. Wait for an owner-approved real product source and/or deployment decision rather than manufacturing architecture work.

Security-domain boundaries:
- Happy Me remains separate by default because family/child-sensitive profiles, child-device least privilege, consent/safeguarding/media/deletion concerns increase blast-radius and authorization risk;
- Senior retains its current Firebase-oriented architecture unless explicitly redesigned;
- Mind Bloom is private owner-only and outside the commercial consumer platform;
- Opinie real data, Smart CV and Domowe Finanse remain outside the consumer cloud boundary.

Happy Me separation is a risk-control architecture decision, not a claim that shared infrastructure is technically impossible. Consolidation would require an explicit privacy/security review proving equivalent isolation.

## 8. Marketing Automation

Target model:

`RSE Marketing Orchestrator -> specialist content/creative agents -> Brand Gate -> publisher -> performance memory`

and in parallel:

`RSE Paid Growth Controller -> tracking -> paid specialists -> KDP Ads Optimizer -> audit -> budget decisions`

Execution boundary:
- Marketing Autopilot remains in a dedicated Marketing execution chat;
- the Central Orchestrator synchronizes milestones, blockers and shared dependencies only;
- chat history is NOT the marketing system of record;
- the durable Marketing execution layer is established in GitHub, so a fresh dedicated Marketing chat must reconstruct from durable files rather than from the dead/old chat.

Existing specialist capabilities identified:
- Content Creator
- Trend Researcher
- Social Media Strategist
- Instagram Curator
- TikTok Strategist
- Video Optimization Specialist
- Short-Video Editing Coach
- Visual Storyteller
- Image Prompt Engineer
- Brand Guardian
- Carousel Growth Engine
- Paid Social Strategist
- PPC Campaign Strategist
- Ad Creative Strategist
- Paid Media Auditor
- Search Query Analyst
- Tracking & Measurement Specialist

RSE-specific layers:
- RSE Marketing Orchestrator
- RSE Paid Growth Controller
- RSE KDP Ads Optimizer

Durable Marketing sources:
- `marketing/MARKETING_RESUME_FROM_ZERO.md`
- `marketing/RSE_MARKETING_AUTOPILOT.md`
- `orchestration/marketing/RSE_MARKETING_AUTOPILOT_CHECKPOINT.md`
- `marketing/DETECTIVE_ACADEMY_Q4_LAUNCH_PLAN.md`
- `marketing/DETECTIVE_ACADEMY_CONTENT_BANK.md`
- `marketing/DETECTIVE_PRELAUNCH_14D_CALENDAR.md`
- `marketing/DETECTIVE_ACADEMY_COVER_A_PLUS_VISUAL_LOCK.md`
- `marketing/DETECTIVE_ACADEMY_KDP_RELEASE_PACKAGE.md`
- `marketing/PERFORMANCE_MEMORY.yml`
- private operational marketing brain in `riseshineevolve-source/riseshineevolve/marketing/`.

Marketing system of record should include:
- brand/voice,
- product registry,
- content source,
- asset library pointers,
- creative rules,
- platform rules,
- performance memory,
- paid economics,
- guardrails.

Operational content strategy:
create a few strong master pieces and adapt them for IG/TikTok/FB/YT rather than generating unrelated platform content.

Paid-media rule:
children may be product users, but paid targeting is to parents/adults and must respect platform child-safety/ad rules.

Historical working budget proposal exists in recovered chat material, but future spend must be revalidated against current economics before activation.

Connector status from recovered history is NOT assumed permanently. Metricool / Creative Claw / Windsor state must be live-verified before use.

## 9. Polish Localization Engine

Goal:
**English original -> Polish native edition**

Not literal translation.

Pipeline:
`INGEST -> UNDERSTAND -> DRAFT -> TRANSCREATE -> LOCALIZE -> VERIFY -> HUMANIZE -> EDIT -> PROOF -> BACKCHECK -> EXPORT`

Core roles:
- RSE Localization Orchestrator
- Semantic Translator PL
- Polish Transcreator
- Polish Cultural Localizer
- Meaning & Fact Guardian
- Natural Polish / Anti-AI Editor
- Polish Logic & Flow Editor
- Polish Proofreader & Final Editor
- Bilingual Localization QA

Conditional specialists:
Brand Guardian, Whimsy Injector, Narratologist, Book Co-Author, SEO, Legal.

Current golden corpus:
published 244-page Happy Makers paperback.

Current accepted evidence:
- Round 2 PASS
- Round 3 PASS after direct bilingual/surface review
- full Day 11 pilot PASS
- bounded Days 05/20/25 PASS
- automated regression validator added
- full-book segmented scale-out still owner-gated

Core rule:
fidelity of intent > fidelity of syntax, but meaning/claims are locked.

## 10. Product portfolio

Wave 1:
- RSE Core / Website / AI Discovery
- Polish Localization Engine
- Happy Makers Detective Academy
- Happy Me Adventures
- Optical Animals
- Senior / Hello Today
- Mind Bloom Assistant
- Opinie

Wave 2 / HOLD:
- happy-makers-quest
- family-mission-control
- unstoppable-me
- night-command
- family-hearth-stories
- spark-joy-fam
- neon-wonder-world (unclassified)
- small gifts/tools: word-search-puzzle, Happy-Makers-Calm-Wheel, 1-minute-challange

Support repos to preserve:
- monochrome-map-master
- robot-voice-maker

Outside current business build queue:
- Kuratoryjny MKJA
- CV Tailor
- Job Search tooling
- Family Finance

## 10A. Detective Academy KDP packaging

Canonical operational KDP package:
- marketing/DETECTIVE_ACADEMY_KDP_RELEASE_PACKAGE.md
- marketing/DETECTIVE_ACADEMY_COVER_A_PLUS_VISUAL_LOCK.md

Current owner-accepted working decisions include:
- 8.5 x 11 paperback;
- black ink + white paper;
- no-bleed interior;
- glossy cover working preference;
- title: Happy Makers Detective Academy;
- subtitle: The Mystery of Room Zero;
- Book 1 series treatment;
- child-facing front/back-cover direction;
- parent-facing Amazon description;
- seven working keyword phrases;
- category targets;
- working US launch price $13.99, not yet frozen;
- honest AI-generated text/images disclosure at upload;
- front-cover selection is CLOSED by owner on 2026-09-25. Final source: `OSTATECZNA OKLADKA ROOM ZERO.png`, SHA-256 `2570df512f3883663aca1c4e5359ba12aa0489276f484b86ac5623ab037429a9`. Treat as immutable/do-not-touch. Back-cover child-facing copy/continuity rules and A+ brief remain locked and must inherit this exact front;
- current V4.1 source contract is 146 pages, but exact final KDP page count must be reconfirmed after the four owner interior visuals are integrated;
- final back/full-wrap proof, physical proof, price, ISBN choice, English freeze and publication remain owner gates.

### Detective modern-props pilot status — 2026-09-24
Latest candidate-v3 preview checkpoint (2026-09-24 evening):
- Codex local HEAD reported: `b7869a1` on `codex/modern-props-pilot`.
- Candidate V3 improved materially: **15 CLEAR / 7 BORDERLINE / 1 REMAKE** across the 23 prop families.
- Only hard remake blocker remains `exam_bench`, which still reads as chair + writing desk instead of medical examination furniture.
- Clue-critical `collaborative_desk` PASS; `mentor_workstation` PASS; prior remake fixes for backpack cubbies, dino statue, operations seating and stool now PASS.
- Borderline owner-review/cleanup set: feeding_trough, field_equipment_case, giant_fern, hydration_station, maker_bench, mentor_workstation, ranger_desk.
- Structural fingerprints PASS for HMDA_02 / HMDA_13 / HMDA_29 with zero locked-field differences; Room Zero meta PASS; CHECK THE OLD MAP PASS.
- Do not touch the 15 CLEAR assets unless owner explicitly requests. Next safe slice: correct `exam_bench`, then run focused HMDA_13 + seven-borderline visual gate before any owner_approved flags or all-15 scaleout.


- Runtime-native redraw architecture is technically accepted for HMDA_02 / HMDA_13 / HMDA_29; rejected V4 prop art must NOT scale to all 15.
- Codex external-prop integration contract is implemented locally with fail-closed hash + owner-approval validation.
- Latest handoff checkpoint reported by Codex: local handoff builder commit `7b1d27d`; external-art-handoff-v1 ZIP SHA-256 `771584ed7425c1b66a9c902baa4b36d763a13ddd3432180caf2ce05769299347`.
- Handoff contains 23 exact stable asset IDs, per-family art specs, transparent canvases, footprint templates, source-context crops, review template and pending manifest.
- No final external prop art exists yet and no prop asset is owner-approved.
- Next safe step is external art creation OUTSIDE Codex from the handoff package, then owner review, exact SHA registration and only then a three-pilot integration render/QA.
- Codex must not invent the final prop visual language and must not scale rejected V4 art to all 15 maps.



Modern-props candidate v3 checkpoint — 2026-09-24:
- 6 REMAKE assets were replaced externally: backpack_cubbies, collaborative_desk, dino_statue, exam_bench, operations_seating, stool.
- 11 BORDERLINE assets received an external cleanup pass: archive_seating, commons_seating, feeding_trough, field_equipment_case, field_guide_kiosk, giant_fern, hydration_station, maker_bench, mentor_workstation, ranger_desk, viewing_bench.
- Combined package: `HMDA_23_props_candidate_v3.zip` with 23/23 exact filenames and updated hashes.
- Local preflight: all 23 technically fit renderer bounds; 8 aspect-envelope REVIEW flags remain (commons_seating, feeding_trough, giant_fern, globe, hydration_station, medical_supply_case, operations_seating, piano). These are not automatic fails and require real three-map print-context review.
- Next gate: rerun exactly HMDA_02 / HMDA_13 / HMDA_29 using candidate v3, compare SOURCE -> V4 -> candidate v3, classify CLEAR/BORDERLINE/REMAKE, preserve all locked structure and do not promote or scale out before owner approval.

## 11. Detective Academy

Current product source:
- 20 native Shigai candidates recovered,
- exactly 15 selected production spatial modules locked,
- 5 remain challengers/backups,
- Book Factory is current production path,
- original Shigai geometry/logic remains authoritative.

Latest recovered creative direction:
one spatial case unit becomes:
**WITNESS BOARD -> LIVE CASE MAP -> ROOM ZERO SIGNAL**

Do not squeeze story + all clues + map into one page.

Map-system owner gate: **CLOSED — owner approved B / APPROVE WITH SMALL FIXES.**

Locked presentation direction:
- white/light map background,
- larger + bold room/zone labels,
- larger + bold row/column coordinates,
- readable legends/person descriptions at print size,
- generous pencil space,
- premium full-page Witness Board with stronger hierarchy and larger/bold names,
- naming direction B: branded / academy / adventure,
- aliases are presentation-only and may never alter puzzle identity, clues, topology, answers or solution logic.

Current V4.1 state:
- PR #571 head `1fed50b7e969c60da1a1b9d743665473ceb15049` is Draft/Open/Mergeable;
- Build Detective Academy PDF #174 PASS and SEO Validation #713 PASS on the current head;
- deterministic finalizer, reverse-entry engine, print-typography QA, grayscale audit, fail-closed final-artifact audit and locked-V4 spatial recovery bridge are present in source;
- the earlier canonical-input materialization blocker is closed; verified Shigai geometry still must never be reconstructed, approximated or reinterpreted;
- asset-independent V4.1 source polish is exhausted; do not manufacture additional refactors or repeated audits while the owner visual gate is open;
- the current physical source contract is 146 pages;
- English is **NOT FROZEN**.

The historical ALL-15 map-system design gate remains closed. The current bounded owner-visual gate expects exactly four final owner files:
- `case03_photo_A.png`,
- `case03_photo_B.png`,
- `case03_solution.png`,
- `book2_archive_photo.png`.

Those files may not inherit the historical map-system approval. Exploratory visual candidates must not be silently selected, committed or promoted, and owner-supplied final files must not be regenerated, restyled, destructively cropped or silently substituted. Once all four exact files are supplied, the final pass must SHA-lock them, extend validation to all four, integrate the exact Case 03 solution asset, fail closed on mismatch, complete the exact final render/audit, independent full-PDF review/back-entry simulation and representative physical proof.

Separate packaging state:
- front cover is **FINAL / OWNER LOCKED** as of 2026-09-25: `OSTATECZNA OKLADKA ROOM ZERO.png`, SHA-256 `2570df512f3883663aca1c4e5359ba12aa0489276f484b86ac5623ab037429a9`; do not regenerate or substitute it;
- the current question-mark/scanner Academy logo direction remains locked;
- back-cover copy/hierarchy/visual rules and the five-module A+ brief are locked for execution, but final wrap/A+ continuity must inherit the ultimately selected front;
- final back/full-wrap output and generated A+ assets remain owner-review gated and do not freeze the English interior.

Current owner actions are independent: **select the winning front-cover file when ready** and **provide the four final interior visual files when ready**. Final interior visual/proof approval, final back/full-wrap proof, explicit English source freeze, pricing and KDP publication remain owner-controlled.

English release candidate first, strict preflight, then Polish only after explicit English freeze.

## 12. Happy Me Adventures

Do not rebuild from scratch.

Canonical active branch is the long-lived mobile-first rebuild with 200+ commits and release-hardening evidence.

Source-only gates have been heavily exercised; remaining work depends on external Supabase/Play signing/device/internal-track verification.

Commercial model, pricing, major redesign and store publication remain owner gates.

## 13. Optical Animals

Project mode:
**CURATION -> FINAL 20 LOCK -> AUTOMATED BOOK CREATION**

Current source-manager truth:
- FINAL20 manifest + local final source folders are authoritative for art selection.
- 12 protected approved visuals remain recorded in the owner-gated production contract; owner separately reports 19/20 illustration creation progress, which is not equivalent to FINAL20 promotion.
- approved art must not be "improved for consistency" automatically.
- old Book Creator roster containing duck/red panda/chameleon/old slot is superseded.
- final PDF must use only the canonical final-source folder after owner promotion.
- PR #14 is Draft/Open/Mergeable at head `f2781667331ccc7782968c128abd1d691fe29aa3`.
- the branch hardens exact-identity proofing by binding seek/find proofs to the renderer implementation SHA and failing closed on stale renderer provenance while preserving the existing `rse.optical-animals.exact-placement-proof.v1` schema for compatibility.
- Optical Book Creator quality #90 **PASS** on the current head; the earlier #88 repository-side unittest failure at head `4c759ba...` was closed by the one-line schema-compatibility repair. Current PR evidence reports 87/87 deterministic/synthetic tests PASS.
- exact seek/find targets must be source-derived from owner-approved hero art; invented/redrawn/reposed lookalikes are rejected by contract.
- Butterfly Finale layout is a separate owner gate between A: one 8.5x11 hero page and B: a true two-page gutter-safe spread. No automatic selection, FINAL20 promotion, manifest change or final spread split is allowed before the owner reviews the actual approved-art comparison packet.
- all art-selection, FINAL20, production-resolution, source-linked token, physical-proof and publication gates remain unchanged; green CI does not cross them.

## 14. Senior / Hello Today

Current execution owner: **dedicated Senior / Mind Bloom delegated worker** under `orchestration/handoffs/SENIOR_MIND_BLOOM_DELEGATED_EXECUTION_HANDOFF.md`.

Central RSE may read/checkpoint project state for portfolio coordination but must not write `riseshineevolve-source/hello-today-android.` while the delegated worker is active.

Current recovered milestone:
Phase 14H paired CHILD_DEVICE and 6+ UX boundary on PR #77 remains the verified release-hardening baseline.

Hard locks:
- no parent credentials on child device,
- no independent child email/password account,
- restricted server-bound child session,
- private Family Circle only,
- revoke supported,
- Child Mode remains production disabled until external/legal/human gates pass.

Current repository-side product/content state:
- PR #77 head `2851552a995b8f870e72c863c0471e81091dee7f` remains Draft/Open/Mergeable;
- prior verified release-hardening evidence remains Android CI #144 PASS, Device Accessibility #81 PASS, Firebase Security #86 PASS;
- repository-side product/content completion remains ACTIVE until the delegated worker explicitly verifies full content/product completeness; do not describe Senior as source-exhausted merely because Phase 14H hardening is green;
- final product target is bilingual EN + PL, with English as canonical stable-content master and the existing Polish Month 01 corpus preserved for later reconciliation/transcreation;
- current Month 01 work has a Days 1-30 English editorial draft plus shared locale-aware runtime factory/parity guards, but remains DRAFT; typed Play / Delight / Then-Now presentation copy is still Polish-specific and current-head Android CI is still required;
- production `strict`, production Child Mode, Play/Firebase/Integrity, legal/Families/Data Safety and real-device/human gates remain external/owner-gated.

## 15. Mind Bloom

Current execution owner for the active bounded lane: **dedicated Senior / Mind Bloom delegated worker**. Central RSE is read-only for `riseshineevolve-source/mind-bloom-assistant` while that worker is active.

Current branch:
`feature/personal-chief-of-staff-foundation`

Current PR:
`#2` (Draft/Open/Mergeable; keep Draft until an explicit future merge/release decision)

Current live head:
`b098b57ba78ff156726ff47c3e077b167981086c`

Current product state:
**PRIVATE V1 SOURCE RELEASE CANDIDATE PASS / ORDINARY FEATURE DEVELOPMENT FROZEN / PRIVATE SINGLE-OWNER DEPLOYMENT + PRIVACY COMPLETION ACTIVE.**

Latest verified live CI:
- Mind Bloom CI **#88: SUCCESS**
- current-head code regression: none established

Owner decision 2026-09-25 reopened only the bounded private deployment/privacy-completion lane. The delegated worker has closed the repository-side shell mismatch and preview-URL exposure; the active private owner shell no longer requires the absent legacy commercial tables merely to render/use the canonical Private V1 operational surfaces, and `preview_urls: false` is set as defense in depth.

Still NOT complete and not to be crossed centrally:
- create exactly one owner account, then disable arbitrary Supabase signup;
- configure and verify whole-app Cloudflare Access / equivalent perimeter;
- constrain auth redirects/origins;
- prove unauthorized browser/account denial and live owner-scoped RLS behavior using zero/synthetic data before private owner data is introduced.

Provider accounts, OAuth, tokens and sync jobs remain intentionally absent. Phase 2B provider implementation remains owner-gated and inactive.

Private-data boundary:
- no owner private data in GitHub, fixtures, logs, screenshots, checkpoints or prompts;
- no weakening RLS;
- no service-role/secret keys in browser or GitHub;
- no public/commercial or multi-user expansion through this bounded lane.

Recovery safety:
before any pull/reset/rebase/checkout, inspect local `git status` + `git diff` and preserve legitimate uncommitted work.

## 16. Opinie

Privacy model evolved and must be stated precisely:

Allowed in remote GitHub:
- source code,
- schemas,
- synthetic fixtures,
- deterministic calculation engine,
- provenance model,
- offline packaging/tests/docs.

Forbidden remotely:
- real case files,
- personal data,
- police/court/insurance evidence,
- real archive opinions,
- embeddings/indexes derived from real files,
- real generated analyses/opinions.

Production runtime is local/offline.

Current branch state is tracked in `PROGRAM_REGISTRY.yml` and `CONFLICT_LOG.md`; any merge-conflict repair must remain synthetic/code-only and must never move real case data remotely.

Target pipeline:
`new case -> evidence/provenance -> timeline/scene -> calculations -> reconstruction variants -> review queue -> opinion base`

Final expert conclusion always requires human review.

## 17. Content-source architecture

GitHub stores the "brain" of books/products:
- manifests,
- checksums,
- structured text when rights/privacy allow,
- glossary,
- character bible,
- edition metadata,
- localization state,
- app-reuse mapping,
- provenance.

Heavy binaries:
PDF/EPUB/KPF/covers/ZIPs remain in private Library/Drive/local archive unless deliberately placed in private Git LFS.

Recovered book-source work includes:
- Happy Me published 244-page master and ebook package,
- World 01,
- World 02,
- derivatives and reusable engines,
- content recovery queue.

`24 Gentle Steps to Christmas` is now recovered as a verified 104-page English paperback source (`24 Gentle Paperback ok.pdf`) with a hardcover cover reference in the connected Library. The earlier missing-master state is SUPERSEDED. A canonical content-source manifest now lives at `orchestration/content-sources/24-gentle-steps-to-christmas.yml`.

## 18. Continuity invariant

No RSE project may depend on "remembering which chat had the answer."

A session is healthy only if another fresh session can recover:
- current truth,
- key decisions,
- current branch/PR/issue,
- blockers,
- owner gates,
- source provenance,
- next safe action,

from GitHub + explicitly referenced private sources.

## Detective Academy owner sync — 2026-09-26

Canonical interior design and non-regression contract: `orchestration/detective/DETECTIVE_ACADEMY_INTERIOR_DESIGN_SYSTEM.md`.

Current rule: Detective EN remains NOT FROZEN. The 146-page logic/map/Case03/reverse-entry gates are green, but owner visual review reopened the interior design gate for recurring structure, Happy Makers Chat restoration, Witness Board modernization, Evidence Grid identity, sixth-slot reveal timing, stale-name cleanup, and a fresh 146-page human visual audit before physical proof.


## Polish Engine reconciliation PASS — 2026-09-26

Current-main reconciliation is technically PASS on local branch `codex/polish-engine-main-reconcile`, local HEAD `147f160c1e5b5df8cd930d817bf42a64cc85af82`.

Durable checkpoint:
`orchestration/brain/checkpoints/2026-09-26-polish-engine-main-reconciliation-pass.md`

All deterministic localization tests are green; 34 fit/provisional-terminology review items remain non-deterministic review work.

Next safe action:
push branch -> draft PR/current-head CI -> Central diff review.

Full Detective PL remains blocked until explicit EN freeze.


## Gentle Steps Days 08–14 language candidate — 2026-09-26

Bounded Polish candidate completed from published English paperback pages 43–63:
- Days 08–14
- 21 activities
- local Codex commit `4fa7700a75c6444ee9e104bf6adf2692d11d8899`
- source fidelity PASS
- natural Polish PASS
- Happy Makers character voice PASS
- claim/safety PASS
- no shared terminology/engine change requested

Durable checkpoint:
`orchestration/brain/checkpoints/2026-09-26-gentle-steps-days08-14-pass.md`

Important: at Central verification time the remote branch is still at `630e39a603177d4b923e74944a7ae4d03863d1ea`; the local Days 08–14 commit must be pushed before the branch state is durable remotely.

Real-template fit remains OPEN for Week 1 and Week 2. Next safe bounded language slice: Days 15–21 after exact source-page-boundary confirmation.

## Polish Engine PR #13 — Central review state 2026-09-26

PR #13 `Reconcile Polish Localization Engine with current main`:
- Draft / Open / Mergeable
- head `147f160c1e5b5df8cd930d817bf42a64cc85af82`
- 56 changed files in the expected localization/engine/role/runbook/workflow scope
- 8/8 current-head GitHub Actions PASS
- no failing jobs
- zero deterministic localization errors
- 34 fit/provisional-terminology review items remain non-publication review work

Central review finds the reconciliation scope consistent with the intended current-main engine recovery. Do not start full Detective PL before explicit EN freeze. Do not merge without the applicable owner/central merge decision.


## Detective final visual-system PASS — 2026-09-26

Owner supplied the completed Codex report from the existing local `codex/modern-props-pilot` worktree.

Local final-interior commit:
`6579ac896c477461fe1c384993315d7455b3f7c5`

Important durability note:
- the commit is local only;
- nothing was pushed or merged;
- treat the exact local artifact/commit as current owner-reviewed working truth until it is safely pushed to a remote branch.

Reported final-interior state:
- recurring case structure 30/30 PASS;
- Happy Makers Chat 37/37 PASS;
- answer/verdict surfaces 30/30 PASS;
- Witness Boards PASS;
- Evidence Grid + scanner-question-mark system PASS;
- page 001 mystery-slot timing PASS;
- stale reader-facing placeholder names eliminated;
- ISBN + AI disclosure PASS;
- Case 03 exact-ten / owner art PASS;
- 30 approved map embeds pixel-identical;
- 15/15 structure + 15/15 unique solutions + all-30 logic PASS;
- Room Zero + CHECK THE OLD MAP PASS;
- 146 pages / Letter / grayscale / embedded fonts / reverse-entry PASS;
- 146/146 human visual audit PASS.

Final reported PDF SHA-256:
`cb1038dcc9086501b86527227550584da7f38fc051bc70442803f82ebddeab7f`

Owner-review ZIP SHA-256:
`07e7a1abf724a401f98a10954d4285ffcb8a6ceb53437ede4b71dcd5be7222f1`

Canonical checkpoint:
`orchestration/brain/checkpoints/2026-09-26-detective-final-visual-system-pass-physical-proof-next.md`

Decision:
**INTERIOR VISUAL-SYSTEM PASS LOCALLY / PHYSICAL PROOF NEXT.**

English remains NOT FROZEN.

Do not reopen the interior broadly. Only fix a concrete KDP-preflight or physical-proof defect.

Remaining Detective EN work:
safe remote persistence -> final full-wrap cover -> KDP previewer/preflight -> representative physical proof -> explicit owner EN freeze -> Detective PL.


## Gentle Steps Days 15–21 PASS — 2026-09-27

Bounded Polish language candidate completed from the published paperback:
- Days 15–21
- PDF pages 65–85
- 21 activities
- source fidelity / completeness / natural Polish / character voice / claim language PASS

Remote branch remains at `4fa7700a75c6444ee9e104bf6adf2692d11d8899`; latest Days 15–21 commit `ef09623a9956ef9a4c197275d4353c7b52b0abd0` is local-only until pushed.

Open gates:
- real-template fit for Weeks 1–3
- Day 18 eyes-closed walking safety decision
- source-rule ambiguities on Days 16, 18 and 21

Checkpoint:
`orchestration/brain/checkpoints/2026-09-27-gentle-steps-days15-21-pass.md`

Next bounded language slice:
Days 22–24 after exact source-page-boundary confirmation.

## World 01 real pilot PASS — 2026-09-27

Branch `codex/interactive-book-world01-pilot` remote HEAD:
`7795e6933c39f4f126666ad712c690ccd418f048`

First source-backed real content-pack pilot is green:
- mission openers 1–3
- 3/10 openers = 30%
- 3/108 pages direct evidence
- 24 fail-closed tests PASS
- Interactive Book Contract CI PASS
- published source remains canonical over divergent app copy

Checkpoint:
`orchestration/brain/checkpoints/2026-09-27-world01-real-pilot-pass.md`

Next safe slice:
audit World 01 Level 1 pages 16–22 and expand only source-supported coverage.


## Detective text-only Gold Master V1 — 2026-09-27

Canonical working text master:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V1.md`

Checkpoint:
`orchestration/brain/checkpoints/2026-09-27-detective-text-gold-master-v1.md`

Commit creating the full master:
`7ddd722f7d5aba29de214cb633c627afbcb652b1`

Scope covers front matter through Book 2 hook plus all three Hint Vault levels and full Solution Files.

Narrative rule:
each case must read as a small believable story inside the larger Room Zero investigation, not as a worksheet prompt.

Current recurring text structure:
CASE FILE / WHAT HAPPENED -> YOUR OBJECTIVE -> INVESTIGATION RULES -> HAPPY MAKERS CHAT -> EVIDENCE -> mechanic-specific response -> CASE CLOSED -> KEEP THIS / SIGNAL LOG.

Spatial named anchors are not missing people or automatic suspects; their room companion is the next useful person to ask, not somebody to blame.

Generic answer lines are prohibited where the mechanic requires marking, sorting, ordering, coding or direct annotation.

Detective layout/Codex integration is PAUSED until owner accepts the Gold Master text direction. The next layout pass must consume fixed text and may not independently shorten/rewrite it to fit a historic page count.


## Detective Text Gold Master V2 — 2026-09-27

Active owner-review text master:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V2.md`

Red-team audit:
`orchestration/detective/DETECTIVE_ACADEMY_TEXT_RED_TEAM_AUDIT_V2.md`

V2 master commit:
`20f8cbeb599ff146fcab02c66cacf3597faa0e55`

V2 SHA-256:
`8a1e02a880f8c3507f8e2007838f96e6d1d44fa7c066ff80d6977948288d3de3`

V1 is retained as archive/reference and is no longer the active working text layer.

Key V2 decisions:
- ordinary files use CASE RESULT, not CASE CLOSED, because many contact cases establish the next interview rather than fully resolving the real-world incident;
- Case 03 INTAKE-03 is a neutral routed comparison record and does not invent a fifth printed 0 on owner art;
- first Act recap uses five routed files / four matching marks;
- Case 26 display title becomes THE CASE OF THE EMPTY ROOMS;
- Case 07 pre-puzzle chat no longer leaks the missing-costume situation;
- all 30 intros were rewritten for story continuity, child clarity and tension;
- all 30 case-result and Keep/Signal beats were red-teamed;
- objective/evidence/puzzle truth remains unchanged;
- layout integration remains PAUSED until owner accepts the V2 text direction.

Do not let later renderer work silently revert V2 copy to V1/current PDF wording.


## Detective Text Gold Master V3 — 2026-09-27

**This section supersedes V2 as the active text-review source.**

Active final-text candidate:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Checkpoint:
`orchestration/brain/checkpoints/2026-09-27-detective-text-gold-master-v3.md`

Master commit:
`01eb2cf1e0f9b868c12f06e1e5390c2632b71123`

V1/V2 remain history/reference.

V3 locks the first ten reader pages as one progressive recruitment sequence:
unexplained `?` -> concise Happy Makers introduction -> black envelope -> blank Recruit Credential -> mistake/coincidence/invitation -> WILL YOU CLAIM IT -> child completes real credential -> concise 30-connected-case/Room Zero promise -> case rhythm -> map/contact rules -> Hint Vault/Case Wall -> Case Index.

V3 also contains the binding non-reader-facing case blueprint and a 30/30 schema compliance matrix.

Detective renderer/Codex integration remains PAUSED until owner explicitly accepts V3 text direction.


## Detective V3 integrity audit — 2026-09-27

V3 was directly audited against V1, V2 and the V2 red-team corrections.

Result:
- substantive V1/V2 fixes preserved;
- two assembly-format regressions fixed in place;
- repeated Act-opening copy consolidated;
- no new V4/V3.1 created.

Audit:
`orchestration/detective/DETECTIVE_ACADEMY_TEXT_V3_INTEGRITY_AUDIT.md`

Current audited Markdown SHA:
`31356a78ee865c7c78068b1451f4c89191fff6e71ac03489a3d030f5a2f2973b`

Current audited editorial PDF SHA:
`8fef53692ad474139d517dae03012f23d4262b302d2756a813003744bc03b166`

Codex layout remains paused pending owner text acceptance.


## Detective V3 owner refinement pass — 2026-09-27

Active text master remains:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Latest canonical content commit after the owner opening/transition/finale pass:
`5fc40a06f9993091875e902f05ce754aac2e2e3f`

Do not create another text version number for minor/editorial fixes.

Current V3 now includes:
- black-envelope cold open before Academy/team explanation;
- real Case Wall location;
- upside-down Hint Vault / Solution Files explanation;
- one `MY DETECTIVE EDGE` credential field;
- Case 01 QUILL/MORSE/PIP/KNOX witness set with answer name visible;
- 17/17 named-answer evidence-visibility audit PASS;
- strengthened purpose sentences in contact-case intros;
- narrative Room Zero finale;
- witness-name library;
- 30/30 narrative-bridge audit.

Layout/Codex remains paused until owner approves the text.


## Room Zero reveal refinement — 2026-09-27

Active V3 master remains:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Latest canonical content commit:
`95621752447c793e8485440a787f406f390b4582`

Owner-approved direction:
two-sentence Room Zero summary first, then Alio asks for a translation and the full Happy Makers family explains the complete causal chain in chat form. No causal detail was dropped.

Layout/Codex remains paused until owner accepts the text.


## Detective V3 evening persistence — 2026-09-27

The full owner-review text master is durably stored at:

`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Latest content commit:
`a735f9e5d09aee1ea0a39b400eb956d7d8d7b22e`

This remains **V3**; do not create another numbered text version for minor/editorial corrections.

Latest owner-approved direction includes the final Room Zero explanation structure:
two-sentence overview -> Alio needs translation -> full Happy Makers causal explanation -> `The Academy could open the door. Only you could earn the badge.`

Current Detective state:
**TEXT OWNER REVIEW OPEN / LAYOUT PAUSED.**
No overnight Detective redesign or renderer work unless new owner feedback arrives.


## Unstoppable Me revival — 2026-09-27

Owner reactivated **Project Unstoppable / Unstoppable Me** as an active parallel product lane because of its strong overlap with the teen coping-skills / self-regulation opportunity.

Canonical code:
`riseshineevolve-source/unstoppable-me`

Base main at revival:
`df1014c7318d6b14a97ef183790c8b3c7b3ad0c2`

Active revival branch:
`codex/unstoppable-me-revival`

Revival setup head:
`651f28ceb09070354394a36deac97df98441ecc1`

Central checkpoint:
`orchestration/brain/checkpoints/2026-09-27-unstoppable-me-revival.md`

Source custody:
- Library: `/AI AGENTS/UNSTOPPABLE/Project_Unstoppable_6x10_Fixed.pdf`
- Library: `/AI AGENTS/UNSTOPPABLE/Project_Unstoppable_extracted_text.docx`

The separate `Unstoppable-Me-Edit` repository is empty and is not canonical.

The project is a dual product:
- 191-page / 31-day KDP workbook;
- interactive 31-day app using the same core content universe.

Strategic direction:
modern teen coping/self-regulation + life-skills adventure, not therapy.

Immediate gates:
baseline CI -> KDP/app parity -> editorial/claims safety -> product-truth cleanup -> Play/privacy/minors release readiness.

Central already removed tracked `.env` from the revival branch, added env ignore protection + `.env.example`, CI workflow and `CODEX_START_HERE.md`. Do not expose historical environment values. If any privileged historical secret exists, rotate it rather than printing it.

No merge, KDP publication, Play publication or production Supabase change without owner gate.


## Detective V3 narrative cleanup — 2026-09-28

Active text master remains:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Latest canonical text commit:
`76519a78cabf2a45dde07b8747b2339b0b97644c`

Checkpoint:
`orchestration/brain/checkpoints/2026-09-28-detective-v3-narrative-cleanup.md`

Owner-driven cleanup now locked:
- recruit credential has no field position; one `MY BEST DETECTIVE SKILL` field;
- no immediate reader-facing CASE RESULT/answer duplication after cases;
- answers/reasoning only in upside-down Hint Vault/Solution Files;
- Case Wall is page 9 and stores only explicitly requested reusable meta evidence, never every verdict;
- Case 03 instruction de-duplicated;
- Case 05 restored to six-symbol code `BALL -> STAR -> BOLT -> HEART -> KEY -> MOON`;
- Case 01 stale hint aliases removed;
- Academy story world now explicitly spans specialist wings, staff requests, field exercises, nearby partner sites, direct witnessed incidents and occasional intake-system routing across multiple days/weeks;
- Case 04 upgraded from cupcake mix-up to `THE EVIDENCE BOX IN THE WRONG TENT` while preserving the exact same locked spatial puzzle;
- main-case intros remain narrative prose, not worksheet fragments;
- solution files use one short `WHY IT MATTERS` consequence rather than duplicating the solved answer.

Do not revert any of these changes in later renderer/Codex work.

Detective layout integration remains PAUSED pending owner text approval.


## Detective V3 final 1000% text audit — 2026-09-28

Active text master remains the SAME V3:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Latest full-content commit:
`3e534a2a5fe95dc183a0825071ae064175803a0b`

Final audit report:
`orchestration/detective/DETECTIVE_ACADEMY_V3_FINAL_TEXT_AUDIT_2026-09-28.md`

Key locked decisions after the audit:
- no reader-facing immediate CASE RESULT / WHAT THIS PROVES after cases;
- answers/reasoning live only in the upside-down back section;
- Case 05 remains the unique six-symbol code BALL -> STAR -> BOLT -> HEART -> KEY -> MOON;
- Case Wall is page 9 and is used only for explicit meta-evidence;
- finale uses Case Wall for RULE / ROOM / CODE and Recruit Credential for DETECTIVE;
- Bibi's Case 09 recognition occurs once, after the reader solves the comparison;
- old Case 26 fixed page references removed;
- Evidence/Puzzle surfaces hydrate exact locked source/raster truth and must not be rewritten from prose.

Text/layout remains PAUSED until owner accepts this V3 text.
Do not create V4 for minor edits.


## Detective V3 owner-feedback final microfix — 2026-09-28

Active text master remains the SAME V3:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Latest canonical text commit:
`3e534a2a5fe95dc183a0825071ae064175803a0b`

Checkpoint:
`orchestration/brain/checkpoints/2026-09-28-detective-v3-owner-feedback-final-microfix.md`

Owner's final reader-level audit request was applied without changing locked puzzle truth. Key closures include:
- Case 02/Max causal purpose made explicit;
- Case 03 photo-copy logic made physically coherent while preserving exact ten;
- repetitive contact-case intro formula removed;
- Room Zero routing vs solving causality clarified;
- duplicated Case 03 solution list and stale appendix residues removed;
- US English normalized;
- 30/30 cases, all three 30/30 Hint Vault levels and 30/30 Solution Files remain structurally present;
- Case 05 six-symbol solution remains unique;
- current production alias layer contains the named Solution File answer for 15/15 mapped spatial cases.

Important production boundary:
the uploaded 71-page text PDF is an editorial review artifact, not the final KDP interior. Final KDP readiness now requires exact V3 renderer integration + locked evidence hydration + post-hydration name/clue/solution checks + full print render/preflight/visual audit/physical proof. Case 01 reader-facing aliases QUILL/MORSE/PIP/KNOX must replace internal source identities on the rendered evidence surface.

Current Detective state:
**TEXT MICROFIX PASS / PRODUCTION RENDER INTEGRATION NEXT / EN NOT FROZEN.**

Do not restore historical V4/V4.1 reader copy when integrating the renderer. Reflow/add pages before deleting V3 story text.


## Detective V3 final KDP text pass — 2026-09-28

Active canonical text remains the SAME V3:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Latest canonical text commit:
`6c2e21a24d760218923cfd8d47655a3cbf72c575`

Current text blob:
`f6e16e99084562ddf56825ccc7bfdd12baad0656`

Owner-directed final reader audit is complete. This supersedes earlier same-day statements that Detective layout/renderer integration is paused pending text acceptance.

Current state:
**FINAL TEXT MASTER / PRODUCTION INTEGRATION AUTHORIZED / EN NOT FROZEN.**

Final pass corrected the remaining Case 21 -> Case 26 causal attribution, made the 15-total-vs-14-selected spatial-map logic explicit, completed the Case 17 -> Annex -> Case 19 travel bridge, removed the unsupported Case 11 phone-photo tease, made the Case 21 Solution answer complete, clarified Max's direct Cup relationship, and removed stale Detective Six wording.

Next safe Detective action:
integrate the exact V3 blob into the production book factory, hydrate exact locked evidence surfaces, rerun all answer/name/clue/coordinate regressions, render the complete final interior using actual page count, run KDP preflight + full human visual audit, then representative physical proof. Do not cut text merely to preserve the historical 146-page count.

English remains NOT FROZEN. Merge, physical-proof approval, explicit EN freeze and KDP publication remain owner gates.


## Detective V3 story-flow + WOW pass — 2026-09-28

Canonical text remains the SAME V3:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Latest canonical story-flow/WOW text commit:
`3c0caedbcc313658767cb4251b2c1741c4a7edcf`

Canonical text blob:
`8370026a811ad3354aaa8e422ebe2edf58464845`

Checkpoint:
`orchestration/brain/checkpoints/2026-09-28-detective-story-flow-wow-pass.md`

Status:
**FINAL STORY-FLOW + WOW TEXT MASTER / PRODUCTION INTEGRATION AUTHORIZED / EN NOT FROZEN.**

Owner-directed final narrative pass now locks:
- 29/29 Case -> next Case transitions as causally bridged, deliberately parallel or explicitly time-shifted;
- no repeated mission instruction across CASE FILE + OBJECTIVE + HM Chat;
- richer Happy Makers dialogue (humor/teasing/relationships/thinking habits; chats are never secret evidence);
- every explicit Case Wall save has a later on-page payoff;
- Case 03 #1 017/071 delayed archive-routing payoff in Case 06;
- Case 16/21 -> Room Zero reveal that Bibi authored the old torn route note as a trainee;
- Case 25 Archive Restoration parcel -> Case 27 overlay tools;
- Case 24 loud-arrow/quiet-mud lesson -> Rule Zero theme;
- post-Book-1 ARCHIVE FILE 001 triangle symbol must match the existing approved Case 03 #8 changed-triangle pattern WITHOUT modifying owner-controlled Case 03 art.

Locked puzzle truth is unchanged: exact-ten Case 03, six-symbol Case 05, Case 21 message, Case 26 CHECK THE OLD MAP, Rule Zero, D3 and final reader call-sign field.

Next safe action remains production integration/hydration -> full render/regression/KDP preflight -> human visual audit -> physical proof -> explicit EN freeze.


## Detective final pre-Codex text master — 2026-09-28

Canonical text remains the SAME V3:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Latest canonical text commit:
`3c0caedbcc313658767cb4251b2c1741c4a7edcf`

Blob:
`8370026a811ad3354aaa8e422ebe2edf58464845`

Checkpoint:
`orchestration/brain/checkpoints/2026-09-28-detective-final-pre-codex-text-master.md`

Status:
**FINAL PRE-CODEX TEXT MASTER / PREMIUM LAYOUT RESTORE NEXT / EN NOT FROZEN.**

Final owner micro-pass adds the Page 2 cozy-site CTA, ten-question-mark Case 03 progress tracker, stronger Case 06 Uma/dragon-tooth-spoon incident bridge and Case 07 local closure. No puzzle truth changed. Full Case 01->30 transition audit remains 29/29 PASS.

The compact 127-page integration proof is not visual/page-count authority. Next action is to restore the established premium Book Factory system around this exact V3 copy: Evidence Grid signature language, boxed sections and HM chat, dedicated left Witness Board + large right Live Case Map, large bold axes, full Case 03 facing comparison spread, quiet Page 2 scanner-question-mark publication design, and reverse Hint/Solutions. Reflow/add pages before cutting copy.


## Detective owner front-matter source lock — 2026-09-30

Owner review found a renderer-side regression in the 2026-09-29 180-page artifact. The canonical V3 text itself had not reverted.

Root cause:
- renderer hardcoded squad art + `YOUR SQUAD` onto physical Page 3 before rendering the canonical black-envelope text;
- global page begin injected the recurring upper-left micro-grid/ruler;
- COMMS used the evidence grid as a text background.

Canonical source remains the SAME V3:
`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Current owner-front-matter source-lock commit:
`e136e94402c8f870f3d9221b7047c1406cbec813`

Current canonical blob:
`8685f8e561d0bfb3837445b72b4d6f799a9a48f2`

Front-matter physical order is now fail-closed:
1 Title
2 Publication Record
3 The Black Envelope only
4 Your Squad
5 Recruit Credential
6 What You Are About To Walk Into
7 How Every Case Works
8 Map Cases
9 Case Wall + Hint Vault
10 Case Index

New Page 2 owner copy includes the HTTPS site invitation and Facebook line. Page 4 uses a general recruit/team opener rather than the premature Alio helmet joke.

Production factory source now removes the global upper-left micro-grid and renders Happy Makers dialogue on a readable light field with only a narrow decorative evidence-grid strip.

Checkpoint:
`orchestration/brain/checkpoints/2026-09-30-detective-owner-frontmatter-source-lock.md`

State:
**FRONT-MATTER REGRESSION SOURCE-FIXED / PREVIEWER GATE REOPENED / EN NOT FROZEN.**

The prior Sep 29 advance-to-Previewer status is superseded until a fresh exact-source rebuild and full audit pass.

Follow-up 2026-09-30: exact private owner packet `final-book-owner-review(1).zip` was recovered from Library and its SHA-256 `55439b308d6d7a2db7b40485665bcc46aceeb9dffde528afffb276790378680c` exactly matches the owner/spatial contract. Public-repo CI now protects source/order/renderer wiring without committing private visuals. Production branch HEAD `e6a531bc6f26b7cafc4fa73b1af5ee549d1c4283`; Build Detective Academy PDF run `36690461519` PASS. Full private premium rebuild remains required before Previewer.


## Detective full graphic-novel print master candidate — 2026-09-30

Complete local 180-page artifact:
`HMDA_Book1_EN_GRAPHIC_NOVEL_PRINT_MASTER_FINAL_CANDIDATE_2026-09-30.pdf`

Checkpoint:
`orchestration/brain/checkpoints/2026-09-30-detective-graphic-novel-full-build-candidate.md`

QA:
- 180 pages / US Letter / openable / unencrypted;
- body text fidelity: 169 pages checked, 0 below 0.97 threshold;
- Front 5–10 token coverage 1.00;
- required locked content missing 0; forbidden superseded phrases 0;
- Page 3 cold-open and Page 4 squad regression guards pass;
- page rotation metadata remains 0; reverse Hint/Solutions rotates only inner content.

Visual system:
modern clean monochrome detective / graphic-novel framing, readable speech-bubble COMMS, separate full-page Witness Boards and large maps, exact approved spatial rasters for map truth/recognizable props, Case 03 facing comparison, enlarged Case 05 analysis surface.

Important: the semantic map-art handoff itself says many all-15 prop families are still NEW_ART_REQUIRED; no nonexistent final modern-prop pack is to be invented. Current candidate therefore uses the exact approved locked raster maps. A future prop-only art replacement may not change puzzle geometry or text.

State:
**FULL GRAPHIC-NOVEL MASTER CANDIDATE BUILT / TEXT & STRUCTURE QA PASS / OWNER VISUAL REVIEW + KDP PREVIEWER NEXT / EN NOT FROZEN.**
