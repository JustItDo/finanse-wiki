# 09 Historia - inline szczegóły i edycja transakcji

## Powiązane notatki

- [[../Inbox zmian|Inbox zmian]]
- [[01 Historia - filtry i domyślny zakres]]

## Cel

Zmienić historię tak, aby szczegóły transakcji rozwijały się po kliknięciu w element listy.

Zamiast panelu szczegółów na dole, użytkownik ma widzieć edycję bezpośrednio przy transakcji, której dotyczy.

## Warianty

### Wariant A

- klik rozwija tylko podgląd read-only
- osobny przycisk `Edytuj` otwiera istniejący formularz
- mniejsze ryzyko, ale mniej wygodne

### Wariant B

- klik w transakcję rozwija inline szczegóły i formularz
- jedna transakcja rozwinięta naraz
- `Edytuj`, `Zapisz`, `Anuluj` w tym samym elemencie
- **rekomendowany wariant**

### Wariant C

- zamiast inline użyć bottom sheet albo modala
- technicznie czystsze niż dynamiczne rozpinanie listy
- słabsze rozwiązanie dla długiej listy

## Rekomendacja

`Wariant B`.

Najlepiej rozwiązuje problem przewijania na dół przy dużej liczbie transakcji i daje jasny kontekst, którą pozycję edytujemy.

## Zakres

- rozwijanie aktywnego elementu historii
- przeniesienie szczegółów pod kliknięty rekord
- zachowanie istniejącej walidacji edycji
- jedna rozwinięta transakcja naraz

## Poza zakresem

- przebudowa całego modelu historii
- wieloselekcyjna edycja
- nowy system filtrowania

## Ryzyka

- konflikt z aktualnym `FlatList`
- problem z wysokością elementów i scrollowaniem
- ukrywanie przycisków usuwania lub zapisu, jeśli element będzie za wysoki

## Kryteria Akceptacji

- kliknięcie transakcji rozwija jej szczegóły na miejscu
- użytkownik może zmienić atrybuty i zapisać bez przewijania do dołu
- nie ma jednocześnie wielu rozwiniętych transakcji
- lista nadal działa płynnie przy większej liczbie wpisów

## Test Telefonu

- wejść w historię
- kliknąć transakcję z góry listy
- sprawdzić rozwinięcie inline
- zmienić pola
- zapisać
- przewinąć listę i sprawdzić, czy nie rozjeżdża się layout

## Prompt Do Codexa

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox zmian.md`
- `04 Plan/Inbox - rozpisane updatey/09 Historia - inline szczegóły i edycja transakcji.md`
- `04 Plan/Inbox - rozpisane updatey/01 Historia - filtry i domyślny zakres.md`

Cel:
Przenieść szczegóły i edycję transakcji bezpośrednio do rozwijanego elementu historii.

Zakres:
- kliknięcie transakcji rozwija jej szczegóły inline
- edycja, zapis i anulowanie są w tym samym elemencie
- jedna transakcja rozwinięta naraz

Zasady:
- pracuj konkretnie w plikach historii
- nie rozbijaj tego na modal, jeśli inline da się zrobić sensownie
- nie zmieniaj logiki walidacji bardziej niż trzeba
- po zmianach opisz, jak działa rozwijanie i jak obsługiwane jest zamykanie

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```

