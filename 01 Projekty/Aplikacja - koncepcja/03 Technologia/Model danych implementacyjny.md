# Model danych implementacyjny

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[../02 Produkt/MVP|MVP]]
- [[../02 Produkt/Model danych finansowych|Model danych finansowych]]
- [[../02 Produkt/User flow|User flow]]
- [[Decyzje techniczne]]
- [[Offline i chmura]]
- [[../04 Plan/Updatey wdrożeniowe/00.2 Lokalna baza i modele|Update 0.2 - lokalna baza i modele]]

## Decyzja
Wybrany model danych pod implementację dla MVP to `Model 2: Zbalansowany schemat implementacyjny`.

## Główne encje
- `transactions`
- `attachments`
- `categories`
- `category_budgets`
- `monthly_budgets`

## Założenie
To jest schemat wystarczająco konkretny, żeby zacząć development, ale nadal na tyle prosty, żeby nie przeciążyć MVP.

## Cel
- wspierać offline-first
- wspierać OCR i screenshoty
- wspierać budżety i analizy
- nie wymagać szybkiej przebudowy po pierwszych iteracjach
