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

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - wdrożony główny ekran szybkiego wglądu w miesiąc z przychodami, wydatkami i bilansem
  - dodany stan „ile zostało z budżetu”, stany puste i komunikat o przekroczeniu planu
  - dodane najważniejsze kategorie budżetowe oraz prosty przełącznik miesiąca
  - logika agregacji dashboardu została wyniesiona poza komponent UI
- następny krok:
  - ręczny smoke test dashboardu na mobile i web, potem `01.3 Historia transakcji`

## Stan commitów

Na moment tego wpisu:

- `finanse-wiki` ma własną historię commitów dla dokumentacji i struktury vaultu
- `finanse-app` ma domkniętą historię wdrożeń `00.1-01.1`, a `01.2` jest gotowe lokalnie do kolejnego logicznego commita

Warto dalej dopisywać tu skrócone odniesienia do hashy po każdym kolejnym update.
