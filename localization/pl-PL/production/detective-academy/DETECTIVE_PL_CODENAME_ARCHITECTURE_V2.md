# Detective Academy PL — Codename Architecture V2

Date: 2026-10-08
Status: **OWNER-DIRECTION / ACTIVE FOR PL PRODUCTION**
Locale: pl-PL
Supersedes: `DETECTIVE_PL_CODENAME_ARCHITECTURE_V1.md`

## Owner direction

Polish codenames must sit at the intersection of:
- modern gamer usernames / handles;
- Polish scout / field-call-sign culture;
- spy / detective atmosphere;
- nickname-like forms that can behave naturally in prose.

Do **not** make the whole system English.
Do **not** make the whole system a list of objects.
Do **not** fall back to stock spy-book names such as `Sokół / Lis / Orzeł / Cień`.

The target should feel like names children could plausibly choose for themselves in an Academy, game lobby or team chat.

## Reader-facing system

Use:

**KRYPTONIM OPERACYJNY**

On dossier / clue cards:
- **KRYPTONIM**
- **SIATKA KONTAKTÓW**
- **KONTAKT**

The child credential keeps:

**TWÓJ KRYPTONIM OPERACYJNY: ______________________________**

## Naming architecture

The full bank deliberately mixes three families.

### A. Nickname-like / username-like

These should sound almost like names and work naturally inside a sentence:

- **KODA**
- **RUNI**
- **LUMO**
- **ZEFI**
- **TAVI**
- **RIKO**
- **NERI**
- **MAVI**
- **KIRO**
- **SAVI**
- **NOXI**
- **VEXA**
- **NEXO**
- **KIVI**
- **RILO**
- **PIKSI**
- **MIGI**
- **LUMA**

Use these when a case contains a lot of narrative prose and an object-like tag would sound stiff.

### B. Modern Polish gamer-tags

Use sparingly but visibly so the Academy has contemporary digital energy:

- **PIKSEL**
- **GLICZ**
- **PING**
- **KLIK**
- **RESET**
- **KURSOR**
- **PĘTLA**
- **SKRÓT**
- **KIKS**
- **MIGOT**

These are intentionally readable in Polish and should not be mechanically translated back to English.

### C. Field / scout / operational tags

These carry the outdoor-investigation / Academy layer without relying on stale animal codenames:

- **AZYMUT**
- **ZWIAD**
- **RYSA**
- **SPLOT**
- **TROP**
- **ISKRA**
- **ECHO**
- **SZLAK**
- **PUNKT**
- **ZWROT**

Use fewer of these than the nickname-like family so the book does not sound like a list of nouns.

## Balance rule

Across the whole book, aim approximately for:
- 50% nickname-like handles;
- 25% modern gamer-tags;
- 25% field / scout / operational tags.

No single case should contain six names from the same family.

The finished book should feel like one Academy culture, not three separate naming systems.

## Modernity rules

A strong codename should:
- usually be 4–10 characters;
- usually have 2–3 syllables when spoken;
- be easy for a Polish 8–12 reader to pronounce;
- look clean on a badge, map or chat card;
- sound natural when another character says it aloud;
- remain memorable without digits or decorative punctuation.

Avoid:
- random numbers;
- `xX...Xx`;
- leetspeak;
- hard-to-pronounce English spellings;
- fantasy-class names;
- obvious "cool" clichés;
- tags that reveal a character's role in the current puzzle.

## Logic firewall

A Polish codename is display-only.

Before assignment, audit whether the English identity participates in:
- initials;
- acrostics;
- word length;
- alphabetic ordering;
- codes/passwords;
- first/last-letter mechanisms;
- repeated callbacks;
- baked-in visual labels;
- solution explanations.

If yes, the codename must preserve the needed mechanic or remain source-locked.

Immutable:
- case ID;
- character identity ID;
- portrait ID;
- gender where source logic uses it;
- coordinate;
- room/zone;
- clue proposition;
- answer identity;
- callback identity.

## Grammar rule

Prefer codenames that can be used naturally:

`Koda była w rzędzie 3.`
`Runi stał przy wejściu.`
`Piksel znajdowała się w Galerii.`

Where a form sounds awkward, use dossier syntax instead:

`KRYPTONIM: AZYMUT`
`Kontakt o kryptonimie AZYMUT...`

Do not force artificial declension.

## Happy Makers

Happy Makers always keep their names as primary identity.

Codenames are secondary Academy badges only:
`MIMI // KRYPTONIM: ...`

They may be used on:
- squad dossier;
- credential/badge surfaces;
- occasional comms jokes;
- special Academy moments.

Normal narrative remains Mimi / Luli / Dilo / Nini / Alio / Bibi.

### Happy Makers — provisional V2 direction

Do not lock these until the whole-book codename audit is complete.

- **MIMI // KODA** — short, controlled, sounds like a real handle; does not over-explain her role.
- **LULI // RYSA** — she notices the place where a story or claim stops fitting.
- **DILO // PING** — tech, testing, response, systems.
- **NINI // PIKSI** — nickname-like, small-detail energy without making her childish.
- **ALIO // SKRÓT** — routes, shortcuts and the recurring acronym joke.
- **BIBI // NERI** — name-like and understated; avoids turning her into "the archive lady" through her codename.

These remain **PROVISIONAL**.

## Approved banter

### Dialogue A — second codename

- **ALIO:** Mogę wybrać sobie drugi kryptonim?
- **LULI:** Nie.
- **ALIO:** A awaryjny?
- **LULI:** Nadal nie.
- **DILO:** A wersję testową?
- **LULI:** Przestaję odpowiadać.

### Dialogue B — the acronym problem

- **ALIO:** Mam pełny kryptonim: **Perfekcyjnie Ukryty Profesjonalny Agent.**
- **LULI:** Nie.
- **ALIO:** To może chociaż skrót?
- **LULI:** Alio... wiesz, jaki z tego będzie skrót?
- **ALIO:** Jasne. P... U... P...
- **ALIO:** ...o nie.
- **DILO:** Za późno. Już wszyscy zapamiętali.

Use each joke once and never inside logic-bearing clue text.

## Production sequence

1. Audit all 30 cases + Hint Vault + Solution Files for identity-dependent mechanics.
2. Build `DETECTIVE_PL_IDENTITY_CODENAME_MAP_V1.yml`.
3. Assign codenames across the whole book using the balance rule.
4. Run duplicate / pronunciation / grammar / accidental-clue review.
5. Freeze the map.
6. Only then apply witness/contact codenames consistently to story, clues, maps, hints and solutions.

Individual weak codenames may be replaced later without reopening puzzle logic, provided immutable identity bindings remain unchanged.
