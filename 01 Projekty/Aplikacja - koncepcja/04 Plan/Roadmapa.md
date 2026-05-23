# Roadmapa

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[../00 Założenia startowe|Założenia startowe]]
- [[../02 Produkt/MVP|MVP]]
- [[../03 Technologia/Decyzje techniczne|Decyzje techniczne]]
- [[Backlog]]
- [[Plan updateów wdrożeniowych]]
- [[Updatey wdrożeniowe/README|Updatey wdrożeniowe]]

## Stan obecny
Na podstawie aktualnych notatek można uznać, że etapy `discovery`, `projekt produktu` i `wybór technologii` są w dużej mierze domknięte koncepcyjnie.

Najbliższy realny etap wejścia w pracę to:
- `Etap 4 - architektura i setup`
- potem `Etap 5 - MVP` wdrażane małymi update'ami

## Kryterium przejścia do implementacji
Można zaczynać development, jeśli:
- zakres MVP pozostaje bez większych zmian
- stack technologiczny jest zaakceptowany
- model danych jest wystarczająco stabilny na start
- pierwszy pakiet update'ów wdrożeniowych jest rozpisany wykonawczo
- otwarte decyzje zostały ograniczone do tych, które można zamknąć w trakcie `Update 0.1` i `0.2`

## Etap 1 - discovery
- doprecyzowanie problemu użytkownika
- opis codziennego flow korzystania z aplikacji
- określenie wartości aplikacji względem zwykłego rejestru wydatków

## Etap 2 - projekt produktu
- ustalenie zakresu MVP
- wybór najważniejszych ekranów
- spisanie kluczowych metryk i budżetów
- rozdzielenie funkcji na MVP, V1 po MVP i V2

## Etap 3 - wybór technologii
- wybór stacku pod mobile i desktop
- decyzja jak obsłużyć OCR paragonów i screenshotów
- decyzja o przechowywaniu danych lokalnie lub w chmurze
- decyzja o architekturze frontendu i backendu

## Etap 4 - architektura i setup
- przygotowanie repozytorium i struktury projektu
- przygotowanie design systemu i modelu danych
- przygotowanie podstaw do autoryzacji lub trybu single-user
- przygotowanie infrastruktury developerskiej
- ustalenie standardów jakości, testów i struktury warstw aplikacji
- wybór rozwiązania dla lokalnego przechowywania załączników i OCR

### Wynik etapu
- istnieje gotowy fundament techniczny do wejścia w pierwszy pełny flow produktu

## Etap 5 - MVP
- dodawanie wydatków i przychodów
- obsługa kategorii
- budżety miesięczne kategorii
- dodawanie zdjęć paragonów i screenshotów
- OCR i ręczna korekta danych
- dashboard główny
- wykresy podstawowe
- historia transakcji
- licznik ile zostało w budżecie kategorii i miesiąca
- podstawowe cele oszczędnościowe
- informacja o wpływie nowego wydatku na budżet

### Wynik etapu
- użytkownik może realnie używać aplikacji do codziennej kontroli finansów

## Etap 6 - testy i poprawki
- poprawa szybkości codziennego flow
- poprawa jakości OCR
- poprawa kategorii i logiki budżetów
- testy użyteczności na telefonie i komputerze
- weryfikacja czy dashboard nie jest przeciążony
- weryfikacja czy ręczne dodawanie wydatku jest wystarczająco szybkie

### Wynik etapu
- aplikacja jest gotowa do regularnego używania bez dużych tarć

## Etap 7 - V1 po MVP
- alerty o nietypowych wydatkach i przekroczeniach
- tygodniowe i miesięczne insighty
- wykrywanie stałych opłat i subskrypcji
- limity dzienne do końca miesiąca
- podział wydatków na potrzeby i zachcianki

## Etap 8 - V2 i rozwój produktu
- rozbijanie jednego paragonu na kilka kategorii
- bardziej inteligentne rekomendacje oszczędzania
- bardziej zaawansowana analityka
- personalizacja dashboardu
- przygotowanie pod rozwój dla większej liczby użytkowników
