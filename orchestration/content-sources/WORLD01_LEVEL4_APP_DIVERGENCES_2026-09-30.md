# World 01 Level 4 — published source vs structured app derivative

Date: 2026-09-30

The published paperback identified by SHA-256
`adf9d384985ec7ad0fb1d7f9f6c3d46189592a171474c38ee93ac35bb808c549`
is the sole authority for copy and visual reading order. The read-only
`spark-joy-fam/src/data/storyContent.ts` comparison source was Git blob
`377463e1853743f82d4d3bca5ce89b6e5b05b210`. No app-only copy enters the graph.

| Printed page | App divergence | Source-graph disposition |
|---|---|---|
| 42 | App adds subtitle `Turning boredom into adventure`. | Excluded; no printed subtitle. |
| 43 | App merges `Dilo rolled onto his side.` with `Luli didn't look up from her book.` and moves the merged log before Luli's line. | Two separate printed system logs retained in their visual positions. |
| 45 | App omits `Dilo sat up straighter.` from the invisible-ink log. | Full printed log retained. |
| 45 | App abridges Alio's bubble to `Drop it! Drop it! Dilo said books are carnivorous!`, dropping the printed action and ant/giant-monster sentence. | Full printed Alio bubble retained. |
| 46 | App omits the printed system logs around Dilo's look, Alio peeking over the sofa, and Luli slamming her book shut. | All three printed logs retained. |
| 47 | App places the laboratory system log and Dilo's lemon-juice line before Alio/Luli; print orders Alio -> Luli -> lab log -> Dilo. | Printed visual order retained. |
| 47 | App flattens `ITEM ACQUIRED` into a generic system-log record and does not model `// FILE: INVENTORY`. | Preserved as the source-derived `inventory` node type; no reward/game semantics inferred. |
| 48 | App changes the printed hyphen in `reading wasn't boring - it was a mission` to an em dash. | Printed hyphen retained. |
| 50 | App strips the printed curly quotation marks around `SPY GEAR OFFLINE` and the enclosing training-line quotation marks. | Printed punctuation retained. |

The derivative remains useful as structural comparison evidence only. It cannot
certify source text, speaker boundaries, printed order, or the semantics of the
new inventory block.
