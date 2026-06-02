# 03 Budżety - limit 0 jako bez limitu

## Powiązane notatki

- [[README|Inbox - rozpisane updatey]]
- [[../Inbox zmian|Inbox zmian]]
- [[../Backlog|Backlog]]
- [[../Plan wdrożeń feedbacku testerskiego|Plan wdrożeń feedbacku testerskiego]]

## Cel update'u

Uprościć ustawianie limitów kategorii: `0 zł` ma oficjalnie oznaczać `Bez limitu`, bez dodatkowego przełącznika i bez pełnego przepisywania modelu danych.

## Wybrany wariant

`3B`:

- `0 zł` oficjalnie oznacza `Bez limitu`
- uwzględnić to w UI i walidacji
- bez pełnego przepisywania modelu danych

## Opis UX

W szczególe kategorii użytkownik wpisuje kwotę limitu. Jeśli wartość wynosi `0 zł`, UI pokazuje stan `Bez limitu`. Jeśli wartość jest większa od zera, kategoria jest traktowana jako kategoria z limitem.

Użytkownik nie musi osobno włączać albo wyłączać limitu. Komunikaty budżetowe nie powinny straszyć przekroczeniem dla kategorii z limitem `0 zł`.

## Zakres wdrożenia

- uznać `0 zł` za oficjalny brak limitu w logice UI
- poprawić walidację formularza limitu, żeby `0` było poprawną wartością
- pokazywać `Bez limitu` zamiast kwoty limitu tam, gdzie limit wynosi `0`
- upewnić się, że kategoria z limitem `0` nie generuje stanu przekroczenia
- zachować istniejący model danych, jeśli da się to zrobić bez migracji
- doprecyzować copy w budżetach i szczególe kategorii

## Poza zakresem

- pełna migracja modelu danych budżetów
- nowe typy limitów
- limity dzienne lub tygodniowe
- rozbudowane alerty przekroczeń

## Ryzyka

- w istniejącej logice `0` może już oznaczać coś technicznego i wymagać ostrożnego sprawdzenia
- rozróżnienie między brakiem rekordu limitu a limitem `0` może powodować niespójne listy
- kategorie przychodów mogą wymagać osobnego traktowania, żeby nie dostały niepotrzebnego języka limitów

## Kryteria akceptacji

- użytkownik może zapisać limit `0 zł`
- po zapisaniu `0 zł` kategoria pokazuje `Bez limitu`
- kategoria z limitem `0 zł` nie pokazuje przekroczenia ani procentu wykorzystania jako błędu
- wpisanie wartości większej niż `0 zł` aktywuje zwykły limit
- istniejące kategorie bez limitu nadal działają poprawnie
- nie ma pełnej migracji modelu danych, jeśli nie jest technicznie konieczna

## Test ręczny na telefonie

- wejść w kategorię wydatkową i ustawić limit `0 zł`
- wrócić do listy budżetów i sprawdzić, czy kategoria jest w stanie `Bez limitu`
- dodać wydatek w tej kategorii i sprawdzić, czy nie pojawia się przekroczenie limitu
- zmienić limit na kwotę większą niż `0 zł` i sprawdzić zwykłe liczenie wykorzystania
- ponownie ustawić `0 zł` i sprawdzić powrót do `Bez limitu`

## Prompt do późniejszego wdrożenia w `Codex: Finanse`

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox - rozpisane updatey/03 Budżety - limit 0 jako bez limitu.md`
- `03 Technologia/Stan repo aplikacji.md`

Cel:
Wdrożyć wariant `3B`: `0 zł` jako oficjalne `Bez limitu` w budżetach kategorii, w UI i walidacji, bez pełnego przepisywania modelu danych.

Zasady:
- najpierw sprawdź istniejącą logikę budżetów i walidacji
- nie rób dużej migracji, jeśli da się zachować obecny model
- upewnij się, że `0 zł` nie generuje przekroczeń budżetu
- po zmianach uruchom dostępne sprawdzenia jakości

Na końcu podaj zmienione pliki, wynik weryfikacji i test ręczny na telefonie.
```

