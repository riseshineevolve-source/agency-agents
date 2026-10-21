# RSE: polska strona na podstawie oryginału EN

Kandydat lokalizacyjny, 21 października 2026. Wersja do oceny i integracji przez Website Factory, bez publikacji.

Źródło: `riseshineevolve-source/RISE.SHINE.EVOLVE`, commit `e6efa82b5194bfb492632aafd58655bb1ff1465d` (PR609). Nie użyto odrzuconej polskiej strony jako podstawy pisania. Odrębny polski autor dostał opis funkcji i faktów, a oryginalne zdania wróciły dopiero do kontroli znaczenia. Polityki i zgody przetłumaczono zachowawczo.

## Co jest w pakiecie

- 35 polskich podstron opartych na strukturze EN, w tym strona główna, sekcje odbiorców, biblioteka, karty książek i aplikacji, Darmowe materiały, mapa strony i prywatność.
- Treści po kliknięciu: portrety rodziny, aktywności, opisy książek, formularze, zgody, motta, wykreślanki i Word Search Studio.
- Osobna kontrola polskich tekstów SEO oraz danych strukturalnych JSON-LD. Polskie menu nie oznacza wydania angielskich książek po polsku.
- Zamrożone źródła, kandydaci, briefy, pakiety dla autora, niezależne recenzje, poprawki, kompilatory i testy.

Sześć zatwierdzonych ścieżek `/pl/guides/` pozostaje bez zmian. Podgląd kieruje do ich istniejących adresów. Zachowano źródłowy DOM i CSS, w tym kolory i układ; nie projektowano nowej strony.

## Otwieranie i odtworzenie

W archiwum `preview/` zawiera gotowy podgląd. Można go uruchomić lokalnie:

```sh
python3 -m http.server 8000 --directory preview
```

Następnie otworzyć `http://localhost:8000/pl/`. Grafiki, fonty i wspólne zasoby źródłowe korzystają z istniejących adresów strony; potrzebne jest połączenie z internetem. Ten pakiet nie jest nowym serwisem produkcyjnym ani kopią backendu kont użytkowników.

Odtworzenie z dokładnych kandydatów po rozpakowaniu:

```sh
python3 website-integration/assemble.py --output rebuilt-preview
python3 website-integration/verify.py rebuilt-preview
```

Oryginalne kontrole CLI zachowują bezwzględne ścieżki wejścia w niezmiennych manifestach i są dowodem tej sesji. Nie edytuj tych manifestów, aby przenosić run; dla nowego źródła wykonaj nowy `prepare`. Kompilator podglądu działa z rozpakowanego folderu.

Wymagane: Python3, lxml i Node do kontroli składni JavaScript. CLI językowe jest dołączone w `rse/`.

## Przekazanie do Website Factory

Writer strony pobiera polskie pliki z `preview/pl/` jako kandydaturę do swojej gałęzi. Nie nadpisuje wspólnych EN zasobów polską treścią. Zlokalizowane dane i skrypty są pod `/pl/assets/` oraz `/pl/data/`. Przy integracji należy przepiąć podglądowe odnośniki zasobów na właściwe ścieżki wdrożenia, zachowując język zasobów i kierunek przełącznika EN/PL.

Wszystkie podstrony podglądu mają `noindex`. Publikacja i zdjęcie `noindex` należą do writera strony po sprawdzeniu gotowego wdrożenia. Brak przeglądarkowego dowodu mobile/desktop: test DOM/CSS nie dowodzi braku przepełnień po zmianie długości tekstu.

## Rzeczywiste kwestie do zamknięcia

Źródło EN zawiera starszy długi opis świątecznej książki z innymi etykietami i wiekiem niż aktualna karta i zatwierdzona tożsamość Gentle Steps. Zachowano pochodzenie zamiast dopisywać nowy produkt. Pozostają też niespójne dane wieku Nini, czasu programu Grandma Bibi oraz mocne twierdzenia o efektach aktywności i niezweryfikowane deklaracje prawne. Raporty wskazują konkretne segmenty. Kontrola poprawności przekładu nie zatwierdza tych twierdzeń do publikacji.

Nie zmieniono masterów książek ani aplikacji Gentle Steps. Detective PL R8 pozostaje chroniony; nie rozpoczęto kolejnego tłumaczenia książki.

## Następne użycie narzędzia

`Użyj $rse-language. Stwórz naturalną polską wersję tej strony na podstawie aktualnego oryginału angielskiego. Zachowaj ofertę, strukturę, fakty i zatwierdzone teksty.`

Nie trzeba ponownie wypisywać zasad języka ani ról recenzentów. Skill prowadzi autora i kontrolę; sam CLI nie generuje prozy.
