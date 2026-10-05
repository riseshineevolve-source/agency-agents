# Gentle Steps PL V03 — MIĘDZY NAMI Final QA

Date: 2026-10-05  
Status: PASS  
Baseline candidate blob: `de78cedd27fdfffe18f4a92a02f03a1187d7d16c`  
Post-review working master blob: `e6befddb4af6196e19658ee513ec116ecc16b492`

## Scope

All 24 MIĘDZY NAMI sections were reviewed under:
- Polish Family Ear;
- Polish Natural Language;
- Polish Book Register;
- Polish Logic;
- anti-cringe / age 8–12;
- repetition / function distribution;
- comment precision.

KEEP won on 20/24 sections.

Changed exactly:
- D08.MIĘDZY NAMI
- D10.MIĘDZY NAMI
- D18.MIĘDZY NAMI
- D21.MIĘDZY NAMI

## Final fixes

### D08
Prompt retained. Only the forced close was replaced.

New Mimi line:
**Nie każda trudna rzecz robi dużo hałasu.**

Reason: direct, grounded, no need to manufacture a joke around a vulnerable answer.

### D10
Old task asked the family to manufacture a "family slogan".

New task:
**ZDANIE, KTÓRE U NAS WRACA**

It asks the family to notice a phrase that genuinely recurs at home rather than inventing identity on command.

New Luli line:
**„Gdzie są klucze?” ma tę przewagę nad mottem, że naprawdę wraca.**

### D18
Old task directed praise around the circle: "Na ciebie mogę liczyć, kiedy…"

New task:
**Z CZYM MOŻNA DO MNIE PRZYJŚĆ?**

Each person names one concrete thing they genuinely like helping with. This preserves family knowledge/support while reducing pressure to evaluate another person.

New Nini line:
**„Ze wszystkim” brzmi odważnie. Za chwilę ktoś przyniesie ci drukarkę.**

### D21
Old task asked the family to invent a special sign, which could feel workshop-like.

New task:
**CO U NAS WIADOMO BEZ SŁÓW?**

The family notices nonverbal signals that already exist naturally at home.

New Luli line:
**Jedno spojrzenie przy ostatnim kawałku pizzy potrafi mieć całkiem precyzyjną treść.**

## Regression result

Exact changed-set check:
PASS — 4/4 allowed segments changed, 0 unscoped drift.

All other:
- 24 ZWOLNIJ;
- 24 GRAMY;
- remaining 20 MIĘDZY NAMI;
- preamble;
- day headers;
- back matter

remain identical to the baseline candidate for this slice.

## Verdict

MIĘDZY NAMI layer is ready for the next owner-read candidate.
No further broad rewrite is recommended.
