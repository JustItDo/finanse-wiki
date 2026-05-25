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

## Wdrożenie MVP w `04.0`
- bazową blokadą wejścia jest lokalny `PIN 4-cyfrowy`
- biometria jest opcjonalnym skrótem odblokowania ponad tym samym PIN-em, a nie osobnym systemem kont
- sekret blokady i ustawienia bezpieczeństwa są trzymane poza `SQLite`:
  - natywnie w `expo-secure-store`
  - na webie w fallbacku przeglądarkowym zgodnym z ograniczeniami platformy
- aplikacja blokuje dostęp przy starcie i po wznowieniu z tła
- baza `SQLite` i lokalne załączniki nie są jeszcze pełnie szyfrowane w tym etapie

## Ograniczenia obecnego poziomu ochrony
- obecne MVP chroni przed przypadkowym lub szybkim dostępem do otwartej aplikacji, ale nie jest jeszcze ochroną klasy full-device forensic
- załączniki i rekordy finansowe pozostają zapisane lokalnie tak jak dotąd, więc pełne szyfrowanie danych spoczynkowych jest tematem na późniejszy etap
- pełny test `Face ID` na iOS wymaga development builda, bo `Expo Go` nie pokrywa tego scenariusza

## Ważne zastrzeżenie na przyszłość
Jeżeli w dalszych iteracjach produktu pojawi się model biznesowy oparty częściowo o dane użytkowników, to będzie to wymagało:

- osobnej decyzji produktowej,
- wyraźnej zgody użytkownika,
- jasnej polityki prywatności,
- zgodności prawnej i bezpieczeństwa na znacznie wyższym poziomie.

To nie jest część MVP.
