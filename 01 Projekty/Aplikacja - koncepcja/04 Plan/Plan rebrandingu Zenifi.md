# Plan rebrandingu Zenifi

## Powiązane notatki

- [[Zenifi - rekomendacja marki]]
- [[Backlog]]
- [[Dziennik wdrożeń]]

## Decyzja

Na ten moment przyjmujemy:

- nowa nazwa marki aplikacji: `Zenifi`
- nazwa sklepowa / marketingowa: `Zenifi: Budżet i wydatki`
- nazwa pod ikoną telefonu: `Zenifi`
- preferowany znak: `zenifi-logo-v3-balance.svg`
- kierunek kolorystyczny:
  - `#0E2F2F` jako główny kolor marki
  - `#F4F9F4` jako jasne tło
  - `#1DB954` jako akcent sukcesu
  - `#FFD700` jako mikro-akcent

## Cel

Wdrożyć podstawowy rebranding aplikacji tak, aby:

- nazwa aplikacji była spójna w projekcie i buildach,
- ikona i zasoby marki były podmienione na nowy kierunek,
- aplikacja nie wyglądała już jak stara wersja robocza,
- zmiana nie rozwaliła obecnego flow developmentu i buildów Androida.

## Zakres zadania dla Codexa

### 1. Audyt obecnego brandingu

Codex ma najpierw znaleźć wszystkie miejsca, gdzie występują:

- stara nazwa aplikacji,
- stare ikony,
- stare assety brandingowe,
- stare kolory albo hardcoded wartości, które kolidują z nowym kierunkiem.

Obszary do sprawdzenia:

- `app.json`
- `package.json`
- ekran logowania i splash / onboarding, jeśli istnieją
- nagłówki ekranów
- assety aplikacji i ikony
- ewentualne teksty buildowe i nazwa aplikacji na Androidzie

### 2. Podmiana nazwy aplikacji

Codex ma:

- ustawić nazwę aplikacji na `Zenifi`
- sprawdzić, czy jest też sens przygotować listingową nazwę sklepową osobno później
- nie wymyślać jeszcze finalnej strategii ASO, tylko ustawić spójną nazwę roboczą produktu

Aktualna decyzja po konsultacji namingowej:

- nazwa systemowa / pod ikoną: `Zenifi`
- nazwa listingowa do sklepu: `Zenifi: Budżet i wydatki`
- krótki opis: `Twój budżet, wydatki i paragony w jednym miejscu.`

### 3. Podmiana ikon i assetów

Codex ma:

- wykorzystać `zenifi-logo-v3-balance.svg` jako źródło kierunku
- przygotować albo podmienić podstawowe assety aplikacji:
  - app icon
  - adaptive icon
  - ewentualny splash asset, jeśli istnieje sensowny brandingowy odpowiednik
- dopilnować, żeby assety działały w Expo / Android buildzie

Jeżeli bezpieczniej będzie najpierw przygotować uproszczoną wersję PNG z istniejącego SVG i podmienić tylko podstawowe ikony, to to jest akceptowalne.

### 4. Uporządkowanie warstwy wizualnej

Jeżeli w aplikacji są już oczywiste miejsca brandingowe, Codex może:

- podmienić nazwę na ekranie logowania,
- dopasować podstawowe kolory marki tam, gdzie nie rozszerza to zakresu za bardzo,
- usunąć stare robocze nazwy, jeśli są jeszcze widoczne dla użytkownika.

Nie chodzi o pełny redesign całego UI.
Chodzi o pierwsze sensowne domknięcie rebrandingu.

### 5. Walidacja

Na końcu Codex ma:

- sprawdzić, czy build Expo nadal ma sens,
- sprawdzić, czy assety nie wywracają konfiguracji,
- zaktualizować wiki tylko wtedy, gdy zmieni się stan wdrożenia albo kolejny krok.

## Prompt do VS Code

Wklej to do sesji `Codex: Finanse` w repo `finanse-app`:

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `01 Projekty/Aplikacja - koncepcja/02 Produkt/Zenifi - rekomendacja marki.md`
- `01 Projekty/Aplikacja - koncepcja/04 Plan/Plan rebrandingu Zenifi.md`

Cel:
Wdrożyć podstawowy rebranding aplikacji do marki `Zenifi`.

Założenia:
- przyjęta nazwa aplikacji: `Zenifi`
- preferowany znak: `zenifi-logo-v3-balance.svg`
- nie robimy teraz pełnego redesignu całego UI
- chodzi o spójny, działający pierwszy rebranding produktu

Zakres pracy:
1. Najpierw zrób audyt obecnego brandingu w repo aplikacji.
2. Znajdź miejsca, gdzie występują:
- stara nazwa aplikacji,
- stare ikony i assety,
- stare widoczne elementy marki,
- kolory lub teksty, które wyraźnie kolidują z nowym brandingiem.
3. Następnie wdroż zmiany:
- ustaw nazwę aplikacji na `Zenifi`,
- podmień podstawowe ikony i assety aplikacji na bazie `zenifi-logo-v3-balance.svg`,
- doprowadź konfigurację Expo / Android do spójnego stanu,
- podmień najbardziej oczywiste miejsca brandingowe w UI, jeśli nie wymaga to dużego redesignu.
4. Jeśli trzeba przygotować po drodze raster assetów z SVG, zrób to praktycznie i bez rozlewania zakresu.
5. Na końcu sprawdź, czy konfiguracja nadal wygląda poprawnie do kolejnego buildu.

Zasady:
- pracuj konkretnie w plikach,
- nie rób dużego redesignu poza zakresem,
- nie zmieniaj niepowiązanych obszarów,
- jeśli napotkasz ograniczenie assetów Expo, wybierz najprostsze bezpieczne obejście,
- zaktualizuj wiki tylko wtedy, gdy zmieni się stan wdrożenia albo kolejny krok.

Format odpowiedzi:
1. Najpierw krótko pokaż plan zmian.
2. Potem wykonaj zmiany w kodzie i assetach.
3. Na końcu podaj:
- co zostało zmienione,
- które miejsca brandingu zostały podmienione,
- czy są jeszcze miejsca wymagające drugiego etapu rebrandingu,
- jaki powinien być następny krok.

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```

## Następny etap

Po wdrożeniu podstawowego rebrandingu można osobno zrobić:

- wdrożenie nazwy listingowej `Zenifi: Budżet i wydatki` w materiałach sklepowych
- drugą iterację ikon i splasha
- pełniejsze dopasowanie UI do nowej marki

## Status

Podstawowy rebranding został już wdrożony w repo aplikacji:

- nazwa Expo została ustawiona na `Zenifi`
- podstawowe assety zostały podmienione na bazie `zenifi-logo-v3-balance.svg`
- konfiguracja buildów została uporządkowana pod kolejne buildy
- najbardziej oczywiste stare elementy marki w UI zostały usunięte

Drugi etap, jeśli będzie potrzebny, dotyczy już głównie pełniejszego dopasowania UI i sklepowego opakowania produktu.

Zaakceptowane sklepowe opakowanie nazwy:

- `Zenifi: Budżet i wydatki`
