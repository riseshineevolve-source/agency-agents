# RSE Content Source Policy

Status: proposed operating standard
Last updated: 2026-09-17

Purpose: make RSE books, ebooks, future app content and localization reusable without turning GitHub into a binary archive, leaking unpublished IP, or forcing agents to rediscover content from old chats.

## Core decision

RSE books and ebooks are part of the product source graph and SHOULD be registered as durable project sources for:

- future Android/app adaptation,
- Polish and later localization,
- derivative activity books / companion apps,
- product/entity consistency,
- AI discovery metadata,
- future sequels and content reuse.

But the published PDF/EPUB binary is not automatically the best Git source.

## Source layers

### 1. Master binary archive

Keep final customer/publication binaries in a private durable file store such as the connected Library / Drive / local master archive.

Examples:
- final print PDF,
- EPUB,
- KPF export,
- cover PDF/JPG,
- final paperback/hardcover interior,
- source-package ZIP where the editable source is binary-heavy.

These files are canonical publication artifacts but normally should NOT be committed to an ordinary Git repository because they are large, opaque diffs and can bloat history.

If a binary truly needs Git versioning, use a private repository with Git LFS. Do not place unpublished or proprietary KDP masters in a public repository.

### 2. Git-managed content source

For every book that may feed localization or future apps, Git should contain a compact, reviewable source package:

- `BOOK_MANIFEST.yml` or JSON,
- canonical title and aliases,
- language / edition / publication state,
- ISBN / ASIN only when verified,
- source master filename + checksum,
- chapter/page/mission structure,
- extracted plain text or Markdown when rights/source allow it,
- glossary / recurring labels / character names,
- product claims and age/audience metadata,
- localization status,
- app-reuse status,
- pointers to artwork/audio assets,
- legal / licensing notes where relevant,
- transformation history.

This is the preferred machine-readable source for agents, translation and app adaptation.

### 3. Project derivative packages

A future app should not scrape a PDF at build time.

Instead, an explicit derivative package should be generated from the registered book source, for example:

`content-derived/happy-me-app/en/...`

or

`content-derived/world-01-app/en/...`

The derivative package should contain only the content actually needed by that app, with provenance back to the source book/edition.

### 4. Localization packages

Localization should work from stable, extracted structured source, not repeatedly OCR/read the visual PDF.

Recommended flow:

master artifact -> verified extraction -> semantic segmentation -> localization package -> Polish Engine -> bilingual QA -> localized master.

The original page/PDF remains available as visual/layout evidence, but text translation is anchored to the structured source once verified.

## Repository privacy rule

`riseshineevolve-source/agency-agents` is not the place for full proprietary book text or unpublished masters.

It may contain:
- orchestration,
- policies,
- schemas,
- manifests without sensitive unpublished content,
- localization-engine rules,
- checksums / references.

Full book text/source packages should live only in a PRIVATE content/code repository or another owner-controlled private source store.

Until a dedicated private content repository exists, do not dump full book binaries or full proprietary text into public GitHub merely to make them discoverable.

## Suggested future private repository shape

Target concept: `rse-content-source` (private; creation is an owner/infrastructure action when tooling permits).

```text
books/
  confident-happy-me/
    en/published-2026/
      BOOK_MANIFEST.yml
      text/
      glossary.yml
      app-reuse.yml
      localization.yml
  level-up-world-01/
    en/published-2026/
      ...
  level-up-world-02/
    ...
  gentle-steps-christmas/
    ...
  grandma-bibi/
    ...
apps/
  ... derivative manifests/pointers only
schemas/
  book-manifest.schema.json
  localization-package.schema.json
```

Large final PDFs/EPUBs remain outside ordinary Git unless deliberately stored through private Git LFS.

## Minimum recovery bundle per KDP / ebook product

When recovering a product from local folders, preserve the strongest available version of:

1. final print interior PDF,
2. final ebook EPUB/KPF if one exists,
3. editable source if available (DOCX/Canva export/InDesign/Affinity/Scrivener/etc.),
4. final cover files,
5. KDP metadata export / listing copy / categories / keywords if available,
6. verified ISBN / ASIN / edition identifiers,
7. any final character/glossary/style source,
8. companion assets that may be reused by apps,
9. publication date/version note,
10. source checksum.

Do not upload passwords, Amazon credentials, payment data or private customer/account exports.

## Translation rule

A published English master may be used as a frozen semantic reference.

Once text extraction is verified, the structured extraction becomes the working translation source while the PDF remains the visual/layout authority.

Translation must preserve:
- recurring terminology,
- character identity,
- mission/section hierarchy,
- claims and safety meaning,
- jokes by function rather than wording,
- cross-book universe consistency.

The Polish Localization Engine owns language quality. The book/project manifest owns product facts and source provenance.

## Future-app rule

A book becomes `APP_REUSE_READY` only when:

- its source edition is identified,
- reusable text/activities are structured,
- asset rights are known,
- child/parent surface boundaries are explicit,
- content provenance is preserved,
- app adaptation does not silently change the book's pedagogical/safety claims.

This is a preparation state, not a commitment to build an app.

## Do not do

- do not put all KDP PDFs into a public repo,
- do not treat OCR from a random export as canonical when an editable source exists,
- do not overwrite published English masters during translation,
- do not make future apps read raw PDFs at runtime,
- do not fork the same book text into multiple untracked app copies,
- do not invent ISBN/ASIN/publication metadata,
- do not delete superseded editions until the canonical edition is proven and linked.
