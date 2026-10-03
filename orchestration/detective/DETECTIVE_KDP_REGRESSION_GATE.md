# Detective Academy — KDP Regression Gate
Date: 2026-10-02
Status: REQUIRED BEFORE OWNER KDP UPLOAD

## Purpose

Prevent the recurring regressions that caused repeated rework during Detective Academy production.

No full-book candidate may be called KDP-ready until every gate below passes.

## G0 — Source authority

PASS only if:
- reader copy derives from current V3/WOW canonical source;
- owner corrections are recorded in current Detective locks/checkpoints;
- no historical V4/V4.1/stale raster silently overrides current source;
- Case 02+ stays unchanged while First18 is under active owner review.

## G1 — Character identity

Required exact identity set:
- Mimi
- Luli
- Dilo
- Alio
- Nini
- Grandma Bibi

Checks:
- no duplicate character standing in for another;
- Dilo != Alio visually;
- correct portrait/name pairing;
- same approved portrait identity reused in squad pages and HM Comms;
- Grandma Bibi visibly older;
- no generated lookalike introduced into a final page.

FAIL if any page uses an approximate substitute where an approved asset exists.

## G2 — Logo / brand mark

Canonical interior mark:
- scanner-question-mark symbol.

FAIL if:
- shield/laurel/crest substitute appears;
- generic magnifying-glass logo replaces the canonical mark;
- an old Detective Academy mark reappears.

## G3 — Typography / readability

At real print size:
- no body text below approved comfort threshold;
- HM Comms must be comfortably readable;
- map keys and coordinate labels must read instantly;
- room labels must not touch borders;
- no line of text may be clipped or covered by decorative art;
- handwriting fields must be large enough for a child.

Any automatic fit that solves overflow by shrinking text is FAIL.

Reflow/add a page instead.

## G4 — Page-family duplication

FAIL if:
- a case has a generic duplicate Evidence Grid / intro page with no unique reader content;
- Objective/Rules are printed twice;
- “Tick each statement...” or equivalent instruction is duplicated;
- parity filler appears as a reader-facing pseudo-page.

## G5 — Case structure

Every case must contain:
- Case Title;
- What Happened;
- Objective;
- Rules;
- HM Comms;
- required evidence/puzzle surface;
- Verdict/Response.

HM Comms may move to a separate page when needed.

No required section may disappear to preserve page count.

## G6 — Spatial-case spread

For spatial cases:
02,04,06,07,10,12,13,15,17,19,20,22,23,25,29

PASS only if:
- full Witness Board exists;
- full Live Case Map exists;
- board/map clue content matches source;
- map geometry matches locked source;
- witness names match solution truth;
- verdict fields exist only where intended.

Preferred physical layout:
Witness Board LEFT / verso;
Map RIGHT / recto.

If pagination requires correction, insert a meaningful designed interlude/parity solution; do not compress board + map onto one page.

## G7 — Map visual lock

Every spatial map must pass:
- white / clean cool-gray surface;
- no beige/dirty gray;
- large bold row/column coordinates;
- thick black walls;
- clear door gaps;
- single room label per room/zone;
- room label centered and not covering critical usable cells;
- modern recognizable props;
- prop footprint preserved;
- high-contrast MAP KEY;
- wall symbol in MAP KEY visually identical to actual wall style;
- usable/blocked state unambiguous;
- generous verdict writing space.

Puzzle invariants:
- grid dimensions unchanged;
- walls/doors unchanged;
- room membership unchanged;
- blocked/usable cells unchanged;
- clue-relevant props unchanged;
- answer unchanged.

## G8 — Witness Board visual lock

PASS only if:
- modern digital investigation / dossier UI;
- no corkboard/post-it aesthetic;
- no school worksheet feel;
- large witness names;
- readable clue cards;
- all canonical witnesses present;
- no clue omitted;
- no verdict field duplicated from map page;
- no decorative slogan competing with facts.

## G9 — Special-case locks

### Case 03
- exact owner Photo A/B;
- exact 10 differences;
- identical scale;
- 10-question-mark tracker;
- no “one difference matters later” spoiler;
- Case 06 is first payoff.

### Case 05
- exactly six symbols;
- BALL → STAR → BOLT → HEART → KEY → MOON;
- large six-slot answer area.

### Case 21
- complete reconstructed message preserved.

### Case 26
- extraction set excludes Case 01;
- 14 maps only;
- output = CHECK THE OLD MAP.

### Case 28
- Rule Zero truth unchanged.

### Case 29
- owner map visual anchor;
- access coordinate preserved.

### Case 30
- four final fields derive from earlier work;
- Room Zero explanation complete;
- Bibi route-note reveal;
- D3;
- Archive File 001;
- triangle callback.

## G10 — Page references

All references are generated from final manifest/pagination.

FAIL if stale references survive:
- Standard Map Rules old page number;
- Case Wall old page number;
- Hint Vault old page number;
- any case says a page number that no longer contains the referenced surface.

## G11 — Back matter

Hint Vault:
- 3 levels × 30 cases;
- upright;
- preserved content.

Solutions:
- 30 cases;
- upright;
- current ritual preserved:
  FINAL CALL / WHY THIS FITS / DETECTIVE TAKEAWAY / HAPPY MAKER NOTE;
- spatial solution maps use readable names/direct placements rather than tiny lookup numbers where current lock requires it.

If pages 121–180 are frozen, render comparison target = 0 changed pages unless an explicit defect is approved.

## G12 — PDF print/preflight

PASS only if:
- correct trim/page size throughout;
- fonts embedded;
- no encryption;
- no accidental page rotation;
- no unexpected blank pages;
- no transparency/layer issue that violates current KDP print requirements;
- grayscale output is clean;
- no low-resolution critical raster below production threshold;
- bleed/margins follow final KDP contract.

## G13 — Visual inspection set

Mandatory rendered inspection at real-print scale:
- all opening/front-matter pages;
- Case 01;
- all 15 Witness Boards;
- all 15 Live Case Maps;
- Case 03;
- Case 05;
- Case 16;
- Case 21;
- Case 26;
- Case 27;
- Case 28;
- Case 29;
- Case 30 / Room Zero;
- Field Certification;
- Archive File 001 / Book 2 hook;
- representative Hint Vault and Solution pages.

## G14 — Content locks

Must detect / preserve:
- QUILL / MORSE / PIP / KNOX where applicable;
- 017/071 payoff;
- exact-ten Case 03;
- six-symbol Case 05;
- Case 21 message;
- CHECK THE OLD MAP;
- Rule Zero;
- D3;
- Bibi reveal;
- Archive File 001;
- triangle callback.

## Release states

Use only:
- DRAFT
- OWNER REVIEW
- KDP PREVIEWER CANDIDATE
- PHYSICAL PROOF CANDIDATE
- EN FROZEN

Never label a file “KDP READY” solely because deterministic checks passed.

Required release order:
1. all gates PASS;
2. owner visual review;
3. KDP Previewer;
4. representative physical proof;
5. explicit owner EN freeze;
6. publication.
