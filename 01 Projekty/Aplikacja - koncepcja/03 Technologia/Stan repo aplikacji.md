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
- `03.0 Budżety`
- `03.1 Analizy`
- `03.2 Oszczędności`
- `04.0 Bezpieczeństwo`
- `04.1 Poprawki UX i wydajności`

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
- osobny moduł `security` spięty providerem nad nawigacją

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
- pełny ekran budżetów dla MVP z sekcjami:
  - kategorie problemowe
  - aktywne kategorie pod kontrolą
  - aktywne kategorie bez limitu
  - nieaktywne kategorie
- procent wykorzystania budżetu kategorii i budżetu miesiąca
- wspólne statusy ryzyka i przekroczenia wyniesione do warstwy danych
- spójne sortowanie kategorii według ryzyka, wykorzystania i aktywności

### Analizy

- osobny ekran `Analizy` w nawigacji tabowej
- przełącznik zakresu `bieżący miesiąc` / `poprzedni miesiąc`
- wykres udziału wydatków według kategorii
- widok największych kategorii kosztów
- wykres trendu dziennego wydatków
- lekka warstwa agregacji poza UI współdzieląca:
  - podsumowanie miesiąca
  - sumy kategorii
  - sumy dzienne wydatków

### Oszczędności

- cel oszczędności kwotowy dla jednego miesiąca
- jeden aktywny cel oszczędności na miesiąc
- oszczędności liczone jako `przychody - wydatki`
- postęp celu pokazany na `Dashboardzie`
- logika celu korzysta ze wspólnych agregacji miesiąca zamiast równoległego modelu danych

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
- heurystyka OCR dla screenów płatności została po ręcznym teście doprecyzowana o:
  - anchory kontekstu płatności typu `zapłacono`, `transakcja`, `przelew`, `otrzymano`
  - filtrowanie szumu bankowego typu saldo, referencje, identyfikatory i długie numery
  - karanie małych opłat i prowizji, gdy obok jest właściwa większa kwota transakcji
- ekran korekty OCR pokazuje pola do poprawy i zapisuje do tej samej warstwy danych co wpis ręczny
- dla emulatora i testów dodany jest praktyczny fallback `Wybierz paragon z galerii`, który uruchamia parser paragonów bez użycia aparatu
- zapis po OCR używa tej samej ścieżki danych co wpis ręczny, więc od razu aktualizuje budżety, dashboard i historię
- historia i szczegół transakcji pokazują już spójne oznaczenie źródła wpisu `Ręcznie` lub `OCR`
- ekran zapisu pokazuje wpływ transakcji na miesiąc także dla wpisów po OCR, bez osobnej ścieżki agregacji
- ekran dodawania rozdziela teraz wyraźnie szybki wpis ręczny od trybu OCR
- ręczne dodawanie ma sekcję `Szybkie powtórki` opartą o ostatnie podobne transakcje
- korekta OCR pokazuje teraz wyraźniej liczbę pól wymagających uwagi, a surowy tekst OCR jest domyślnie schowany
- historia przy filtrach nie robi już zbędnego pełnego pobrania danych tylko do rozpoznania pustego stanu

### Bezpieczeństwo

- osobny provider bezpieczeństwa pilnuje stanu blokady, wznowienia aplikacji i odblokowania
- wejście do aplikacji można zabezpieczyć `PIN-em 4-cyfrowym`
- dostępna jest opcjonalna biometria jako szybsza ścieżka odblokowania nad tym samym PIN-em
- sekret blokady jest przechowywany poza `SQLite`:
  - natywnie przez `expo-secure-store`
  - na webie przez fallback przeglądarkowy
- po starcie aplikacji z aktywną blokadą użytkownik musi ponownie odblokować dostęp
- po przejściu aplikacji do tła i wznowieniu dane nie zostają widoczne bez ponownego odblokowania
- dodana została zakładka `Bezpieczeństwo` z konfiguracją PIN-u, biometrii i wyłączenia blokady
- pełne szyfrowanie lokalnej bazy i załączników nie weszło do `04.0`; obecny etap daje sensowną ochronę MVP, ale nie pełne szyfrowanie danych spoczynkowych

### Ręczne transakcje

- wspólny ekran dodawania transakcji
- ręczne dodawanie wydatku
- ręczne dodawanie przychodu
- wspólny model `transaction` dla `income` i `expense`
- wspólne agregacje miesiąca dla salda, przychodów i wydatków
- tryb ręczny został uproszczony do szybkiej ścieżki `kwota -> kategoria -> zapis`, a szczegóły są rozwijane tylko gdy są potrzebne

## Stan Git repo aplikacji

- gałąź robocza: `master`
- ostatnie commity:
  - `2dfc98c` `Complete 02.2 OCR dashboard integration`
  - `8f6f4f5` `Finalize 02.0-02.1 OCR receipt flow`
  - `b4d31c4` `Fix income category budget entry`
- `origin/master` jest obecnie zgodny z lokalnym `HEAD` do `02.2`

To oznacza, że etapy `00.1-03.1` są już zapisane w historii repo, a `03.2 Oszczędności` jest obecnie domknięte lokalnie w workspace przed commitem tej sesji.

Etapy `04.0 Bezpieczeństwo` i `04.1 Poprawki UX i wydajności` są obecnie domknięte lokalnie w workspace przed commitem tej sesji.

## Najbliższy krok Git

- przygotować commit domykający `03.2 Oszczędności`, `04.0 Bezpieczeństwo` i `04.1 Poprawki UX i wydajności`

## Znaczenie dla kolejnych etapów

Repo jest gotowe, żeby wejść w:

- ręczny test pełnego codziennego flow po poprawkach `04.0-04.1`
- [[../04 Plan/Updatey wdrożeniowe/04.2 Test MVP|04.2 Test MVP]]

Kolejne update'y powinny korzystać bezpośrednio z istniejących repozytoriów, wspólnego modelu transakcji, dashboardowych agregacji, warstwy historii transakcji, gotowego flow OCR i wspólnej warstwy statusów budżetowych zamiast budować własną logikę danych od zera.
