# Golden Test Output 001: Project Unstoppable Hero

Source: current production screenshot supplied by the user on 2026-09-18.
Locale: pl-PL
Audience: teenagers + parents browsing teen product page
Profile: RSE web / teen / gaming
Status: PASS for language calibration, pending in-browser surface-fit check

## Locked approach

This calibration intentionally uses natural Polish teen-facing gaming language without chasing short-lived slang. It preserves the playful game metaphor while avoiding literal translationese and generic self-help wording.

### PU-HERO-001
**SOURCE**
Stop Playing on Hard Mode. Level Up Your Mindset in 31 Days.

**SEMANTIC INTENT**
A bold gaming-metaphor headline: stop making life feel unnecessarily difficult and improve the way you think/approach challenges over a 31-day experience.

**IMMUTABLES**
- 31 days
- gaming metaphor
- mindset / way of thinking is the thing being improved
- no guaranteed psychological outcome

**FINAL PL**
Nie graj ciągle na hardzie. W 31 dni wbij wyższy level myślenia.

**WHY**
Natural Polish gaming register, compact enough for a hero, keeps the two-part punch and avoids stiff `tryb trudny` or coaching-style `rozwiń swój mindset`.

**QA**
Meaning: PASS
Natural Polish: PASS
Teen register: PASS
Humor/gaming function: PASS
Surface: CHECK IN BROWSER

---

### PU-HERO-002
**SOURCE**
COMING SOON ON GOOGLE PLAY

**FINAL PL**
JUŻ WKRÓTCE W GOOGLE PLAY

**QA**
PASS

---

### PU-HERO-003
**SOURCE**
Welcome to Project Unstoppable. A 31-day mobile experience built like a video game to help teens hack their focus, translate 'parent logic', block the haters, and unlock their inner Legend.

**SEMANTIC INTENT**
Introduce a 31-day mobile experience structured like a game. It is intended to help teens with focus, interpreting parent logic, handling haters and building a stronger sense of personal agency/confidence. Tone is playful and game-native.

**IMMUTABLES**
- Project Unstoppable brand name
- 31 days
- mobile experience
- video-game structure
- intended to help, not guarantee outcomes
- four functions: focus, parent logic, haters, inner Legend

**FINAL PL**
Witaj w Project Unstoppable. To 31-dniowa mobilna przygoda zbudowana jak gra, która ma pomóc nastolatkom ogarnąć skupienie, rozszyfrować „logikę rodziców”, zablokować hejterów i odblokować tryb Legendy.

**WHY**
- `mobilna przygoda` reads more naturally than literal `mobilne doświadczenie`
- `ma pomóc` preserves claim strength
- `ogarnąć skupienie` keeps the hack-your-focus informality without a calque
- `rozszyfrować „logikę rodziców”` recreates the joke instead of translating mechanically
- `zablokować hejterów` keeps the social/game metaphor
- `tryb Legendy` recreates the branded unlock metaphor without the AI-like phrase `wewnętrzna Legenda`

**QA**
Meaning fidelity: PASS
Claim strength: PASS
Natural Polish: PASS
Cultural fit: PASS
Teen audience: PASS
Gaming voice: PASS
Logic: PASS
Polish correctness: PASS
Surface: CHECK IN BROWSER

---

### PU-HERO-004
**SOURCE ALT**
Project Unstoppable app cover

**FINAL PL ALT**
Okładka aplikacji Project Unstoppable

**QA**
PASS

---

## Provisional terminology created by this fixture

- hardzie: accepted for this teen gaming profile, lowercase in running copy unless visual design requires a display treatment
- level: accepted in teen gaming copy where the metaphor is intentional
- „logika rodziców”: accepted recurring joke candidate
- tryb Legendy: PROVISIONAL recurring branded term, lock only after recurrence and surface review

## Rejected literal/AI-sounding directions

- `Przestań grać w trybie trudnym`
- `Rozwiń swój sposób myślenia w 31 dni`
- `31-dniowe mobilne doświadczenie`
- `zhakuj swoje skupienie`
- `odblokuj swoją wewnętrzną Legendę`
- generic motivational filler not present in the source

## Next verification

1. Render the Polish hero in the actual responsive layout.
2. Check headline wrapping on desktop and mobile.
3. Check CTA width.
4. Compare `tryb Legendy` against later recurring uses of Legend/Legend Mode before glossary-locking.
5. If the page contains `The Ultimate Cheat Codes for Real Life`, calibrate it in the same batch to keep the gaming lexicon coherent.
