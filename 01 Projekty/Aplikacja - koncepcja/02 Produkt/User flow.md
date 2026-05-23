# User flow

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[MVP]]
- [[Ekrany aplikacji]]
- [[Główny ekran]]
- [[Flow OCR i screenów]]
- [[../03 Technologia/Model danych implementacyjny|Model danych implementacyjny]]
- [[../04 Plan/Updatey wdrożeniowe/01.0 Ręczne dodawanie wydatku|Update 1.0 - ręczne dodawanie wydatku]]
- [[../04 Plan/Updatey wdrożeniowe/02.0 OCR i dodawanie zdjęcia|Update 2.0 - OCR i dodawanie zdjęcia]]

## Decyzja
Wybrany model user flow dla MVP to `Model 2: Zbalansowany`.

## Główne flow 1 - ręczne dodanie wydatku
1. użytkownik otwiera aplikację
2. klika szybkie dodanie wydatku
3. wpisuje kwotę, kategorię i ewentualnie opis
4. zapisuje transakcję
5. wraca na dashboard i widzi wpływ na budżet

## Główne flow 2 - dodanie przez paragon lub screen
1. użytkownik otwiera dodawanie wydatku
2. wybiera zdjęcie paragonu albo screen
3. aplikacja robi OCR i proponuje dane
4. użytkownik poprawia lub zatwierdza
5. transakcja zapisuje się
6. dashboard aktualizuje budżet i stan miesiąca

## Główne flow 3 - analiza finansów
1. użytkownik otwiera dashboard
2. widzi szybki stan miesiąca
3. przechodzi do analiz albo budżetów
4. sprawdza szczegóły kategorii, historii i wykresów

## Założenia wdrożeniowe
- projektujemy 3 główne flow jako podstawę MVP
- ręczne dodawanie i korekta OCR są krytyczne dla używalności
- dashboard ma prowadzić użytkownika do analiz i budżetów bez przeciążenia
