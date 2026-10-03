# RSE Book Factory v1 architecture checkpoint
Date: 2026-10-03
Status: ARCHITECTURE LOCKED / IMPLEMENTATION READY

Central decision:
RSE book production moves from manually regenerated AI pages to a deterministic fixed-layout publishing engine.

Canonical architecture:
`orchestration/architecture/RSE_BOOK_FACTORY_V1.md`

Execution bootstrap:
`orchestration/bootstrap/RSE_BOOK_FACTORY_EXECUTION_BOOTSTRAP.md`

Primary implementation target:
new repo `riseshineevolve-source/rse-book-factory`

First consumer:
Detective Academy EN Cases 02–30 after the First18/Case01 owner gate.

Key production rule:
Approved Pages 1–20 may enter the first release as frozen high-resolution PNG pages. The factory does not need to rebuild those pages before publication.

Case 01 becomes the template family for:
- case intro;
- HM Comms;
- Witness Board;
- Live Map + Verdict.

Later consumers:
- Detective Academy PL via same templates + PL content;
- Gentle Steps EN/PL;
- Optical Animals assembly/preflight.

Implementation should use max four coordinated lanes and stop for owner visual approval after generated Case 02 proof before bulk rollout.
