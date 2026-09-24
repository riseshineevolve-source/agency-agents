# RSE Brain Master

Status: CANONICAL
Rebuilt: 2026-09-18
Last reconciled: 2026-09-24
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
- Senior / Hello Today execution,
- Mind Bloom Assistant execution,
- marketing architecture,
- content-source recovery.

Dedicated execution remains separate for:
- Marketing Autopilot.

Mind Bloom's previous dedicated execution chat is parked/archive-only. The Central Orchestrator is now the single implementation owner for Mind Bloom and must preserve the project's worktree, reviewed-SQL and external-provider gates.

Senior / Hello Today is executed directly by the Central Orchestrator, with its production/legal/Play/human gates preserved.

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

Current measurement state is tracked in the central project registry and issue #584.

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
- `marketing/RSE_MARKETING_AUTOPILOT.md`
- `orchestration/marketing/RSE_MARKETING_AUTOPILOT_CHECKPOINT.md`
- `marketing/DETECTIVE_ACADEMY_Q4_LAUNCH_PLAN.md`
- `marketing/DETECTIVE_ACADEMY_CONTENT_BANK.md`
- `marketing/DETECTIVE_PRELAUNCH_14D_CALENDAR.md`
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
- approved front-cover artwork is now visually locked; back cover is in refinement under the locked child-facing copy/continuity rules; A+ visual brief is locked for Marketing execution.
- final full-wrap proof, page count, physical proof, price, ISBN choice, English freeze and publication remain owner gates.

### Detective modern-props pilot status — 2026-09-24

External-prop integration checkpoint:
- Codex local pilot head reported: `c14b40c` on `codex/modern-props-pilot`.
- External asset contract/schema, hash validator, owner-approved flag gate and pilot-only renderer integration are implemented locally and tests PASS.
- No external assets are approved yet; renderer correctly fails closed and produces no maps until an owner-approved curated pack exists.
- Next owner-safe slice: create the external curated 23-family premium prop atlas outside Codex, approve exact PNGs, then record hashes and run the same three pilot maps. Codex must not invent final prop art.


- Runtime-native redraw architecture is technically accepted for the three pilot maps HMDA_02 / HMDA_13 / HMDA_29.
- V4 local pilot head reported by Codex: `22e703c9e02e02de8f5dc4d139edb53dfbbe5727` on `codex/modern-props-pilot`.
- Structural QA remains PASS; no story, puzzle logic, answer, ROOM/ZONE, Room Zero meta or CHECK THE OLD MAP changes.
- **V4 prop art is NOT owner-approved and is visually rejected as too schematic / floor-plan-like / icon-like.**
- Do not scale V4 to all 15 maps.
- Durable direction: keep Codex as integration/validation engine, but move final prop art creation outside Codex. Produce a curated premium modern-kid-relevant prop atlas externally, then let Codex place exact approved assets against verified runtime geometry and re-run structural/print QA.
- Do not let Codex continue inventing the visual asset language autonomously.

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
- PR #571 head `a5fab13da7e90a9ea99d57d7082fb2f701d67073`;
- Build Detective Academy PDF #148 PASS and SEO Validation #661 PASS;
- deterministic finalizer, reverse-entry engine, print-typography QA, grayscale audit, fail-closed final-artifact audit and locked-V4 spatial recovery bridge are present in source;
- the earlier canonical-input materialization blocker is closed; verified Shigai geometry still must never be reconstructed, approximated or reinterpreted;
- bounded source-side polish remains active: explicit STOP / HINT VAULT boundary if required, parity-interlude diversification, cinematic Book 2 hook presentation, and final human visual QA/back-entry simulation on the exact artifact;
- English is **NOT FROZEN**.

The historical ALL-15 map-system design gate remains closed. The current bounded owner-visual gate expects exactly four final owner files:
- `case03_photo_A.png`,
- `case03_photo_B.png`,
- `case03_solution.png`,
- `book2_archive_photo.png`.

Those files may not inherit the historical map-system approval. Exploratory visual candidates must not be silently selected, committed or promoted, and owner-supplied final files must not be regenerated, restyled, destructively cropped or silently substituted. Once all four exact files are supplied, the final pass must SHA-lock them, extend validation to all four, integrate the exact Case 03 solution asset, fail closed on mismatch, complete the exact final render/audit, independent full-PDF review and representative physical proof.

Current owner action required: **none until the four final visual files are ready**. Final visual/proof approval, explicit English source freeze, final cover/proof, pricing and KDP publication remain owner-controlled.

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
- 12 approved visuals.
- 8 unresolved owner-gated slots.
- approved art must not be "improved for consistency" automatically.
- old Book Creator roster containing duck/red panda/chameleon/old slot is superseded.
- final PDF must use only the canonical final-source folder after owner promotion.
- PR #14 head `56dd2599ce13d6edd6e97c422b56835c85d2af9c` hardens the owner-gated FINAL20 contract; Optical Book Creator quality #18 is green.

## 14. Senior / Hello Today

Current execution owner: Central RSE Orchestrator.

The Central Orchestrator may perform bounded implementation/self-repair and checkpointing, but may not cross production/legal/Play/human owner gates.

Current recovered milestone:
Phase 14H paired CHILD_DEVICE and 6+ UX boundary on PR #77.

Hard locks:
- no parent credentials on child device,
- no independent child email/password account,
- restricted server-bound child session,
- private Family Circle only,
- revoke supported,
- Child Mode remains production disabled until external/legal/human gates pass.

## 15. Mind Bloom

Current execution owner: **Central RSE Orchestrator**. The previous dedicated Mind Bloom chat is parked/archive-only and must not run a parallel implementation stream.

Current branch:
`feature/personal-chief-of-staff-foundation`

Current PR:
`#2` (Draft; keep Draft until an explicit future merge/release decision)

Current live head:
`bec72d0b45c3dd6e11715d3c77fa3c4d1f592a13`

Current product state:
**PRIVATE V1 SOURCE RELEASE CANDIDATE = PASS / FEATURE DEVELOPMENT FROZEN.**

Latest live CI on the current head:
- Mind Bloom CI **#81: SUCCESS**
- current-head code regression: none established

Durable implemented domains include:
Today, Inbox, Tasks, Saved, Projects, Reminders, Media, Life Admin, People, Daily Brief/Attention, reviewed Inbox promotions and Universal Chief-of-Staff Search.

Completed foundation includes:
- Phase 1G A/B/C,
- Phase 1H A/B/C/D,
- Phase 2A-0 architecture + threat model,
- Phase 2A-1 metadata-only integration foundation,
- Phase 2A-2 reviewed external-ingestion contract,
- Phase 2A-3 transactional reviewed staging foundation,
- integration security regression hardening.

Remote database state:
- `20260921064152_add_integration_metadata_foundation_v0` is active and verified,
- `20260921071341_add_integration_ingest_staging_v0` is active and verified,
- no reapplication is authorized,
- provider accounts/OAuth tokens/provider secrets/real sync jobs remain intentionally absent.

Private V1 closure also introduced a low-risk lazy-loading improvement for legacy workspace views. The initial entry bundle moved from about **2,009.17 kB / 545.74 kB gzip** to about **1,397.49 kB / 386.61 kB gzip** without changing the data model, RLS, provider boundary, credentials, `.env`, or remote Supabase state.

Current rule:
- do not spend further Codex/Actions on Mind Bloom merely to continue a roadmap;
- reopen feature development only for a reproducible Private V1 release blocker or explicit owner instruction;
- Google Calendar/Gmail/GitHub provider work is POST-V1 and remains owner-gated;
- a future commercial fork is a separate project and must never inherit private owner data/configuration by default.

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
