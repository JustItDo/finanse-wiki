# Updatey wdrożeniowe

## Powiązane notatki

- [[../../Mapa projektu|Mapa projektu]]
- [[../Roadmapa|Roadmapa]]
- [[../Backlog|Backlog]]
- [[../Plan updateów wdrożeniowych|Plan updateów wdrożeniowych]]
- [[../../02 Produkt/MVP|MVP]]
- [[../../03 Technologia/Decyzje techniczne|Decyzje techniczne]]

To jest roboczy folder do przechodzenia przez wdrożenie krok po kroku.

## Jak z tego korzystać
- realizuj update'y po kolei według numeracji
- każdy plik opisuje osobny zakres wdrożeniowy
- po zakończeniu update'u wróć do tego indeksu i przejdź do następnego

## Kolejność
1. [00.1 Start projektu](./00.1 Start projektu.md)
2. [00.2 Lokalna baza i modele](./00.2 Lokalna baza i modele.md)
3. [00.3 Kategorie i budżet startowy](./00.3 Kategorie i budżet startowy.md)
4. [01.0 Ręczne dodawanie wydatku](./01.0 Ręczne dodawanie wydatku.md)
5. [01.1 Ręczne dodawanie przychodu](./01.1 Ręczne dodawanie przychodu.md)
6. [01.2 Dashboard MVP](./01.2 Dashboard MVP.md)
7. [01.3 Historia transakcji](./01.3 Historia transakcji.md)
8. [02.0 OCR i dodawanie zdjęcia](./02.0 OCR i dodawanie zdjęcia.md)
9. [02.1 Korekta OCR](./02.1 Korekta OCR.md)
10. [02.2 Dashboard po OCR](./02.2 Dashboard po OCR.md)
11. [03.0 Budżety](./03.0 Budżety.md)
12. [03.1 Analizy](./03.1 Analizy.md)
13. [03.2 Oszczędności](./03.2 Oszczędności.md)
14. [04.0 Bezpieczeństwo](./04.0 Bezpieczeństwo.md)
15. [04.1 Poprawki UX i wydajności](./04.1 Poprawki UX i wydajności.md)
16. [04.2 Test MVP](./04.2 Test MVP.md)

## Najlepszy punkt wejścia
Jeśli zaczynasz development teraz, zacznij od:

1. [00.1 Start projektu](./00.1 Start projektu.md)
2. [00.2 Lokalna baza i modele](./00.2 Lokalna baza i modele.md)
3. [00.3 Kategorie i budżet startowy](./00.3 Kategorie i budżet startowy.md)
4. [01.0 Ręczne dodawanie wydatku](./01.0 Ręczne dodawanie wydatku.md)

## Stan realizacji

- `00.1 Start projektu`:
  - wykonane w workspace aplikacji
  - obejmuje setup `Expo + React Native + TypeScript`, nawigację, wspólne UI i bazową konfigurację jakości
- `00.2 Lokalna baza i modele`:
  - wykonane w workspace aplikacji
  - obejmuje warstwę danych `SQLite`, migracje, seed, repozytoria i fallback webowy
- `00.3 Kategorie i budżet startowy`:
  - wykonane w workspace aplikacji
  - obejmuje konfigurację kategorii, budżetu miesiąca, budżetów kategorii i logikę przeliczania stanu budżetu
- `01.0 Ręczne dodawanie wydatku`:
  - wykonane w repo `finanse-app`
  - razem z `01.1` domknięte commitem `49fac8f`
- `01.1 Ręczne dodawanie przychodu`:
  - wykonane w repo `finanse-app`
  - obejmuje wspólny formularz transakcji, zapis przychodu i wspólne agregacje bilansu miesiąca
- `01.2 Dashboard MVP`:
  - wykonane w repo `finanse-app`
  - obejmuje główny ekran miesiąca z przychodami, wydatkami, bilansem, stanem budżetu, kategoriami budżetowymi, pustymi stanami i prostym przełącznikiem miesiąca

## Stan Git a stan wdrożenia

- stan wdrożenia `00.1-01.1` jest już zapisany w historii repo `finanse-app`
- ostatni commit aplikacji: `49fac8f` `01.0-01.1 Add shared manual transaction entry flow`
- lokalny workspace aplikacji ma też przygotowany update `01.2 Dashboard MVP`
- kolejnym logicznym krokiem wdrożeniowym pozostaje `01.3 Historia transakcji`

## Otwarte decyzje przed pierwszym commitem
- wybór biblioteki lub podejścia do OCR on-device
- decyzja, czy web rozwijasz równolegle od dnia 1, czy tylko utrzymujesz zgodność techniczną
- minimalny zestaw kategorii startowych
- decyzja, czy cel oszczędności wchodzi do modelu danych od razu, czy dopiero w `03.2`
- decyzja, czy historia ma wspierać edycję i usuwanie już w pierwszej wersji

## Dokument źródłowy
Pełny plan zbiorczy pozostaje w [Plan updateów wdrożeniowych](../Plan updateów wdrożeniowych.md).
