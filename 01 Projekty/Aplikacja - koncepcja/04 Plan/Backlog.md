# Backlog

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[Roadmapa]]
- [[Plan updateów wdrożeniowych]]
- [[Feedback testerski 2026-05-25]]
- [[Plan wdrożeń feedbacku testerskiego]]
- [[Plan rebrandingu Zenifi]]
- [[Inbox zmian]]
- [[Inbox - rozpisane updatey/README|Inbox - rozpisane updatey]]
- [[../02 Produkt/MVP|MVP]]
- [[../02 Produkt/User flow|User flow]]
- [[../03 Technologia/Decyzje techniczne|Decyzje techniczne]]
- [[../03 Technologia/Model danych implementacyjny|Model danych implementacyjny]]

## Do omówienia
- dokładna lista kategorii startowych
- wybór i konfiguracja runnera testów jednostkowych dla `finanse-app`
- ewentualny powrót do `LM Studio` dopiero po rozwiązaniu timeoutów MCP
- wybrać priorytet wdrażania z [[Inbox - rozpisane updatey/README|rozpisanych update'ów z inboxu]]

## Do rozpisania
- jak ma działać szybkie ręczne dodawanie wydatku
- jak ma działać korekta błędnego OCR
- jak ma zachowywać się dashboard, żeby nie był przeładowany
- jak utrzymać spójność kategorii i sensowną analitykę
- jak przygotować model danych pod późniejszy sync i chmurę

## Gotowe do realizacji
- plan updateów wdrożeniowych
- lista ekranów aplikacji
- user flow
- finalny stack technologiczny
- model danych implementacyjny
- szybka poprawka sesji po `04.2`:
  - logowanie PIN-em albo biometrią ma otwierać aktywną sesję
  - dodanie paragonu nie może wymagać ponownego wpisania PIN-u
  - ponowna autoryzacja ma wracać dopiero po wygaśnięciu sesji albo dla akcji wrażliwych
- pakiet poprawek po review jakości i UX:
  - ograniczyć nadmiar tekstu na ekranach
  - usunąć pozostałe napisy typu `update` i inne robocze artefakty
  - poprawić ekran dodawania transakcji tak, żeby klawiatura nie zasłaniała połowy ekranu
  - zmienić komunikat po zapisie wydatku na krótszy i mniej zasłaniający flow, najlepiej nisko i w formie prostego `Dodano`
  - dopracować panel logowania wizualnie i UX-owo
  - uprościć usuwanie tak, żeby drugie kliknięcie `Usuń` potwierdzało akcję zamiast pokazywania osobnego przycisku niżej

## Po review
- najpierw zrobić pełne review jakości kodu, czystości struktury i UX
- potem połączyć findings z listą poprawek produktowych i wdrożyć jeden sensowny pakiet zmian
- uwzględnić pełną listę z `Feedback testerski 2026-05-25`
- wdrażać paczki w kolejności zapisanej w `Plan wdrożeń feedbacku testerskiego`

## Zrobione
