# Offline i chmura

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[Decyzje techniczne]]
- [[Stack technologiczny]]
- [[Model danych implementacyjny]]
- [[Prywatność i bezpieczeństwo]]
- [[../04 Plan/Updatey wdrożeniowe/00.2 Lokalna baza i modele|Update 0.2 - Lokalna baza i modele]]
- [[../04 Plan/Updatey wdrożeniowe/04.0 Bezpieczeństwo|Update 4.0 - Bezpieczeństwo]]

## Decyzja
Wybrany model działania danych dla MVP to `Model 2: Offline-first z opcją chmury później`.

## Co to oznacza
- aplikacja działa lokalnie i nie wymaga internetu do codziennych operacji
- dane podstawowe są zapisywane na urządzeniu
- zdjęcia paragonów i screenshoty są trzymane lokalnie
- architektura od początku ma umożliwiać późniejsze dodanie synchronizacji i backupu

## Założenia wdrożeniowe
- MVP działa lokalnie
- internet nie jest wymagany do codziennego użycia
- później można dodać sync, backup i chmurę bez zmiany głównego kierunku produktu
