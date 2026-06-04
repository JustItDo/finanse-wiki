# Inbox - rozpisane updatey

## Powiązane notatki

- [[../Inbox zmian|Inbox zmian]]
- [[../Backlog|Backlog]]
- [[../Plan wdrożeń feedbacku testerskiego|Plan wdrożeń feedbacku testerskiego]]
- [[../Roadmapa|Roadmapa]]
- [[../../START SESJI CODEX|Start sesji Codex]]

## Cel

Ten folder rozbija wybrane pomysły z [[../Inbox zmian|Inbox zmian]] na konkretne, osobne update'y do późniejszego wdrożenia w `finanse-app`.

To nie jest jeszcze implementacja. Każda notatka ma być gotowym briefem do osobnej sesji `Codex: Finanse`.

## Zasady użycia

- jeden plik = jeden update
- każdy update ma własny zakres, ryzyka, kryteria akceptacji i test telefonu
- wdrożenia uruchamiać osobno, bez mieszania kilku zmian w jednej sesji
- po wdrożeniu konkretnego update'u uzupełnić [[../Dziennik wdrożeń|Dziennik wdrożeń]] i aktualny stan repo

## Lista update'ów

1. [[01 Historia - filtry i domyślny zakres]]
2. [[02 Zwijane sekcje UI]]
3. [[03 Budżety - limit 0 jako bez limitu]]
4. [[04 Ustawienia jako centrum aplikacji]]
5. [[05 Backup do plików telefonu]]
6. [[06 Analiza - wybór okresu]]
7. [[07 Analiza - bilans okresu]]
8. [[08 Ustawienia - reset stanu i komunikatów]]
9. [[09 Historia - inline szczegóły i edycja transakcji]]
10. [[10 Rebranding v2 - nowe logo i żywszy UI]]
11. [[10A Rebranding v2 - kolory i logo]]
12. [[10B Rebranding v2 - wdrożenie w kodzie]]
13. [[11 Tryb ciemny i system motywów]]
14. [[12 Motywy kolorystyczne - wybór palety]]
15. [[13 Start aplikacji - nazwa i splash]]

## Proponowana kolejność

1. [[01 Historia - filtry i domyślny zakres]] - najbliżej codziennego użycia i już częściowo zgodne z istniejącą historią.
2. [[08 Ustawienia - reset stanu i komunikatów]] - mały bugfix po zmianach w ustawieniach i backupie.
3. [[09 Historia - inline szczegóły i edycja transakcji]] - duża poprawa mobile UX historii.
4. [[03 Budżety - limit 0 jako bez limitu]] - mały, konkretny porządek modelu UX budżetów.
5. [[04 Ustawienia jako centrum aplikacji]] - porządkuje miejsce dla backupu i przyszłej synchronizacji.
6. [[05 Backup do plików telefonu]] - naturalny następny krok po ustawieniach.
7. [[10A Rebranding v2 - kolory i logo]] - najpierw decyzja o palecie i logo bez zmian w kodzie.
8. [[10B Rebranding v2 - wdrożenie w kodzie]] - dopiero po decyzji z `10A`.
9. [[13 Start aplikacji - nazwa i splash]] - pilny bugfix startu aplikacji, bez czekania na finalne logo.
10. [[11 Tryb ciemny i system motywów]] - dopiero po tokenizacji brandingu i kolorów.
11. [[12 Motywy kolorystyczne - wybór palety]] - po `11`, żeby nie robić dwóch osobnych systemów theme.
12. [[06 Analiza - wybór okresu]] - przygotowuje analizę pod dłuższe zakresy.
13. [[07 Analiza - bilans okresu]] - korzysta z wybranego okresu.
14. [[02 Zwijane sekcje UI]] - najlepiej wdrażać po identyfikacji ekranów, które realnie są za ciężkie.
