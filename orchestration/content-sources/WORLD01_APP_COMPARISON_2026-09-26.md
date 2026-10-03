# World 01 structured app vs published paperback — 2026-09-26

## Deterministic text triage

The read-only app source was `spark-joy-fam/src/data/storyContent.ts` (Git blob `377463e1853743f82d4d3bca5ce89b6e5b05b210`). `scripts/compare-world01-derivative.py` extracts the first three World 01 sections and searches each app string field within that mission's PDF pages. It lowercases, applies NFKD, and removes punctuation/whitespace for **same-page lexical triage only**. This intentionally cannot certify punctuation, speaker, order, omissions, or scientific accuracy. Reproduction requires a read-only local copy of the app file and the private PDF; neither binary is committed.

| Mission | Published pages | App fields found by extraction | Not found by extraction | Visual/disposition |
|---|---:|---:|---|---|
| 1 — The After-School Crash | 15–22 | 40/42 | App subtitle; `glitch.inStory` sentence | Subtitle is app-only; the extra glitch sentence was not located on the published console page 20. Only opener fields enter the pack. |
| 2 — The Ice Cream Tragedy | 23–32 | 43/46 | App subtitle; two scene strings | Both scene strings are visible on page 26 but PDF extraction splits/reorders them. App speaker metadata diverges from the published page. Only opener fields enter the pack. |
| 3 — The Invisible XP | 33–41 | 37/40 | App subtitle; two merged scene strings | Pages 36–37 show intervening logs and a different split; app merges separate published utterances/logs. Only opener fields enter the pack. |

Total lexical triage: 120/128 fields found (93.75%) under the lossy normalization. This is **not** a source-parity percentage. A text string's presence does not validate the app's speaker or scene structure.

## Published-supported and app-matching content

PDF pages 15, 23, and 33 visually confirm the first three title/key/objective triples. The app's `title`, `key`, and `missionObjective` agree for levels 1 and 2. The Level 3 objective is substantively the same but the PDF prints a hyphen (`'broken' - it`) where the app uses an em dash. The pack uses the PDF punctuation. The first three app `subtitle` values are not printed on their mission opener pages and are excluded.

Many narrative, console, quest, and secret-code strings also appear in the corresponding PDF page ranges. They remain comparison evidence only. A complete mission requires visual transcription and scene-level verification before its text or speaker assignments can enter a canonical pack.

## Confirmed divergence and review queue

- **Level 2, PDF page 26:** `But Dilo looked so professional!` is spoken by **ALIO** in the paperback and assigned to `nini` in the app. `Dilo! Stop it! Ants don't mutate...` is spoken by **NINI** in the paperback and assigned to `luli` in the app. This is a concrete reason not to promote the app's dialogue records wholesale.
- **Level 3, PDF pages 36–37:** the app has a single Mimi line beginning `Who said anything about an hour?` and continuing into `Let's make a deal...`; the paperback separates these with `Mimi tapped his nose.` The app also merges `She picked up a cleat and tossed it to him. Dilo caught it.` while the paperback separates those logs around further dialogue. The app omits the intervening `Dilo stood up.` log visible on page 37.
- **Level 1, PDF page 20:** the app's `glitch.inStory` sentence was not found in the published console section. Treat it as app-only pending a full page audit.
- The first three app subtitles are app-only descriptions unless another published page is specifically identified. They are not canonical opener copy.

## Reusable structure, separate from product copy

The app's `StoryContent` grouping, `StoryDialogue` speaker/system-log model, `NeuroConsole` sections, `Quest` sections, `SecretCode` structure, and mission lookup/list concepts are useful runtime/content-model inputs. Their **shape** can inform future language-neutral IDs and UI behavior. Their text, labels, speaker IDs, scientific claims, and progression semantics need source-specific review. The pilot uses only `world01_mission_001_overview` through `world01_mission_003_overview` as language-neutral overview activity IDs.
