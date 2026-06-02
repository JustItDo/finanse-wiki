# 06 Analiza - wybór okresu

## Powiązane notatki

- [[README|Inbox - rozpisane updatey]]
- [[../Inbox zmian|Inbox zmian]]
- [[../Backlog|Backlog]]
- [[../Plan wdrożeń feedbacku testerskiego|Plan wdrożeń feedbacku testerskiego]]

## Cel update'u

Rozszerzyć ekran `Analizy` o wygodny wybór okresu, żeby użytkownik mógł oglądać dane nie tylko dla bieżącego i poprzedniego miesiąca.

## Wybrany wariant

`6C`:

- kompaktowy przycisk z aktualnym okresem
- po kliknięciu bottom sheet / wysuwany wybór zakresu

## Opis UX

Na górze analizy widoczny jest kompaktowy przycisk z aktualnym okresem, np. `Ten miesiąc`, `3 miesiące`, `6 miesięcy`, `Cały okres`. Po kliknięciu pojawia się wysuwany selektor z listą zakresów.

Wybór okresu odświeża wszystkie agregacje na ekranie analizy. Przycisk pozostaje mały, żeby nie zabierał miejsca wykresom.

## Zakres wdrożenia

- zastąpić obecny przełącznik miesięcy kompaktowym przyciskiem okresu
- dodać wysuwany selektor zakresu
- obsłużyć zakresy: `Ten miesiąc`, `Poprzedni miesiąc`, `3 miesiące`, `6 miesięcy`, `Rok`, `Cały okres`
- dostosować agregacje analizy do zakresów wielomiesięcznych
- zaktualizować copy pustych stanów dla dłuższych okresów
- zachować czytelność na telefonie

## Poza zakresem

- własny zakres dat wybierany z kalendarza
- zmiana dashboardu
- eksport danych z analizy
- zaawansowane porównania okres do okresu

## Ryzyka

- obecne agregacje mogą być zbyt miesięczne i wymagać ostrożnego uogólnienia
- `Cały okres` przy dużej liczbie transakcji może wymagać optymalizacji
- bottom sheet może wymagać dodatkowej biblioteki albo prostego własnego wariantu

## Kryteria akceptacji

- użytkownik widzi aktualny okres na kompaktowym przycisku
- po kliknięciu może wybrać jeden z predefiniowanych zakresów
- wykresy i listy analizy odświeżają się po zmianie zakresu
- `Cały okres` pokazuje dane ze wszystkich transakcji
- ekran nadal jest czytelny na telefonie
- brak danych pokazuje komunikat dopasowany do wybranego okresu

## Test ręczny na telefonie

- otworzyć analizę i sprawdzić domyślny okres
- otworzyć selektor okresu i wybrać każdy predefiniowany zakres
- porównać, czy wartości zmieniają się między miesiącem, 6 miesiącami i całym okresem
- sprawdzić ekran bez danych dla wybranego okresu
- zamknąć selektor gestem lub przyciskiem i upewnić się, że wybór nie zmienił się przypadkiem

## Prompt do późniejszego wdrożenia w `Codex: Finanse`

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox - rozpisane updatey/06 Analiza - wybór okresu.md`
- `03 Technologia/Stan repo aplikacji.md`

Cel:
Wdrożyć wariant `6C`: kompaktowy przycisk aktualnego okresu w analizie i wysuwany selektor zakresu.

Zasady:
- nie zmieniaj dashboardu w tym update'cie
- użyj najprostszego rozwiązania zgodnego z obecną architekturą UI
- dostosuj agregacje analizy do zakresów wielomiesięcznych
- po zmianach uruchom dostępne sprawdzenia jakości

Na końcu podaj zmienione pliki, wynik weryfikacji i test ręczny na telefonie.
```

