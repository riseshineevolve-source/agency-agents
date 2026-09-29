# World 01 Level 1 — published source vs structured app derivative

Date: 2026-09-30

The published World 01 paperback, SHA-256
`adf9d384985ec7ad0fb1d7f9f6c3d46189592a171474c38ee93ac35bb808c549`,
is the authority for product copy. The `spark-joy-fam` file
`src/data/storyContent.ts` was inspected read-only through GitHub at blob
`377463e1853743f82d4d3bca5ce89b6e5b05b210`. Its structure is useful
comparison evidence, but its copy is not a source for the graph.

The 26 printed content blocks on PDF pages 15–22 are represented in
`world01-level1-page-evidence.json` and the generated Level 1 pack. The
following nine concrete derivative divergences were found:

| # | Printed page/block | App derivative difference | Disposition |
|---|---|---|---|
| 1 | 15, opener | App adds `subtitle: Learning to shake off heavy school energy`. | Excluded; no printed subtitle. |
| 2 | 16, `p16_b01` | One printed system-log box with two paragraphs is split into two app dialogue records. | One graph node, preserving the printed box. |
| 3 | 18, `p18_b01` | App omits `Alio stopped crying about his nose. Nini froze with her jacket half-on.` | Restored as its own source-proven system-log node. |
| 4 | 18, `p18_b02` | One printed Mimi bubble with two paragraphs is split into two app dialogue records. | One graph node, preserving both paragraphs. |
| 5 | 19, `p19_b03`–`p19_b04` | App places Mimi's `10 minutes of calm...` before the printed log about Mimi placing cushions; the paperback has the log first. | Graph follows printed visual order. |
| 6 | 20, `p20_b03` | App adds a `glitch.inStory` sentence about the kids exploding; no such sentence is in the printed third console file. | Excluded. |
| 7 | 22, `p22_b02` | App `secretCode.code` omits the printed curly quotation marks around `DECOMPRESSION MODE`. | Printed marks retained in source copy. |
| 8 | 22, `p22_b02` | App `parentSays` omits the printed trailing apostrophe after `Stop fighting!`. | Printed punctuation retained, even though asymmetrical. |
| 9 | 22, `p22_b02` | App `teachToSay` omits the printed enclosing apostrophes. | Printed punctuation retained. |

Other app prose fields located within the Level 1 pages match the corresponding
published wording after accounting for those block splits and punctuation.
The app also omits many printed UI headings and labels because its data shape
does not model them; the source graph includes those printed fields. This is a
content comparison, not a scientific accuracy review or a license to adopt
app-only wording.
