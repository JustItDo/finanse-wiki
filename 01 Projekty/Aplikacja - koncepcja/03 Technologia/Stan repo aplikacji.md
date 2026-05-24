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
- budżety kategorii
- logika liczenia pozostałego budżetu

### Ręczne transakcje

- wspólny ekran dodawania transakcji
- ręczne dodawanie wydatku
- ręczne dodawanie przychodu
- wspólny model `transaction` dla `income` i `expense`
- wspólne agregacje miesiąca dla salda, przychodów i wydatków

## Stan Git repo aplikacji

- gałąź robocza: `master`
- ostatni commit: `49fac8f` `01.0-01.1 Add shared manual transaction entry flow`
- `origin/master` jest zsynchronizowany z lokalnym `HEAD`

To oznacza, że etapy `00.1-01.1` są już zapisane w historii repo aplikacji i wypchnięte do `origin/master`.

## Najbliższy krok Git

- przygotować kolejny logiczny commit dla `01.2 Dashboard MVP`, gdy zmiana będzie domknięta

## Znaczenie dla kolejnych etapów

Repo jest gotowe, żeby wejść w:

- [[../04 Plan/Updatey wdrożeniowe/02.0 OCR i dodawanie zdjęcia|02.0 OCR i dodawanie zdjęcia]]
- [[../04 Plan/Updatey wdrożeniowe/03.0 Budżety|03.0 Budżety]]

Kolejne update'y powinny korzystać bezpośrednio z istniejących repozytoriów, wspólnego modelu transakcji, dashboardowych agregacji oraz nowej warstwy historii transakcji zamiast budować własną logikę danych od zera.
