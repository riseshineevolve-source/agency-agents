# Central RSE — Detective Factory truth correction

Date: 2026-10-06

Current canonical agency-agents main: b143529523d297daa9963eb8084fc33446ebf6ae.

A current Detective Book Factory v2 integration ref exists in riseshineevolve-source/RISE.SHINE.EVOLVE:
- branch: feature/rse-book-factory-v2
- exact HEAD: df42a5cca4757c6fd5dbca3a02babe219bc84ee0

Its current control/checkpoint still queues an AUTHORIZED V7 content sync from source commit:
58501f5682fa3d87e0c9ddad9bc1d48c200bb038.

Current Detective product truth has advanced to:
- agency-agents branch: feature/detective-en-premium-content-upgrade-20261005
- exact HEAD: 24918a3a747373d1d25375e3e6aff3b8a7387f32
- exact V10 owner-read candidate blob: 19df709e381445a6f5a52d7b0c1c898bd5b706be
- state: OWNER_READ_CANDIDATE / CONTENT NOT YET FROZEN

Correction: the release-integration blocker is not a missing Factory ref. It is a stale content-source authority mismatch: Factory v2 is queued against V7 while current content truth is V10.

Delegated Factory next bounded action:
1. supersede the V7 source lock with exact V10 source lock;
2. rehash Book Map dependencies;
3. compute exact changed-page closure;
4. rebuild/review changed pages only;
5. rerun Case01 and Case05 deterministic solution regressions;
6. preserve Case03 visual as unresolved with no substitution;
7. do not redesign or freeze.

Separate gates remain:
- content: owner approval of exact V10 candidate before EN freeze;
- visual/template: corrected Case01 Pages 16–18 remain READY_FOR_OWNER_VISUAL_REVIEW, owner_approved=false, template_frozen=false, scaling_authorized=false;
- Case03 final rendered visual is a later production/owner gate.

Central remains read/sync-only on the delegated Detective product surface. No main merge, EN freeze, KDP/Play publication, production deploy, spend, secret/signing action, or owner-art mutation is authorized.
