# CODEX START HERE — 24 Gentle Steps controlled Polish scale-out

Status: OWNER-AUTHORIZED BOUNDED TRANSLATION / QA
Authority: Central RSE Technical Orchestrator
Date: 2026-09-26

## Collision rule

This branch may run in parallel with Polish Engine reconciliation ONLY because its write surface is restricted.

You MAY write:
- new Gentle Steps bounded translation candidate files under `localization/pl-PL/golden-tests/`;
- Gentle Steps project-specific review/checkpoint docs.

You MUST NOT write:
- localization engine scripts;
- shared terminology JSON;
- shared regression framework;
- general Polish Engine docs;
- PR6 reconciliation files.

If a shared terminology/engine change seems necessary, REPORT it instead of editing it.

## Read first

- `localization/pl-PL/POLISH_STYLE_GUIDE.md`
- `localization/pl-PL/ACCEPTED_TERMINOLOGY.md`
- `localization/pl-PL/FORBIDDEN_AIISMS_PL.yml`
- `localization/pl-PL/QUALITY_GATES.md`
- `localization/pl-PL/GENTLE_STEPS_WEEK1_REAL_TEMPLATE_FIT_GATE.md`
- `localization/pl-PL/golden-tests/gentle-steps-christmas-calibration-round1.md`
- `localization/pl-PL/golden-tests/gentle-steps-christmas-week1-controlled-expansion.md`
- `orchestration/content-sources/24-gentle-steps-to-christmas.yml`

Canonical product:
24 Gentle Steps to Christmas
Published English paperback: 104 pages.

The Library source file known to the owner is:
`24 Gentle Paperback ok.pdf`

If that exact source is attached/available in this Codex task, use it.
If it is NOT available, do NOT invent source text and do NOT OCR unrelated material. Stop translation at the exact missing-source boundary and still prepare the extraction/QA plan.

## Goal

Translate the next complete bounded segment after the accepted Week 1 candidate.

Preferred scope:
Days 8–14, ONLY if exact source boundaries/content are available from the canonical published source.

Preserve the recurring ritual model and character voice:
- Mindful Moment / Spokojna chwila
- Fun Spark / Iskra zabawy
- Family Connection / Chwila bliskości
with labels still subject to final product-wide confirmation where previously marked provisional.

## Quality requirements

For every day/activity:
- source fidelity;
- natural Polish;
- no literal/AI feel;
- Happy Makers voice preserved;
- mechanics unchanged;
- numbers/order/timing unchanged;
- consent/safety boundaries preserved;
- no new therapeutic/medical claims;
- no meaning compression merely to shorten Polish.

Create explicit QA sections:
- source fidelity
- naturalness
- character voice
- claim/safety review
- designed-surface risk
- terminology/engine issues to report upstream

## Layout gate

DO NOT falsely close the real-template fit gate.

The four accepted Week 1 long headings still require genuine real-template evidence.
No proxy, character count, or smaller body text counts as PASS.

Translation scale-out may proceed as bounded LANGUAGE candidate work, but publication/promotion remains blocked on real layout proof.

## Deliverable

Create a new bounded candidate document for Days 8–14 (or the largest exact complete subset available), plus a project checkpoint.

Do not claim full-book completion.

Final response:
- source actually used
- exact days translated
- QA result
- unresolved layout risks
- any shared terminology/engine request
- files changed
- local commit
- recommendation for next bounded segment.
