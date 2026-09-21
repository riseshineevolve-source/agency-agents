# RSE Content Recovery Queue

Last updated: 2026-09-18

This queue asks only for assets that materially improve continuity, translation, future app reuse or publication control. Do not re-upload assets already recovered.

## Already recovered - do not resend

### The Confident, Mindful & Happy Me Adventure

Recovered current source set:
- `Paperback  final fixed print.pdf` - 244-page published English print interior master.
- `Paperback_final_fixed_extracted_text.docx` - clean extracted-text working source for localization, always cross-checked against the PDF.
- `Paperback cover final.pdf` - paperback cover master.
- `the  confident HARDCOVER BOOK COVER(1).pdf` - hardcover cover master.
- `ebook the confident ostateczny druk rgb_KC OSTATECZNY.kcb` - small Kindle Create project descriptor.
- `ebook the confident ostateczny druk rgb OSTATECZNY(1).kpf` - recovered full Kindle package, about 239 MB, containing `book.kcb` plus the Kindle Create `resources` payload.

The full KPF now covers the previously missing Kindle resources dependency. Do not spend time hunting the old sibling `resources` directory unless there is a reason to recover a different historical edition.

### Level Up Your Brain - World 01

Recovered current source set:
- `Paperback 10 STORIES WORLD 01 FINAL standard.pdf` - 108-page print master with parseable text.
- earlier flattened 108-page variant preserved as publication evidence.
- `cover ebook(1).jpg` - ebook/front-cover artwork.
- `ebook 10 STORIES WORLD 01 FINAL_KC.kcb` - Kindle Create project descriptor.

World 01 no longer needs an urgent text recovery because the standard PDF is parseable. A clean editable manuscript or KPF/EPUB remains useful only if it is easy to find.

### Level Up Your Brain - World 02

Recovered current source set:
- `paperback 10 STORIES WORLD 02 FINAL standard(1).pdf` - 104-page print master.
- `ebook 10 STORIES WORLD 02 FINAL standard(1).pdf` - distinct 104-page ebook PDF master.
- `world02_full_text_extracted(1).doc` - full extracted-text working source, suitable for localization/content extraction when cross-checked against final pages.
- `COVER PAPERBACK world 02 FUN STories(1).pdf` - recovered cover candidate/prior-final file.
- `COVER WORLD 02 NEW final(1).pdf` - recovered newer-named cover candidate.
- `LEVEL UP YOUR BRAIN COVER WORLD 02(1).jpg` - front-cover image.

Paperback ISBN recovered from the print master: `9798249971823`.

Two distinct PDF cover files are preserved. Do not spend time choosing between them now; canonical full-wrap cover selection remains an owner gate until the strongest publication evidence is checked.

If convenient later, useful remaining World 02 material is only:
- Kindle Create KCB + its sibling `resources` folder, or KPF/EPUB export,
- editable source if there is a stronger source than the extracted DOC,
- KDP listing metadata / ASIN.

### Level Up Your Brain interactive derivative

Repository identified: `riseshineevolve-source/spark-joy-fam`.

This is not an unrelated generic Lovable prototype. Its `src/data/storyContent.ts` explicitly says the full story content, neuro-coaching console, secret codes and family missions were extracted from The Happy Makers World 01 and World 02 books. It already contains structured `StoryContent`, dialogue, Neuro Console, Quest and Secret Code data for an interactive adaptation.

Keep it in Wave 2 for engineering-budget purposes, but preserve its product relationship now. When promoted, compare its content against the recovered published book masters before rebuilding or localizing it.

### Grandma Bibi / word-search Gift

Grandma Bibi is NOT treated as a missing published book master.

Recovered product intent from the owner:
- Grandma Bibi was a Gift/learning experience intended to teach month names.
- substantial earlier work existed but is considered low-level and needs a future redesign/rebuild rather than publication as-is.
- the RSE word-search capability is part of this concept.

Reusable engine identified: `riseshineevolve-source/word-search-puzzle`.

Verified current engine already supports:
- `Months of a year` with January through December,
- additional days/numbers/custom word sets,
- Square, Circle, Hexagon, Diamond and Heart grids,
- Easy, Medium and Hard difficulty,
- interactive finding + hints,
- printable/PDF puzzle and answer versions.

Do not discard this engine. Treat it as reusable prototype infrastructure for a future Grandma Bibi-themed learning experience. The exact Grandma Bibi-branded source/art/copy package is still worth recovering only if it appears naturally while browsing old folders; do not conduct a broad archaeological search now.

### Detective / Optical / technical workstreams

Already recovered:
- Detective current Shigai checkpoint/PDF plus Book Factory source stack.
- Optical Animals source-manager manifest/scripts plus current Book Creator branch.
- Senior and Mind Bloom technical handoffs already recovered from Library/GitHub.

## 24 Gentle Steps to Christmas — recovered print master

Priority: RECOVERED / CURRENT SUPPORT

Recovered on 2026-09-17 after the earlier mistaken Happy Me upload:
- `24 Gentle Paperback ok.pdf` — published 104-page English paperback interior used as the current calibration/source reference.
- `24 Gentle Steps to Christmas COVER HARDCOVER.pdf` — hardcover cover reference.

Canonical product name is `24 Gentle Steps to Christmas`. Do not let generic `Christmas Family Book` or the historical Happy Me / `Gentle Steps to New Year` naming override it.

Verified product framing from the recovered cover:
- family Advent / Christmas journey,
- approximately 10 minutes a day,
- three recurring mini-rituals: `Mindful Moment`, `Fun Spark`, `Family Connection`.

The Polish Localization Engine already uses this source as a second calibration corpus in PR #6.

Still useful if found later, but no longer launch-blocking for source recovery:
- ebook/KPF/EPUB master,
- editable source,
- final paperback wrap if distinct from the recovered hardcover cover,
- KDP listing metadata / identifiers.

Do not search broadly for these unless they appear naturally; the critical missing-master state is closed.

## Medium-priority future app / book assets

Recover only if they exist as clearly final/current versions:
- Project Unstoppable canonical content/source package beyond the preserved app repository,
- other published RSE book masters not represented in the current product ledger,
- final audiobook/script assets if they are intended for future product reuse,
- authoritative character/universe bibles used across multiple products,
- Grandma Bibi-specific art/copy/prototype assets if encountered without a broad search.

## Optical Animals

Do not resend historical candidate batches.

Only useful new input is:
- a newly owner-approved replacement for one of the eight unresolved canonical slots,
- or a final local snapshot/listing of `01_FINAL_20_SOURCE` after promotions.

## Detective Academy

No broad recovery upload is needed now.

Only send a local asset if it is newer than the recovered checkpoint/manifest or if it contains a visual standard / map asset that never reached GitHub/Library.

## Senior / Hello Today

No broad recovery upload needed. Current implementation is under the Central RSE Orchestrator. Continue from the active GitHub branch/PR/checkpoints; do not depend on the lost Senior chat for recovery.

## Mind Bloom

No broad recovery upload needed. Continue in its dedicated execution chat; the Central RSE Orchestrator only synchronizes milestones, blockers and shared dependencies.

## Marketing Autopilot

No broad recovery upload needed from the central chat. Marketing continues in its dedicated execution chat; central orchestration only synchronizes milestones, blockers and shared dependencies.

## Opinie

DO NOT upload real case files, names, archive opinions, evidence, embeddings, reconstruction outputs or confidential material to ChatGPT/GitHub for recovery.

Only sanitized code/config/synthetic fixtures may be moved remotely.

## Preferred handoff method

Best: one folder or ZIP per still-missing product, preserving original filenames. Do not spend time renaming everything first.

If the source already lives in connected Google Drive, a folder share/reference is preferable to manually uploading dozens of files one-by-one. The recovery process can then inventory candidates and identify the strongest master before anything is promoted.
