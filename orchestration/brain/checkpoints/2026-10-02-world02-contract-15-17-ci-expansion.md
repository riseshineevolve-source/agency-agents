# World 02 — contract CI expansion through Level 17

Date: 2026-10-02
Status: **SOURCE CONTRACT COVERAGE PREPARED / REMOTE CI TRIGGER PENDING**

## Scope

This bounded slice extends the source-graph contract tooling from World 02 Levels 11–14 through Levels 15–17.

Canonical paperback authority remains:
`paperback 10 STORIES WORLD 02 FINAL standard(1).pdf`

SHA-256:
`e94d2937cc459a5c7c3c5968c64ba39f2a03702f929488e42b00b5db3f9f7f76`

## Durable changes

- graph builder accepts Levels 11–17;
- validator has bounded mission specs for Levels 15–17;
- regression tests load and verify Levels 15–17;
- Interactive Book Contract workflow rebuilds and validates Levels 11–17;
- workflow path filters include Level 15–17 evidence manifests;
- Level 16 source pack/evidence/canonical-validation artifacts were reconciled into the combined 15–17 contract lane because the Level 17 source branch did not contain those Level 16 final artifacts.

## Deterministic reconciliation evidence

Level 15:
- pages 47–54;
- 26 nodes;
- opener 1 / system log 5 / dialogue 13 / console 3 / quest 2 / science 1 / secret code 1;
- published code: ALL HANDS ON DECK!.

Level 16:
- pages 55–63;
- 32 nodes;
- opener 1 / system log 6 / dialogue 18 / console 3 / quest 2 / science 1 / secret code 1;
- published code: SWAP GOGGLES.

Level 17:
- pages 64–71;
- 30 nodes;
- opener 1 / system log 8 / dialogue 14 / console 3 / quest 2 / science 1 / secret code 1;
- published code: DELETE SPAM MESSAGE.

All three packs were rechecked for:
- canonical SHA pin;
- exact pack/evidence node count parity;
- page-range parity;
- deterministic node IDs and next-node chain;
- localized-copy equality to locked evidence;
- EN supported / pl-PL planned only;
- absence of invented XP, score, entitlement, auth or paywall runtime fields.

A stale Level 17 type-count assumption (13 dialogue / 6 system log) was found during reconciliation and corrected to the actual canonical graph counts above.

## Gate

No product copy was changed.

Remote GitHub Actions evidence is still required before this contract slice can be treated as green CI. The connected write path did not permit the required PR/ref transition in this run, so no CI PASS is claimed.

Do not promote Levels 18–20 into runtime on the basis of this checkpoint alone.
