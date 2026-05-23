# Offline i chmura

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
