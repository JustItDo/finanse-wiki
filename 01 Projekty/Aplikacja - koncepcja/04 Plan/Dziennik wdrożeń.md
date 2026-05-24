# Dziennik wdrożeń

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[README|README]]
- [[Updatey wdrożeniowe/README|Updatey wdrożeniowe]]
- [[../START SESJI CODEX|Start sesji Codex]]
- [[../03 Technologia/Stan repo aplikacji|Stan repo aplikacji]]

## Cel notatki

To jest krótki dziennik wykonanych etapów wdrożeniowych.

Nie zastępuje szczegółowych notatek produktowych ani technicznych.
Ma dawać szybki obraz:

- co zostało realnie wykonane
- w jakim repo znajduje się efekt
- co jest następnym krokiem

## 2026-05-24

### `00.1 Start projektu`

- status: `wykonane w workspace finanse-app`
- wynik:
  - postawiony projekt `Expo + React Native + TypeScript`
  - dodana nawigacja
  - dodane bazowe komponenty UI
  - dodane lint, prettier, aliasy i wsparcie web
- następny krok:
  - `00.2 Lokalna baza i modele`

### `00.2 Lokalna baza i modele`

- status: `wykonane w workspace finanse-app`
- wynik:
  - wdrożone `SQLite`
  - dodane migracje
  - dodane repozytoria i bootstrap storage
  - przygotowane pola pod OCR i przyszły import z wiki
- następny krok:
  - `00.3 Kategorie i budżet startowy`

### `00.3 Kategorie i budżet startowy`

- status: `wykonane w workspace finanse-app`
- wynik:
  - wdrożony ekran i logika konfiguracji kategorii
  - wdrożony opcjonalny budżet miesiąca
  - wdrożone budżety kategorii i liczenie pozostałego budżetu
- następny krok:
  - `01.0 Ręczne dodawanie wydatku`

### `01.0 Ręczne dodawanie wydatku`

- status: `wykonane w repo finanse-app`
- commit:
  - `49fac8f` `01.0-01.1 Add shared manual transaction entry flow`
- wynik:
  - wdrożony szybki formularz ręcznego dodawania transakcji
  - zapis wydatku aktualizuje budżet kategorii i stan miesiąca
  - dodana walidacja formularza i stan sukcesu po zapisie
- następny krok:
  - `01.1 Ręczne dodawanie przychodu`

### `01.1 Ręczne dodawanie przychodu`

- status: `wykonane w repo finanse-app`
- commit:
  - `49fac8f` `01.0-01.1 Add shared manual transaction entry flow`
- wynik:
  - dodany tryb przychodu w tym samym flow formularza
  - przychód zapisuje się do wspólnego modelu `transactions`
  - bilans miesiąca liczy się na wspólnych agregacjach dla przychodów i wydatków
- następny krok:
  - `01.2 Dashboard MVP`

### `01.2 Dashboard MVP`

- status: `wykonane w repo finanse-app`
- commit:
  - `e7dd3a9` `01.2 Add MVP dashboard overview`
- wynik:
  - wdrożony główny ekran szybkiego wglądu w miesiąc z przychodami, wydatkami i bilansem
  - dodany stan „ile zostało z budżetu”, stany puste i komunikat o przekroczeniu planu
  - dodane najważniejsze kategorie budżetowe oraz prosty przełącznik miesiąca
  - logika agregacji dashboardu została wyniesiona poza komponent UI
- następny krok:
  - `01.3 Historia transakcji`

### `01.3 Historia transakcji`

- status: wykonane w repo finanse-app
- commit: `673b39b` `01.3 Add transaction history management flow`
- wynik:
  - wdrożona lista historii transakcji z filtrowaniem po typie, miesiącu i kategorii.
  - dodane wyszukiwanie, edycja inline i usuwanie.
- następny krok:
  - `02.0 OCR i dodawanie zdjęcia`

### `02.0 OCR i dodawanie zdjęcia`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - działa wybór zdjęcia paragonu z aparatu
  - działa wybór screena płatności z galerii
  - dodany został fallback `Wybierz paragon z galerii` do testów na emulatorze
  - obrazy zapisują się lokalnie jako załączniki i trafiają do tego samego flow danych co dalszy import
  - OCR on-device działa przez `@react-native-ml-kit/text-recognition`
  - poprawiono zapis załącznika pod `Expo 56` przez odejście od deprecated `FileSystem.copyAsync` na rzecz `File.copy`
  - flow OCR czeka na zakończone kopiowanie pliku i waliduje istnienie załącznika przed odczytem
- następny krok:
  - `02.1 Korekta OCR`

### `02.1 Korekta OCR`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - działa ekran korekty OCR z poprawą kwoty, daty, sklepu i kategorii
  - pola o niskiej pewności są oznaczane i prowadzą użytkownika do ręcznej poprawy
  - zapis kończy się w tej samej warstwie danych co wpis ręczny
  - heurystyka kwot dla paragonów została dopracowana pod końcowy blok płatności `SUMA PLN`, `DO ZAPŁATY`, `ZAPŁACONO`
  - parser odrzuca teraz linie podatkowe, datoczas i mylące wartości z pozycji towaru
- następny krok:
  - `02.2 Dashboard po OCR`

### `02.2 Dashboard po OCR`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - zapis po OCR używa tej samej ścieżki danych co wpis ręczny
  - po zapisie OCR budżety, bilans miesiąca i dashboard aktualizują się bez osobnych wyjątków
  - ekran zapisu pokazuje wpływ transakcji na miesiąc także dla wpisów z OCR
  - historia i szczegół transakcji pokazują spójne źródło wpisu `Ręcznie`, `OCR paragonu` albo `OCR screena`
  - oznaczenie źródła zostało wyniesione poza UI do wspólnej warstwy domenowej
- następny krok:
  - `03.0 Budżety`

### `03.0 Budżety`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - ekran budżetów został przebudowany z etapu konfiguracji `00.3` do codziennego widoku kontroli budżetu
  - kategorie wydatkowe są teraz porządkowane poza UI według ryzyka, wykorzystania i aktywności
  - dodane zostały sekcje `Wymagają uwagi`, `Aktywne i pod kontrolą`, `Aktywne bez limitu` i `Nieaktywne kategorie`
  - dla budżetu miesiąca i kategorii pokazywane są limit, wydane, pozostało i procent wykorzystania
  - wspólne statusy `w normie`, `blisko limitu` i `przekroczony` korzystają z jednej warstwy danych współdzielonej z dashboardem
- następny krok:
  - `03.1 Analizy`

### `03.1 Analizy`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - dodany został osobny ekran `Analizy` w nawigacji tabowej w miejsce placeholdera ustawień
  - analizy pokazują udział wydatków według kategorii, największe kategorie kosztów i trend dzienny wydatków
  - zakres danych można przełączyć między bieżącym i poprzednim miesiącem
  - logika agregacji została wyniesiona poza UI do wspólnej warstwy danych i korzysta z przygotowanych sum kategorii oraz nowych sum dziennych
- następny krok:
  - `03.2 Oszczędności`

### `03.2 Oszczędności`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - dodany został miesięczny, kwotowy cel oszczędności dla jednego aktywnego miesiąca
  - oszczędności liczą się prosto jako `przychody - wydatki`
  - cel ustawia się w zakładce `Budżety` razem z planem miesiąca
  - dashboard pokazuje aktualny stan oszczędności, cel, brakującą kwotę albo nadwyżkę i prosty postęp celu
  - logika celu korzysta ze wspólnych agregacji miesiąca zamiast dublować logikę budżetu
- następny krok:
  - `04.0 Bezpieczeństwo`

### `03.x Doprecyzowanie OCR po teście ręcznym`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - po wdrożeniu `03.0` ręczny test wykazał regresję heurystyk OCR dla części screenów płatności i części paragonów
  - parser paragonów dostał wyższy priorytet dla wyniku z układu OCR bloków nad surowym fallbackiem tekstowym
  - parser screenów został doprecyzowany o anchory płatności, filtrowanie szumu bankowego i karanie małych opłat/prowizji
  - po tej poprawce ręcznie sprawdzone przykłady zaczęły znowu zwracać poprawne kwoty
- następny krok:
  - `04.0 Bezpieczeństwo`

### Budżety przychodów

- status: `doprecyzowane lokalnie w repo finanse-app`
- wynik:
  - w budżetach przychodów przyjęto uproszczenie MVP: brak osobnych celów i limitów per kategoria, pozostaje podgląd realnych wpływów
- następny krok:
  - utrzymać to uproszczenie do czasu osobnego etapu rozwoju budżetów

## Stan commitów

Na moment tego wpisu:

- `finanse-wiki` ma własną historię commitów dla dokumentacji i struktury vaultu
- `finanse-app` ma w historii repo domknięte wdrożenia `00.1-01.3`
- kolejne lokalne commity aplikacji obejmują:
  - `2dfc98c` `Complete 02.2 OCR dashboard integration`
  - `8f6f4f5` `Finalize 02.0-02.1 OCR receipt flow`
  - `83cd25e` `02.0-02.1 Add OCR import and correction flow`
  - `b4d31c4` `Fix income category budget entry`

Warto dalej dopisywać tu skrócone odniesienia do hashy po każdym kolejnym update.
