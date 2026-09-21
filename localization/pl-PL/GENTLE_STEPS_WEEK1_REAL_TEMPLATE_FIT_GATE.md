# 24 Gentle Steps to Christmas — Week 1 real-template fit gate

Status: **OWNER/RENDER FIT GATE — NOT YET PASS**  
Updated: 2026-09-21  
Source of truth: published English paperback, 104 pages  
Scope: the four longest accepted Week 1 Polish headings only

## Why this exists

Week 1 already passes localization regression and source-fidelity review. The remaining promotion gate is visual fit in the real designed daily template. A proxy, character-count estimate or smaller body text is not acceptable evidence.

The published paperback confirms the actual source surfaces and source wrapping:

| Source PDF page | Source heading surface | Accepted PL candidate | Preferred safe line break for the real-template proof |
|---|---|---|---|
| 25 | `Fun Spark - Family Sound Symphony` (source uses one heading line) | `ISKRA ZABAWY — RODZINNA SYMFONIA DŹWIĘKÓW` | `ISKRA ZABAWY — RODZINNA SYMFONIA` / `DŹWIĘKÓW` |
| 26 | `Family Connection -` / `What I Love About Being Us` (source already uses two heading lines) | `CHWILA BLISKOŚCI — CO LUBIĘ W NASZEJ RODZINIE` | `CHWILA BLISKOŚCI —` / `CO LUBIĘ W NASZEJ RODZINIE` |
| 35 | `Family Connection -` / `The Sound I Love at Home` (source already uses two heading lines) | `CHWILA BLISKOŚCI — MÓJ ULUBIONY DŹWIĘK DOMU` | `CHWILA BLISKOŚCI —` / `MÓJ ULUBIONY DŹWIĘK DOMU` |
| 38 | `Family Connection - A Word of Calm` (source uses one heading line) | `CHWILA BLISKOŚCI — SŁOWO NA SPOKÓJ` | first try one line; if the real box overflows, use `CHWILA BLISKOŚCI —` / `SŁOWO NA SPOKÓJ` |

## Pass / fail rule

PASS only when all four accepted Polish headings are rendered on the actual editable/rendering surface and:

- no glyph is clipped;
- no heading collides with body copy, character note or decorative elements;
- body-copy font size/leading is unchanged;
- the heading does not require an unnatural Polish rewrite merely to fit;
- the approved two-line breaks above are sufficient without compressing tracking to a visibly inferior result;
- Polish diacritics render correctly at print size.

FAIL if any heading can fit only by shrinking body text, materially reducing heading legibility, distorting tracking, clipping diacritics or changing the activity meaning.

## Current evidence boundary

The real published PDF pages are available and confirm the page mapping and source line structure. The current automation runtime does **not** have an authorized raw-byte/editable-template materialization path for the paperback, so it cannot truthfully perform the final Polish overlay/render proof in this run.

Therefore:

- Week 1 remains **candidate / REVIEW REQUIRED for designed-surface fit**;
- do not promote Week 1 to accepted calibration yet;
- do not start full-book Gentle Steps localization from this evidence alone;
- no owner copy decision is required: the four Polish candidates above remain the accepted language candidates unless a real render demonstrates a concrete fit defect.

## Smallest owner handoff

When the editable/rendering surface is available, render only pages corresponding to source PDF pages **25, 26, 35 and 38** with the accepted PL headings and the preferred line breaks above. Review at real print scale. If all four pass, the Week 1 fit gate can be closed without reopening translation/content scope.
