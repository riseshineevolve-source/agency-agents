# Optical Halloween — brakująca piątka: opisy, dokładne prompty i wynik
Data: 2026-10-21, Europe/Warsaw.
Status: FIVE_FINAL_ART_CANDIDATES_QA_PASS. Etap generowania i technicznej kontroli pięciu ilustracji zakończony. Końcowa ocena estetyczna właścicielki pozostaje otwarta; to nie jest automatyczne zatwierdzenie rosteru20 ani certyfikacja druku.

## Zakres
Wyłącznie Optical Halloween Illustration Studio. Oficjalny bootstrap: orchestration/bootstrap/OPTICAL_HALLOWEEN_ILLUSTRATION_STUDIO_BOOTSTRAP.md.
Nadal istnieją trzy osobne światy: The House That Remembers, The Midnight Carnival Below the City, The Eclipse Museum of Lost Nights. Ten komplet domyka bieżącą brakującą piątkę, a nie rozpoczyna nowego świata.
Wszystkie15 zatwierdzonych źródłowych PNG ponownie sprawdzono względem MANIFEST_15.csv: bez zmian. Zachowano wszystkie wcześniejsze wersje pięciu kandydatów. Żadnych zmian w Optical Animals, maskach, tokenach, seek-and-find, paginacji, składzie czy KDP.

## Rzeczywisty zespół i wynik kontroli
- Visual Storyteller + Image Prompt Engineer: agent five_final_prompts opracował opisy, kompozycje i zabezpieczenia promptów.
- Brand Guardian: agent five_brand_final porównał wcześniejsze BEST oraz nową piątkę z zatwierdzoną piętnastką; wynik5/5 PASS do oceny właścicielki. Zalecane uproszczenie naczyń kelnera wykonane.
- Reality Checker + UI/Print Finish-Gate Reviewer: agent five_finish_final sprawdził każdą nową ilustrację. Wynik5/5 PASS w zakresie anatomii, kontaktów, głównej iluzji i istotnego kadrowania.
- Narzędzie generowania: built-in ImageGen, po jednej niezależnej generacji dla każdego obrazu. Użyto poprzedniej najmocniejszej wersji jako odniesienia. Nie podmieniono starego pliku.

## Pliki wynikowe — identyfikacja
Obrazy pokazano bezpośrednio w rozmowie i obejmuje je automatyczne zapisywanie wygenerowanych obrazów. Poniższe ścieżki służą identyfikacji sesji, nie są trwałymi linkami GitHub. Binarne PNG nie zostały przesłane do tego repozytorium.
Runtime root: /workspace/scratch/c4ccdc821df4/generated_images/

| ID | PNG | Rozmiar | SHA-256 |
| --- | --- | --- | --- |
| OH_FIVE_FRAME_CARRIER_v02 | exec-73f8b401-21d2-4226-85fc-52ad746eab99.png | 1103×1426 | fda37c4930efcbf96b57d39ed027078bf3f577cd914f486583491a4a600b75d0 |
| OH_FIVE_FALLING_SKELETON_v03 | exec-3d59827b-318a-40e6-b99a-0bb6b7cb8173.png | 1102×1427 | f1cd00083ed036f435daf86f94b4fa859c373028e68a0f3177dc4fcba87a3520 |
| OH_FIVE_PAINTER_LADDER_v04 | exec-afb6c4dc-0ce0-4813-ba54-f9071464b671.png | 1102×1427 | 4fb75dc3bcf0ecfe16ab7523380fb7d66b5d82d278374ec40176643c8dc72760 |
| OH_FIVE_FLYING_WAITER_v02 | exec-3e67e768-870a-419e-839b-3f23501ffd1d.png | 1102×1427 | 1d38b329ae7b15476c777cd083c32745c8c175d228494d119927155e0ed8f846 |
| OH_FIVE_CANDLE_QUEEN_v03 | exec-15ecfbcb-c009-4787-aa3c-089e23cffc28.png | 1102×1427 | ebf613f97b7e112c500fdd88ecb5255742ead87420ddc3eb06e8b0712eb60f8b |

## Opisy i dokładne prompty użyte do generowania
Prompty poniżej są zapisane w pełnym brzmieniu; opis polski jest krótkim opisem koncepcji, nie tekstem do umieszczenia na ilustracji.

### 1. Przenośny pokój
**ID:** OH_FIVE_FRAME_CARRIER_v02

**Opis:** Zamaskowany wędrowiec niesie ramę otwierającą się na prawdziwy, głęboki pokój. Schody i szerokie pasy peleryny łączą postać z niemożliwą architekturą.

**Źródłowa wersja odniesienia:** exec-3d54c88e-f034-4c4d-ba45-86febe1a7bab.png

**Dokładny prompt:**
```text
Use case: illustration-story. Produce ONE finished premium Optical Halloween coloring-book illustration, portrait aspect ratio 8.5:11. The supplied image is the previous BEST composition to refine faithfully; preserve its strong identity, camera, anatomy, spatial layout and optical idea. Gallery-quality pure solid black and clean white, bold precise contours with clear line-weight hierarchy, broad dimensional optical bands and generous large enclosed white areas for coloring. One dominant adult hero and one traceable optical paradox. Patterns follow anatomy and perspective. No gray shading, gradients, hatching, fuzzy texture, tiny decorative clutter, moon/stars, text, labels, signature, watermark or page border. Important anatomy and identifying objects stay comfortably inside page edges; never crop fingers, shoes, headwear or flames. Exactly two arms and two legs on any human-shaped hero, no extra figures or duplicated body parts. This is a final fidelity and linework polish, not a redesign; do not add props.

Retain tall white-masked traveler, black top hat, enormous broadly striped cape, diamond trousers and ONE rigid four-sided portal frame. Exactly two gloved hands grip opposite edges; two connected legs and boots rest on separate broad stair treads. Inside frame retain deep room in coherent perspective: ONE armchair, ONE side table with lamp, ONE plant, ONE striped ceiling pendant, tiled floor and distant doorway. Room is an open portable space, not a flat picture/mirror. Furniture stays separate from hands/body. Preserve asymmetrical hero silhouette, carefully joined frame corners and few large nested optical arch bands in background; no tiny duplicate travelers. Sharpen broad solid black contours and retain large clean white areas, avoid microdetails. All fingers, hat and boots fully visible.
```

### 2. Hotelowa otchłań
**ID:** OH_FIVE_FALLING_SKELETON_v03

**Opis:** Kościotrup w stroju hotelowego portiera spada przez pionowe atrium. Powiększona dłoń i podeszwa wychodzą ku widzowi, a balkony zbiegają się w głębokim wirze.

**Źródłowa wersja odniesienia:** exec-8eb590df-66d9-4f09-9fa4-361486643cdb.png

**Dokładny prompt:**
```text
Use case: illustration-story. Produce ONE finished premium Optical Halloween coloring-book illustration, portrait aspect ratio 8.5:11. The supplied image is the previous BEST composition to refine faithfully; preserve its strong identity, camera, anatomy, spatial layout and optical idea. Gallery-quality pure solid black and clean white, bold precise contours with clear line-weight hierarchy, broad dimensional optical bands and generous large enclosed white areas for coloring. One dominant adult hero and one traceable optical paradox. Patterns follow anatomy and perspective. No gray shading, gradients, hatching, fuzzy texture, tiny decorative clutter, moon/stars, text, labels, signature, watermark or page border. Important anatomy and identifying objects stay comfortably inside page edges; never crop fingers, shoes, headwear or flames. Exactly two arms and two legs on any human-shaped hero, no extra figures or duplicated body parts. This is a final fidelity and linework polish, not a redesign; do not add props.

Preserve extreme straight-down90degree view into cylindrical optical hotel atrium. ONE intact skeleton hotel bellboy unmistakably FALLS airborne; two naturally bent legs, two outstretched attached arms, expressive skull and pillbox cap. ENTIRE enlarged near skeletal hand with EXACTLY FIVE digits including thumb remains inside left margin, with at least4%page-width clear space; full foreshortened boot remains inside opposite margin. Maintain strong fall and intact joints, not a standing pose. Preserve white double-breasted uniform panels and broad black stripes, three major balcony rings receding into huge deep vortex below, simplified small distant geometry. Fine line cleanup only, no extra rings, luggage, tiny door numbers, detached bones or extra fingers.
```

### 3. Schody spod pędzla
**ID:** OH_FIVE_PAINTER_LADDER_v04

**Opis:** Malarz na drabinie prowadzi pędzel po ścianie. Szeroki ślad farby staje się przestrzennymi schodami przechodzącymi przez pustą ramę.

**Źródłowa wersja odniesienia:** exec-2fbe67b4-51f0-429e-bb3f-94ad31836fd0.png

**Dokładny prompt:**
```text
Use case: illustration-story. Produce ONE finished premium Optical Halloween coloring-book illustration, portrait aspect ratio 8.5:11. The supplied image is the previous BEST composition to refine faithfully; preserve its strong identity, camera, anatomy, spatial layout and optical idea. Gallery-quality pure solid black and clean white, bold precise contours with clear line-weight hierarchy, broad dimensional optical bands and generous large enclosed white areas for coloring. One dominant adult hero and one traceable optical paradox. Patterns follow anatomy and perspective. No gray shading, gradients, hatching, fuzzy texture, tiny decorative clutter, moon/stars, text, labels, signature, watermark or page border. Important anatomy and identifying objects stay comfortably inside page edges; never crop fingers, shoes, headwear or flames. Exactly two arms and two legs on any human-shaped hero, no extra figures or duplicated body parts. This is a final fidelity and linework polish, not a redesign; do not add props.

Preserve living adult painter, beret, white broadly striped overalls, rear three-quarter low camera and face in profile. EXACTLY TWO ARMS, retain their established pose: RIGHT arm raised with brush touching wall; LEFT arm descends along IMAGE-LEFT torso edge and hand clearly grips IMAGE-LEFT ladder rail beside hip. No arm or hand on right waist, no pocket hand; both shoulders/elbows/wrists traceable. Two connected legs, two boots supported on distinct rungs. Keep two ladder rails, coherent rungs and full ladder feet just inside bottom trim. Brushstroke becomes physical projecting black/white staircase going through one huge empty picture frame; preserve readable paint-to-depth transition. One hanging paint bucket. Refine dominant outer contours a little bolder, especially body and near ladder, without filling spacious white overalls or white wall fields. No extra decoration or new architecture.
```

### 4. Kelner między dwiema grawitacjami
**ID:** OH_FIVE_FLYING_WAITER_v02

**Opis:** Żywy kelner unosi się ku stołowi przymocowanemu do sufitu. Taca podlega jednej grawitacji, a odwrócona filiżanka i nakrycia stołu drugiej.

**Źródłowa wersja odniesienia:** exec-cfce288c-67a7-4129-a90c-10e9a4390fed.png

**Dokładny prompt:**
```text
Use case: illustration-story. Produce ONE finished premium Optical Halloween coloring-book illustration, portrait aspect ratio 8.5:11. The supplied image is the previous BEST composition to refine faithfully; preserve its strong identity, camera, anatomy, spatial layout and optical idea. Gallery-quality pure solid black and clean white, bold precise contours with clear line-weight hierarchy, broad dimensional optical bands and generous large enclosed white areas for coloring. One dominant adult hero and one traceable optical paradox. Patterns follow anatomy and perspective. No gray shading, gradients, hatching, fuzzy texture, tiny decorative clutter, moon/stars, text, labels, signature, watermark or page border. Important anatomy and identifying objects stay comfortably inside page edges; never crop fingers, shoes, headwear or flames. Exactly two arms and two legs on any human-shaped hero, no extra figures or duplicated body parts. This is a final fidelity and linework polish, not a redesign; do not add props.

Preserve expressive living adult human maître d', swept hair, airborne diagonal pose, two attached arms and two separated trailing legs with shoes not touching floor. Lower hand supports ONE tray with teapot and cup; upper hand serves ONE upside-down cup toward ceiling table. Preserve unmistakably INVERTED table above: legs point UP toward ceiling, dressed tabletop and plates/goblets/covered dish face DOWN. Existing inversion is correct; do not flip it upright. Preserve white striped tailcoat, flowing coattails and bold geometric dining-room bands. TARGETED CLEANUP: remove ALL tiny floral/filigree decoration from plates, dishes, teapot/cups; replace ornate rims with ONE clean broad geometric black band and keep broad white dish interiors. No flowers, small ornamental dots or new utensils. Keep tablecloth and all figure/tray contours clearly separate. Strong precise outlines, no gray modeling, no Gothic chandelier.
```

### 5. Woskowa królowa
**ID:** OH_FIVE_CANDLE_QUEEN_v03

**Opis:** Opaska świecznika wyrasta nad czołem królowej. Wosk spływający z jej dłoni tworzy szeroką suknię, której fałdy przechodzą w duże świece.

**Źródłowa wersja odniesienia:** exec-924a3337-fb85-4abb-8249-15f7fad75444.png

**Dokładny prompt:**
```text
Use case: illustration-story. Produce ONE finished premium Optical Halloween coloring-book illustration, portrait aspect ratio 8.5:11. The supplied image is the previous BEST composition to refine faithfully; preserve its strong identity, camera, anatomy, spatial layout and optical idea. Gallery-quality pure solid black and clean white, bold precise contours with clear line-weight hierarchy, broad dimensional optical bands and generous large enclosed white areas for coloring. One dominant adult hero and one traceable optical paradox. Patterns follow anatomy and perspective. No gray shading, gradients, hatching, fuzzy texture, tiny decorative clutter, moon/stars, text, labels, signature, watermark or page border. Important anatomy and identifying objects stay comfortably inside page edges; never crop fingers, shoes, headwear or flames. Exactly two arms and two legs on any human-shaped hero, no extra figures or duplicated body parts. This is a final fidelity and linework polish, not a redesign; do not add props.

Preserve elegant mature living queen face, wavy hair, extreme low viewpoint and enormous wax gown. Thin branching CANDELABRUM HEADBAND across forehead supports EXACTLY FIVE separate candles; all five COMPLETE flames have clear top headroom at least4%page-height. Two coherent arms and hands: one raised releases continuous wax ribbon joining gown, other lifts side of skirt. Five major broad wax gown folds continuously become five dominant candle columns at hem, with connected material and simple drips, crisp white outlined flames without glow. Gown IS wax, not cloth with pasted candles. Keep huge usable WHITE wax volumes and broad black channels. Strengthen primary queen/gown/candle outer contours subtly, remove fine gray facial modeling, retain beautiful face and delicate but readable eyes. Background remains restrained modern surreal museum with existing offset ring; no new cathedral, chandelier or candle forest. No small new candle forms.
```

## Końcowy protokół kontroli
| Ilustracja | Wynik |
| --- | --- |
| Przenośny pokój | Dwa osobne chwyty ramy, cztery sztywne boki, głęboki spójny pokój, dwie nogi i czytelny kontakt ze schodami. |
| Hotelowa otchłań | Pełna dłoń pierwszego planu, pięć palców, spójne kończyny i jednoznaczne spadanie. |
| Schody spod pędzla | Dokładnie dwa ramiona, chwyt lewej szyny, pędzel przy ścianie, dwa buty na szczeblach; zachowana przemiana farby w schody. |
| Dwie grawitacje | Dwa ramiona i dwie nogi, lot, odrębna taca i odwrócona filiżanka, jednoznacznie odwrócony stół. |
| Woskowa królowa | Pięć pełnych płomieni opaski w kadrze, dwie ręce, ciągły wosk przechodzący w suknię i świece. |

Duże białe pola pozostają użytkowe. Nie ma podstaw do kolejnego generowania z powodu zidentyfikowanego błędu technicznego. Wersje wcześniejsze pozostają dostępne do porównania, a nowszość nie jest traktowana jako automatyczne zatwierdzenie.

## Handoff
15 ilustracji zatwierdzonych wcześniej +5 nowych kompletnych kandydatów. Obrazy są natywnymi RGB proofami1103×1426 /1102×1427, nie masterami300DPI. Nie wykonano upscalingu, binarnej produkcji, książki ani publikacji.
Następny krok: końcowa ocena wizualna/wybór właścicielki i zapis zatwierdzonego rosteru ilustracji; ewentualnie wyłącznie konkretna wskazana korekta. Nie uruchamiać dalszych nieograniczonych iteracji ani fabryki książki w tej ścieżce.
