# Ekrany aplikacji

## Cel
Ta notatka opisuje ekran po ekranie, jak ma wyglądać MVP aplikacji.

Założenie:
- główny ekran ma być prosty,
- ważne funkcje mają być łatwo dostępne,
- bardziej rozbudowane rzeczy mają być rozdzielone na osobne ekrany.

## 1. Dashboard

### Cel ekranu
Dać użytkownikowi szybki obraz sytuacji finansowej po otwarciu aplikacji.

### Co ma być widoczne
- stan miesiąca:
  - przychody
  - wydatki
  - bilans
- ile zostało z budżetu miesiąca
- 3 do 5 najważniejszych kategorii budżetowych
- szybki przycisk dodania wydatku
- lista ostatnich transakcji
- jeden prosty wykres wydatków według kategorii

### Najważniejsze akcje
- dodaj wydatek
- dodaj przychód
- przejdź do historii
- przejdź do budżetów
- przejdź do analiz

### Założenia UX
- ekran ma być prosty i szybki do zeskanowania wzrokiem
- nie pokazujemy tu wszystkiego
- bardziej szczegółowe analizy są na osobnych ekranach

## 2. Dodaj wydatek / przychód

### Cel ekranu
Pozwolić szybko dodać nową transakcję.

### Tryby dodawania
- ręcznie
- przez zdjęcie paragonu
- przez screen płatności

### Co ma być widoczne
- wybór typu:
  - wydatek
  - przychód
- pole kwoty
- wybór kategorii
- data
- opis opcjonalny
- metoda płatności
- przycisk dodania zdjęcia albo screena
- przycisk zapisu

### Najważniejsze akcje
- wpisz dane ręcznie
- dodaj zdjęcie
- dodaj screen
- zapisz transakcję

### Założenia UX
- ręczne dodanie ma być bardzo szybkie
- użytkownik nie może czuć, że aplikacja zmusza go do OCR
- formularz ma być prosty i krótki

## 3. Podgląd i korekta OCR

### Cel ekranu
Pozwolić użytkownikowi szybko sprawdzić i poprawić dane odczytane z paragonu albo screena.

### Co ma być widoczne
- podgląd obrazu
- wykryta kwota
- wykryta data
- wykryty sklep lub źródło
- sugerowana kategoria
- możliwość ręcznej zmiany każdego pola
- status wpisu, jeśli OCR jest niepewny
- przycisk zatwierdzenia

### Najważniejsze akcje
- popraw kwotę
- popraw datę
- popraw kategorię
- zaakceptuj wpis
- anuluj wpis

### Założenia UX
- ten ekran musi być szybki i czytelny
- poprawki muszą wymagać minimum klikania
- użytkownik musi mieć poczucie kontroli nad danymi

## 4. Historia transakcji

### Cel ekranu
Pozwolić przeglądać i kontrolować wszystkie zapisane transakcje.

### Co ma być widoczne
- lista transakcji
- kwota
- kategoria
- data
- sklep lub opis
- oznaczenie typu:
  - wydatek
  - przychód
- proste filtrowanie
- wyszukiwarka

### Najważniejsze akcje
- otwórz szczegóły transakcji
- wyszukaj transakcję
- filtruj po kategorii albo dacie

### Założenia UX
- historia ma być czytelna i szybka
- użytkownik ma łatwo znaleźć i poprawić błędny wpis

## 5. Szczegóły transakcji

### Cel ekranu
Pokazać pełne informacje o jednej transakcji i umożliwić korektę.

### Co ma być widoczne
- typ transakcji
- kwota
- data
- kategoria
- sklep albo opis
- metoda płatności
- źródło dodania
- załącznik, jeśli istnieje

### Najważniejsze akcje
- edytuj transakcję
- usuń transakcję
- otwórz załącznik

### Założenia UX
- ekran ma być prosty
- edycja ma być łatwa, bo błędy OCR są realnym scenariuszem

## 6. Analizy

### Cel ekranu
Dać użytkownikowi czytelny obraz tego, na co idą pieniądze.

### Co ma być widoczne
- wykres wydatków według kategorii
- wykres wydatków w czasie
- podsumowanie miesiąca
- największe kategorie kosztów
- podstawowy wniosek typu:
  - na co poszło najwięcej
  - która kategoria zjada budżet najszybciej

### Najważniejsze akcje
- przełącz okres
- przejdź do szczegółów kategorii
- przejdź do budżetów

### Założenia UX
- analizy mają być praktyczne, nie przeładowane
- pokazujemy tylko takie rzeczy, które pomagają podjąć decyzję

## 7. Budżety

### Cel ekranu
Pokazać użytkownikowi, jak wygląda realizacja budżetu w miesiącu.

### Co ma być widoczne
- budżet całego miesiąca
- ile zostało
- lista kategorii budżetowych
- dla każdej kategorii:
  - limit
  - wydano
  - pozostało
  - procent wykorzystania

### Najważniejsze akcje
- przejrzyj stan kategorii
- przejdź do szczegółów kategorii
- edytuj budżet

### Założenia UX
- ekran ma dawać szybki obraz przekroczeń i wolnej przestrzeni w budżecie
- kategorie muszą być łatwe do porównania

## 8. Zarządzanie kategoriami

### Cel ekranu
Pozwolić użytkownikowi uporządkować system kategorii.

### Co ma być widoczne
- lista kategorii wydatków
- lista kategorii przychodów
- stan aktywności kategorii

### Najważniejsze akcje
- dodaj kategorię
- edytuj kategorię
- wyłącz kategorię

### Założenia UX
- ekran ma być prosty administracyjnie
- nie robimy tu zbyt rozbudowanego systemu konfiguracji

## 9. Ustawienia

### Cel ekranu
Dać użytkownikowi dostęp do podstawowej konfiguracji aplikacji.

### Co ma być widoczne
- ustawienia budżetu miesiąca
- ustawienia celu oszczędności
- ustawienia bezpieczeństwa:
  - PIN
  - biometria
- ustawienia danych i prywatności
- podstawowe informacje o aplikacji

### Najważniejsze akcje
- ustaw budżet
- ustaw cel oszczędności
- włącz PIN lub biometrię
- przejdź do ustawień danych

### Założenia UX
- ustawienia mają być uporządkowane
- nie mogą być przesadnie techniczne

## Wniosek projektowy
Na MVP najważniejsze są ekrany:
- dashboard
- dodaj wydatek / przychód
- podgląd i korekta OCR
- historia transakcji
- analizy
- budżety

To jest rdzeń produktu.

Pozostałe ekrany wspierają jakość użycia i porządek danych.
