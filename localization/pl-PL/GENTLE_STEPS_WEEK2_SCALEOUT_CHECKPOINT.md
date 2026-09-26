# 24 Gentle Steps to Christmas — Week 2 scale-out checkpoint

- Date: 2026-09-26
- Branch: codex/gentle-steps-week2-scaleout
- Status: **bounded language candidate complete; publication/promotion blocked**

## Source and scope

- Canonical source actually used: the owner-attached published English paperback, **24 Gentle Paperback ok.pdf** (104 PDF pages; SHA-256 **1F79EDD316F353963EF33BB980843B37F367A0BACB9198BD63E0D221CB8C9BA7**).
- The PDF has no extractable text layer. Source fidelity was checked from rendered page images.
- Translated **Days 8–14 only**, PDF pages **43–63**, with three complete daily activities per day: 21 headings, 21 taglines, 21 instruction blocks and 21 character notes.
- PDF page 42 is the Week 2 divider and is outside this bounded daily candidate.
- Candidate: [gentle-steps-christmas-week2-bounded-candidate.md](golden-tests/gentle-steps-christmas-week2-bounded-candidate.md).
- The Week 1 candidate and all shared localization-engine, terminology and regression files remain untouched.

## QA disposition

| Gate | Result | Evidence / limit |
| --- | --- | --- |
| Source fidelity | PASS for mapped text | Pages 43–63 reviewed one by one; ages/order, counts, directions, two-person variants, metaphors and notes checked in the candidate's day matrix. Published-source defects remain below. |
| Natural Polish | PASS as a language candidate | Family-facing instructions revised for Polish cadence; no gender slashes or generic AI filler; the Day 12 example is exactly five Polish words. |
| Character voice | PASS as a language candidate | Nini, Alio, Dilo, Luli and Mimi retain distinct note functions and humor. |
| Claim / safety | PASS as a language candidate | Imagined light, river, smile and warmth stay metaphors; no new medical or guaranteed wellbeing claims. Willingness is explicit for physical touch. |
| Designed surface | **BLOCK for publication** | No editable real-template Polish render exists for Week 2 pages; the four accepted Week 1 long headings still lack their required real-template evidence. |
| Product mechanics | **REVIEW REQUIRED before publication** | The published English source contains the four editorial/mechanical issues listed below. |

## Published-source issues for the product owner

1. **Day 9, PDF p. 47:** the knot requires two different non-neighbor hand partners. The source gives a two-person variant but no workable rule for some three-/four-person groups. The candidate preserves the published wording and flags the gap.
2. **Day 12, PDF p. 56:** the starter depends on a second/middle name. The candidate preserves it. A fallback for families without second names needs a product decision.
3. **Day 12, PDF p. 56:** the instruction requires exactly five words, while the printed English Harry Potter example uses more. The Polish sample was rebuilt to five standalone words with three true clues and two absurd zmyłki.
4. **Day 14, PDF p. 63:** the activity is called a circle but only directs the first person to speak to the person on the left. The candidate does not invent a continuation.

These are source/editorial decisions. **No shared terminology or localization-engine change is requested.** The three ritual labels stay provisional until genuine layout and product-wide recurrence review.

## Real-template handoff

The Week 1 fit gate remains **NOT YET PASS**. Its exact accepted headings on PDF pages **25, 26, 35 and 38** need placement and print-scale review on the genuine editable/rendering surface, with unchanged body font size and leading. A proxy or character-count estimate cannot close that gate.

For Week 2, place **all 21** candidate activity pages in that same genuine template. First inspect the long headings on Days 9, 11, 12 and 13 named in the candidate, then verify every page for clipping, collisions, Polish diacritics, readable hierarchy, body copy and character notes. Do not shorten meaning or shrink body text to rescue fit.

## Scope and next bounded segment

This checkpoint authorizes no full-book completion claim and no merge to main. The next reasonable translation batch is **Days 15–21**, after verifying exact day boundaries in the same published PDF. Keep it a separate language candidate with the same page-by-page bilingual, Polish, voice, claim/safety and real-template checks. Do not promote this batch or the Week 1 candidate to print-ready status until the named gates have evidence.
