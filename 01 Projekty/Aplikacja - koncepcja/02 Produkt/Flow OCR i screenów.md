# Flow OCR i screenów

## Decyzja
Wybrany model flow OCR i screenów dla MVP to `Model 2: Zbalansowany`.

## Jak działa wybrany model
- użytkownik dodaje jedno zdjęcie paragonu albo jeden screen płatności
- aplikacja odczytuje:
  - kwotę
  - datę
  - nazwę sklepu lub źródła
  - sugerowaną kategorię
- użytkownik widzi ekran podglądu i może poprawić dane
- po zatwierdzeniu transakcja zapisuje się do historii
- budżet kategorii i budżet miesiąca aktualizują się od razu

## Założenia wdrożeniowe
- screen płatności jest obsługiwany tak samo jak paragon
- jeśli OCR nie jest pewny, wpis dostaje status `do poprawy`
- użytkownik zawsze ma możliwość ręcznej korekty
- w MVP obsługujemy jedno zdjęcie albo jeden screen na raz
