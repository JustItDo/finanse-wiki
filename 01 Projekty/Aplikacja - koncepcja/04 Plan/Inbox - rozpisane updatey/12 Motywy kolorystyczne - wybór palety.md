# 12 Motywy kolorystyczne - wybór palety

## Powiązane notatki

- [[../Inbox zmian|Inbox zmian]]
- [[10A Rebranding v2 - kolory i logo]]
- [[10B Rebranding v2 - wdrożenie w kodzie]]
- [[11 Tryb ciemny i system motywów]]
- [[../../02 Produkt/Zenifi - Palety rebrandingu v2.html]]

## Cel

Dodać w aplikacji możliwość wyboru kolorystyki, nie tylko trybu `Jasny / Ciemny / Systemowy`.

Użytkownik powinien móc wybrać gotową paletę, np.:

- `Neon Mint`
- `Electric Pine`
- `Signal Finance`

To ma być kontrolowana personalizacja wyglądu, a nie pełny edytor motywu.

## Decyzja Produktowa

Motyw aplikacji powinien składać się z dwóch niezależnych ustawień:

- `tryb`: `Systemowy`, `Jasny`, `Ciemny`
- `kolorystyka`: `Neon Mint`, `Electric Pine`, `Signal Finance`

Przykład:

- użytkownik może mieć `Ciemny + Neon Mint`
- użytkownik może mieć `Jasny + Signal Finance`
- użytkownik może mieć `Systemowy + Electric Pine`

Domyślnie:

- `tryb`: `Systemowy`
- `kolorystyka`: `Neon Mint`

## Palety Startowe

### Neon Mint

Domyślna, najbardziej żywa i dopaminowa.

- `base`: `#102A2A`
- `primary`: `#19FF8A`
- `secondary`: `#8AFFE0`
- `goal`: `#FFB84D`
- `lightBackground`: `#F6FFF9`

### Electric Pine

Bardziej fintechowa i nadal mocna wizualnie.

- `base`: `#082F2F`
- `primary`: `#00E676`
- `secondary`: `#00C2FF`
- `goal`: `#FFCF33`
- `lightBackground`: `#F3FFF8`

### Signal Finance

Najbardziej klasyczna, czytelna i finansowa.

- `base`: `#111827`
- `primary`: `#12D576`
- `secondary`: `#2563EB`
- `goal`: `#FACC15`
- `lightBackground`: `#F8FAFC`

## Zasada Techniczna

Nie wolno robić osobnych kolorów porozrzucanych po komponentach.

System powinien działać tak:

1. Aplikacja trzyma `themeMode`.
2. Aplikacja trzyma `paletteId`.
3. Theme builder składa finalny theme z `mode + palette`.
4. Ekrany korzystają wyłącznie z tokenów semantycznych.

Przykładowy model:

```ts
type ThemeMode = 'system' | 'light' | 'dark';
type PaletteId = 'neonMint' | 'electricPine' | 'signalFinance';
```

Przykładowy kierunek:

```ts
const theme = createTheme({
  mode: resolvedMode,
  palette: palettes[paletteId],
});
```

Tokeny powinny pozostać semantyczne, np.:

- `background`
- `surface`
- `surfaceMuted`
- `text`
- `textMuted`
- `border`
- `primary`
- `primarySoft`
- `secondary`
- `success`
- `warning`
- `danger`
- `income`
- `expense`
- `goal`
- `cta`
- `accent`

## Ważna Decyzja UI

W tym update nie robimy pełnej zmiany każdego koloru ekranu dla każdej palety.

Paleta ma kontrolować głównie:

- CTA
- aktywne taby
- elementy sukcesu
- wykresy i progres
- akcenty kart
- kolor celu oszczędnościowego
- pozytywne stany finansowe

Tryb jasny/ciemny ma kontrolować głównie:

- tło
- karty
- tekst
- obramowania
- cienie
- status bar

Powód:

- to utrzymuje kontrast
- ogranicza koszt wdrożenia
- nie tworzy sześciu ręcznie utrzymywanych motywów
- później łatwiej dodać kolejne palety

## UX w Ustawieniach

Sekcja ma nazywać się `Motywy`.

Nie wrzucać wyboru motywu ani palety do sekcji `Aplikacja`.

Podział odpowiedzialności:

- `Motywy` - konfiguracja wyglądu
- `Aplikacja` - informacje o aplikacji, wersji, trybie danych i platformie

W środku:

- wybór trybu: `Systemowy`, `Jasny`, `Ciemny`
- wybór kolorystyki: `Neon Mint`, `Electric Pine`, `Signal Finance`

Rekomendowany wygląd wyboru palety:

- małe kafelki z nazwą palety
- 3-4 kropki / paski z kolorami
- zaznaczenie aktywnej palety
- krótki opis, np. `Żywa`, `Fintech`, `Klasyczna`

Nie robić:

- suwaka kolorów
- ręcznego wpisywania HEX
- wielkiego kreatora personalizacji
- osobnych ustawień koloru dla każdego elementu UI

## Zakres

- dodać listę dostępnych palet
- dodać `paletteId` do ustawień aplikacji
- zapamiętywać wybór palety
- dodać osobny kafel / sekcję `Motywy` w `Ustawieniach`
- przenieść wybór trybu motywu z `Aplikacja` do `Motywy`, jeśli wcześniej został tam dodany
- połączyć `paletteId` z globalnym theme
- sprawdzić główne ekrany pod kontrast i czytelność
- przygotować strukturę tak, żeby później dało się dodać kolejne palety

## Poza Zakresem

- pełny edytor własnego motywu
- custom HEX od użytkownika
- zmiana logo
- zmiana ikon aplikacji
- animowane przejścia między paletami
- pełny redesign wszystkich ekranów
- synchronizacja motywu między urządzeniami

## Zależności

Najlepiej wdrażać po update:

- [[11 Tryb ciemny i system motywów]]

Jeśli update `11` nie jest jeszcze wdrożony, ten update może zostać połączony z budową theme providera, ale trzeba pilnować, żeby nie powstały dwa niezależne systemy:

- osobny dark mode
- osobny selector kolorów

Ma być jeden system:

- `mode + paletteId -> theme`

## Ryzyka

- zbyt wiele zmian kolorów naraz może pogorszyć czytelność danych finansowych
- ciemny tryb z jasną paletą może wymagać ręcznej korekty kontrastu
- wykresy i kategorie mogą mieć własne kolory niezależne od theme
- część komponentów może nadal mieć hardcodowane HEX-y
- jeśli zapiszemy strukturę źle, dodanie kolejnej palety będzie kosztowne

## Kryteria Akceptacji

- w ustawieniach można wybrać paletę kolorystyczną
- wybór palety jest w `Ustawienia -> Motywy`
- sekcja `Aplikacja` nie zawiera wyboru motywu ani palety
- dostępne są co najmniej 3 palety: `Neon Mint`, `Electric Pine`, `Signal Finance`
- wybór palety jest zapamiętywany po restarcie aplikacji
- zmiana palety wpływa na globalny theme, a nie tylko na jeden ekran
- tryb jasny/ciemny/systemowy i paleta są niezależnymi ustawieniami
- główne ekrany pozostają czytelne w każdej palecie
- nowe kolory są używane przez tokeny, nie przez hardcodowane HEX-y w komponentach

## Test Telefonu

- wejść w `Ustawienia`
- wejść w sekcję `Motywy`
- zmienić paletę na `Electric Pine`
- sprawdzić dashboard, historię, budżet i ustawienia
- zmienić paletę na `Signal Finance`
- sprawdzić te same ekrany
- wejść w sekcję `Aplikacja` i sprawdzić, że nie ma tam wyboru motywu/palety
- przełączyć tryb jasny/ciemny, jeśli update `11` jest już wdrożony
- zamknąć i uruchomić aplikację ponownie
- sprawdzić, czy wybrana paleta została zapamiętana

## Prompt Do Codexa

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox - rozpisane updatey/10B Rebranding v2 - wdrożenie w kodzie.md`
- `04 Plan/Inbox - rozpisane updatey/11 Tryb ciemny i system motywów.md`
- `04 Plan/Inbox - rozpisane updatey/12 Motywy kolorystyczne - wybór palety.md`
- `02 Produkt/Zenifi - Palety rebrandingu v2.html`

Cel:
Dodać możliwość wyboru kolorystyki aplikacji poza samym trybem jasnym i ciemnym.

Model docelowy:
- `themeMode`: `system | light | dark`
- `paletteId`: `neonMint | electricPine | signalFinance`
- finalny theme powstaje z `mode + paletteId`

Wymagania:
- dodaj 3 gotowe palety: `Neon Mint`, `Electric Pine`, `Signal Finance`
- domyślna paleta to `Neon Mint`
- paleta ma być zapamiętywana w ustawieniach
- użytkownik zmienia paletę w sekcji `Ustawienia -> Motywy`
- jeśli obecny wybór motywu jest w `Ustawienia -> Aplikacja`, przenieś go do `Ustawienia -> Motywy`
- sekcja `Aplikacja` ma zostać informacyjna i nie może zawierać konfiguracji motywu ani palety
- UI wyboru palety ma być prosty: kafelki z nazwą i próbkami kolorów
- nie rób pełnego edytora kolorów
- nie pozwalaj wpisywać własnych HEX-ów
- nie rozrzucaj kolorów bezpośrednio po komponentach
- używaj semantycznych tokenów theme
- tryb jasny/ciemny/systemowy i paleta mają być niezależne

Jeśli system motywów z update'u `11` nie jest jeszcze wdrożony:
- najpierw zbuduj minimalny wspólny mechanizm theme provider / storage
- nie twórz osobnego systemu tylko dla palet
- całość ma działać jako `mode + paletteId -> theme`

Po zmianach:
- sprawdź typowanie TypeScript
- uruchom dostępne szybkie testy/lint, jeśli są tanie
- opisz, gdzie zapisuje się `themeMode` i `paletteId`
- wypisz, które ekrany ręcznie sprawdzić na telefonie

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```
