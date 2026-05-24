# Stan repo aplikacji

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[../README|README]]
- [[Decyzje techniczne]]
- [[Workflow developera]]
- [[Model danych implementacyjny]]
- [[../04 Plan/Updatey wdrożeniowe/README|Updatey wdrożeniowe]]
- [[../04 Plan/Dziennik wdrożeń|Dziennik wdrożeń]]
- [[../START SESJI CODEX|Start sesji Codex]]

## Rola repo

Repo `finanse-app` przechowuje implementację aplikacji `Finansowy Copilot`.

To repo jest osobne od `finanse-wiki`, ale od początku działa z założeniem, że wiki projektu znajduje się obok jako vault Obsidiana.

Najważniejsza relacja katalogów:

- repo aplikacji: `../finanse-app`
- vault projektu: `../Obsidian Vault`

## Aktualny stan techniczny

Na poziomie workspace aplikacji są już wykonane:

- `00.1 Start projektu`
- `00.2 Lokalna baza i modele`
- `00.3 Kategorie i budżet startowy`
- `01.0 Ręczne dodawanie wydatku`
- `01.1 Ręczne dodawanie przychodu`
- `01.2 Dashboard MVP`
- `01.3 Historia transakcji`

Na poziomie workspace aplikacji są już wykonane także:

- `02.0 OCR i dodawanie zdjęcia`
- `02.1 Korekta OCR`
- `02.2 Dashboard po OCR`

## Obecna struktura kodu

Najważniejsze katalogi:

- `src/navigation` - nawigacja aplikacji
- `src/providers` - bootstrap aplikacji i provider usług
- `src/domain` - typy domenowe
- `src/storage` - warstwa danych, repozytoria i bootstrap storage
- `src/features` - logika i ekrany per obszar produktu
- `src/shared` - UI, theme, helpery i konfiguracja współdzielona

## Co jest już wdrożone

### Fundament aplikacji

- `Expo + React Native + TypeScript`
- nawigacja tabowa
- wspólne komponenty UI
- bazowa konfiguracja `eslint`, `prettier`, aliasów i buildów web

### Warstwa danych

- `SQLite` dla natywnych platform
- migracje schematu i wersjonowanie
- repozytoria dla:
  - `transactions`
  - `attachments`
  - `categories`
  - `category_budgets`
  - `monthly_budgets`
- fallback webowy z tym samym kontraktem repozytoriów

### Budżety i kategorie

- lista kategorii startowych
- aktywacja i edycja kategorii
- opcjonalny budżet miesiąca
- budżety kategorii wydatkowych
- uproszczone kategorie przychodów bez osobnych celów i limitów
- logika liczenia pozostałego budżetu

### Historia i OCR

- ekran historii transakcji z filtrowaniem, wyszukiwaniem, szczegółem, prostą edycją i usuwaniem
- działający flow wyboru obrazu, załączników, OCR i korekty
- zapis załącznika został poprawiony pod `Expo 56` po usunięciu zależności od deprecated `FileSystem.copyAsync`
- flow OCR waliduje teraz istnienie lokalnego pliku po kopiowaniu, zanim przekaże go do rozpoznawania tekstu
- OCR dla paragonów i screenów działa on-device przez `@react-native-ml-kit/text-recognition`
- heurystyka OCR dla kwot paragonów została rozszerzona o:
  - końcowy blok płatności `SUMA PLN`, `DO ZAPŁATY`, `ZAPŁACONO`
  - filtrowanie wartości podatkowych i datoczasów
  - poprawną normalizację `66.33` i podobnych formatów
- ekran korekty OCR pokazuje pola do poprawy i zapisuje do tej samej warstwy danych co wpis ręczny
- dla emulatora i testów dodany jest praktyczny fallback `Wybierz paragon z galerii`, który uruchamia parser paragonów bez użycia aparatu
- zapis po OCR używa tej samej ścieżki danych co wpis ręczny, więc od razu aktualizuje budżety, dashboard i historię
- historia i szczegół transakcji pokazują już spójne oznaczenie źródła wpisu `Ręcznie` lub `OCR`
- ekran zapisu pokazuje wpływ transakcji na miesiąc także dla wpisów po OCR, bez osobnej ścieżki agregacji

### Ręczne transakcje

- wspólny ekran dodawania transakcji
- ręczne dodawanie wydatku
- ręczne dodawanie przychodu
- wspólny model `transaction` dla `income` i `expense`
- wspólne agregacje miesiąca dla salda, przychodów i wydatków

## Stan Git repo aplikacji

- gałąź robocza: `master`
- ostatnie commity:
  - `b4d31c4` `Fix income category budget entry`
  - `83cd25e` `02.0-02.1 Add OCR import and correction flow`
  - `673b39b` `01.3 Add transaction history management flow`
  - `e7dd3a9` `01.2 Add MVP dashboard overview`
- `origin/master` jest obecnie za lokalnym `HEAD`

To oznacza, że etapy `00.1-02.2` są już wdrożone lokalnie, a historia repo zawiera domknięte commity do `02.1` przed bieżącym domknięciem dashboardowego spięcia OCR.

## Najbliższy krok Git

- przygotować commit domykający `02.2 Dashboard po OCR`

## Znaczenie dla kolejnych etapów

Repo jest gotowe, żeby wejść w:

- [[../04 Plan/Updatey wdrożeniowe/03.0 Budżety|03.0 Budżety]]

Kolejne update'y powinny korzystać bezpośrednio z istniejących repozytoriów, wspólnego modelu transakcji, dashboardowych agregacji, warstwy historii transakcji i gotowego flow OCR zamiast budować własną logikę danych od zera.
