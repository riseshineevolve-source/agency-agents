# RSE Commercial Priority Stack — Q4 2026

Status: **CANONICAL**
Owner decision: 2026-09-21
Applies to: central RSE Orchestrator, Brain Sync, Day/Night/24-7 shift, marketing synchronization, Codex budget governor.

## Priority order

| Priority | Project | Business reason | Current execution rule |
|---|---|---|---|
| **#1** | **Happy Makers Detective Academy EN -> KDP** | Closest path to real revenue and does not depend on DUNS or Google Play. | **Final English interior PASS** at `6aef8cefdce029413f2cc29e656d5fbad99d546c`: 141 pages, 141 print-scale previews, ALL-15 15/15 remote, canonical 30-mission integration PASS, KDP preflight PASS, Build #93 PASS, SEO #551 PASS. Product engineering is at **OWNER RELEASE GATE**. Do not reopen maps, Witness Boards, naming, clues, story architecture, character asset sync or final interior engineering unless owner visual review reveals a concrete defect. Remaining owner tasks: final cover/proof, pricing, KDP upload/publication. English interior/source freeze is a separate owner gate. |
| **#2** | **Happy Makers Detective Academy PL -> KDP Poland** | Immediate second commercial edition after the English source is explicitly frozen; reuses the validated book and the Polish Localization Engine. | Branch `rse/polish-localization-engine-v1` is reconciled with main at `10b8189cd7c589b1f0fa0b281c6b22d0b5f4c436`; PR #6 mergeable; local regression PASS across 7 accepted fixtures / 37,159 candidate chars. Full-book Detective PL remains blocked until explicit owner English-source freeze. Before that, only bounded glossary/segmentation/logic/surface-fit calibration is allowed. |
| **#3** | **24 Gentle Steps to Christmas** | Seasonal window is becoming time-sensitive for Q4/Christmas. | Week 1 regression PASS and source-side spot-check PASS. Remaining promotion gate is real-template overflow/fit for the four longest Polish headings. Do not treat proxies as final fit evidence and do not shrink body text merely to rescue headings. |
| **#4** | **Optical Animals** | Strong giftable KDP product if the remaining 8 final visual slots are resolved. | Preserve 12 approved visuals. Advance tooling/manifest/preflight automatically; final 20 visual selection remains owner-gated. Local hardening commit `5e69b43` must not be pushed until canonical remote state is confirmed and reconciled non-destructively. |
| **#5** | **RSE Consumer App Factory / Google Play apps** | Strategically important shared infrastructure, but external Google/DUNS/Play dependencies reduce near-term revenue value. | Continue only high-value safe architecture/verification below gates. Do not let this outrank shippable KDP revenue lanes while Google/DUNS is pending. |
| **parallel below gates** | **Senior / Happy Me / Opinie / AI Discovery / Website** | Important active programs but not the current primary revenue unlock. | Continue safe AUTO/AUTO+VERIFY work when not blocked; park at external/legal/privacy/owner gates and move capacity to higher-priority lanes. |

## Frozen / non-active commercial lane

**Mind Bloom Private V1 = SOURCE RELEASE CANDIDATE PASS / FEATURE DEVELOPMENT FROZEN.**

Do not spend further Codex or GitHub Actions on Mind Bloom unless a reproducible release blocker appears or the owner explicitly reopens it. Future Google Calendar/Gmail/GitHub integrations and any commercial fork are separate POST-V1 decisions and must not delay current revenue lanes.

## Revenue-first rule

Do **not** wait for Google Play to begin generating revenue from products that can ship independently through KDP.

The central operating sequence is:

**Detective EN KDP -> Detective PL KDP -> seasonal Gentle Steps -> Optical Animals gift lane -> Google Play/app-factory acceleration when external gates clear.**

Detective PL is handled through the Polish Localization Engine and starts full-book production only after the English canonical master/source is explicitly frozen. ALL-15 spatial validation already passes remotely; do not reopen it merely to create work.

## Detective owner decision — CLOSED

Previous map-system owner gate is resolved.

Owner decision:
**B — APPROVE WITH SMALL FIXES**

Locked implementation direction:
- white/light map background rather than gray;
- larger and bold room/zone names;
- larger and bold row/column coordinate labels;
- readable legends and person/object descriptions at real print size;
- generous pencil-writing space;
- premium Witness Board using the full page more effectively;
- larger typography and bold names on Witness Board clue/evidence cards;
- child experience must feel like opening a detective case file, never a school worksheet;
- naming direction **B — branded / academy / adventure**;
- deterministic alias layer may change presentation names only and must never change puzzle identity, clue meaning, topology, answer or solution logic;
- examples of naming style include Nova, Echo, Blaze, Clover, Scout and Pixel, but per-case names must remain distinct and immediately readable.

No further owner design gate is required for the implemented ALL-15 system. Current engineering state is the final-English-interior PASS recorded in Priority #1 above.

## Detective positioning lock

Canonical marketing source:
`marketing/detective-academy-kdp-positioning.md`

Protect:
- child = the missing detective;
- **THE BOOK ITSELF IS THE EVIDENCE**;
- 30 cases form one book-long mystery;
- solved cases may later become evidence;
- do not spoil `CHECK THE OLD MAP`;
- 3-level Hint Vault supports confidence rather than shame;
- solutions explain **why**, not only the answer;
- premium Detective Academy dossier / case-file experience, never worksheet positioning;
- screen-free benefit without parent guilt;
- gift framing: an experience/adventure, not merely another object.

Preferred hero:
**30 CASES. ONE HIDDEN MYSTERY. YOU'RE THE MISSING DETECTIVE.**

Supporting hook:
**Every case can be solved. Not every case is finished.**

## Q4 persuasion / marketing rule

Use:
**situation -> desire -> hesitation -> evidence -> imagined use -> genuine timing -> CTA**

Do not use:
- fake scarcity,
- fabricated proof,
- fear amplification,
- parent guilt,
- unsupported neuroscience/medical claims,
- manipulation disguised as psychology.

Canonical framework:
`orchestration/marketing/RSE_Q4_ETHICAL_PERSUASION_FRAMEWORK.md`

## Seasonal framing lock

- **Sep-Oct / Detective:** immersive screen-free detective experience; never educational-workbook framing.
- **Black Friday:** prove depth/value first — 30 connected cases, progressive challenge, Hint Vault, reasoning solutions and Room Zero payoff — before any owner-approved discount decision.
- **Nov-Dec:** gift-an-adventure framing for Detective; Optical Animals as a creative gift; `24 Gentle Steps to Christmas` as a holiday-native ritual/connection product without ideal-Christmas pressure.

## Automation rule

Hourly/24-7 orchestration should select the highest-value safe task from this stack.
A project at an owner/external gate is parked; the shift moves to the next safe lane rather than stopping.

This priority stack remains in force until the owner explicitly changes it.