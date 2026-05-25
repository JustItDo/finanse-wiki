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

Aktualny kierunek marki dla produktu to `Zenifi`, a podstawowy rebranding aplikacji został już wdrożony w konfiguracji Expo, assetach i najprostszych miejscach UI.

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
- `04.2 Test MVP`

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
- podstawowy rebranding do marki `Zenifi`:
  - nazwa aplikacji i slug Expo
  - bundle identifier / package pod kolejne buildy
  - ikona aplikacji, adaptive icon, splash i favicon
  - bazowy kierunek kolorystyczny zgodny z notatką marki
- osobny moduł `security` spięty providerem nad nawigacją
- root `SafeAreaProvider` działa teraz z `initialWindowMetrics`, żeby bezpieczne insets były stabilniejsze od pierwszego renderu

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
- tworzenie własnych kategorii
- aktywacja, edycja i usuwanie kategorii
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
- zakładka `Budżety` pokazuje teraz listę kategorii z krótkim opisem, a edycja limitu dzieje się dopiero po wejściu w element
- sekcja `Aktywne bez limitu` została uproszczona do `Kategorie bez limitu`, a główna sekcja limitów do `Kategorie z limitem`
- usunięcie kategorii odłącza stare transakcje od tej kategorii i czyści jej limit miesięczny
- użytkownik może też ustawić ikonę kategorii, która pojawia się potem na dashboardzie

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
- historia pozwala teraz filtrować także przez `Wszystkie miesiące`
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
- po dłuższym przejściu aplikacji do tła i wznowieniu dane nie zostają widoczne bez ponownego odblokowania
- dodana została zakładka `Bezpieczeństwo` z konfiguracją PIN-u, biometrii i wyłączenia blokady
- pełne szyfrowanie lokalnej bazy i załączników nie weszło do `04.0`; obecny etap daje sensowną ochronę MVP, ale nie pełne szyfrowanie danych spoczynkowych
- w `04.2` poprawiono sesję bezpieczeństwa tak, żeby krótkie wejście do aparatu lub galerii nie zrywało OCR i aktywnego flow użytkownika
- po pakiecie dopracowań auto-biometria próbuje odblokowania tylko raz po blokadzie, a po anulowaniu nadal można normalnie wejść PIN-em

### Ręczne transakcje

- wspólny ekran dodawania transakcji
- ręczne dodawanie wydatku
- ręczne dodawanie przychodu
- wspólny model `transaction` dla `income` i `expense`
- wspólne agregacje miesiąca dla salda, przychodów i wydatków
- tryb ręczny został uproszczony do szybkiej ścieżki `kwota -> kategoria -> zapis`, a szczegóły są rozwijane tylko gdy są potrzebne
- po pakiecie dopracowań przed testami telefonu ekran startuje bez agresywnego otwierania klawiatury
- potwierdzenie zapisu ma teraz prostą formę `Dodano`, jest niżej na ekranie i nie zasłania dalszego dodawania
- techniczne etykiety typu `update` zostały usunięte z głównych ekranów, żeby interfejs wyglądał bardziej produktowo
- po paczce 3 formularze i listy z edycją korzystają z jednej lekkiej obsługi dolnego insetu ekranu i tabbara, żeby klawiatura nie zasłaniała tak łatwo pól na telefonie
- dolne menu uwzględnia już bezpieczny dolny inset systemu i nie wpada pod pasek telefonu na urządzeniach z gestami

## Stan Git repo aplikacji

- gałąź robocza: `master`
- ostatnie commity:
  - `c5faecc` `Polish pre-phone-test UX and lock session flow`
  - `ebaf687` `Implement 04.0 security and 04.1 UX polish`
  - `f5a6df7` `Implement 03.2 monthly savings goal`
- `origin/master` jest obecnie o `1` commit za lokalnym `HEAD`

To oznacza, że etapy `00.1-04.2` oraz pakiet dopracowań przed testami telefonu są już zapisane w historii repo.

Etap `04.2 Test MVP` i pakiet dopracowań UX oraz sesji bezpieczeństwa są już zapisane commitem `c5faecc`.

Bieżący workspace zawiera teraz jeszcze lokalną implementację `Paczki 3` i `Paczki 4` z feedbacku testerskiego:

- poprawiony keyboard-aware scroll dla formularzy
- poprawione bottom insets i wysokość tabbara
- lepsze zachowanie na małych ekranach telefonu w `Dodaj transakcję`, `Budżety`, `Historia` i `Bezpieczeństwo`
- przy pierwszym uruchomieniu pojawia się pytanie o ustawienie PIN-u z przejściem do zakładki `Bezpieczeństwo`
- ekran odblokowania dostał 4 pola PIN-u z maskowaniem cyfr kropkami i prostsze copy
- wyłączenie biometrii wymaga teraz potwierdzenia biometrią albo PIN-em
- aktywna sesja nadal chroni zwykłe powroty z aparatu i galerii przed zbędnym ponownym PIN-em
- obszar `Budżety` dostał też lokalną implementację `Paczki 2` z CRUD-em kategorii i lżejszym widokiem listy + szczegółu
- `Historia` i `Dashboard` dostały też lokalną implementację `Paczki 1` z filtrem `Wszystkie miesiące` i lżejszym copy głównych sekcji

## Najbliższy krok Git

- przygotować commit dla `Paczki 1`, `Paczki 2`, `Paczki 3` i `Paczki 4`
- potem zrobić ręczny test telefonu pod historię, dashboard, kategorie, budżety, klawiaturę, scroll, onboarding PIN-u i blokadę biometryczną
- następnym krokiem po tym pakiecie jest kolejna selekcja tylko tych poprawek, które wyjdą z realnego użycia

Po wdrożeniu podstawowego rebrandingu `Zenifi` następnym osobnym krokiem może być już tylko drugi etap marki:

- pełniejsze dopasowanie UI do nowej marki
- druga iteracja splasha i ewentualnie sklepowej nazwy listingowej
- sprawdzenie buildów urządzeniowych już pod nową nazwą i ikonami

## Znaczenie dla kolejnych etapów

Repo jest gotowe, żeby wejść w:

- test telefonu na codziennych scenariuszach
- kilka dni realnego używania jako głównego rejestru finansów
- krótkie poprawki tylko tam, gdzie wyjdą z prawdziwego użycia

Kolejne update'y powinny korzystać bezpośrednio z istniejących repozytoriów, wspólnego modelu transakcji, dashboardowych agregacji, warstwy historii transakcji, gotowego flow OCR i wspólnej warstwy statusów budżetowych zamiast budować własną logikę danych od zera.
