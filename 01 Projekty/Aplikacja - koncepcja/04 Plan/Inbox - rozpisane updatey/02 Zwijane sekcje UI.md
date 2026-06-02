# 02 Zwijane sekcje UI

## Powiązane notatki

- [[README|Inbox - rozpisane updatey]]
- [[../Inbox zmian|Inbox zmian]]
- [[../Backlog|Backlog]]
- [[../Plan wdrożeń feedbacku testerskiego|Plan wdrożeń feedbacku testerskiego]]

## Cel update'u

Wprowadzić wspólny wzorzec zwijanych sekcji, żeby długie ekrany na telefonie były łatwiejsze do skanowania i nie wymagały ciągłego przewijania przez nieistotne w danym momencie bloki.

## Wybrany wariant

`2C`:

- wspólny mechanizm zwijania sekcji
- zapamiętywanie stanu rozwinięcia per ekran / sekcja

## Opis UX

Sekcja ma nagłówek z tytułem, krótkim podsumowaniem i chevronem. Kliknięcie nagłówka rozwija albo zwija treść. Stan jest zapamiętywany osobno dla danego ekranu i sekcji, więc użytkownik po powrocie do ekranu widzi układ, który sam ustawił.

Wzorzec ma być stosowany tylko tam, gdzie ekran realnie jest za długi albo ma kilka niezależnych obszarów. Najważniejsze akcje startowe nie powinny być chowane domyślnie.

## Zakres wdrożenia

- przygotować wspólny komponent lub helper dla zwijanej sekcji
- zapisać stan rozwinięcia per ekran i per identyfikator sekcji
- zastosować wzorzec pilotażowo na jednym lub dwóch ekranach z największym zyskiem UX
- zadbać o czytelny nagłówek, chevron i obszar klikalny
- ustalić domyślne rozwinięcie najważniejszych sekcji

## Poza zakresem

- pełna przebudowa wszystkich ekranów aplikacji
- chowanie krytycznych akcji takich jak szybkie dodanie transakcji
- animacje zaawansowane albo zależne od gestów
- synchronizacja stanu zwinięcia między urządzeniami

## Ryzyka

- zbyt agresywne zwijanie może ukryć ważne funkcje
- zapamiętany stan może utrudnić debugowanie, jeśli użytkownik zapomni, że coś zwinął
- wspólny komponent może stać się zbyt elastyczny i ciężki, jeśli od razu obsłuży zbyt wiele wariantów

## Kryteria akceptacji

- istnieje jeden wspólny mechanizm zwijania sekcji
- stan rozwinięcia jest zapamiętywany osobno dla ekranu i sekcji
- najważniejsze sekcje są domyślnie rozwinięte
- nagłówek jasno pokazuje, że sekcję można rozwinąć lub zwinąć
- na telefonie ekran pilotażowy wymaga mniej przewijania bez utraty dostępu do funkcji

## Test ręczny na telefonie

- otworzyć ekran pilotażowy i sprawdzić domyślny stan sekcji
- zwinąć i rozwinąć kilka sekcji
- przejść na inny ekran i wrócić, sprawdzając zapamiętanie stanu
- zamknąć i uruchomić aplikację ponownie, jeśli stan ma być trwały między sesjami
- potwierdzić, że żadna główna akcja nie jest ukryta w sposób zaskakujący

## Prompt do późniejszego wdrożenia w `Codex: Finanse`

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Inbox - rozpisane updatey/02 Zwijane sekcje UI.md`
- `03 Technologia/Stan repo aplikacji.md`

Cel:
Wdrożyć wariant `2C`: wspólny mechanizm zwijanych sekcji UI z zapamiętywaniem stanu rozwinięcia per ekran i per sekcja.

Zasady:
- zacznij od najwęższego sensownego pilotażu, nie przebudowuj całej aplikacji
- nie chowaj krytycznych akcji startowych
- użyj istniejących wzorców UI i storage, jeśli pasują
- po zmianach uruchom dostępne sprawdzenia jakości

Na końcu podaj zmienione pliki, ekran pilotażowy i test ręczny na telefonie.
```

