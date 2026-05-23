# Pomysły produktowe

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[MVP]]
- [[Funkcje aplikacji]]
- [[Sukces MVP]]
- [[../04 Plan/Roadmapa|Roadmapa]]
- [[../04 Plan/Backlog|Backlog]]

## Kierunek produktu
Aplikacja nie powinna być tylko rejestrem wydatków.

Docelowo ma działać jak osobisty panel kontroli budżetu, który po każdym nowym wydatku od razu pokazuje użytkownikowi, co się zmieniło i jaki to ma wpływ na miesiąc.

## Pomysły według istotności i etapu

### Krytyczne dla produktu

#### Etap: MVP
- budżety kategorii na miesiąc
  Istotność: krytyczna
  Powód: bez tego aplikacja nie kontroluje budżetu, tylko zapisuje historię wydatków.
- licznik ile zostało w budżecie dla każdej kategorii
  Istotność: krytyczna
  Powód: użytkownik musi od razu widzieć, ile jeszcze może wydać.
- licznik ile zostało z całego budżetu miesiąca
  Istotność: krytyczna
  Powód: to jeden z najważniejszych wskaźników dla codziennego użycia.
- możliwość dodawania nie tylko zdjęć paragonów, ale też screenshotów płatności
  Istotność: krytyczna
  Powód: to realnie zwiększa częstotliwość używania aplikacji.
- szybka informacja po dodaniu wydatku: ile zostało w danej kategorii i jak zmienił się bilans
  Istotność: krytyczna
  Powód: aplikacja ma pokazywać konsekwencję wydatku od razu po zapisie.
- automatyczna sugestia kategorii na podstawie sklepu, treści paragonu i historii użytkownika
  Istotność: wysoka
  Powód: mocno skraca proces dodawania wpisu, ale może działać początkowo prościej.
- cel oszczędności i podstawowe obliczanie postępu
  Istotność: wysoka
  Powód: sama kontrola wydatków bez celu oszczędnościowego daje mniejszy efekt.
- limit dzienny do końca miesiąca
  Istotność: wysoka
  Powód: bardzo praktyczny wskaźnik dla zwykłego użytkownika.

### Bardzo ważne po MVP

#### Etap: V1 po sprawdzeniu podstaw
- alert typu: w tej kategorii wydajesz więcej niż zwykle
  Istotność: wysoka
  Powód: pomaga wychwycić problem wcześnie, ale wymaga już trochę danych historycznych.
- automatyczne podsumowania tygodniowe i miesięczne
  Istotność: wysoka
  Powód: zwiększa wartość analityczną bez dokładania pracy użytkownikowi.
- insighty typu: na co poszło najwięcej pieniędzy w tym tygodniu lub miesiącu
  Istotność: wysoka
  Powód: użytkownik dostaje gotowe wnioski, nie tylko suche wykresy.
- wykrywanie stałych opłat i subskrypcji
  Istotność: wysoka
  Powód: stałe koszty to jeden z najczęstszych problemów w domowym budżecie.
- podział wydatków na potrzeby i zachcianki
  Istotność: średnio-wysoka
  Powód: bardzo pomaga w budowaniu świadomości finansowej.
- top 3 kategorie drenażu budżetu
  Istotność: średnio-wysoka
  Powód: prosty sposób pokazania, gdzie realnie uciekają pieniądze.

### Wartościowe, ale nie na start

#### Etap: V2 i dalszy rozwój
- rozbijanie jednego paragonu na kilka kategorii
  Istotność: średnia
  Powód: przydatne, ale zwiększa złożoność OCR i edycji danych.
- wykrywanie nietypowych wzrostów wydatków
  Istotność: średnia
  Powód: wymaga lepszego modelu analitycznego i stabilniejszej historii danych.
- inteligentne sugestie oszczędzania na podstawie historii wydatków
  Istotność: średnia
  Powód: duża wartość, ale dopiero gdy baza danych użytkownika jest wystarczająco bogata.
- bardziej spersonalizowany dashboard
  Istotność: średnia
  Powód: użyteczne, ale nie poprawia kluczowego core'u na starcie.
- wydatki stałe z automatycznym przypomnieniem
  Istotność: średnia
  Powód: sensowne rozszerzenie po dopracowaniu zwykłych transakcji.

## Wnioski
Największą wartością produktu ma być połączenie:

- prostoty codziennego dodawania wydatków,
- wygodnego OCR i obsługi screenshotów,
- czytelnej analizy danych,
- realnego wpływu na kontrolę budżetu i oszczędzanie.

## Rekomendacja wdrożeniowa
Nie ma sensu robić wszystkiego na start.

Najpierw trzeba doprowadzić do bardzo dobrej jakości:

- dodawanie wydatków,
- budżety kategorii,
- informację o wpływie wydatku na miesiąc,
- podstawowe wykresy i podsumowania.

Dopiero potem warto dokładać inteligencję, alerty i bardziej zaawansowane insighty.
