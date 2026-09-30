# Detective Academy — owner front-matter source lock
Date: 2026-09-30

## Why this checkpoint exists

Owner review of the 2026-09-29 180-page artifact exposed a real production regression that the previous bounded audit did not catch.

The canonical V3 reader text had NOT reverted. The regression was introduced by the renderer:

- `draw_front()` hardcoded `YOUR SQUAD` + squad art onto physical opening page 3 and then rendered the canonical Page 3 black-envelope copy underneath it.
- `Book.begin()` injected a small upper-left micro-grid/ruler on every page.
- Happy Makers COMMS panels placed thin white dialogue over a full black evidence grid, reducing readability and making the grid a text background instead of a decorative motif.

This explains why the book appeared to “mix” old/new versions even though the canonical Gold Master V3 source remained intact.

## Canonical reader-copy authority

Same version family, no V4 created:

`orchestration/detective/DETECTIVE_ACADEMY_BOOK1_TEXT_GOLD_MASTER_V3.md`

Owner-front-matter source-lock commit:
`e136e94402c8f870f3d9221b7047c1406cbec813`

Canonical blob after owner front-matter copy changes:
`8685f8e561d0bfb3837445b72b4d6f799a9a48f2`

The owner-directed copy changes are:
- Page 2 publication CTA now uses the full website invitation with HTTPS plus Facebook line.
- Physical Page 3 remains THE BLACK ENVELOPE cold open only and ends on WILL YOU CLAIM IT?
- Physical Page 4 is YOUR SQUAD.
- The first Happy Makers dialogue is now a general team/recruit opener and does not reference Alio's helmet before the reader knows the team.

## Locked physical front-matter order

1. TITLE / modern Detective Academy dossier-evidence-board direction
2. PUBLICATION RECORD
3. THE BLACK ENVELOPE — no squad art, no YOUR SQUAD heading, no Happy Makers dialogue
4. YOUR SQUAD — approved squad image, Academy/team introduction and first general COMMS
5. CLAIM YOUR RECRUIT CREDENTIAL
6. WHAT YOU ARE ABOUT TO WALK INTO
7. HOW EVERY CASE WORKS
8. MAP CASES — READ THIS ONCE
9. YOUR CASE WALL + HINT VAULT
10. CASE INDEX

Renderer-side semantic reordering of these pages is prohibited.

## Production factory source changes

Repository:
`riseshineevolve-source/RISE.SHINE.EVOLVE`

Branch:
`feature/detective-book-factory`

Changes persisted:
- canonical content snapshot synced to blob `8685f8e561d0bfb3837445b72b4d6f799a9a48f2`;
- front-text contract now binds Page 4 to `## YOUR SQUAD`;
- source verifier now fails closed on Page 3/Page 4 order, owner website/Facebook CTA and general squad opener;
- premium renderer no longer adds the global upper-left micro-grid;
- Page 3 no longer hydrates squad art;
- Page 4 owns the squad image;
- Happy Makers COMMS uses a white readable copy field with a narrow evidence-grid strip as decoration only;
- premium audit now fails if Page 3 contains YOUR SQUAD, leaks the Academy explanation, or loses WILL YOU CLAIM IT, and if Page 4 loses the squad opener.

Key production commits in this bounded correction sequence:
- content sync: `6f9aed19db11ab2d27febc14e9d35d17af578295`
- front contract: `1c1f6bd5ab98f5ffcfbafa6c89c67340e7f04301`
- source verifier: `4f9ff0f242ce42c807e944e680b43f51a898607b`
- verifier syntax repair: `3ff3f52cccb08a1ac2790b810f56ba038b152637`
- opening + COMMS renderer: `41d202ad51b85a7656249f707cd9a49159dd047a`
- premium audit regression guard: `73216edde86c0e59c3e8a10dac8867bf249e1aea`
- Page 4 two-column squad layout: `83a3d9c1b738688a0bae716832a5f70127271c65`

## Owner-review proof made in chat

A bounded 180-page review PDF was produced from the latest uploaded 2026-09-29 180-page owner-review artifact:
`HMDA_Book1_EN_OWNER_FRONTMATTER_LOCK_2026-09-30.pdf`

It includes:
- rebuilt Pages 1–4 with the owner-directed order/copy;
- the modern monochrome detective/evidence-board Page 1 direction;
- Page 2 publication layout with exact new copy;
- standalone Page 3 black-envelope cold open;
- Page 4 squad image + general opening dialogue;
- removal of the upper-left micro-grid from the remaining pages;
- conversion of the 35 existing black-grid COMMS panels into readable light panels with a narrow grid motif only at the side.

Local PDF preflight: 180 pages, openable, unencrypted.

This review PDF is an owner-review proof, not release authority. The source-backed production factory must still rebuild the exact book from its private locked assets and run its full audit.

## State / gate

**FRONT-MATTER REGRESSION FOUND AND SOURCE-FIXED / PREVIEWER GATE REOPENED / EN NOT FROZEN**

The 2026-09-29 “advance to KDP Previewer” statement is superseded by this checkpoint because that artifact still contained the front-matter assembly regression.

Next safe sequence:
1. wait for branch CI / exact source checks;
2. rebuild from the corrected source in the production environment with the locked private assets;
3. run full reader-copy + spatial + visual audit;
4. KDP Previewer/preflight;
5. representative physical proof;
6. explicit owner EN freeze;
7. only then publication / PL handoff.

Do not broadly rewrite the story or puzzle mechanics during this pass.
