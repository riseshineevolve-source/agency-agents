# RSE Integration Map

Status: active control document  
Last live verification: 2026-09-18  
Owner: Rise.Shine.Evolve.  
Purpose: make tool connectivity, source-of-truth boundaries, and handoff rules reconstructible without relying on chat memory.

## Operating rule

Connections are capabilities, not sources of truth by themselves.

For current project state, use:
1. GitHub repository files / branches / PRs / issues,
2. verified project checkpoints and manifests,
3. connected Drive / Library master artifacts,
4. live measurement systems such as GSC / GA4 / Metricool,
5. conversational memory only when it does not conflict with durable evidence.

Never commit passwords, OAuth tokens, service-role keys, API secrets, private customer data, confidential case data, or private unpublished master binaries into this repository.

## Verified ChatGPT-side integrations

| System | Verified state on 2026-09-18 | RSE role | Source-of-truth rule |
|---|---|---|---|
| GitHub / ChatGPT Codex Connector | CONNECTED; write-capable on core RSE repositories | Code, branches, PRs, issues, CI/workflow coordination, durable orchestration | Primary technical source of truth |
| Google Drive | CONNECTED; search/read verified | Heavy files, source documents, publication masters, working assets | Master-file store when the project manifest points to Drive |
| Gmail | CONNECTED | Explicit email search/read/draft/send workflows | Never treat mailbox content as project truth unless reconciled into project state |
| GSC Wizard / Google Search Console | CONNECTED; RSE domain property visible | Indexing, search performance, recrawl and SEO evidence | Canonical measurement source for Google Search state |
| Metricool | CONNECTED; RSE brand visible | Social scheduling, publishing review and social analytics | Operational social source; reconcile strategic decisions back to GitHub |
| Creative Claw | CONNECTED; RSE film drafts and approved reference assets visible | Video/image/audio creative production | Generated media is derivative; approved brand/product truth remains in GitHub/Drive |
| Supabase | CONNECTED; project inventory readable | Backend/database/auth/storage for app projects | Project-specific backend truth; use repo migrations/checkpoints for implementation history |
| Windsor.ai | CONNECTED on Trial; Facebook is currently the only live connector observed | Optional cross-channel analytics aggregation | Secondary aggregator, never replace native source systems as canonical evidence |

## Current verified RSE connection details

### GitHub

Core repositories live-verified:
- `riseshineevolve-source/agency-agents`
- `riseshineevolve-source/RISE.SHINE.EVOLVE`

The central portfolio registry is:
- `orchestration/rse-business-projects.yml`

Central recovery / continuity sources:
- `orchestration/RESUME_FROM_ZERO.md`
- `orchestration/RSE_BUSINESS_PORTFOLIO.md`
- `orchestration/RSE_RECOVERY_INDEX.md`
- `orchestration/RSE_TECHNICAL_ORCHESTRATOR.md`
- this file: `orchestration/RSE_INTEGRATION_MAP.md`

### Google Search Console

Connected property:
- `sc-domain:rise-shine-evolve-learning-hub.com`

Use it for live indexing/search evidence. Do not create new content merely to respond to slow recrawl.

### Metricool

RSE brand is connected with timezone `Europe/Warsaw`.

Observed connected publishing networks:
- Facebook
- Instagram
- YouTube

TikTok was not present in the verified network payload on 2026-09-18, so treat TikTok publishing connectivity as NOT VERIFIED until a later readback confirms it.

### Creative Claw

Verified RSE creative workspace contains current film drafts including:
- Screen Zombie
- Lizard Brain
- Family Motto
- Happy Makers Episode 1
- You Hold the Key

Verified reference library also contains approved RSE brand/book assets imported from official sources.

Creative Claw may generate derivatives, but it must not silently redefine approved product names, claims, brand facts, or book/source hierarchy.

### Supabase

Connector access is live.

Observed project-level state:
- main RSE source project: active/healthy,
- Mind Bloom Assistant: active/healthy,
- The Confident, Mindful & Happy Me Adventure backend project: inactive.

Do not infer that an inactive Supabase project means the product itself is abandoned. Product status comes from the portfolio registry and project repository.

### Windsor.ai

Current plan observed: Trial.

Current connected source observed:
- Facebook only.

Google Analytics 4 is supported by Windsor.ai but was not observed as connected in the live connector list during this verification. Treat Windsor as optional until it has data sources that add value beyond native tools.

### GA4

Website-side GA4 implementation was merged in `RISE.SHINE.EVOLVE` through PR #586.

Current production gate is tracked in issue #587:
- privacy disclosure / consent verification,
- production tag behavior verification,
- GA4 Realtime / DebugView verification,
- keep Google Signals / ads personalization / remarketing off until deliberately changed.

A direct GA4 data connection inside the central ChatGPT orchestration surface was NOT verified on 2026-09-18. Do not claim live GA4 reporting access from this chat unless a later connector read proves it.

## Local / external engineering toolchain

These tools are part of RSE execution architecture but are not automatically controlled by the current ChatGPT connector session.

### Codex CLI
Last known verified state from RSE work:
- Codex CLI `0.154.0` installed after installer/config troubleshooting,
- corrupted local `.codex/config.toml` was backed up/removed,
- subsequent repository work completed successfully.

Before relying on a new local Codex session, re-check the local CLI/session rather than assuming it stayed authenticated.

### Claude Code / Cursor
Last known verified state:
- Claude Code `v2.1.268` working inside Cursor,
- used against the Detective Academy working copy,
- Claude/API billing is separate from ChatGPT/GitHub connector usage.

### Git Bash / PowerShell / local Windows filesystem
Useful for local-only or large-file workflows, especially:
- Optical Animals production assets,
- Opinie confidential local runtime,
- local Android/device tooling,
- local Codex/Claude sessions.

The central ChatGPT session cannot assume it can execute commands on the user's Windows machine. Local state must be verified by a local tool/session before depending on it.

### Gemini CLI / GitHub Copilot
They remain part of the broader RSE tooling architecture but were not live-verified from this central ChatGPT session on 2026-09-18. Do not treat them as active execution channels until verified.

### Video Express
External paid tool used for image/video transformation experiments. No direct RSE connector was verified from this ChatGPT session. Keep it as an external production tool unless a supported connector becomes available.

## Routing by system

- Code / project status / automation rules -> GitHub first.
- Heavy book/PDF/media masters -> Drive/Library/local master storage, with manifests/checksums in GitHub.
- Search/index evidence -> GSC.
- Website analytics -> GA4 after issue #587 production gate is verified.
- Social scheduling/analytics -> Metricool.
- Creative generation / film assembly -> Creative Claw, with approved references.
- App backend/data/auth -> project-specific Supabase.
- Cross-channel aggregation -> Windsor only when its connectors add useful coverage.
- Confidential accident-reconstruction case data -> LOCAL ONLY. Never GitHub/Drive/remote agent contexts unless explicitly sanitized.
- Senior / Hello Today -> Central RSE Orchestrator execution.\n- Mind Bloom -> Central RSE Orchestrator ownership; Private V1 is frozen after green current-head CI, and the old dedicated chat is archive-only.\n- Marketing Autopilot -> dedicated execution chat with central milestone/blocker synchronization.

## Handoff rule

Every fresh central RSE technical session should read this file after the core portfolio documents and then live-verify any integration that is essential to the task. A connection marked VERIFIED here means it worked on the date above, not that future OAuth/session state can be assumed forever.
