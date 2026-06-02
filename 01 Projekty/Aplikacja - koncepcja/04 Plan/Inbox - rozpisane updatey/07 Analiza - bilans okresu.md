# 07 Analiza - bilans okresu

## Powiązane notatki

- [[README|Inbox - rozpisane updatey]]
- [[../Inbox zmian|Inbox zmian]]
- [[../Backlog|Backlog]]
- [[../Plan wdrożeń feedbacku testerskiego|Plan wdrożeń feedbacku testerskiego]]
- [[06 Analiza - wybór okresu]]

## Cel update'u

Dodać do analizy mocną kartę bilansu dla wybranego okresu, żeby użytkownik szybko widział, czy w danym zakresie jest finansowo na plusie czy na minusie.

## Wybrany wariant

`7B`:

- karta z mocnym wynikiem bilansu
- mały breakdown: przychody, wydatki, wynik

## Opis UX

Na ekranie analizy pojawia się karta `Bilans okresu`. Największym elementem jest wynik: przychody minus wydatki. Pod spodem znajduje się mały breakdown: `Przychody`, `Wydatki`, `Wynik`.

Copy musi jasno mówić, że to bilans zapisanych transakcji w aplikacji, a nie aktualny stan konta bankowego.

## Zakres wdrożenia

- dodać kartę `Bilans okresu` do ekranu `Analizy`
- wyliczać przychody, wydatki i wynik dla aktualnego zakresu analizy
- użyć mocnego formatowania wyniku dodatniego, zerowego i ujemnego
- dodać krótkie wyjaśnienie, że wynik dotyczy danych zapisanych w aplikacji
- jeśli [[06 Analiza - wybór okresu]] nie jest jeszcze wdrożony, ograniczyć kartę do obecnego zakresu analizy

## Poza zakresem

- podpinanie realnego salda bankowego
- prognozy przyszłych wydatków
- szczegółowa analiza cashflow
- zmiana sposobu liczenia oszczędności na dashboardzie

## Ryzyka

- użytkownik może pomylić bilans z saldem konta
- karta może dublować istniejące miesięczne podsumowanie, jeśli copy nie będzie precyzyjne
- wdrożenie przed wyborem okresu ograniczy użyteczność do obecnego zakresu analizy

## Kryteria akceptacji

- analiza pokazuje kartę `Bilans okresu`
- karta pokazuje przychody, wydatki i wynik
- wynik jest liczony jako `przychody - wydatki`
- karta reaguje na aktualny zakres analizy, jeśli wybór okresu jest dostępny
- copy nie sugeruje, że to saldo rachunku bankowego
- brak danych pokazuje zrozumiały stan zerowy

## Test ręczny na telefonie

- dodać przychód i wydatek w tym samym okresie
- otworzyć analizę i sprawdzić wynik bilansu
- sprawdzić wariant dodatni, ujemny i zerowy
- jeśli wybór okresu istnieje, zmienić okres i sprawdzić przeliczenie karty
- sprawdzić copy dla pustego okresu bez transakcji

## Prompt do późniejszego wdrożenia w `Codex: Finanse`

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox - rozpisane updatey/07 Analiza - bilans okresu.md`
- `04 Plan/Inbox - rozpisane updatey/06 Analiza - wybór okresu.md`
- `03 Technologia/Stan repo aplikacji.md`

Cel:
Wdrożyć wariant `7B`: kartę `Bilans okresu` w analizie z mocnym wynikiem i breakdownem `Przychody`, `Wydatki`, `Wynik`.

Zasady:
- wynik licz jako `przychody - wydatki`
- nie sugeruj, że to saldo konta bankowego
- jeśli wybór okresu jest już wdrożony, karta ma reagować na aktualny okres
- jeśli wybór okresu nie jest wdrożony, ogranicz kartę do obecnego zakresu analizy i opisz to w finalu
- po zmianach uruchom dostępne sprawdzenia jakości

Na końcu podaj zmienione pliki, wynik weryfikacji i test ręczny na telefonie.
```

