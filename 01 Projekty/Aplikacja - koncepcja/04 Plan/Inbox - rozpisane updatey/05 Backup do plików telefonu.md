# 05 Backup do plików telefonu

## Powiązane notatki

- [[README|Inbox - rozpisane updatey]]
- [[../Inbox zmian|Inbox zmian]]
- [[../Backlog|Backlog]]
- [[../Plan wdrożeń feedbacku testerskiego|Plan wdrożeń feedbacku testerskiego]]

## Cel update'u

Dać użytkownikowi kontrolę nad miejscem zapisu backupu, żeby eksport danych nie kończył się wyłącznie systemowym udostępnianiem do innej aplikacji.

## Wybrany wariant

`5B`:

- jeden główny przycisk `Utwórz backup`
- potem wybór sposobu: `Zapisz do plików` albo `Udostępnij`

## Opis UX

W sekcji backupu użytkownik widzi główną akcję `Utwórz backup`. Po jej wybraniu aplikacja przygotowuje plik ZIP i pyta, co zrobić dalej: zapisać do plików telefonu albo udostępnić przez systemowy share sheet.

`Zapisz do plików` ma być preferowaną ścieżką dla prywatnego archiwum. `Udostępnij` zostaje jako elastyczna alternatywa.

## Zakres wdrożenia

- zmienić UI eksportu na jeden główny przycisk `Utwórz backup`
- po przygotowaniu pliku pokazać wybór `Zapisz do plików` / `Udostępnij`
- sprawdzić techniczną możliwość zapisu do lokalizacji wybranej przez użytkownika na Androidzie w Expo
- zachować obecny format backupu ZIP
- zachować import z pliku jako ścieżkę spójną z eksportem
- jasno komunikować, że backup zawiera wrażliwe dane finansowe

## Poza zakresem

- szyfrowanie backupu
- automatyczny backup cykliczny
- synchronizacja chmurowa
- backup sekretów PIN-u lub biometrii
- zmiana formatu `manifest.json` i `data.json`, jeśli nie jest wymagana

## Ryzyka

- Expo / Android mogą ograniczać bezpośredni zapis do dowolnego folderu
- różne wersje Androida mogą inaczej obsługiwać picker plików
- jeśli zapis do plików nie jest dostępny, UX musi mieć uczciwy fallback do udostępniania

## Kryteria akceptacji

- użytkownik zaczyna eksport jednym przyciskiem `Utwórz backup`
- po utworzeniu backupu może wybrać `Zapisz do plików`
- użytkownik może nadal wybrać `Udostępnij`
- utworzony plik ma ten sam poprawny format backupu ZIP
- import działa z plikiem zapisanym lokalnie
- komunikat ostrzega, że plik backupu zawiera dane finansowe

## Test ręczny na telefonie

- utworzyć backup i wybrać `Zapisz do plików`
- sprawdzić, czy plik ZIP jest widoczny w wybranej lokalizacji telefonu
- utworzyć backup ponownie i wybrać `Udostępnij`
- zaimportować zapisany lokalnie plik
- sprawdzić zachowanie anulowania wyboru lokalizacji

## Prompt do późniejszego wdrożenia w `Codex: Finanse`

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox - rozpisane updatey/05 Backup do plików telefonu.md`
- `03 Technologia/Decyzje techniczne.md`
- `03 Technologia/Stan repo aplikacji.md`

Cel:
Wdrożyć wariant `5B`: jeden przycisk `Utwórz backup`, a po przygotowaniu pliku wybór `Zapisz do plików` albo `Udostępnij`.

Zasady:
- zachowaj obecny format backupu ZIP
- najpierw sprawdź możliwości Expo/Android w aktualnej wersji projektu
- nie wdrażaj szyfrowania ani synchronizacji
- po zmianach uruchom dostępne sprawdzenia jakości

Na końcu podaj zmienione pliki, wynik weryfikacji i test ręczny na telefonie.
```

