# 11 Tryb ciemny i system motywów

## Powiązane notatki

- [[../Inbox zmian|Inbox zmian]]
- [[10 Rebranding v2 - nowe logo i żywszy UI]]
- [[12 Motywy kolorystyczne - wybór palety]]

## Cel

Dodać pełny system motywów z trybem ciemnym i przełącznikiem w ustawieniach.

Ustawienia motywu mają być w osobnej kategorii `Motywy`, a nie w sekcji `Aplikacja`.

## Warianty

### Wariant A

- prosty przełącznik `Jasny / Ciemny`
- łatwe do zrozumienia
- brak obsługi motywu systemowego

### Wariant B

- `Systemowy / Jasny / Ciemny`
- zapamiętywanie wyboru w ustawieniach
- spójna integracja z globalnym theme
- **rekomendowany wariant**

### Wariant C

- pełna personalizacja motywu
- duża elastyczność
- za duży koszt i zakres na ten etap

## Rekomendacja

`Wariant B`.

Najbardziej przyszłościowy, a jednocześnie wciąż prosty dla użytkownika.

## Zakres

- theme provider dla jasnego i ciemnego motywu
- zapis preferencji motywu
- osobny kafel / sekcja `Motywy` w ustawieniach
- dopasowanie podstawowych komponentów i status bara

## Poza zakresem

- pełny design system z personalizacją każdego koloru
- animowane przejścia między motywami
- osobne brandingowe warianty dla każdego ekranu
- wybór kilku palet kolorystycznych przez użytkownika

Wybór palety kolorystycznej jest osobnym update'em:

- [[12 Motywy kolorystyczne - wybór palety]]

## Ryzyka

- obecne kolory są statyczne, więc trzeba będzie przepiąć shared theme
- niektóre ekrany mogą wymagać ręcznej korekty kontrastu
- status bar i app.json mogą wymagać spójnej konfiguracji
- jeśli później dodajemy palety, ten update nie może tworzyć zamkniętej struktury tylko pod `lightTheme` i `darkTheme`

## Kryteria Akceptacji

- motyw można zmienić w ustawieniach
- motyw jest dostępny w `Ustawienia -> Motywy`
- motyw nie jest schowany w `Ustawienia -> Aplikacja`
- wybór jest zapamiętywany
- ekran po restarcie ma ten sam motyw
- dark mode działa czytelnie na ekranach głównych i ustawieniach

## Test Telefonu

- zmienić motyw w ustawieniach
- sprawdzić, że wejście jest osobnym kaflem `Motywy`
- sprawdzić, że sekcja `Aplikacja` nie zawiera konfiguracji motywu
- wyjść z aplikacji i wrócić
- sprawdzić, czy motyw został zapamiętany
- sprawdzić czy tekst i tła są czytelne w obu motywach

## Prompt Do Codexa

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox zmian.md`
- `04 Plan/Inbox - rozpisane updatey/11 Tryb ciemny i system motywów.md`
- `04 Plan/Inbox - rozpisane updatey/10 Rebranding v2 - nowe logo i żywszy UI.md`

Cel:
Dodać system motywów z trybem ciemnym i przełącznikiem w ustawieniach.

Zakres:
- `Systemowy / Jasny / Ciemny`
- zapis preferencji
- integracja z shared theme i status barem
- dostępne w `Ustawienia -> Motywy`
- przygotowanie struktury tak, żeby później dało się dodać `paletteId`

Zasady:
- nie rób pełnej personalizacji motywu
- pracuj na wspólnych tokenach theme
- nie blokuj późniejszego update'u `12 Motywy kolorystyczne - wybór palety`
- nie wkładaj wyboru motywu do sekcji `Aplikacja`
- sekcja `Aplikacja` ma zostać informacyjna
- sprawdź czy wszystkie kluczowe ekrany zachowują czytelność
- po zmianach opisz, jak działa zapis motywu i co zostało dopasowane

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```
