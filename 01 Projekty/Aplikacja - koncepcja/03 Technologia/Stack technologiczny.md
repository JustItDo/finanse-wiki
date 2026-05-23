# Stack technologiczny

## Decyzja
Wybrany stack technologiczny dla MVP to `Model 2: Mobile-first z Expo i React Native`.

## Wybrany stack
- frontend aplikacji: `React Native + Expo + TypeScript`
- komputer / web: `ten sam projekt z działaniem także na webie`
- lokalna baza danych: `SQLite`
- OCR: `na urządzeniu`
- backend: `dopiero później, jeśli wejdzie sync, backup albo chmura`

## Dlaczego ten wybór
- najlepiej pasuje do telefonu jako głównej platformy
- dobrze wspiera OCR, zdjęcia i screeny
- dobrze łączy mobile-first, offline-first i sensowne użycie na komputerze
- pozwala później dołożyć backend bez przebudowy całego projektu

## Założenia wdrożeniowe
- MVP skupia się na aplikacji działającej lokalnie
- backend nie jest wymagany na start
- architektura ma pozostać gotowa na późniejsze rozszerzenie o sync i chmurę
