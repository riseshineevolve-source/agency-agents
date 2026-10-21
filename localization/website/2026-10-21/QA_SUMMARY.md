# Kontrola pakietu

- 2087 unikalnych jednostek: 1180 statycznych,551 dynamicznych (w tym49 chronionych literałów implementacji),145 Motto,65 Word Hunt,53 Studio,64 prywatność/zgody,29 JSON-LD. Teksty powtarzające się na stronach mapowane są do wspólnych jednostek.
- Faktyczne niezależne recenzje i ich końcowe poprawki znajdują się przy kandydatach. Kontrola polszczyzny obejmuje całe kandydatury; po poprawkach sprawdzono zmienione jednostki i ich zależności, zachowując recenzje niezmienionych hashy.
- CLI rse-language: deterministyczne kontrole źródeł, kompletności, ID, tokenów i zakresu przechodzą. Główne treści strony i aktywności pozostają OWNER_GATE z uwagi na jawne konflikty/ryzyko źródła; poprawny język nie usuwa tych bramek. Zestawy Motto/WordHunt/Studio/Privacy/Schema osiągnęły OWNER_READ_CANDIDATE.
- 35/35 stron: zgodne drzewa elementów,23 zachowane bloki stylów, niezmienione style inline,573 istniejące odwołania względne,10 poprawnych skryptów inline i3 poprawne lokalne skrypty zewnętrzne. Nie nadpisano zatwierdzonych Guides.
- Word Hunt:2500 siatek,30000 sprawdzeń słów,zero braków; przetestowano wymuszony fallback i błędne wejście.
- Word Search Studio:270 prób,zero niemożliwych do znalezienia słów i błędów generowania; przetestowano długie polskie słowa, rozdzielanie białymi znakami, izolację stanu PL oraz widoczne komunikaty błędów.
- 56 oryginalnych plików zgodnych z Git blobami przypiętego źródła. Trzy końcowe znaki nowego wiersza dodane przy przenoszeniu plików usunięto dopiero po zgodności Git SHA; kandydaci i treść zdekodowanego Studio bez zmian.

To nie jest dowód działania UI w przeglądarce, logowania, formularzy sieciowych, druku lub dopasowania do telefonu. Wizualny odbiór po integracji oraz prawdziwość źródłowych deklaracji medycznych/prawnych pozostają otwarte. Nie ogłaszamy wydania PL książek ani aplikacji z samego faktu lokalizacji strony.

Dotychczasowe testy narzędzia (31) i starego silnika (59) z PR40 pozostają historycznymi wynikami; kod tych silników nie był tu zmieniany. Osobny kontrakt starego silnika dla pełnej strony nie został uruchomiony; użyto faktycznego rse-language oraz kompilatora i kontroli strony. Hosted CI nie zostało potwierdzone dla nowej gałęzi.

Routing modeli: obowiązuje centralna rekomendacja projektu; brak niezależnego potwierdzenia przełączenia modelu w tym runtime. Nie uruchamiano płatnego fallbacku. Jedno zgłoszenie capacity obsłużono ponowieniem tej samej pracy, bez zmiany modelu.
