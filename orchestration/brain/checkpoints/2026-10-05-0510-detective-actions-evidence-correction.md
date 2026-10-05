# Detective Actions evidence correction — 2026-10-05 05:10 CEST

Status: VERIFIED CORRECTION / CENTRAL RELEASE-PACKAGE TRUTH
Authority: Central RSE Technical Orchestrator
Product writer: delegated Book Production / Detective lane; Central remains read-only on the product surface.

The earlier checkpoint wording that relevant Detective v2 commits had no GitHub Actions workflow runs/artifacts was too broad.

Fresh GitHub verification:
- Case01 reconstruction execution head `a3c7de3c490ce60441518b647087890ae66f6c08`: SEO Validation run `37187802626` succeeded; retained artifacts are only `lighthouse-results` and `seo-status`.
- M1 head `83b4ffbb1f7dfe9cb9a3ed425fc716446c2b0a5c`: SEO Validation run `37201384354` succeeded; retained artifacts are only `lighthouse-results` and `seo-status`.
- current delegated head `bbe4941ea190d8ef3d2617fe18c1b26c8a562864`: SEO Validation run `37215233747` succeeded; retained artifacts are only `lighthouse-results` and `seo-status`.
- reconstructed-review head `f14eed4b93dcc610c8730c216ac5e37ee7bb19122`: zero workflow runs.
- there is still no open PR whose head is `feature/rse-book-factory-v2`.
- the repository still has no GitHub Releases.

Release conclusion is unchanged: no retained remote artifact contains the required Case01 owner-review packet (`case01-reconstructed.pdf`, contact sheet, or Pages 16–18 side-by-side images).

Current blocker: durable exact-hash export of the existing five-file Case01 owner-review packet.

Exact owner gate after export: review physical Pages 16–18 -> approve or bounded-correct -> G4 freeze -> Case02 regeneration on the locked template -> Case02 exception review.

The 24 half-inch safe-zone flags remain a separate print-master blocker after template approval.

No rerender merely for transport, no Cases03–30 batch, no EN freeze, no main merge, and no KDP publication are authorized.
