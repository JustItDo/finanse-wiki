# Aplikacja - koncepcja

To jest główny obszar roboczy dla pomysłu na aplikację.

## Mapa

- [[Mapa projektu]]
- [[00 Założenia startowe]]
- [[01 Wizja/Start - brief projektu|Brief projektu]]
- [[02 Produkt/MVP]]
- [[03 Technologia/Decyzje techniczne]]
- [[03 Technologia/Workflow developera|Workflow developera]]
- [[03 Technologia/Workflow modeli AI|Workflow modeli AI]]
- [[03 Technologia/Stan repo aplikacji]]
- [[04 Plan/Roadmapa]]
- [[04 Plan/Dziennik wdrożeń]]
- [[START SESJI CODEX]]

## Struktura

- `01 Wizja` - po co powstaje aplikacja i jaki problem rozwiązuje
- `02 Produkt` - funkcje, użytkownicy, scenariusze użycia, MVP
- `03 Technologia` - stack, architektura, decyzje techniczne
- `04 Plan` - etapy, milestone'y, taski, wdrożenie
- `99 Robocze` - luźne notatki i szybkie pomysły

## Kolejność pracy

1. Opis pomysłu
2. Zakres MVP
3. Lista funkcji
4. Wybór technologii
5. Plan realizacji

## Aktualny stan

- wiki projektu jest rozpisane na poziomie wizji, produktu, technologii i planu wdrożenia
- implementacja aplikacji została rozpoczęta w osobnym repo `finanse-app`
- wykonane w workspace aplikacji są update'y:
- `00.1 Start projektu`
- `00.2 Lokalna baza i modele`
- `00.3 Kategorie i budżet startowy`
- `01.0 Ręczne dodawanie wydatku`
- `01.1 Ręczne dodawanie przychodu`
- `01.2 Dashboard MVP`
- `01.3 Historia transakcji`
- `02.0 OCR i dodawanie zdjęcia`
- `02.1 Korekta OCR`
- najbliższym krokiem implementacyjnym jest `02.2 Dashboard po OCR`

## Repozytoria

- `finanse-wiki`:
  - przechowuje vault Obsidiana i trwałą dokumentację projektu
  - aktualna gałąź: `main`
  - ostatnie commity:
    - `abc83c8` `Update implementation notes and Codex session workflow`
    - `366be00` `Build finanse-wiki project structure and navigation`
    - `3b089ff` `Initialize project context, planning notes, and Codex skills`
- `finanse-app`:
  - przechowuje implementację aplikacji `Expo + React Native + TypeScript`
  - aktualna gałąź robocza: `master`
  - ostatnie lokalne commity:
    - `b4d31c4` `Fix income category budget entry`
    - `83cd25e` `02.0-02.1 Add OCR import and correction flow`
    - `673b39b` `01.3 Add transaction history management flow`
    - `e7dd3a9` `01.2 Add MVP dashboard overview`
  - stan wdrożenia `00.1-01.3` jest zapisany w historii repo, a prace nad OCR są lokalnie rozpoczęte

## Najważniejsze notatki

- [[00 Założenia startowe]]
- [[01 Wizja/Start - brief projektu|Brief projektu]]
- [[02 Produkt/MVP]]
- [[02 Produkt/Pomysły produktowe]]
- [[03 Technologia/Decyzje techniczne]]
- [[03 Technologia/Workflow developera|Workflow developera]]
- [[03 Technologia/Workflow modeli AI|Workflow modeli AI]]
- [[04 Plan/Roadmapa]]
- [[04 Plan/Backlog]]
