# 10B Rebranding v2 - wdrożenie w kodzie

## Powiązane notatki

- [[10A Rebranding v2 - kolory i logo]]
- [[10 Rebranding v2 - nowe logo i żywszy UI]]
- [[../Inbox zmian|Inbox zmian]]

## Cel

Wdrożyć w `finanse-app` wybrane decyzje z `10A`.

Ten etap zaczynamy dopiero po tym, jak paleta i kierunek logo są już wybrane.

## Warunek Startu

Nie zaczynać wdrożenia, jeśli nie ma decyzji z `10A`:

- finalna paleta HEX
- zasady użycia kolorów
- wybrany kierunek logo
- wskazanie, które assety mają zostać podmienione

## Zakres

- podmienić lub przygotować assety logo / app icon
- zaktualizować tokeny kolorów w aplikacji
- uporządkować kolory jako semantyczne tokeny motywu, a nie luźne HEX-y po ekranach
- dodać żywsze akcenty w CTA, sukcesach, wykresach i stanach
- zachować czytelność danych finansowych
- nie robić pełnego redesignu wszystkich ekranów

## Zasada Theme Tokens

Rebranding nie może polegać na rozrzuceniu nowych HEX-ów po komponentach.

Kolory mają być opisane jako tokeny, np.:

- `background`
- `surface`
- `surfaceMuted`
- `text`
- `textMuted`
- `border`
- `primary`
- `primarySoft`
- `success`
- `warning`
- `danger`
- `income`
- `expense`
- `cta`
- `accent`

Docelowo struktura powinna ułatwić późniejsze dodanie:

- `lightTheme`
- `darkTheme`
- `paletteId`
- przełącznika motywu w ustawieniach
- wyboru gotowej kolorystyki z update'u [[12 Motywy kolorystyczne - wybór palety]]

W tym update nie wdrażamy jeszcze dark mode, ale nie wolno robić zmian w sposób, który utrudni update [[11 Tryb ciemny i system motywów]].
Nie wolno też zamknąć struktury kolorów tak, żeby późniejszy wybór palety wymagał przepisywania ekranów.

## Sugerowane Obszary Kodu

- `app.json`
- `assets/`
- `src/shared/theme/index.ts`
- wspólne komponenty UI
- dashboard i podstawowe ekrany, jeśli korzystają z twardych kolorów

## Poza Zakresem

- tryb ciemny
- pełny system motywów
- przebudowa layoutów
- zmiana nazwy aplikacji

Tryb ciemny jest osobnym update'em:

- [[11 Tryb ciemny i system motywów]]

Wybór kilku gotowych palet jest osobnym update'em:

- [[12 Motywy kolorystyczne - wybór palety]]

## Ryzyka

- zmiana tokenów może ujawnić hardcodowane kolory w ekranach
- zbyt mocny akcent może pogorszyć czytelność kwot
- asset logo może wymagać osobnego przygotowania PNG pod Expo / Android

## Kryteria Akceptacji

- aplikacja używa nowych kolorów z decyzji `10A`
- logo / icon asset jest spójny z nowym kierunkiem
- nowe kolory są zdefiniowane w theme tokens, a nie wpisane ręcznie w ekranach
- struktura theme jest przygotowana pod późniejsze `lightTheme` / `darkTheme`
- struktura theme nie blokuje późniejszego `paletteId`
- dashboard i główne CTA wyglądają żywiej
- teksty i dane finansowe są nadal czytelne
- zmiana nie obejmuje dark mode

## Test Telefonu

- sprawdzić ikonę aplikacji
- sprawdzić splash / start aplikacji, jeśli asset jest używany
- sprawdzić dashboard
- sprawdzić dodawanie transakcji
- sprawdzić historię i ustawienia pod kątem kontrastu

## Prompt 2 - wdrożenie zmian w kodzie

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox - rozpisane updatey/10A Rebranding v2 - kolory i logo.md`
- `04 Plan/Inbox - rozpisane updatey/10B Rebranding v2 - wdrożenie w kodzie.md`
- `04 Plan/Inbox - rozpisane updatey/10 Rebranding v2 - nowe logo i żywszy UI.md`

Cel:
Wdrożyć w kodzie decyzje rebrandingowe wybrane w `10A`.

Warunek:
Jeśli w `10A` nie ma finalnie wybranej palety i kierunku logo, zatrzymaj się i najpierw poproś o decyzję. Nie wdrażaj kolorów na podstawie domysłów.

Zakres:
- podmień lub przygotuj assety logo / app icon
- zaktualizuj tokeny kolorów w `src/shared/theme`
- uporządkuj kolory jako semantyczne theme tokens zamiast rozsypywania HEX-ów po ekranach
- przygotuj strukturę tak, żeby później dało się dodać `lightTheme` i `darkTheme`
- podbij żywsze akcenty dla CTA, sukcesów, wykresów i ważnych stanów
- zachowaj czytelność danych finansowych
- popraw tylko miejsca, które bezpośrednio wynikają z rebrandingu

Poza zakresem:
- nie wdrażaj dark mode
- nie przebudowuj całych ekranów
- nie zmieniaj nawigacji
- nie zmieniaj logiki danych
- nie wpisuj nowych kolorów bezpośrednio w komponentach, jeśli można dodać token w theme

Na końcu:
- podaj, które assety i tokeny zostały zmienione
- wskaż, czy zostały jeszcze hardcodowane kolory do osobnej poprawki
- podaj, co sprawdzić ręcznie na telefonie

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```
