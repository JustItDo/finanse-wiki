# Prywatność i bezpieczeństwo

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[Decyzje techniczne]]
- [[Offline i chmura]]
- [[Zakres platform]]
- [[../02 Produkt/Flow OCR i screenów|Flow OCR i screenów]]
- [[../04 Plan/Updatey wdrożeniowe/04.0 Bezpieczeństwo|Update 4.0 - Bezpieczeństwo]]

## Decyzja
Wybrany model prywatności i bezpieczeństwa dla MVP to `Model 2: Zbalansowany`.

## Co to oznacza
- dane finansowe są przechowywane lokalnie
- aplikacja powinna wspierać PIN albo biometrię
- wrażliwe dane i pliki powinny być zabezpieczone lokalnie
- chmura nie wchodzi do MVP

## Założenia wdrożeniowe
- użytkownik ma pełną kontrolę nad tym, że dane nie wychodzą do chmury w pierwszej wersji
- bezpieczeństwo ma być sensowne, ale bez przeciążania MVP zbyt ciężką architekturą

## Ważne zastrzeżenie na przyszłość
Jeżeli w dalszych iteracjach produktu pojawi się model biznesowy oparty częściowo o dane użytkowników, to będzie to wymagało:

- osobnej decyzji produktowej,
- wyraźnej zgody użytkownika,
- jasnej polityki prywatności,
- zgodności prawnej i bezpieczeństwa na znacznie wyższym poziomie.

To nie jest część MVP.
