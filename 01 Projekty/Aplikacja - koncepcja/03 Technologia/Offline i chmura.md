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
- ręczny backup ZIP jest pierwszym lokalnym krokiem do przenoszenia danych między instalacjami bez chmury
- później można dodać sync i chmurę bez zmiany głównego kierunku produktu

## Wdrożenie backupu ZIP

W `04.3 Backup ZIP` wdrożono ręczny eksport/import kopii danych dla aplikacji mobilnej.

Backup:

- przenosi dane finansowe z `SQLite`
- przenosi pliki załączników z lokalnego katalogu aplikacji
- nie przenosi PIN-u, biometrii ani sekretów urządzenia
- nie wymaga backendu ani internetu
- ma manifest przygotowany pod przyszłe szyfrowanie i upload do chmury

To nadal nie jest synchronizacja. Import scala dane z lokalną bazą i nie kasuje obecnego stanu urządzenia.
