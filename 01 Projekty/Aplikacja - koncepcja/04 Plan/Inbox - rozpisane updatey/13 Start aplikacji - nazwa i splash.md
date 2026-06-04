# 13 Start aplikacji - nazwa i splash

## Powiązane notatki

- [[../Inbox zmian|Inbox zmian]]
- [[10A Rebranding v2 - kolory i logo]]
- [[10B Rebranding v2 - wdrożenie w kodzie]]
- [[12 Motywy kolorystyczne - wybór palety]]

## Cel

Naprawić niespójność startu aplikacji:

- przy ładowaniu aplikacji nie może pojawiać się stara nazwa `finanse-app`
- przy ładowaniu aplikacji nie może pojawiać się stare pierwsze logo, jeśli asset został już podmieniony
- konfiguracja Expo / Android / assetów ma jednoznacznie wskazywać na `Zenifi`

Nowe finalne logo jest poza tym update'em, bo zostanie dostarczone później.

## Obserwacja

W aktualnym repo `finanse-app` plik `app.json` wskazuje:

- `expo.name`: `Zenifi`
- `expo.slug`: `zenifi`
- `expo.scheme`: `zenifi`
- `android.package`: `com.justitdo.zenifi`
- `ios.bundleIdentifier`: `com.justitdo.zenifi`

Decyzja namingowa:

- nazwa pod ikoną i w konfiguracji aplikacji: `Zenifi`
- nazwa sklepowa / marketingowa: `Zenifi: Budżet i wydatki`
- krótki opis: `Twój budżet, wydatki i paragony w jednym miejscu.`

Nie zmieniać `expo.name` na pełną nazwę sklepową, bo pod ikoną telefonu ma zostać krótka nazwa marki.

Jeśli na telefonie nadal pojawia się `finanse-app`, to prawdopodobne przyczyny są inne niż sama wartość `expo.name`:

- zainstalowany jest stary build APK
- Android / Expo trzyma cache starego builda
- odpalany jest dev build / Expo Go z metadanymi projektu zamiast aktualnego APK
- splash albo icon asset nadal wygląda jak pierwsze logo
- natywne pliki Androida, jeśli istnieją po `prebuild`, mają stare labelki
- build nie został wykonany z aktualnego commita

## Zakres

- sprawdzić `app.json`
- sprawdzić `package.json`
- sprawdzić assety:
  - `assets/icon.png`
  - `assets/splash-icon.png`
  - `assets/android-icon-foreground.png`
  - `assets/android-icon-background.png`
  - `assets/android-icon-monochrome.png`
  - `assets/favicon.png`
- sprawdzić, czy istnieją wygenerowane pliki natywne Androida:
  - `android/app/src/main/res/values/strings.xml`
  - `android/app/src/main/AndroidManifest.xml`
- jeżeli istnieją pliki natywne, upewnić się, że label aplikacji to `Zenifi`
- upewnić się, że splash używa aktualnego tymczasowego assetu albo neutralnego assetu zgodnego z brandem
- przygotować instrukcję czystej reinstalacji / rebuilda APK

## Poza Zakresem

- projektowanie finalnego logo
- podmiana finalnych assetów brandingu, jeśli nowe logo nie jest jeszcze dostarczone
- zmiana package id aplikacji
- migracja danych użytkownika między starym i nowym package id
- publikacja do sklepu

## Decyzja Tymczasowa

Dopóki nowe logo nie jest gotowe:

- nazwa aplikacji ma być `Zenifi`
- splash nie może pokazywać `finanse-app`
- można zostawić obecny tymczasowy asset, jeśli jest spójny z `Zenifi`
- jeśli obecny asset wygląda jak stary / błędny znak, lepiej użyć prostego neutralnego splashu niż udawać finalne logo

## Decyzja po dostarczeniu logo 2026-06-04

Logo zostało dostarczone jako SVG:

- [[../../02 Produkt/zenifi logo.svg]]

Podgląd przygotowanych assetów:

- [[../../02 Produkt/Zenifi - logo asset preview.png]]

Zasada:

- nie przerabiać samego znaku
- wolno zmieniać tylko canvas, skalowanie, margines i tło assetu
- master / foreground / splash mogą mieć przezroczyste tło
- główna ikona aplikacji nie powinna być czysto transparentna

Decyzja tła:

- dla app icon używać jasnego tła `#F6FFF9`
- dla Android adaptive icon używać `backgroundColor: #F6FFF9`
- dla Android foreground używać transparentnego PNG
- dla splash używać transparentnego PNG na tle `#F6FFF9`

Powód:

- logo ma ciemny górny element, który ginie na ciemnym tle `#102A2A`
- jasne tło pokazuje cały znak bez utraty kontrastu
- transparentny foreground jest właściwy dla Android adaptive icon
- pełna transparentność jako jedyny app icon jest ryzykowna, bo launcher / platforma może dać niekontrolowane tło

Aktywne assety przygotowane w `finanse-app/assets`:

- `icon.png` - 1024x1024, jasne tło `#F6FFF9`
- `android-icon-foreground.png` - 1024x1024, transparentne tło
- `android-icon-background.png` - 1024x1024, jasne tło `#F6FFF9`
- `android-icon-monochrome.png` - 1024x1024, maska monochrome
- `splash-icon.png` - 1024x1024, transparentne tło
- `favicon.png` - 512x512, jasne tło `#F6FFF9`
- `zenifi-logo-source.svg` - kopia źródła SVG

## Checklist Naprawy

1. Potwierdzić `expo.name = Zenifi`.
2. Potwierdzić `expo.slug = zenifi`.
3. Potwierdzić `scheme = zenifi`.
4. Potwierdzić `android.package = com.justitdo.zenifi`.
5. Sprawdzić, czy nie ma tekstu `finanse-app` w źródłach poza starymi artefaktami.
6. Sprawdzić wszystkie ścieżki assetów splash/icon.
7. Jeżeli telefon nadal pokazuje starą nazwę, odinstalować stary build z telefonu.
8. Wyczyścić cache Expo / Metro przed kolejnym testem.
9. Zbudować APK z aktualnego commita.
10. Po instalacji sprawdzić nazwę aplikacji, ikonę i splash na telefonie.

## Ryzyka

- Android może pokazywać starą nazwę z poprzednio zainstalowanego APK
- po zmianie `android.package` aplikacja będzie traktowana jako osobna aplikacja, więc nie zmieniać package bez decyzji
- splash może być cache'owany przez build, więc sama podmiana pliku bez nowego buildu nic nie zmieni
- Expo Go / dev build może pokazywać inne metadane niż standalone APK

## Kryteria Akceptacji

- aplikacja na telefonie pokazuje nazwę `Zenifi`
- nazwa sklepowa jest ustalona jako `Zenifi: Budżet i wydatki`
- ekran startowy nie pokazuje nazwy `finanse-app`
- splash korzysta z aktualnego assetu logo na tle `#F6FFF9`
- app icon korzysta z jasnego tła `#F6FFF9`, nie z ciemnego tła zasłaniającego znak
- nie ma aktywnych referencji do `finanse-app` w konfiguracji aplikacji
- wiadomo, które assety trzeba podmienić po dostarczeniu finalnego logo

## Test Telefonu

- odinstalować starą wersję aplikacji z telefonu
- zainstalować świeży build APK
- uruchomić aplikację
- sprawdzić nazwę pod ikoną
- sprawdzić splash / ekran ładowania
- sprawdzić ekran blokady / start aplikacji
- sprawdzić, czy w `Ustawienia -> Aplikacja` nazwa to `Zenifi`

## Prompt Do Codexa

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox - rozpisane updatey/13 Start aplikacji - nazwa i splash.md`
- `04 Plan/Inbox - rozpisane updatey/10B Rebranding v2 - wdrożenie w kodzie.md`

Cel:
Naprawić problem, że przy ładowaniu aplikacji albo na telefonie pojawia się stara nazwa `finanse-app` lub stare logo.

Ważne:
- nowe finalne logo nie jest jeszcze gotowe, więc nie projektuj logo
- nie zmieniaj `android.package`, jeśli nie ma twardej potrzeby
- nazwa aplikacji ma być `Zenifi`
- splash/icon mają być spójne z aktualnym tymczasowym brandem

Sprawdź:
- `app.json`
- `package.json`
- wszystkie assety w `assets/` używane przez `icon`, `splash`, `adaptiveIcon`, `favicon`
- czy istnieją wygenerowane pliki natywne Androida z labelką aplikacji
- czy w repo nie ma aktywnych referencji do `finanse-app`

Jeśli `app.json` jest już poprawny:
- wyjaśnij, czy problem wynika raczej ze starego APK/cache/builda
- przygotuj konkretne kroki czystej reinstalacji i rebuilda
- jeśli trzeba, popraw tylko realne niespójności w repo

Po zmianach:
- uruchom szybkie sprawdzenia, które mają sens
- podaj, które pliki zostały zmienione
- podaj, co sprawdzić ręcznie na telefonie

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```
