# Gentle Steps — published-page fit risk and reconstruction specification

**Gate: OPEN.** These are measurements of the published English PDF, not a Polish template render. No English or Polish page here is a validated target text frame. All 104 pages were rendered and visually inspected; no genuine editable 104-page production template was found in the searched local Advent Calendar project.

## Production-surface investigation

- Canonical PDF: 104 pages, 621 × 810 pt = 8.625 × 11.25 in MediaBox/TrimBox; SHA-256 `1F79EDD316F353963EF33BB980843B37F367A0BACB9198BD63E0D221CB8C9BA7`. The file is the published visual reference and has no reliable text layer. The 8.625 × 11.25 measurement suggests a bleed-sized sheet around 8.5 × 11 in, but the final KDP trim and bleed settings must be confirmed from production settings.
- Local Advent Calendar folder search covered `.docx`, `.docm`, `.indd`, `.idml`, `.afpub`, `.pptx`, `.psd`, `.ai`, `.svg`, `.html` filenames. No matching design-native source was located. Several large Word files are editable content/early layouts. Read-only Word page-statistics checks: `HappyMakers_Advent_Final_Polished.docx` **69**, `Magical_Edition` **79**, `Ultimate` **71**, `Cranberry_Final` **74**, `Polish_Edition` **74**, `Ultimate_Edition` **69**, `Premium_With_Photos` **70**, `Spread v2` **68** pages; all tested at 612 × 792 pt (8.5 × 11 in). A read-only PDF export of Final_Polished confirmed that it is 69 pages. None reproduces the published 104-page geometry/page count, so none proves print fit.
- Shortest unblock: supply the editable project used to produce `24 Gentle Paperback ok.pdf` (for example the Canva/InDesign/Affinity source with linked assets/fonts), or authorize reconstruction in a specified production application with the exact KDP trim/bleed settings and original fonts/assets. Then place this master into a working copy, export all pages, inspect at actual trim, and record a page-by-page PASS/FIX.

## Deterministic reconstruction constraints

1. Preserve 104-page source order, including blank pp. 4, 18 and 96, the four week dividers, 72 separate activity pages, and three letter pages. Preserve the four role tiers on each activity page: day/ritual heading, italic tagline, instruction block, named character note.
2. Begin from the observed 621 × 810 pt published PDF canvas. Confirm whether this is 8.5 × 11 in trim plus 0.125 in bleed on each outer dimension before setting live text areas. Do not treat a dark-pixel envelope as a safe text box.
3. Use source typography, image/gradient background and ornaments from an authorized editable source where available. Keep body type readable and character notes distinct. Do not shrink body text or cut meaning to force fit; resolve long Polish headings with controlled line breaks/spacing and review.
4. Export a proof PDF from the real source. Compare all 104 pages at 100% and print size, check diacritics and embedded fonts, no clipped words/ornaments, intact role hierarchy, bleed/safe margins, page order and images. Record line wraps, overflow, clipping and final owner signoff.

## Page-level measured envelopes and risk

Dark-ink envelopes below are approximate `(left, top, right, bottom)` in PDF points from a 100 dpi render with mean RGB < 110. They include ornaments and illustrations and **are not text-frame boundaries**. `PL chars` measures the activity-page candidate including heading/note; longer copy is a triage signal only. Front/closing text spans multiple pages and cannot be allocated to exact page frames without the actual template.

| PDF p. | Published role | Approx. dark-ink envelope (pt) | PL chars | Fit / editorial risk |
| ---: | --- | --- | ---: | --- |
| 1 | Title | 129, 75, 484, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 2 | Copyright/legal | 141, 359, 470, 719 | — | HIGH: edition ISBN/legal metadata owner gate |
| 3 | Dedication | 101, 75, 525, 719 | — | Open: render and inspect |
| 4 | Blank | — | — | Blank; preserve |
| 5 | Happy-Makers intro | 91, 75, 528, 720 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 6 | Happy-Makers intro | 91, 75, 528, 720 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 7 | Nini profile | 91, 75, 528, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 8 | Alio profile | 91, 75, 528, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 9 | Dilo profile | 91, 75, 528, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 10 | Luli profile | 91, 75, 528, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 11 | Mimi profile | 91, 75, 528, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 12 | Journey | 117, 74, 507, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 13 | Journey | 131, 74, 491, 720 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 14 | How it works | 86, 74, 524, 720 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 15 | How it works | 96, 74, 523, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 16 | How it works | 102, 74, 514, 720 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 17 | How it works | 96, 74, 525, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 18 | Blank | — | — | Blank; preserve |
| 19 | 24-day entry | 95, 74, 541, 720 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 20 | Week 1 divider | 95, 84, 541, 720 | — | Divider typography; check single-page fit |
| 21 | D01 Spokojna chwila — Shared Silence | 94, 84, 522, 719 | 372 | Open: render and inspect |
| 22 | D01 Iskra zabawy — The Compliment Toss | 104, 84, 516, 727 | 586 | Elevated: expansion/headings; inspect wraps |
| 23 | D01 Chwila bliskości — One True Word | 119, 84, 500, 719 | 262 | Open: render and inspect |
| 24 | D02 Spokojna chwila — Gentle Breath Flow | 94, 84, 521, 718 | 362 | Open: render and inspect |
| 25 | D02 Iskra zabawy — Family Sound Symphony | 93, 84, 527, 718 | 634 | Elevated: expansion/headings; inspect wraps |
| 26 | D02 Chwila bliskości — What I Love About Being Us | 91, 84, 523, 718 | 386 | Open: render and inspect |
| 27 | D03 Spokojna chwila — Still Hands | 106, 84, 520, 718 | 420 | Open: render and inspect |
| 28 | D03 Iskra zabawy — Freeze Family | 90, 84, 531, 718 | 498 | Elevated: expansion/headings; inspect wraps |
| 29 | D03 Chwila bliskości — My Favorite Moment Today | 100, 84, 518, 718 | 399 | Open: render and inspect |
| 30 | D04 Spokojna chwila — Flame Focus | 105, 84, 509, 729 | 421 | HIGH: real flame option; adult line needs owner safety/fit review |
| 31 | D04 Iskra zabawy — Echo Wave | 104, 84, 520, 718 | 780 | HIGH: long Polish page; inspect wraps |
| 32 | D04 Chwila bliskości — The Color of My **[printed heading ends here]** | 90, 84, 522, 718 | 310 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 33 | D05 Spokojna chwila — Listening to Quiet | 115, 84, 499, 718 | 354 | Open: render and inspect |
| 34 | D05 Iskra zabawy — Human Clock | 87, 84, 531, 718 | 819 | HIGH: long Polish page; inspect wraps |
| 35 | D05 Chwila bliskości — The Sound I Love at Home | 128, 84, 494, 718 | 389 | Open: render and inspect |
| 36 | D06 Spokojna chwila — Breathing Circle | 120, 84, 499, 718 | 411 | Open: render and inspect |
| 37 | D06 Iskra zabawy — Family Balance Flow | 91, 84, 529, 718 | 813 | HIGH: long Polish page; inspect wraps |
| 38 | D06 Chwila bliskości — A Word of Calm | 116, 84, 499, 718 | 403 | Open: render and inspect |
| 39 | D07 Spokojna chwila — Weight of Peace | 102, 84, 518, 718 | 403 | Open: render and inspect |
| 40 | D07 Iskra zabawy — Rolling Smile | 90, 84, 530, 718 | 754 | HIGH: long Polish page; inspect wraps |
| 41 | D07 Chwila bliskości — The Quiet Hero | 117, 84, 498, 719 | 369 | Open: render and inspect |
| 42 | Week 2 divider | 95, 84, 541, 718 | — | Divider typography; check single-page fit |
| 43 | D08 Spokojna chwila — Heart Touch | 139, 84, 474, 719 | 337 | Open: render and inspect |
| 44 | D08 Iskra zabawy — One-Word Story Remix | 112, 84, 512, 719 | 570 | Elevated: expansion/headings; inspect wraps |
| 45 | D08 Chwila bliskości — One Thank You That Matters | 124, 84, 499, 719 | 474 | Elevated: expansion/headings; inspect wraps |
| 46 | D09 Spokojna chwila — Warm Light Breath | 109, 84, 509, 718 | 385 | Open: render and inspect |
| 47 | D09 Iskra zabawy — The Human Knot | 101, 84, 520, 721 | 649 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 48 | D09 Chwila bliskości — Tiny Family Blessings | 129, 91, 486, 718 | 286 | Open: render and inspect |
| 49 | D10 Spokojna chwila — Inner River | 124, 84, 492, 719 | 300 | Open: render and inspect |
| 50 | D10 Iskra zabawy — The Family Machine | 92, 84, 527, 719 | 575 | Elevated: expansion/headings; inspect wraps |
| 51 | D10 Chwila bliskości — Our Family Motto | 105, 84, 509, 719 | 328 | Open: render and inspect |
| 52 | D11 Spokojna chwila — Inner Smile | 130, 84, 484, 719 | 318 | Open: render and inspect |
| 53 | D11 Iskra zabawy — The Weird Command | 125, 84, 494, 719 | 689 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 54 | D11 Chwila bliskości — Our Family Superpower | 141, 84, 477, 719 | 315 | Open: render and inspect |
| 55 | D12 Spokojna chwila — Gratitude Glance | 120, 84, 494, 719 | 356 | Open: render and inspect |
| 56 | D12 Iskra zabawy — The Five-Word Limited Truth | 88, 84, 532, 719 | 766 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 57 | D12 Chwila bliskości — Kindness in Our Circle | 127, 84, 507, 726 | 441 | Open: render and inspect |
| 58 | D13 Spokojna chwila — Slow Motion | 127, 84, 488, 719 | 357 | Open: render and inspect |
| 59 | D13 Iskra zabawy — The Gate of Kindness | 117, 84, 507, 719 | 507 | Elevated: expansion/headings; inspect wraps |
| 60 | D13 Chwila bliskości — Family Treasure Map | 114, 84, 501, 719 | 364 | Open: render and inspect |
| 61 | D14 Spokojna chwila — Palm Warmth | 112, 84, 509, 719 | 410 | Open: render and inspect |
| 62 | D14 Iskra zabawy — The Rhythm Race | 107, 84, 512, 726 | 526 | Elevated: expansion/headings; inspect wraps |
| 63 | D14 Chwila bliskości — Circle of Appreciation | 125, 84, 494, 719 | 313 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 64 | Week 3 divider | 95, 84, 541, 619 | — | Divider typography; check single-page fit |
| 65 | D15 Spokojna chwila — Breathing Wave | 114, 84, 502, 719 | 343 | Open: render and inspect |
| 66 | D15 Iskra zabawy — Dancing Movement Chain | 92, 84, 526, 719 | 445 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 67 | D15 Chwila bliskości — A Joyful Flashback | 102, 84, 513, 719 | 301 | Open: render and inspect |
| 68 | D16 Spokojna chwila — Floating Hands | 130, 84, 485, 719 | 353 | Open: render and inspect |
| 69 | D16 Iskra zabawy — Family Orchestra | 106, 84, 518, 719 | 704 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 70 | D16 Chwila bliskości — Secret Dreams | 112, 84, 511, 719 | 294 | Open: render and inspect |
| 71 | D17 Spokojna chwila — Gentle Stretch | 109, 84, 506, 719 | 318 | Open: render and inspect |
| 72 | D17 Iskra zabawy — Follow the Funny Leader | 114, 84, 502, 719 | 582 | Elevated: expansion/headings; inspect wraps |
| 73 | D17 Chwila bliskości — One Thing That Makes me Feel Alive | 101, 84, 514, 719 | 239 | Open: render and inspect |
| 74 | D18 Spokojna chwila — Ripple Breath | 128, 84, 491, 719 | 342 | Open: render and inspect |
| 75 | D18 Iskra zabawy — Trust Web | 91, 84, 530, 719 | 803 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 76 | D18 Chwila bliskości — The Compliment Circle | 133, 84, 485, 719 | 300 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 77 | D19 Spokojna chwila — Light Between | 113, 84, 507, 719 | 400 | Open: render and inspect |
| 78 | D19 Iskra zabawy — Shape Switch | 94, 84, 525, 719 | 695 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 79 | D19 Chwila bliskości — The Happiness Echo | 106, 84, 512, 719 | 354 | Open: render and inspect |
| 80 | D20 Spokojna chwila — Face of Calm | 99, 84, 530, 719 | 323 | Open: render and inspect |
| 81 | D20 Iskra zabawy — The Tunnel of Cheers | 86, 84, 530, 719 | 537 | Elevated: expansion/headings; inspect wraps |
| 82 | D20 Chwila bliskości — Remember When Round | 114, 84, 504, 723 | 335 | Open: render and inspect |
| 83 | D21 Spokojna chwila — Joyful Stillness | 123, 84, 496, 719 | 331 | Open: render and inspect |
| 84 | D21 Iskra zabawy — Energy Ripple | 68, 84, 553, 719 | 845 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 85 | D21 Chwila bliskości — Symbol of Love & Gratitude | 87, 84, 530, 719 | 458 | Elevated: expansion/headings; inspect wraps |
| 86 | Week 4 divider | 95, 84, 541, 619 | — | Divider typography; check single-page fit |
| 87 | D22 Spokojna chwila — Light Within | 134, 84, 480, 719 | 313 | Open: render and inspect |
| 88 | D22 Iskra zabawy — The Family Values Line-Up | 87, 84, 534, 719 | 1050 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 89 | D22 Chwila bliskości — Lesson of the Month | 140, 84, 479, 719 | 396 | Open: render and inspect |
| 90 | D23 Spokojna chwila — Silent Snow-Globe | 87, 84, 526, 719 | 325 | Open: render and inspect |
| 91 | D23 Iskra zabawy — Know-Me Switch | 88, 84, 532, 719 | 1086 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 92 | D23 Chwila bliskości — I Am Sorry | 109, 84, 509, 719 | 392 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 93 | D24 Spokojna chwila — Circle of Light | 109, 84, 509, 719 | 603 | HIGH: source issue, safety or dense mechanics; inspect individually |
| 94 | D24 Iskra zabawy — Christmas Family Singing Moment | 132, 84, 493, 726 | 457 | Elevated: expansion/headings; inspect wraps |
| 95 | D24 Chwila bliskości — Circle of Gratitude & Wishes | 104, 84, 530, 719 | 561 | Elevated: expansion/headings; inspect wraps |
| 96 | Blank | — | — | Blank; preserve |
| 97 | Merry Christmas | 130, 84, 490, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 98 | Reflections | 107, 74, 507, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 99 | Family promise | 104, 74, 515, 717 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 100 | Family promise | 100, 74, 520, 717 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 101 | Blessing | 130, 74, 492, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 102 | Letter | 96, 73, 517, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 103 | Letter | 103, 73, 522, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |
| 104 | Letter | 133, 73, 486, 719 | — | HIGH: multi-page/source hierarchy or designed panel; full reflow |

## Priority headings / designed surfaces

- Week 1: p. 32 has a truncated printed English heading; the accepted Polish completion must be approved in context. Other long activity headings and notes need actual line-break checks.
- Week 2: pp. 47, 56 and 63 have source mechanics/continuation issues. Page 56 uses an exact-five-word rule with a longer printed example.
- Week 3: pp. 66, 69, 75, 76, 78 and 84 have source/physical-feasibility or safety issues documented in the source map and checkpoint.
- Week 4: p. 88 is exceptionally dense (six prompts, two-person variant, movement legend), p. 91 has three rounds/examples, p. 92 contains a sensitive apology prompt, and pp. 93–95 contain long closing copy.
- Front/end: pp. 1, 5–17, 19 and 97–104 have designed typography/panels; p. 2 has edition metadata. Keep the three-page letter structure, final maxim panel and closing signature.

**Verdict:** full Polish language copy is ready for editorial/owner review; genuine-template fit and print approval are OPEN.
