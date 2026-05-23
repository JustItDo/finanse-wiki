# Model budżetu

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[MVP]]
- [[Kategorie]]
- [[Źródła przychodów]]
- [[../03 Technologia/Model danych implementacyjny|Model danych implementacyjny]]
- [[../04 Plan/Updatey wdrożeniowe/00.3 Kategorie i budżet startowy|Update 0.3 - Kategorie i budżet startowy]]
- [[../04 Plan/Updatey wdrożeniowe/03.0 Budżety|Update 3.0 - Budżety]]
- [[../04 Plan/Updatey wdrożeniowe/03.2 Oszczędności|Update 3.2 - Oszczędności]]

## Wybrany model na start
Wybrany został `Model 2: Zbalansowany`.

To jest model rekomendowany na MVP, ponieważ daje realną kontrolę nad finansami, ale nadal pozostaje prosty i praktyczny dla codziennego użycia.

## Jak działa ten model
- budżet działa w cyklu `kalendarzowym miesięcznym`
- użytkownik ustawia `budżet główny na miesiąc`
- użytkownik ustawia `budżety kategorii`
- każdy wydatek:
  - trafia do odpowiedniej kategorii,
  - pomniejsza budżet tej kategorii,
  - wpływa na budżet całego miesiąca
- przekroczenie budżetu kategorii jest dozwolone, ale aplikacja pokazuje ostrzeżenie
- po każdym dodaniu wydatku aplikacja pokazuje:
  - ile zostało w kategorii,
  - ile zostało w całym miesiącu,
  - jaki jest wpływ na bilans i plan miesiąca

## Założenia MVP
- miesiąc liczony jest kalendarzowo
- budżety kategorii nie przenoszą się automatycznie na kolejny miesiąc
- aplikacja ma wspierać użytkownika, a nie blokować wydatki
- priorytetem jest prostota oraz szybkie zrozumienie sytuacji finansowej

## Dlaczego ten model został wybrany
- jest dużo bardziej użyteczny niż prosty rejestr wydatków
- dobrze wspiera główny cel aplikacji, czyli kontrolę budżetu i oszczędzanie
- dobrze pasuje do flow z paragonami i screenshotami
- nadaje się do wdrożenia w MVP bez nadmiernej komplikacji logiki produktu

## Co odkładamy na później
W późniejszych iteracjach produkt może wejść w bardziej złożony model budżetowania, na przykład:

- bardziej rozbudowane reguły budżetowe
- budżet liczony od wypłaty do wypłaty
- przenoszenie części środków między okresami
- rozróżnienie wydatków na potrzeby i zachcianki
- bardziej zaawansowane analizy i rekomendacje

To może być przyszły kierunek rozwoju produktu, a część tych funkcji może w przyszłości trafić do bardziej zaawansowanej, płatnej warstwy aplikacji.
