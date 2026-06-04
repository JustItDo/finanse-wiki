# 08 Ustawienia - reset stanu i komunikatów

## Powiązane notatki

- [[../Inbox zmian|Inbox zmian]]
- [[04 Ustawienia jako centrum aplikacji]]
- [[05 Backup do plików telefonu]]

## Cel

Naprawić zachowanie ustawień tak, aby po wyjściu z ekranu i ponownym wejściu użytkownik widział główne menu ustawień, a nie ostatnio otwarty podwidok.

Dodatkowo komunikaty po eksporcie backupu nie powinny wisieć po zmianie taba albo po ponownym wejściu do ustawień.

## Warianty

### Wariant A

- czyścić tylko `feedback` i `error`
- zostawiać ostatnio otwartą sekcję ustawień
- najmniejsza zmiana, ale nie rozwiązuje problemu powrotu do podwidoku

### Wariant B

- po opuszczeniu taba `Ustawienia` wracać zawsze do `home`
- czyścić `feedback`, `error`, `backupSummary` i ewentualne potwierdzenia
- formularze PIN / import zostawiać tylko tam, gdzie ich reset nie irytuje użytkownika
- **rekomendowany wariant**

### Wariant C

- twardy reset całego ekranu ustawień po każdym wyjściu
- czyścić wszystkie formularze i wszystkie stany sekcji
- najczyściej technicznie, ale może być zbyt agresywne

## Rekomendacja

`Wariant B`.

To najlepiej pasuje do ustawień jako centralnego menu i rozwiązuje konkretny błąd z backup summary oraz zapamiętywaniem podwidoku.

## Zakres

- reset `activeSection` na `home` przy opuszczeniu ekranu
- czyszczenie komunikatów i zapamiętanych wyników akcji
- powrót do głównego kaflowego menu ustawień

## Poza zakresem

- przebudowa całego ekranu ustawień
- zmiana logiki PIN / biometrii
- nowy system nawigacji z nested stackami

## Ryzyka

- niechciany reset formularzy przy powrocie
- komunikat może zostać ustawiony po async akcji, jeśli nie dodamy guardów

## Kryteria Akceptacji

- po eksporcie backupu komunikat znika po opuszczeniu ustawień
- po ponownym wejściu do ustawień widoczny jest ekran główny, a nie konkretny podwidok
- użytkownik nie wraca do poprzedniej sekcji przez przypadek

## Test Telefonu

- wejść w ustawienia
- otworzyć backup
- zrobić eksport
- przełączyć tab
- wrócić do ustawień
- sprawdzić, czy startuje główne menu

## Prompt Do Codexa

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox zmian.md`
- `04 Plan/Inbox - rozpisane updatey/08 Ustawienia - reset stanu i komunikatów.md`
- `04 Plan/Inbox - rozpisane updatey/04 Ustawienia jako centrum aplikacji.md`
- `04 Plan/Inbox - rozpisane updatey/05 Backup do plików telefonu.md`

Cel:
Naprawić zachowanie ustawień: po wyjściu z taba i ponownym wejściu ma być główne menu ustawień, a nie ostatni podwidok.

Zakres:
- reset `activeSection` na `home` przy opuszczeniu ustawień
- czyszczenie `feedback`, `error` i `backupSummary`
- dopilnowanie, żeby komunikaty backupu nie wisiały po zmianie taba

Zasady:
- pracuj konkretnie w plikach
- nie przebudowuj całych ustawień
- nie zmieniaj logiki PIN / biometrii poza tym, co jest potrzebne do resetu stanu
- po zmianach podaj, co dokładnie się resetuje i co zostało celowo zostawione

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```

