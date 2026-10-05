# Detective CASE 00 Sampler V1

Status: NON-PRODUCTION GROWTH SUPPORT ARTIFACT  
Owner directive: FINISH -> PUBLISH -> SELL -> LEARN -> SCALE  
Deployment: NOT DEPLOYED  
Paid services: NONE

## Source lock

This sampler reuses the real Case 05 code-order mechanism from the delegated Detective EN premium source; it does not invent or modify book canon.

- source branch: `feature/detective-en-premium-content-upgrade-20261005`
- source commit: `d2ba3b704d22ef9a19f677db5b6a164cee63ed1d`
- source file: `orchestration/detective/content-upgrade/detective-en-premium-v1/OWNER_READ_CANDIDATE_EN_PREMIUM_V7.md`
- source Git blob: `532631900666570f958fa3384cca247e98b565ba`
- exact clues preserved:
  1. STAR comes immediately before BOLT.
  2. BALL appears somewhere before STAR.
  3. HEART appears somewhere after BOLT.
  4. KEY is not first or last.
  5. MOON appears after KEY.
  6. Exactly one symbol sits between HEART and MOON.
- canonical Hint Vault seed preserved: `Treat STAR -> BOLT as one two-symbol block. Do not split them.`

## Deterministic proof

All 6! = 720 possible symbol orders were enumerated against the six canonical constraints.

Result: exactly one valid order:

`BALL -> STAR -> BOLT -> HEART -> KEY -> MOON`

## Product-sampler behavior

- mobile-first single static HTML file;
- no account, backend, secrets, signing keys, database, paid service or vendor dependency;
- tap/keyboard-accessible symbol placement;
- three progressive hints;
- explicit solution reveal;
- disabled full-book CTA until a verified live listing URL exists;
- local CustomEvent hooks only; no external analytics library is added.

## Adoption-gate result

No new vendor/tool/agent is required. This extends existing static-web capability and therefore passes the Growth Operating System adoption gate.

## Release boundary

This artifact is support-only. It does not:
- deploy production;
- publish KDP;
- freeze English;
- change Detective source/book content;
- cross any visual, legal, print, store or spend owner gate.
