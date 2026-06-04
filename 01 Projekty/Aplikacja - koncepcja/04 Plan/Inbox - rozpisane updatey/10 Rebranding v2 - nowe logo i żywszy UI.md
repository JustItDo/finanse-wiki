# 10 Rebranding v2 - nowe logo i żywszy UI

## Powiązane notatki

- [[../Inbox zmian|Inbox zmian]]
- [[../02 Produkt/Zenifi - rekomendacja marki]]

## Cel

Odświeżyć branding aplikacji bez robienia pełnego redesignu wszystkich ekranów.

W centrum jest nowe logo i żywsza, bardziej angażująca kolorystyka UI.

Ten update dzielimy na dwa kroki:

- [[10A Rebranding v2 - kolory i logo]] - decyzja kreatywna bez zmian w kodzie
- [[10B Rebranding v2 - wdrożenie w kodzie]] - wdrożenie wybranej palety i logo w `finanse-app`

## Warianty

### Wariant A

- tylko nowe logo i app icon
- minimalne ryzyko
- nie rozwiązuje problemu zbyt spokojnego UI

### Wariant B

- nowe logo + żywsze tokeny kolorów
- akcenty dla CTA, sukcesu, oszczędności, wykresów i stanów
- zachowana spokojna baza dla danych finansowych
- **rekomendowany wariant**

### Wariant C

- pełny redesign całej aplikacji
- największy efekt wizualny
- za duże ryzyko i zakres

## Rekomendacja

`Wariant B`.

To daje wyraźniejszą tożsamość marki i nadal trzyma czytelność finansów.

## Zakres

- nowe logo / icon asset
- żywsze tokeny kolorów
- bardziej wyraziste stany sukcesu, CTA i ważne akcenty
- spójność brandingu z aplikacją

## Poza zakresem

- pełny redesign wszystkich ekranów
- zmiana struktury nawigacji
- przepisywanie wszystkich komponentów UI

## Ryzyka

- za dużo energii wizualnej może obniżyć czytelność liczb
- zmiana tokenów może wymagać korekt w wielu ekranach
- zbyt mocny branding może wejść w konflikt z fintechem i „przekrzyczeć” dane

## Kryteria Akceptacji

- nowe logo wygląda lepiej jako ikona aplikacji
- UI jest wyraźniej zbrandowany, ale nadal czytelny
- dane finansowe nie giną w kolorach
- assety są spójne na telefonie i w buildzie

## Test Telefonu

- sprawdzić ekran główny
- sprawdzić dashboard
- sprawdzić przyciski CTA
- sprawdzić czy logo i kolory nie psują czytelności sald i wykresów

## Prompt Do Codexa

Docelowo używamy dwóch osobnych promptów:

- prompt decyzyjny z [[10A Rebranding v2 - kolory i logo]]
- prompt wdrożeniowy z [[10B Rebranding v2 - wdrożenie w kodzie]]

Poniższy prompt jest starszym wariantem zbiorczym i nie powinien być używany jako pierwszy.

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox zmian.md`
- `04 Plan/Inbox - rozpisane updatey/10 Rebranding v2 - nowe logo i żywszy UI.md`
- `02 Produkt/Zenifi - rekomendacja marki.md`

Cel:
Odświeżyć branding aplikacji: nowe logo i żywsza kolorystyka UI bez pełnego redesignu.

Zakres:
- podmienić logo / icon asset
- podbić żywsze akcenty kolorów
- zachować czytelność danych finansowych
- utrzymać spójność z marką `Zenifi`

Zasady:
- nie rób pełnego redesignu wszystkich ekranów
- nie psuj czytelności liczb i wykresów
- pracuj konkretnie w assetach i theme
- po zmianach opisz, które elementy brandingu zostały podmienione

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```
