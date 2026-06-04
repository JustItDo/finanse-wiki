# Workflow modeli AI

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[../README|README]]
- [[Workflow developera]]
- [[Decyzje techniczne]]
- [[Stan repo aplikacji]]
- [[PROMPT LM STUDIO - testy jednostkowe.txt]]
- [[../04 Plan/Backlog|Backlog]]
- [[../START SESJI CODEX|Start sesji Codex]]

## Cel dokumentu

To jest dokument opisujący workflow pracy z modelami AI w projekcie `Finansowy Copilot`.

Ma jasno określać:

- kiedy używamy `Codexa`,
- jaki jest aktualny status odłożonej integracji z `LM Studio`,
- jak ograniczać zużycie tokenów,
- jak bezpiecznie wrócić do lokalnego modelu w przyszłości.

## Aktualny stan

- integracja MCP `lmstudio-unit-tests` jest obecnie wyłączona
- powód: start MCP timeoutował po 30 sekundach i powodował ostrzeżenie `MCP startup incomplete`
- globalny wpis MCP został usunięty z konfiguracji Codexa
- skrypty `scripts/lmstudio-unit-tests-mcp.py` i `scripts/test-lmstudio-unit-tests-mcp.py` zostają w repo jako materiał do ewentualnego powrotu później
- repo `finanse-app` nie ma jeszcze skonfigurowanego standardowego runnera testów jednostkowych ani skryptu `test`

To oznacza, że na teraz testy i planowanie testów robimy bezpośrednio przez Codexa oraz lokalne komendy projektu.

## Podział ról modeli

### Codex

Codex jest głównym narzędziem do:

- zmian wieloplikowych,
- zadań wymagających szerokiego kontekstu projektu,
- decyzji technicznych i architektonicznych,
- review zmian,
- naprawy problemów po nieudanej pierwszej implementacji,
- aktualizacji wiki i stanu projektu.

### LM Studio / lokalny model

Lokalny model jest odłożonym pomysłem pomocniczym do:

- generowania pierwszej wersji testów jednostkowych,
- generowania listy przypadków testowych,
- dopisywania edge case'ów,
- generowania fixture'ów testowych,
- szybkiego rozpisania mocków dla jednego modułu.

Nie jest obecnie częścią obowiązkowego workflow Codexa.

## Główna zasada

Lokalny model nie jest źródłem prawdy dla projektu.

Jeżeli wrócimy do tego później, lokalny model ma generować materiał roboczy, który potem:

- trafia do `finanse-app`,
- jest uruchamiany lokalnie,
- jest poprawiany ręcznie albo przez `Codexa`, jeśli wymaga szerszego kontekstu.
- wymaga działającego daemonu albo otwartej aplikacji `LM Studio`

## Kiedy ewentualnie wrócić do LM Studio

Do lokalnego modelu warto wrócić dopiero, gdy:

- MCP startuje stabilnie bez timeoutów
- `finanse-app` ma ustalony runner testów i skrypt `test`
- testujesz jedną funkcję, parser, formatter albo walidator,
- testujesz jedną małą warstwę danych,
- potrzebujesz tylko jednego pliku testowego,
- zależy Ci bardziej na obniżeniu kosztu tokenów niż na szerokim rozumieniu całego repo.

Najlepsze cele w naszym projekcie:

- `src/shared`
- czyste helpery i utilsy
- logika dat, formatowania i walidacji
- małe funkcje domenowe
- logika repozytoriów i mapperów, jeśli da się je izolować

## Kiedy nie używać LM Studio jako głównego narzędzia

Nie używaj lokalnego modelu jako głównego narzędzia, gdy:

- zmiana dotyka wielu plików naraz,
- test wymaga zrozumienia nawigacji, providerów albo storage bootstrapu,
- trzeba jednocześnie poprawić kod i testy,
- trzeba zaktualizować wiki,
- trzeba wykonać review albo podjąć decyzję techniczną,
- problem jest bardziej diagnostyczny niż generacyjny.

## Minimalny workflow dla testów jednostkowych

Aktualny minimalny workflow:

1. Wybierz dokładnie jeden plik albo jedną funkcję do przetestowania.
2. Ogranicz prompt Codexa do minimalnego kontekstu.
3. Poproś o test cases albo jeden plik testowy, bez szerokiego review całego repo.
4. Uruchom lokalnie dostępne komendy projektu, np. `lint` i `typecheck`.
5. Jeżeli test runner zostanie później dodany, uruchamiaj najpierw testy obszaru, którego dotyczy zmiana.

## Reguły oszczędzania tokenów

- nie przekazuj całego repo do lokalnego modelu
- nie wrzucaj całych długich notatek z wiki do promptu testowego
- generuj jeden plik testowy naraz
- najpierw proś o listę przypadków, a dopiero potem o pełny plik, jeśli logika jest niejasna
- proś o brak wyjaśnień, jeśli zależy Ci głównie na kodzie
- używaj lokalnego modelu do boilerplate'u, a nie do całego złożonego tasku implementacyjnego

## Szablon promptu do lokalnego modelu

Gotowy plik do skopiowania:

- `03 Technologia/PROMPT LM STUDIO - testy jednostkowe.txt`

```text
You are writing unit tests only.

Project:
- Expo + React Native + TypeScript
- Write tests only for the provided file
- Do not redesign production code
- Do not explain the solution

Target:
- file under test: [tu wklej ścieżkę]
- test runner: [Jest / Vitest / not configured yet]

Task:
- generate unit tests for the provided function or module
- cover normal cases, edge cases, and invalid input where relevant
- keep mocks minimal

Output rules:
- return only the test file content
- do not add commentary
- do not modify unrelated files

Context:
[tu wklej tylko potrzebny kod]
```

## Integracja z Codexem

Status integracji:

- `lmstudio_unit_tests` nie jest obecnie zarejestrowany jako MCP
- Codex nie powinien próbować używać tego narzędzia na starcie sesji
- powrót do tej integracji wymaga osobnej decyzji i testu startu MCP

Ten temat zostaje odłożony, a nie usunięty z projektu.

## Praktyczny podział pracy dla naszego projektu

Rekomendowany podział:

- `Codex`:
  - update'y wdrożeniowe,
  - architektura,
  - integracja wielu plików,
  - porządkowanie kodu,
  - review,
  - aktualizacja wiki,
  - testy i planowanie testów
- `LM Studio`:
  - odłożone do czasu stabilnego MCP i runnera testów

## Ważne ograniczenie na dziś

Największe braki w obecnym workflow są proste:

- `finanse-app` nie ma jeszcze jednego ustalonego runnera testów jednostkowych
- MCP `lmstudio-unit-tests` timeoutował przy starcie Codexa

Przed powrotem do lokalnego generowania testów trzeba domknąć:

- wybór narzędzia testowego,
- skrypt `test` w `package.json`,
- minimalną konwencję dla lokalizacji plików testowych,
- sposób uruchamiania testów w VS Code i z terminala.

## Rekomendacja praktyczna

Najprostszy model pracy na teraz:

1. `Codex` prowadzi projekt i większe zmiany.
2. `Codex` generuje albo planuje wąskie testy, jeśli są potrzebne.
3. Lokalnie uruchamiamy dostępne komendy, bez wklejania długich logów do czatu.
4. `LM Studio` wraca dopiero po osobnym naprawieniu MCP.

To usuwa timeouty przy starcie Codexa i upraszcza sesje robocze.
