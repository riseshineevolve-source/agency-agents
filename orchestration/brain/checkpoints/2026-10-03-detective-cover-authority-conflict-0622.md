# Detective cover authority conflict — 2026-10-03

Status: CONFIRMED / FAIL-CLOSED FOR FINAL WRAP

Fresh main verification found two conflicting cover authorities:
- 2026-09-25 Cover + A+ lock: `OSTATECZNA OKLADKA ROOM ZERO.png`, SHA-256 `2570df512f3883663aca1c4e5359ba12aa0489276f484b86ac5623ab037429a9`.
- 2026-10-02 FINAL Happy Makers Character Lock: `Akademia Detektywów_ Tajemnica Pokoju Zero.png`, SHA-256 `935cdf705c4107a3139cd55e8f639eaae5c0959631b1f28ebc359376cd9b77ad`.

The 2026-10-02 A+ Final Production Manifest explicitly says its parent-closer uses the exact owner-supplied final cover from 2026-10-02, which strengthens the newer-cover signal for marketing/A+ work. The KDP Release Package still points to the 2026-09-25 cover and stale 146-page geometry.

Central will not edit the delegated Marketing surface. Final KDP wrap generation stays fail-closed until the marketing/KDP release package is reconciled to one exact front filename/SHA and the exact final interior page count is known.

No art was changed and no wrap was generated.
