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
17. [04.3 Backup ZIP](./04.3 Backup ZIP.md)

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
- `01.3 Historia transakcji`:
  - wykonane lokalnie w repo `finanse-app`
  - obejmuje listę transakcji, filtrowanie, wyszukiwanie, szczegół oraz prostą edycję i usuwanie z zachowaniem spójnych agregacji
- `02.0 OCR i dodawanie zdjęcia`:
  - wykonane lokalnie w repo `finanse-app`
  - obejmuje aparat dla paragonu, galerię dla screena płatności oraz fallback `paragon z galerii` do testów emulatora
  - obejmuje lokalny zapis załącznika, OCR on-device, podstawowe mapowanie danych do formularza i fallback ręczny
- `02.1 Korekta OCR`:
  - wykonane lokalnie w repo `finanse-app`
  - obejmuje ekran korekty OCR, oznaczanie pól niepewnych, poprawę kluczowych pól i zapis do tego samego flow co wpis ręczny
- `02.2 Dashboard po OCR`:
  - wykonane lokalnie w repo `finanse-app`
  - obejmuje pełne spięcie `OCR -> korekta -> zapis -> budżet -> dashboard -> historia`
  - obejmuje spójne oznaczenie źródła wpisu i wspólną ścieżkę danych dla OCR i wpisu ręcznego
- `03.0 Budżety`:
  - wykonane lokalnie w repo `finanse-app`
  - obejmuje pełny ekran budżetów z porządkiem sekcji, procentem wykorzystania, sygnałami ryzyka i wspólną logiką statusów poza UI
  - obejmuje utrzymanie konfiguracji limitów i budżetu miesiąca bez rozdzielania osobnego flow danych
- `03.1 Analizy`:
  - wykonane lokalnie w repo `finanse-app`
  - obejmuje ekran analiz z przełącznikiem bieżącego i poprzedniego miesiąca
  - obejmuje wykres udziału kategorii, największe kategorie kosztów i trend dzienny wydatków
  - obejmuje lekką warstwę agregacji analitycznej poza komponentami UI
- `03.2 Oszczędności`:
  - wykonane lokalnie w repo `finanse-app`
  - obejmuje miesięczny, kwotowy cel oszczędności liczony jako `przychody - wydatki`
  - obejmuje ustawianie celu w `Budżetach` i pokazywanie postępu celu na `Dashboardzie`
  - obejmuje wspólną logikę postępu celu poza komponentami UI
- `04.3 Backup ZIP`:
  - wykonane lokalnie w repo `finanse-app`
  - obejmuje ręczny eksport i import pliku ZIP z danymi finansowymi oraz załącznikami
  - backup nie przenosi PIN-u, biometrii ani sekretów z `SecureStore`
  - import scala dane po stabilnych `id` i nie kasuje lokalnego stanu

## Stan Git a stan wdrożenia

- stan wdrożenia `00.1-01.3` jest już zapisany w historii repo `finanse-app`
- nowsze lokalne commity obejmują `01.3`, pierwszy commit `02.0-02.1` oraz późniejszą korektę budżetów
- lokalny workspace ma już domknięte także poprawki OCR, `02.2`, `03.0`, `03.1`, `03.2` i ręcznie sprawdzony flow OCR na emulatorze

## Otwarte decyzje i ryzyka
- decyzja, czy `Wybierz paragon z galerii` zostaje jako normalna ścieżka MVP, czy tylko wygodny fallback testowy
- decyzja, czy web rozwijasz równolegle od dnia 1, czy tylko utrzymujesz zgodność techniczną
- przed `04.0` warto zrobić krótki ręczny smoke test celu oszczędności na danych z przychodami i wydatkami

## Dokument źródłowy
Pełny plan zbiorczy pozostaje w [Plan updateów wdrożeniowych](../Plan updateów wdrożeniowych.md).
