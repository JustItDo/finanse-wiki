# 01 Historia - filtry i domyślny zakres

## Powiązane notatki

- [[README|Inbox - rozpisane updatey]]
- [[../Inbox zmian|Inbox zmian]]
- [[../Backlog|Backlog]]
- [[../Plan wdrożeń feedbacku testerskiego|Plan wdrożeń feedbacku testerskiego]]

## Cel update'u

Uprościć ekran historii tak, żeby podstawowe przeglądanie transakcji było szybkie, a dodatkowe filtry nie zajmowały stale miejsca na telefonie.

## Wybrany wariant

`1B`:

- `Szukaj` na górze
- `Typ` jako segment
- reszta filtrów pod przyciskiem `Filtry aktywne: X`
- domyślnie `Wszystkie miesiące`
- sortowanie najnowsze na górze

## Opis UX

Na ekranie historii użytkownik od razu widzi pole `Szukaj`, segment typu transakcji i listę najnowszych wpisów. Domyślny zakres to `Wszystkie miesiące`, więc starsze transakcje nie są ukryte przez aktualny miesiąc.

Dodatkowe filtry, takie jak miesiąc, kategoria albo inne przyszłe kryteria, są schowane pod jednym przyciskiem `Filtry aktywne: X`. Liczba pokazuje tylko aktywne filtry poza domyślnym stanem. Po kliknięciu użytkownik rozwija panel filtrów albo przechodzi do kompaktowego selektora.

## Zakres wdrożenia

- ustawić domyślny zakres historii na `Wszystkie miesiące`
- zapewnić sortowanie historii od najnowszych transakcji do najstarszych
- zostawić `Szukaj` jako pierwszą kontrolkę ekranu
- zostawić `Typ` jako stale widoczny segment
- schować pozostałe filtry pod kontrolką `Filtry aktywne: X`
- pokazywać liczbę aktywnych filtrów zgodnie ze stanem filtrów
- dopasować puste stany do nowego domyślnego zakresu

## Poza zakresem

- przebudowa szczegółu transakcji
- nowe typy filtrów, których nie ma jeszcze w danych
- zaawansowane sortowanie wybierane przez użytkownika
- zmiany w dashboardzie

## Ryzyka

- użytkownik może nie zauważyć schowanych filtrów, jeśli przycisk będzie zbyt mało widoczny
- licznik aktywnych filtrów może mylić, jeśli domyślne wartości będą liczone jako aktywne
- zbyt ciężki panel filtrów może przenieść problem przeładowania z listy do rozwijanego widoku

## Kryteria akceptacji

- po wejściu w historię widoczne są transakcje ze wszystkich miesięcy
- najnowsze transakcje są na górze listy
- `Szukaj` i `Typ` są dostępne bez rozwijania filtrów
- pozostałe filtry są dostępne pod `Filtry aktywne: X`
- licznik filtrów rośnie tylko wtedy, gdy użytkownik ustawi filtr inny niż domyślny
- puste stany jasno odróżniają brak transakcji od braku wyników filtrowania

## Test ręczny na telefonie

- otworzyć historię po kilku transakcjach z różnych miesięcy i potwierdzić, że domyślnie widać wszystkie miesiące
- sprawdzić, czy najnowszy wpis jest pierwszy
- wyszukać transakcję po nazwie albo kwocie
- przełączyć segment `Typ` i sprawdzić wynik listy
- rozwinąć `Filtry aktywne: X`, ustawić miesiąc lub kategorię i sprawdzić licznik
- wyczyścić filtry i sprawdzić powrót do pełnej listy

## Prompt do późniejszego wdrożenia w `Codex: Finanse`

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox - rozpisane updatey/01 Historia - filtry i domyślny zakres.md`
- `03 Technologia/Stan repo aplikacji.md`

Cel:
Wdrożyć wariant `1B` dla historii: `Szukaj` na górze, `Typ` jako segment, pozostałe filtry pod `Filtry aktywne: X`, domyślnie `Wszystkie miesiące`, sortowanie najnowsze na górze.

Zasady:
- pracuj konkretnie w `finanse-app`
- nie wdrażaj innych update'ów z inboxu
- po zmianach uruchom dostępne sprawdzenia jakości
- zaktualizuj wiki tylko wtedy, gdy zmieni się status wdrożenia albo decyzja produktowa

Na końcu podaj zmienione pliki, wynik weryfikacji i test ręczny na telefonie.
```

