# Quick Desk Owner Decision Candidate

Status: RECONCILED
Date: 2026-09-30
Scope: 24 Gentle Steps to Christmas — Polish edition/app copy
Source conversation: RSE Quick Desk

## Owner decision

The Polish Gentle Steps edition/app must NOT be produced as a conventional translation or close transcreation of the English sentences.

The English book is a REFERENCE SOURCE for:
- daily mechanics,
- core intent/function,
- factual constraints,
- character roles,
- sequence,
- safety/claim boundaries.

The Polish product should be re-authored from scratch as if originally created for a contemporary Polish family.

Desired Polish voice:
- natural present-day family Polish;
- less spiritual / less mindfulness-coaching language where it sounds foreign in Polish;
- more situational humor, self-awareness and everyday family reality;
- no corporate/coaching/therapy-speak;
- no obvious 1:1 English syntax or motivational cadence;
- warm without being syrupy;
- playful without forced youth slang;
- credible for parents and children in Poland today.

Current Gentle Steps PL calibration (Days 1–7/24 and related fixtures) is REFERENCE ONLY and should not be treated as approved production copy.

## Reason / context

Owner reviewed current PL calibration and judged it too literal, too coaching/corporate in tone, and insufficiently culturally re-authored for Polish readers. The concern is commercial: the text should feel like an original Polish family product, not a translated American mindfulness book.

## Affected canonical surfaces

- localization/pl-PL/POLISH_STYLE_GUIDE.md
- localization/pl-PL/QUALITY_GATES.md
- localization/pl-PL/golden-tests/gentle-steps-*
- orchestration/content-sources/24-gentle-steps-to-christmas.yml
- Gentle Steps app content conversion checkpoint

## Safe immediate effect

Quick Desk should treat existing Gentle Steps Polish copy as calibration/reference only, not production-approved.

## Central reconciliation required

Create a Gentle Steps-specific PL re-authoring profile and new workflow:
1. extract immutable source function/mechanics without preserving English phrasing;
2. draft native Polish copy from that functional brief, ideally without viewing sentence-level source during first-write;
3. run a Polish cultural/family-language editor;
4. run humor/character-voice pass;
5. run anti-coaching/anti-translationese pass;
6. only then compare against English source for factual/mechanical fidelity;
7. run read-aloud and target-surface QA.

Use multiple independent agents/roles rather than one translator rewriting its own output.

## Conflict check

This supersedes the current Gentle Steps calibration copy as production language but does not discard the English source, mechanics, safety boundaries, or reusable Polish Localization Engine infrastructure.

## Central reconciliation receipt — 2026-10-05

Reconciled by Central into `orchestration/brain/COMMERCIAL_PRIORITY_STACK.md` under `Owner revenue-ASAP execution override — 2026-10-05`.

Canonical effect: Polish Gentle Steps copy remains owned by the Polish Localization stream and is produced as Polish-first re-authoring/transcreation rather than literal translation.

No delegated product branch/worktree was mutated by this reconciliation.
