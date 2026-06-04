# 04 Ustawienia jako centrum aplikacji

## Powiązane notatki

- [[README|Inbox - rozpisane updatey]]
- [[../Inbox zmian|Inbox zmian]]
- [[../Backlog|Backlog]]
- [[../Plan wdrożeń feedbacku testerskiego|Plan wdrożeń feedbacku testerskiego]]

## Cel update'u

Przebudować `Ustawienia` w centralne miejsce konfiguracji aplikacji, zamiast ekranu będącego głównie listą opcji bezpieczeństwa i backupu.

## Wybrany wariant

`4B` z późniejszą korektą po rebrandingu:

- kafle ustawień z krótkim opisem i wejściem w szczegół
- sekcje: bezpieczeństwo, backup/dane, synchronizacja, motywy, aplikacja

## Opis UX

Ekran `Ustawienia` pokazuje krótkie kafle / wiersze wejściowe. Każdy kafel ma nazwę, jednozdaniowy opis i stan pomocniczy, np. `PIN włączony`, `Backup lokalny`, `Sync niedostępny w MVP`.

Kliknięcie kafla prowadzi do szczegółu albo rozwija sekcję. Na start wystarczy szczegół dla istniejących funkcji: bezpieczeństwo i backup/dane. Synchronizacja może mieć stan informacyjny bez działania, jeśli nie jest jeszcze wdrażana.

Po dodaniu systemu motywów `Motywy` mają być osobną kategorią ustawień, a nie blokiem wrzuconym do `Aplikacja`.

`Aplikacja` ma zostać miejscem na informacje techniczne:

- nazwa
- wersja
- tryb danych
- platforma
- informacje o działaniu offline-first

`Motywy` mają trzymać:

- tryb: `Systemowy`, `Jasny`, `Ciemny`
- kolorystykę: np. `Neon Mint`, `Electric Pine`, `Signal Finance`

## Zakres wdrożenia

- przebudować pierwszy widok `Ustawień` na listę kafli
- dodać kafel `Bezpieczeństwo` dla PIN-u, biometrii i blokady
- dodać kafel `Backup i dane` dla eksportu, importu i informacji o danych lokalnych
- dodać kafel `Synchronizacja` jako miejsce przyszłe lub stan `Jeszcze niedostępne`
- dodać kafel `Motywy` dla trybu jasnego/ciemnego/systemowego i palet kolorystycznych
- dodać kafel `Aplikacja` dla informacji o aplikacji i wersji, jeśli dane są dostępne
- przenieść istniejące formularze pod szczegóły albo sekcje, bez zmiany ich logiki

## Poza zakresem

- wdrożenie realnej synchronizacji
- konta użytkowników
- pełna strona informacji prawnych
- zmiana mechaniki PIN-u, biometrii lub backupu
- redesign całej nawigacji aplikacji

## Ryzyka

- przebudowa ekranu może przypadkiem utrudnić dostęp do często używanego backupu
- szczegóły ustawień mogą wymagać dodatkowej nawigacji, jeśli obecna struktura tabów nie ma stacka
- kafel synchronizacji może sugerować gotową funkcję, jeśli copy nie będzie jasne

## Kryteria akceptacji

- dolna zakładka `Ustawienia` prowadzi do centrum konfiguracji, a nie tylko do bezpieczeństwa
- widoczne są sekcje: `Bezpieczeństwo`, `Backup i dane`, `Synchronizacja`, `Motywy`, `Aplikacja`
- istniejące akcje PIN-u, biometrii, wyłączenia blokady, eksportu i importu są nadal dostępne
- synchronizacja jest oznaczona jako przyszła albo niedostępna, jeśli nie jest wdrażana
- ustawienia motywu nie są schowane w sekcji `Aplikacja`
- ekran jest czytelny na telefonie i nie ma długiej ściany formularzy na pierwszym widoku

## Test ręczny na telefonie

- otworzyć `Ustawienia` i sprawdzić widoczność czterech głównych kafli
- wejść w `Bezpieczeństwo` i sprawdzić dostęp do PIN-u oraz biometrii
- wejść w `Backup i dane` i sprawdzić dostęp do eksportu oraz importu
- wejść w `Motywy` i sprawdzić dostęp do wyboru wyglądu
- wejść w `Aplikacja` i sprawdzić, że są tam informacje o aplikacji, a nie konfiguracja motywów
- sprawdzić, że `Synchronizacja` nie obiecuje gotowej funkcji
- wrócić z każdego szczegółu do głównego ekranu ustawień

## Prompt do późniejszego wdrożenia w `Codex: Finanse`

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox - rozpisane updatey/04 Ustawienia jako centrum aplikacji.md`
- `03 Technologia/Stan repo aplikacji.md`

Cel:
Wdrożyć wariant `4B`: `Ustawienia` jako centrum aplikacji z kaflami `Bezpieczeństwo`, `Backup i dane`, `Synchronizacja`, `Motywy`, `Aplikacja`.

Zasady:
- zachowaj istniejącą logikę PIN-u, biometrii i backupu
- nie wdrażaj realnej synchronizacji
- nie chowaj motywów w sekcji `Aplikacja`
- sekcja `Aplikacja` ma być informacyjna, a `Motywy` konfiguracyjne
- jeśli potrzebna jest lokalna nawigacja szczegółów, zrób ją najprościej zgodnie z obecną architekturą
- po zmianach uruchom dostępne sprawdzenia jakości

Na końcu podaj zmienione pliki, wynik weryfikacji i test ręczny na telefonie.
```
