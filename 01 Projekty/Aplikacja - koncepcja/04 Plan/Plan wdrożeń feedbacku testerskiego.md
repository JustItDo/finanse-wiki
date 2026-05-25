# Plan wdrożeń feedbacku testerskiego

## Powiązane notatki

- [[Backlog]]
- [[Feedback testerski 2026-05-25]]
- [[Roadmapa]]
- [[Dziennik wdrożeń]]
- [[../START SESJI CODEX|Start sesji Codex]]

## Cel dokumentu

To jest operacyjny plan wdrażania feedbacku od testerów po wypuszczeniu `.apk`.

Ma jasno ustawiać:

- kolejność paczek zmian,
- zakres każdej paczki,
- gotowe prompty do uruchomienia w `VS Code` w repo `finanse-app`.

## Ustalona kolejność

Zgodnie z aktualnym priorytetem pracujemy w tej kolejności:

1. `Paczka 3` - klawiatura, safe area i małe ekrany
2. `Paczka 4` - logowanie, PIN, biometria i sesja
3. `Paczka 2` - kategorie i budżety
4. `Paczka 1` - historia oraz dashboard copy i filtrowanie miesięcy

## Paczka 3 - klawiatura, safe area i małe ekrany

### Zakres

- poprawić pola formularzy tak, żeby klawiatura nie zasłaniała wpisywanej treści
- poprawić ekran dodawania transakcji pod małe ekrany
- poprawić dolne menu na telefonach z systemowym dolnym paskiem
- dopilnować poprawnego `safe area` i zachowania scrolla przy focusie pól

### Status

- `wdrożone lokalnie w repo finanse-app`
- wynik:
  - formularze i lista z edycją dostały poprawione zachowanie z klawiaturą
  - `Dodaj transakcję` lepiej działa na małych ekranach
  - tabbar uwzględnia dolny bezpieczny inset telefonu
  - root safe area i dolne paddingi ekranów zostały ujednolicone lekkim helperem współdzielonym
- następny krok:
  - ręczny test telefonu dla tej paczki
  - potem przejść do `Paczki 4`

### Prompt do VS Code

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Feedback testerski 2026-05-25.md`
- `04 Plan/Backlog.md`

Teraz wdrażamy paczkę 3 z planu feedbacku testerskiego.

Cel:
Naprawić problemy z klawiaturą, safe area i małymi ekranami na telefonie.

Zakres:
- poprawić formularze tak, żeby klawiatura nie zasłaniała pól tekstowych podczas wpisywania
- poprawić ekran dodawania transakcji pod małe ekrany
- poprawić dolne menu tak, żeby nie było zasłaniane przez systemowy pasek telefonu
- dopilnować poprawnego zachowania scrolla, insetów i safe area

Zasady:
- pracuj konkretnie w plikach
- nie rozlewaj zakresu na inne paczki
- jeśli trzeba, zrób mały lokalny refaktor tylko w obrębie tego flow
- po zmianach podaj, co poprawiłeś i co sprawdzić ręcznie na telefonie

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```

## Paczka 4 - logowanie, PIN, biometria i sesja

### Zakres

- dodać pytanie przy pierwszym uruchomieniu, czy użytkownik chce ustawić PIN
- jeśli tak, przekierować do `Bezpieczeństwo`
- jeśli nie, zapamiętać wybór i nie pytać ponownie
- poprawić UI odblokowania PIN-em:
  - 4 pola / kreski
  - zamiast cyfr kropki
- usunąć tekst `PIN zapasowy`, zostawić tylko `PIN`
- przy wyłączeniu biometrii wymagać potwierdzenia palcem albo PIN-em
- usunąć zbędne napisy `sesja` i `Face ID / odcisk palca` z panelu logowania
- dopilnować logiki sesji zgodnie z wcześniejszym feedbackiem

### Status wdrożenia

- status: `wdrożone lokalnie`
- zrobione:
  - prompt pierwszego uruchomienia pyta o ustawienie PIN-u i prowadzi do zakładki `Bezpieczeństwo`
  - wybór `Nie teraz` jest zapamiętywany lokalnie
  - ekran odblokowania używa 4 pól PIN-u z maskowaniem cyfr kropkami
  - copy zostało uproszczone do `PIN` i `biometria`
  - wyłączenie biometrii wymaga potwierdzenia biometrią albo PIN-em
  - sesja po odblokowaniu nadal pozwala wrócić z aparatu lub galerii bez zbędnego ponownego PIN-u
- do sprawdzenia ręcznie:
  - pierwszy start bez PIN-u
  - anulowanie promptu biometrii i ręczne odblokowanie PIN-em
  - wyłączenie biometrii obiema ścieżkami potwierdzenia

### Prompt do VS Code

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Feedback testerski 2026-05-25.md`
- `04 Plan/Backlog.md`

Teraz wdrażamy paczkę 4 z planu feedbacku testerskiego.

Cel:
Poprawić logowanie, PIN, biometrię i UX sesji.

Zakres:
- przy pierwszym uruchomieniu zapytać użytkownika, czy chce ustawić PIN
- jeśli chce, skierować go do zakładki `Bezpieczeństwo`
- jeśli nie chce, zapamiętać wybór i nie pokazywać ponownie tego pytania
- poprawić ekran odblokowania:
  - 4 pola / kreski na PIN
  - maskowanie cyfr kropkami
- zmienić copy tak, żeby nie było `PIN zapasowy`, tylko `PIN`
- przy usuwaniu biometrii wymagać potwierdzenia palcem albo PIN-em
- usunąć zbędne napisy `sesja` i `Face ID / odcisk palca` z panelu logowania
- utrzymać sensowną logikę aktywnej sesji i nie wracać do ponownego PIN-u po zwykłych akcjach

Zasady:
- pracuj konkretnie w plikach
- nie ruszaj innych paczek bez potrzeby 
- po zmianach podaj, co poprawiłeś i co trzeba ręcznie sprawdzić na telefonie

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```

## Paczka 2 - kategorie i budżety

### Zakres

- możliwość dodania własnej kategorii
- możliwość usuwania istniejących kategorii
- możliwość dowolnej modyfikacji kategorii
- przebudowa zakładki `Budżet`:
  - lista kategorii z krótkim opisem
  - kwota ustawiana dopiero po wejściu w element
- zmiana nazewnictwa:
  - `Aktywne bez limitu` -> `Kategorie bez limitu`
  - `Aktywne kategorie z limitem` dla drugiej sekcji
- skrócenie zbyt długich opisów w najważniejszych kategoriach budżetowych

### Status wdrożenia

- status: `wdrożone lokalnie`
- zrobione:
  - dodawanie własnych kategorii
  - edycja istniejących kategorii
  - usuwanie kategorii z czyszczeniem limitu i odłączeniem starych transakcji od kategorii
  - lista kategorii z krótkim opisem i osobnym wejściem w detal do ustawienia limitu
  - zmiana nazw sekcji na `Kategorie z limitem` i `Kategorie bez limitu`
  - skrócenie opisów w głównych sekcjach budżetowych
  - wybór ikony kategorii, widocznej potem na dashboardzie
- do sprawdzenia ręcznie:
  - dodanie własnej kategorii wydatkowej i przychodowej
  - ustawienie limitu dopiero po wejściu w detal kategorii
  - usunięcie kategorii użytej wcześniej w transakcjach

### Prompt do VS Code

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Feedback testerski 2026-05-25.md`
- `04 Plan/Backlog.md`

Teraz wdrażamy paczkę 2 z planu feedbacku testerskiego.

Cel:
Przebudować obszar kategorii i budżetów pod realne codzienne używanie.

Zakres:
- dodać możliwość tworzenia własnych kategorii
- dodać możliwość usuwania istniejących kategorii
- dodać możliwość modyfikacji kategorii
- przebudować zakładkę `Budżet`, żeby pokazywała listę kategorii z krótkim opisem
- ustalanie kwoty ma się odbywać dopiero po wejściu w dany element
- zmienić nazwę `Aktywne bez limitu` na sensowniejszą, np. `Kategorie bez limitu`
- odpowiednio nazwać sekcję kategorii z limitem
- skrócić zbyt długie opisy przy najważniejszych kategoriach budżetowych

Zasady:
- pracuj konkretnie w plikach
- nie mieszaj tej paczki z dashboardem i historią
- jeśli potrzebny jest mały refaktor modeli albo UI budżetów, możesz go zrobić w granicach tej paczki
- po zmianach podaj, co wdrożyłeś i jakie są skutki uboczne lub migracyjne

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```

## Paczka 1 - historia oraz dashboard copy i filtrowanie miesięcy

### Zakres

- w historii dodać opcję `wszystkie miesiące`
- w dashboardzie umożliwić wejście do miesięcy, których jeszcze nie było, jeśli to ma sens dla flow
- usunąć niepotrzebny tekst pustego stanu i wzmiankę o `guardrailach budżetowych`
- zmienić `cel oszczędności` na `cel oszczędnościowy`
- skrócić lub usunąć zbędny tekst przy najważniejszych kategoriach budżetowych, jeśli jeszcze został
- zmienić `Sytuacja miesiąca` na `Ten miesiąc`

### Status wdrożenia

- status: `wdrożone lokalnie`
- zrobione:
  - historia ma opcję `Wszystkie miesiące`
  - dashboard zachowuje prosty dostęp do pustych miesięcy przez istniejący przełącznik
  - usunięty został tekst o `guardrailach budżetowych`
  - `Cel oszczędności` zmieniono na `Cel oszczędnościowy`
  - `Sytuacja miesiąca` zmieniono na `Ten miesiąc`
  - skrócone zostały zbędne teksty w pustych i pomocniczych sekcjach dashboardu
- do sprawdzenia ręcznie:
  - historia z filtrem `Wszystkie miesiące`
  - dashboard dla miesiąca bez transakcji i dla kolejnego przyszłego miesiąca

### Prompt do VS Code

```text
Pracujemy w projekcie `finanse-app` i `finanse-wiki`.

Najpierw wykonaj obowiązkową procedurę startową projektu z wiki.
Potem przeczytaj:
- `04 Plan/Feedback testerski 2026-05-25.md`
- `04 Plan/Backlog.md`

Teraz wdrażamy paczkę 1 z planu feedbacku testerskiego.

Cel:
Poprawić historię oraz copy i zachowanie dashboardu.

Zakres:
- w historii dodać możliwość wybrania opcji `wszystkie miesiące`
- poprawić dashboard tak, żeby można było wejść także do miesięcy, których jeszcze nie było, jeśli zachowanie ma sens dla produktu
- usunąć niepotrzebny tekst pustego stanu i wzmiankę o `guardrailach budżetowych`
- zmienić `cel oszczędności` na `cel oszczędnościowy`
- zmienić `Sytuacja miesiąca` na `Ten miesiąc`
- skrócić albo usunąć zbędne teksty przy sekcjach informacyjnych, jeśli nadal są zbyt długie

Zasady:
- pracuj konkretnie w plikach
- nie rozwalaj logiki danych tylko po to, żeby zmienić copy
- jeśli któryś punkt wymaga decyzji produktowej, wybierz najprostszy wariant zgodny z aktualnym feedbackiem
- po zmianach podaj, co poprawiłeś i co trzeba sprawdzić ręcznie

Pisz po polsku i wdrażaj zmiany, nie kończ na samym opisie.
```

## Uwaga operacyjna

Każdą paczkę odpalaj osobno w `VS Code` z repo `finanse-app` jako głównym workspace.

Nie mieszaj dwóch paczek w jednym promptcie, jeśli nie ma bardzo mocnego powodu.
