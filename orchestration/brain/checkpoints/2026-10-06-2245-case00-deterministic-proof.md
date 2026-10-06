# Central RSE checkpoint — CASE 00 deterministic proof gate

Date: 2026-10-06
Status: SAFE GROWTH ENABLEMENT / NON-PRODUCTION

Detective production remains owner-gated; this branch does not write the Book Factory surface.

Implemented:
- self-contained CASE 00 sampler carried onto a fresh branch from current main;
- deterministic verifier for puzzle uniqueness and clue integrity;
- visible non-production / V12 provenance guard;
- disabled pre-live full-book CTA;
- fail-closed checks against external scripts and external URLs.

Verification:
- all six CASE 00 clues were independently rechecked against the current Detective V12 candidate before implementation;
- brute-force permutation check yields exactly one valid code:
  BALL -> STAR -> BOLT -> HEART -> KEY -> MOON;
- local verifier PASS.

Boundary:
No production deployment, analytics, backend, account, paid service, EN freeze, KDP action, owner-approved art change or owner gate was crossed.
