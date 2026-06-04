# Workflow developera

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[../README|README]]
- [[Decyzje techniczne]]
- [[Workflow modeli AI]]
- [[Stan repo aplikacji]]
- [[../04 Plan/Roadmapa|Roadmapa]]
- [[../04 Plan/Dziennik wdrożeń|Dziennik wdrożeń]]
- [[../START SESJI CODEX|Start sesji Codex]]

## Cel dokumentu

To jest główny dokument pracy developerskiej dla projektu `Finansowy Copilot`.

Ma jasno rozdzielać:

- gdzie trzymamy trwały kontekst projektu,
- gdzie piszemy kod,
- jak uruchamiamy Codexa,
- jak traktujemy odłożoną integrację z `LM Studio`,
- kiedy aktualizujemy wiki,
- kiedy robimy commit.

## Trzy narzędzia i ich role

### 1. Obsidian / `finanse-wiki`

To jest źródło prawdy dla:

- wizji produktu,
- zakresu MVP,
- decyzji technicznych,
- planu wdrożenia,
- statusu wykonanych etapów,
- zasad pracy zespołu i Codexa.

W wiki nie piszemy kodu aplikacji.

### 2. VS Code / `finanse-app`

To jest główne środowisko wykonawcze dla:

- implementacji ekranów,
- logiki danych,
- testów,
- konfiguracji projektu,
- pracy z Gitem dla aplikacji.

Kod aplikacji zmieniamy w `finanse-app`, nie w vaultcie.

### 3. Codex

Codex ma pomagać w realizacji jednego konkretnego zadania naraz.

Ma:

- czytać minimalny potrzebny kontekst z wiki,
- wprowadzać zmiany w odpowiednim repo,
- na końcu dopisywać do wiki stan projektu, jeśli zmiana wpływa na dokumentację lub workflow.

### 4. LM Studio / lokalny model

Integracja `LM Studio` jest obecnie odłożona i nie jest aktywną częścią startu Codexa.

Powód:

- MCP `lmstudio-unit-tests` powodował timeout startu sesji Codexa
- każda nowa sesja dostawała przez to ostrzeżenie `MCP startup incomplete`

Na teraz:

- nie używamy automatycznego MCP do `LM Studio`
- testy i planowanie testów robi Codex
- lokalny model można rozważyć później dopiero po stabilnym uruchomieniu daemonu i runnera testów

## Zasada źródła prawdy

Najważniejsza reguła:

- czat nie jest źródłem prawdy,
- commit nie jest źródłem prawdy dla decyzji produktowych,
- trwały stan projektu ma być zapisany w wiki.

To oznacza:

- decyzje produktowe zapisujemy w wiki,
- decyzje techniczne zapisujemy w wiki,
- stan wdrożenia zapisujemy w wiki,
- kod i implementację zapisujemy w repo aplikacji.

## Standardowy obieg pracy

### Krok 1. Zanim otworzysz Codexa

Najpierw ustal:

- jaki jest jeden konkretny temat sesji,
- czego dokładnie dotyczy zadanie,
- jaki ma być wynik końcowy,
- które pliki wiki są potrzebne do startu.

Jeżeli temat zmienia projekt, dopisz brief do odpowiedniej notatki w wiki.

### Krok 2. Start sesji

Jeżeli pracujesz nad aplikacją:

- otwórz repo `finanse-app` w VS Code,
- uruchom task `Codex: Finanse`,
- pozwól Codexowi pobrać kontekst z wiki,
- dopiero potem daj konkretne zadanie.

Jeżeli pracujesz tylko nad dokumentacją:

- możesz pracować bezpośrednio w `finanse-wiki`.

Jeżeli zadanie dotyczy głównie testów jednostkowych:

- użyj Codexa bezpośrednio
- ogranicz kontekst do konkretnego modułu albo funkcji
- uruchamiaj lokalne komendy projektu zamiast analizować długie logi w czacie

## Jak formułować zadanie dla Codexa

Jeden prompt powinien dotyczyć jednego głównego celu.

Dobra wiadomość startowa powinna zawierać:

- cel,
- zakres,
- poza zakresem,
- definicję ukończenia,
- 1 do 5 plików kontekstowych.

Nie każ Codexowi zgadywać, czego chcesz.

Szczegółowe zasady pracy z modelami są opisane w:

- [[Workflow modeli AI]]

## Gdzie trafiają zmiany

### Zmiany w `finanse-app`

Tutaj trafiają:

- ekrany,
- komponenty,
- logika danych,
- nawigacja,
- testy,
- konfiguracja projektu.

### Zmiany w `finanse-wiki`

Tutaj trafiają:

- nowy stan wdrożenia,
- nowe decyzje,
- korekty roadmapy,
- aktualizacja update'ów,
- workflow pracy,
- status repozytoriów.

## Kiedy trzeba aktualizować wiki

Wiki aktualizujesz zawsze, gdy zmiana wpływa na:

- stan wdrożenia,
- kolejny planowany krok,
- decyzję produktową,
- decyzję techniczną,
- workflow pracy,
- status repo,
- interpretację MVP.

Nie aktualizujesz wiki tylko wtedy, gdy zmiana jest czysto lokalna, techniczna i niczego nie zmienia na poziomie projektu.

## Reguły Git

Najważniejsza zasada:

- `1 commit = 1 logiczna zmiana`

### W repo aplikacji

Commit rób, gdy:

- zamknięty jest jeden update albo jego sensowny slice,
- kod jest spójny,
- wynik da się nazwać jednym komunikatem.

Nie rób commita:

- po każdym pojedynczym promptcie,
- w połowie zadania,
- gdy kilka tematów miesza się w jednym worktree.

### W repo wiki

Commit rób, gdy:

- zaktualizowałeś status projektu,
- dopisałeś decyzje,
- uporządkowałeś strukturę dokumentacji,
- zmieniłeś workflow albo zasady pracy.

Jeżeli da się rozdzielić kod i wiki, rób osobne commity w osobnych repo.

## Jak traktować status repo

Są dwa osobne repo:

- `finanse-wiki`
- `finanse-app`

Status jednego repo nie zastępuje statusu drugiego.

Przed końcem większej sesji sprawdź zawsze:

- `git status` w `finanse-app`
- `git status` w `finanse-wiki`

Jeżeli zmiana dotknęła obu repo, oba muszą być ocenione osobno.

## Kiedy odpalać testy

Nie odpalaj pełnych testów po każdej drobnej zmianie.

Najważniejsza zasada:

- testy uruchamiaj po domknięciu logicznego kawałka pracy, a nie po każdym promptcie

Dobra praktyka:

- mała zmiana UI:
  - zwykle wystarczy szybkie sprawdzenie ręczne na emulatorze albo telefonie
- zmiana logiki danych, walidacji albo storage:
  - warto uruchomić przynajmniej odpowiednie testy obszaru, `lint` albo `typecheck`
- większy update:
  - przed commitem zrób obowiązkową weryfikację

Jeżeli testy istnieją:

- uruchamiaj najpierw testy tylko dla obszaru, którego dotyczy zmiana
- pełniejszy zestaw uruchamiaj przed zakończeniem większego etapu albo przed bardziej ryzykownym commitem

Jeżeli testów jeszcze nie ma:

- rób ręczne sprawdzenie na emulatorze albo telefonie
- przy zmianach strukturalnych uruchom przynajmniej `lint` i `typecheck`, jeśli są dostępne

## Testy a zużycie tokenów

Same testy uruchamiane lokalnie nie zużywają tokenów modelu.

Tokeny rosną głównie wtedy, gdy:

- model generuje testy,
- model analizuje długi output testów,
- model czyta duże logi błędów.

Żeby ograniczać koszty:

- nie każ Codexowi analizować całego outputu testów, jeśli wszystko przeszło
- pokazuj mu tylko fragment błędu, jeśli coś padło
- nie wklejaj całych logów testów, jeśli wystarczy krótki fragment błędu
- nie generuj testów dla całego modułu, jeśli wystarczy jeden mały plik albo jedna funkcja

## Kiedy nowa sesja Codexa

Ten sam czat:

- gdy kończysz ten sam temat,
- gdy doprecyzowujesz ten sam obszar,
- gdy poprawiasz efekt tej samej zmiany.

Nowa sesja:

- gdy zmienia się temat,
- gdy przechodzisz z kodu do audytu albo odwrotnie,
- gdy zmienia się główny kontekst zadania,
- gdy potrzebujesz innego zakresu plików startowych.

## Minimalna checklista końca sesji

Na końcu sesji sprawdź:

- czy kod jest w odpowiednim repo,
- czy wiki odzwierciedla realny stan,
- czy następny krok jest zapisany,
- czy commit jest potrzebny teraz czy później,
- czy oba repo mają poprawny stan Git.

## Anti-patterny

Nie rób tak:

- nie trzymaj ważnego stanu projektu tylko w czacie,
- nie zmieniaj kodu aplikacji w vaultcie,
- nie aktualizuj wiki na podstawie przypuszczeń zamiast realnego stanu repo,
- nie mieszaj wielu tematów w jednym commicie,
- nie zakładaj, że jeśli kod jest gotowy, to wiki też jest aktualna.

## Najkrótsza wersja zasad

Jeżeli chcesz skrót:

- wiki = prawda o projekcie,
- app = prawda o kodzie,
- Codex = wykonanie jednego zadania,
- po zmianie sprawdź, czy trzeba zaktualizować oba światy,
- commit dopiero po domknięciu logicznego kawałka pracy.
