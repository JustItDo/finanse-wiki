# Stack technologiczny

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[Decyzje techniczne]]
- [[Offline i chmura]]
- [[Zakres platform]]
- [[../02 Produkt/Flow OCR i screenów|Flow OCR i screenów]]
- [[../04 Plan/Updatey wdrożeniowe/00.1 Start projektu|Update 0.1 - Start projektu]]
- [[../04 Plan/Updatey wdrożeniowe/02.0 OCR i dodawanie zdjęcia|Update 2.0 - OCR i dodawanie zdjęcia]]

## Decyzja
Wybrany stack technologiczny dla MVP to `Model 2: Mobile-first z Expo i React Native`.

## Wybrany stack
- frontend aplikacji: `React Native + Expo + TypeScript`
- komputer / web: `ten sam projekt z działaniem także na webie`
- lokalna baza danych: `SQLite`
- OCR: `na urządzeniu`
- backup lokalny: `expo-file-system`, `expo-document-picker`, `expo-sharing`, `fflate`
- backend: `dopiero później, jeśli wejdzie sync albo chmura`

## Dlaczego ten wybór
- najlepiej pasuje do telefonu jako głównej platformy
- dobrze wspiera OCR, zdjęcia i screeny
- dobrze łączy mobile-first, offline-first i sensowne użycie na komputerze
- pozwala później dołożyć backend bez przebudowy całego projektu

## Założenia wdrożeniowe
- MVP skupia się na aplikacji działającej lokalnie
- backend nie jest wymagany na start
- ręczny backup ZIP działa bez backendu i bez internetu
- architektura ma pozostać gotowa na późniejsze rozszerzenie o sync i chmurę
