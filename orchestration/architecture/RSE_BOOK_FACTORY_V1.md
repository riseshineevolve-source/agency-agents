# RSE Book Factory v1

Status: CANONICAL ARCHITECTURE
Date: 2026-10-03
Owner: Central RSE Technical Orchestrator
Primary objective: turn approved book pages + canonical structured content into repeatable KDP-ready English/Polish books without re-generating pages manually.

## 1. Core decision

RSE book production becomes a deterministic publishing system.

AI is NOT the page renderer.

AI may:
- help normalize source content into structured data;
- suggest copy in explicitly editable fields;
- audit screenshots/PDFs;
- create decorative art assets when owner-approved.

AI must NOT:
- invent page copy during render;
- invent or substitute characters;
- change coordinates, witness facts, puzzle truth, map geometry, page numbering, logo, or locked brand elements;
- recreate approved pages from scratch when a frozen asset already exists.

The renderer must produce the same output from the same inputs every time.

## 2. Recommended stack

Primary renderer:
- Node.js + TypeScript
- React components for page templates
- CSS for fixed-layout typography/layout
- SVG for maps, diagrams, borders, icons and line art
- Playwright/Chromium for deterministic PDF export

QA / preflight:
- Python + PyMuPDF for page/image/DPI checks
- pdfinfo / pdffonts / qpdf where available
- pixel/screenshot regression for approved golden pages
- JSON Schema validation for content
- deterministic puzzle/map validation scripts

CI:
- GitHub Actions builds EN and PL outputs from the same template engine.

Optional external assistants:
- Codex Pro = primary implementation/coding agent
- ChatGPT/RSE = source-of-truth orchestration, owner feedback reconciliation, content/schema decisions
- Claude/Gemini = optional independent visual/editorial QA only; they are not render authorities
- Colab = portable emergency runner / batch proof environment, not source of truth

## 3. Repo shape

Create a dedicated repository:
`riseshineevolve-source/rse-book-factory`

Recommended structure:

```
rse-book-factory/
  AGENTS.md
  PROJECT_BRIEF.md
  CHECKPOINT.yml
  package.json
  tsconfig.json

  src/
    renderer/
      renderBook.ts
      renderPage.ts
      pdf.ts
    components/
      PageFrame.tsx
      Header.tsx
      CaseIntro.tsx
      HMComms.tsx
      WitnessBoard.tsx
      LiveMap.tsx
      VerdictBox.tsx
      CaseWall.tsx
      HintPage.tsx
      SolutionPage.tsx
      ProfilePage.tsx
      IndexPage.tsx
      DividerPage.tsx
    templates/
      frontmatter/
      cases/
      puzzles/
      backmatter/
    maps/
      MapRenderer.tsx
      mapSchema.ts
      props/
    qa/
      layout.ts
      sourceLocks.ts
      puzzleTruth.ts
      references.ts
      regression.ts

  books/
    detective-academy/
      book.yml
      design/
        tokens.yml
        typography.yml
        character-lock.yml
        icon-lock.yml
        page-types.yml
      content/
        en/
          frontmatter.yml
          cases/
            case-01.yml
            ...
            case-30.yml
          hints.yml
          solutions.yml
        pl/
          frontmatter.yml
          cases/
            case-01.yml
            ...
            case-30.yml
          hints.yml
          solutions.yml
      assets/
        frozen-pages/
          en/
            p001.png
            ...
            p020.png
        characters/
        logos/
        decorative/
        maps/
        props/
      goldens/
        contact-sheets/
        approved-page-renders/
      build/
        en/
        pl/

    gentle-steps/
      ...
```

## 4. First release strategy — do not rebuild approved pages

For Detective Academy:
- owner-approved PNG pages 1–20 are imported as FROZEN page assets;
- if they meet print-resolution requirements, they are placed 1:1 in the first release PDF;
- do not reconstruct them in code before publication unless a defect forces a targeted repair.

This means the Book Factory can ship before every approved frontmatter page is recreated as vector HTML.

The template engine begins with Case 01 and is used to create Cases 02–30.

Later, if desired, frozen raster pages can be migrated to vector templates without changing the production contract.

## 5. Fixed-layout page model

Each rendered page is an explicit fixed-size page component.

Book config defines:
- trim width/height;
- bleed;
- interior color mode;
- target DPI for raster art;
- safe margins;
- gutter policy;
- page numbering policy.

No automatic word-processor pagination.

Each page component receives structured data and renders to a fixed page surface.

## 6. Design tokens — one source of visual truth

`design/tokens.yml` controls:
- page background;
- cool-gray palette;
- black/white levels;
- line weights;
- corner treatment;
- borders;
- label bars;
- padding;
- gutters;
- speech bubble geometry;
- icon sizes;
- map key style;
- spacing scale.

`typography.yml` controls:
- exact font families already approved/licensed for production;
- title sizes;
- heading sizes;
- body sizes;
- caption sizes;
- line heights;
- minimum readable font size;
- PL language overrides where required.

No renderer component may hardcode its own unrelated typography.

## 7. Character identity lock

`character-lock.yml` maps:
- Mimi
- Luli
- Dilo
- Alio
- Nini
- Grandma Bibi

to exact approved assets.

HM Comms, squad pages and case pages reference IDs, never filenames selected ad hoc.

Example:
```yml
DILO:
  portrait: characters/dilo/portrait-approved.png
  full: characters/dilo/full-approved.png
ALIO:
  portrait: characters/alio/portrait-approved.png
  full: characters/alio/full-approved.png
```

Renderer fails if a required identity asset is missing.

## 8. Structured case schema

Every case is data, not a hand-built page.

Example:

```yml
id: 02
title: THE TROPHY THAT CAME BACK TOO EARLY
family: spatial
act: 1

what_happened: |
  ...

objective: |
  ...

rules:
  - ...
  - ...

comms:
  - order: 1
    speaker: ALIO
    text: ...
  - order: 2
    speaker: LULI
    text: ...

witnesses:
  - name: MAX
    clue: ...
  - name: ...

map:
  columns: [A,B,C,D,E,F]
  rows: [1,2,3,4,5,6]
  rooms: [...]
  walls: [...]
  doors: [...]
  props: [...]
  usable: [...]
  blocked: [...]

verdict:
  fields:
    - person
    - coordinate

case_wall:
  save: false
```

English and Polish use the same IDs and puzzle geometry.

Only language copy changes.

## 9. Case template families

### Spatial
- Case Intro
- optional standalone HM Comms if intro is full
- Witness Board LEFT
- Live Case Map + Verdict RIGHT

### Visual comparison
- Case Intro
- paired visual puzzle spread
- response tracker/verdict

### Code
- Case Intro
- code/evidence surface
- answer slots/verdict

### Timeline / timing
- Case Intro
- timeline evidence surface
- verdict

### Reconstruction
- Case Intro
- reconstruction surface
- verdict

### Meta / finale
- explicitly named custom template
- still built from deterministic components and canonical data

No case gets a generic duplicate “intro” page just because an old PDF had one.

## 10. Overflow policy — critical for Polish

Text never shrinks indefinitely.

Every component defines:
- preferred size;
- minimum size;
- maximum lines/height.

If content exceeds the approved area:
1. use an approved compact layout variant;
2. move HM Comms to the next page;
3. use a second evidence page if the source genuinely needs it;
4. only then flag OWNER REVIEW.

Never reduce body text below the print-readability floor.

This allows EN and PL to share a design system without forcing identical line breaks.

## 11. Map engine

Maps are programmatic SVG.

Map renderer owns:
- row/column axes;
- room boundaries;
- thick black walls;
- doorway gaps;
- room/zone labels;
- usable/blocked cells;
- modern prop placement;
- prop footprints;
- map key;
- verdict fields.

The same map data is used for:
- player map;
- solution map;
- validation.

Therefore a solution map cannot silently drift from the live puzzle.

Map theme for Detective:
- white / clean cool gray;
- no beige/dirty gray;
- no diagonal background pattern;
- black walls;
- labels centered on designated room-label lines;
- readable map key;
- modern recognizable props.

## 12. Witness Board engine

Witness Boards are deterministic digital-investigation UI pages.

Data:
- witness name;
- exact clue;
- optional small locked avatar/icon;
- optional evidence category if canonical.

No:
- corkboards;
- random decorative notes;
- slogans;
- duplicate verdict fields.

If 6 cards fit, use 6-card layout.
If 8 fit, use 8-card layout.
If text density exceeds threshold, switch to approved 2-page board variant rather than shrink type.

## 13. Frozen PNG handling

Approved PNG page requirements:
- verify pixel dimensions against trim/bleed at >=300 ppi;
- preserve aspect ratio;
- place without AI resampling/cropping unless owner approves;
- keep checksum in manifest.

Example manifest:
```yml
page: 7
mode: frozen-raster
file: assets/frozen-pages/en/p007.png
sha256: ...
status: FROZEN
```

A checksum change fails CI until explicitly accepted.

## 14. Build commands

Required CLI:

```
npm run build -- --book detective-academy --lang en
npm run build -- --book detective-academy --lang pl
npm run build:case -- --book detective-academy --lang en --case 02
npm run proof -- --book detective-academy --lang en
npm run contact-sheet -- --book detective-academy --lang en
npm run preflight -- --book detective-academy --lang en
```

Outputs:
- full PDF;
- per-page PNG proof;
- contact sheet;
- preflight JSON/MD;
- page manifest;
- failed checks.

## 15. Automated QA

### Layout
- text overflow;
- clipping;
- overlap;
- safe margin breach;
- font below minimum;
- room label collision;
- map-key collision;
- wrong page dimensions.

### Content
- missing required sections;
- duplicate section;
- missing witness;
- missing HM speaker;
- stale page reference;
- empty required field.

### Brand
- wrong logo asset;
- unknown character asset;
- unapproved icon;
- unapproved slogan.

### Puzzle truth
- coordinate validity;
- witness count;
- map dimensions;
- wall/door coordinates;
- solution uniqueness where a deterministic solver is available;
- solution map matches live map.

### PDF
- page count;
- dimensions;
- embedded fonts;
- no accidental rotation;
- no encryption;
- raster DPI;
- grayscale/colour contract.

## 16. Visual regression

Approved pages become golden snapshots.

For template pages:
- render PNG;
- compare against last owner-approved snapshot;
- show diff image when changed.

This prevents:
- Dilo/Alio substitution;
- logo drift;
- moved headers;
- lost margins;
- accidental font-size changes.

Visual regression is a safety net, not a license to accept incorrect content.

## 17. Human/AI QA roles

### RSE / ChatGPT
- resolve source conflicts;
- owner feedback;
- canonical copy;
- pagination decisions;
- final owner review packet.

### Codex Pro
- implement engine;
- parse structured data;
- write renderers/tests;
- run CI;
- fix deterministic failures.

### Claude / Gemini
Optional independent page-review pass:
- readability;
- visual balance;
- repeated visual problems;
- consistency across contact sheets.

Their output is advisory only.
They may not rewrite locked source automatically.

### Colab
- can run batch render/preflight from repo;
- useful when local machine setup is inconvenient;
- must pull the exact Git commit and produce build metadata.

## 18. GitHub Actions

On PR:
1. validate schemas;
2. render changed pages only;
3. run layout/content/puzzle tests;
4. create changed-page contact sheet;
5. attach PDF proof artifact.

On release tag:
1. render whole book;
2. run full preflight;
3. build EN/PL artifacts;
4. produce manifest/checksums.

## 19. Polish edition workflow

Do NOT duplicate the design project.

Polish book is:
- same templates;
- same asset IDs;
- same puzzle geometry;
- same maps;
- same page-family rules;
- different canonical text files;
- language-specific typography/overflow variants.

Flow:
EN TEMPLATE FREEZE
→ create PL content package
→ render PL
→ overflow report
→ targeted Polish layout variants
→ PL QA
→ PL PDF.

This is the core reason to build the factory.

## 20. Other books

Gentle Steps should reuse:
- renderer;
- design-token system;
- page manifest;
- localization;
- PDF/preflight;
- frozen-page system;
- contact-sheet/regression tooling.

It gets its own components/templates, not a second publishing engine.

Optical Animals should reuse:
- page manifest;
- raster/print preflight;
- page assembly;
- cover/interior build pipeline;
- KDP packaging.

## 21. Implementation lanes — max four

LANE A — Engine / Build
- repo skeleton;
- React/TS renderer;
- Playwright PDF;
- CLI.

LANE B — Detective content/schema
- normalize V3 + locks into EN YAML;
- page manifest;
- references.

LANE C — Detective templates
- Case Intro;
- HM Comms;
- Witness Board;
- Map + Verdict;
- remaining case-family components.

LANE D — QA / preflight
- schema;
- overflow;
- visual regression;
- puzzle/map checks;
- PDF checks.

Do not launch 280 parallel writers.
One canonical writer per file/surface.

## 22. Fastest path to publication

Phase 1:
- import approved Pages 1–20 as frozen PNGs;
- verify 300 ppi;
- build PDF assembly immediately.

Phase 2:
- build Case 01 template family;
- prove it by rendering Case 02 from structured data;
- owner checks ONE generated spatial case.

Phase 3:
- batch spatial cases;
- build special puzzle families;
- batch remaining cases.

Phase 4:
- import locked hints/solutions;
- preflight full EN book;
- owner/KDP/physical proof.

Phase 5:
- freeze EN template;
- feed canonical PL copy through the same engine.

## Definition of done

Book Factory v1 is done when:
- same Git commit renders the same PDF;
- no hand-placement is required for an ordinary case;
- Case 02–30 can be regenerated from YAML;
- PL can be generated by changing language data, not rebuilding pages;
- preflight catches regressions before owner review;
- one command produces PDF + contact sheet + QA report.
