# Detective Academy — CASE 00 sampler V1

Status: IMPLEMENTATION-READY CENTRAL GROWTH SUPPORT / NO PRODUCT-SURFACE MUTATION
Date: 2026-10-05
Strategy: `orchestration/strategy/RSE_GROWTH_OPERATING_SYSTEM_2026_Q4.md`

## Purpose

Create a 1–5 minute real-product sampler for Happy Makers Detective Academy without inventing new puzzle truth, reopening book design, exposing Room Zero spoilers, or requiring a new vendor/backend.

This is a growth-support surface only. The book remains the source of truth and the live product release path has higher priority.

## Canonical source locks

Reader copy:
- `orchestration/detective/DETECTIVE_ACADEMY_BOOK1_READER_TEXT_V3.txt`
- blob SHA: `4d45e4a4fcd9e5c15906479b196efd6c82b21e59`
- source Gold Master blob declared by that projection: `8685f8e561d0bfb3837445b72b4d6f799a9a48f2`
- EN remains NOT FROZEN.

Positioning:
- `marketing/detective-academy-kdp-positioning.md`
- blob SHA: `6012d699cc883effafcb832568d5579637ad6504`

Do not expose `CHECK THE OLD MAP`, Room Zero identity/reveal, solution coordinates, meta carrier mechanics or internal Shigai terminology.

## V1 experience

Use a real, self-contained code deduction already present in the canonical reader text: the six-symbol puzzle from Case 05. Present it as a sampler training file, not as a rewritten book page.

Flow:
1. Recruit moment: one short black-envelope / missing-detective hook from the approved opening promise.
2. Objective: decode the one six-symbol order that makes every clue true.
3. Evidence: the six canonical clues and six symbols from Case 05, unchanged.
4. User interaction: reorder/select symbols into six slots.
5. Optional Hint Vault: reveal at most three progressively stronger nudges, never the answer automatically.
6. Check: deterministic exact-order validation.
7. Success: short Academy-style completion state plus a direct path to the full product/listing when a verified live URL exists.

The sampler must not reproduce the Case 05 narrative paragraph that references the wider mystery thread. It demonstrates the actual puzzle mechanism while keeping the book-long mystery protected.

## Locked puzzle data

Symbols:
`BALL`, `STAR`, `BOLT`, `HEART`, `KEY`, `MOON`

Canonical clues:
- STAR comes immediately before BOLT.
- BALL appears somewhere before STAR.
- HEART appears somewhere after BOLT.
- KEY is not first or last.
- MOON appears after KEY.
- Exactly one symbol sits between HEART and MOON.

Deterministic solution for QA only:
`BALL -> STAR -> BOLT -> HEART -> KEY -> MOON`

The solution is unique under exhaustive permutation verification. Do not change clues or solution to create variety; a future second sampler requires a separate source-backed content decision.

## Hint Vault V1

Hints are sampler-specific presentation derived from the canonical rules, not new puzzle facts:
- Level 1: Start with the pair that must stay together.
- Level 2: Place BALL before the STAR/BOLT pair, then use the clue about the gap between HEART and MOON.
- Level 3: KEY cannot be at either end, and MOON must sit after it. Test the remaining open slots against every clue.

No shame/failure language. A hint is a detective tool.

## UI contract

Mobile-first, fast, no account required, no backend required.

Required states:
- intro/recruit;
- puzzle active;
- hint drawer;
- incorrect-but-try-again;
- solved;
- CTA unavailable state until a verified product URL exists.

Accessibility:
- symbols must have text labels, not color-only identity;
- keyboard/touch controls must work without drag-only interaction;
- clear focus states;
- result state announced accessibly;
- reduced-motion safe.

## Measurement contract

Reuse existing RSE measurement only; do not add another analytics stack.

When analytics consent exists, emit:
- `case00_start`
- `case00_hint` with level 1–3
- `case00_check` with success boolean and attempt bucket
- `case00_complete`
- `case00_product_click`

Primary decision signal: sampler completion -> verified product/listing click. Reach alone does not qualify the sampler as a winner.

## Release guardrails

- No deployment from this central branch.
- No paid activation.
- No unverified Amazon/KDP URL, price, availability or review claims.
- No new account, social, AI or backend complexity.
- Do not modify Detective book source/artifacts.
- Do not use this work to bypass the active owner visual/KDP release gate.
- Do not add a new vendor without passing the Growth Operating System adoption gate.

## Acceptance test

PASS only when a future implementation:
- renders the six locked clues exactly;
- accepts only the unique locked solution;
- works on a representative phone viewport and keyboard navigation;
- does not leak protected Room Zero/meta content;
- works without login/backend;
- leaves the product CTA disabled or generic until a verified live destination exists;
- emits only the approved measurement events when consent permits.

## Next implementation action

Build this as one isolated static sampler route/component using the existing RSE web stack, then run local/browser QA. Production deployment remains owner-gated and must not occur until the product/listing destination is verified.
