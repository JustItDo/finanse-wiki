# Start Sesji Codex

## Powiązane notatki

- [[Mapa projektu]]
- [[README]]
- [[00 Założenia startowe]]
- [[01 Wizja/Start - brief projektu|Brief projektu]]
- [[02 Produkt/MVP]]
- [[03 Technologia/Decyzje techniczne]]
- [[03 Technologia/Workflow developera|Workflow developera]]
- [[03 Technologia/Workflow modeli AI|Workflow modeli AI]]
- [[04 Plan/Roadmapa]]

## Co jest gotowe

- projekt `Finansowy Copilot` ma uporządkowaną dokumentację w vaultcie
- repo `finanse-wiki` działa na gałęzi `main`
- repo `finanse-app` działa na gałęzi `master`
- ostatnie commity w `finanse-wiki`:
  - `abc83c8` `Update implementation notes and Codex session workflow`
  - `366be00` `Build finanse-wiki project structure and navigation`
  - `3b089ff` `Initialize project context, planning notes, and Codex skills`
- ostatni commit w `finanse-app`:
  - `2dfc98c` `Complete 02.2 OCR dashboard integration`
- w historii repo aplikacji są już zapisane:
  - `00.1 Start projektu`
  - `00.2 Lokalna baza i modele`
  - `00.3 Kategorie i budżet startowy`
  - `01.0 Ręczne dodawanie wydatku`
  - `01.1 Ręczne dodawanie przychodu`
  - `01.2 Dashboard MVP`
  - `01.3 Historia transakcji`
- lokalnie wykonane zostały też:
  - `02.0 OCR i dodawanie zdjęcia`
  - `02.1 Korekta OCR`
  - `02.2 Dashboard po OCR`
  - `03.0 Budżety`
  - `03.1 Analizy`
  - `03.2 Oszczędności`
- flow OCR jest już domknięte jako działający slice MVP
- ekran budżetów jest już przebudowany do codziennej kontroli limitów i ryzyka
- analizy mają już pierwszy poziom wykresów i agregacji dla bieżącego oraz poprzedniego miesiąca
- dashboard pokazuje już także prosty postęp miesięcznego celu oszczędności
- na emulatorze praktycznym fallbackiem testowym jest `Wybierz paragon z galerii`
- `.obsidian/` i `99 Robocze/` są wykluczone z Git przez `.gitignore`

## Gdzie jest kontekst projektu

Najważniejsze pliki do czytania tylko wtedy, gdy są potrzebne do zadania:

- `README.md`
- `00 Założenia startowe.md`
- `01 Wizja/Start - brief projektu.md`
- `02 Produkt/MVP.md`
- `03 Technologia/Decyzje techniczne.md`
- `03 Technologia/Workflow developera.md`
- `03 Technologia/Workflow modeli AI.md`
- `03 Technologia/Stan repo aplikacji.md`
- `04 Plan/Roadmapa.md`
- `04 Plan/Updatey wdrożeniowe/README.md`
- `04 Plan/Dziennik wdrożeń.md`
- `05 Codex Skills/`

## Gdzie są repozytoria

- wiki projektu:
  - `../Obsidian Vault`
- aplikacja:
  - `../finanse-app` albo katalog otwarty jako workspace implementacyjny

Najważniejsza zasada:

- trwały kontekst projektu zapisuj w wiki
- zmiany kodowe wykonuj w repo aplikacji
- jeżeli sesja zmienia decyzje, status wdrożenia albo workflow, wróć na koniec do wiki i dopisz stan

## Jakie skille są przygotowane

W projekcie i w aktywnym katalogu `~/.codex/skills` są dostępne:

- `feature-implementation`
- `code-review`
- `behavior-preserving-refactor`
- `service-diagnosis`
- `skill-router`

Dodatkowe lokalne narzędzie workflow:

- MCP tool `lmstudio_unit_tests` do szkicowania wąskich testów jednostkowych lokalnym modelem `LM Studio`

## Jak zaczynać nową sesję

Domyślny prompt startowy projektu jest zapisany w:

- `01 Projekty/Aplikacja - koncepcja/PROMPT STARTOWY CODEX.txt`

Najwygodniejszy start w VS Code dla repo aplikacji:

- uruchom task `Codex: Finanse`
- task odpala lokalny skrypt `scripts/start-codex-finanse.sh`
- ten skrypt uruchamia `codex` z gotowym promptem projektu
- domyślny model dla tego startu to `gpt-5.4` z reasoning `medium`
- skrypt dodaje też kontekst:
  - repo implementacyjne to bieżący workspace aplikacji
  - wiki projektu jest dostępne obok jako dodatkowy katalog
  - kod zmieniamy w `finanse-app`, a wiki tylko wtedy, gdy zadanie tego wymaga

Jeżeli uruchamiasz sesję ręcznie, na początku nowego czatu wklej:

```text
Use $skill-router first. This is Finansowy Copilot. Project context is in:
- README
- 00 Założenia startowe
- 02 Produkt/MVP
- 03 Technologia/Decyzje techniczne
- 04 Plan/Roadmapa
- 05 Codex Skills

Read only what is necessary for the task. Then continue with: [tu wpisz zadanie].
```

## Workflow Obsidian <-> VS Code <-> Codex

Szczegółowy dokument pracy developerskiej jest tutaj:

- `03 Technologia/Workflow developera.md`
- `03 Technologia/Workflow modeli AI.md`

Podział ról:

- Obsidian = decyzje, zakres, backlog, briefy, notatki z sesji
- VS Code = wykonanie, kod, testy, integracje, praca z Codexem
- Codex = realizacja jednego konkretnego zadania w plikach, z minimalnym potrzebnym kontekstem

Zasada:

- nie zaczynaj sesji Codexa od pustego polecenia
- najpierw przygotuj notatkę zadania w Obsidianie
- potem uruchom Codexa w VS Code z odwołaniem do konkretnych plików
- po zakończeniu pracy wróć do Obsidiana i zapisz wynik sesji
- jeżeli sesja dotyczy aplikacji, zaczynaj z repo `finanse-app`, a nie z poziomu samego vaultu

## Jak ma wyglądać obieg pracy

1. W Obsidianie wybierz jeden konkretny temat.
2. Zapisz go w odpowiednim pliku produktu, technologii albo planu.
3. Jeżeli zadanie jest wykonawcze, dopisz krótki brief sesji:
   - cel
   - zakres
   - kryterium ukończenia
   - ograniczenia
   - pliki do przeczytania
4. Otwórz repo lub projekt w VS Code.
5. Uruchom nową sesję Codexa.
6. W pierwszej wiadomości wskaż dokładnie notatki do przeczytania i opisz jedno zadanie.
7. Pozwól Codexowi pracować w plikach, a nie tylko opisywać rozwiązanie.
8. Po zakończeniu sesji wróć do Obsidiana i zapisz:
   - co zostało zrobione
   - jakie decyzje zapadły
   - co jest następnym krokiem

## Minimalny szablon notatki zadania

Do każdej większej sesji przygotuj notatkę albo sekcję z takim układem:

- Cel
- Zakres
- Poza zakresem
- Kryterium ukończenia
- Pliki kontekstowe
- Następny krok

Przykład:

```text
Cel:
- wdrożyć pierwszy flow ręcznego dodawania wydatku

Zakres:
- formularz dodawania
- model danych wydatku
- zapis lokalny

Poza zakresem:
- OCR
- synchronizacja

Kryterium ukończenia:
- użytkownik może dodać wydatek ręcznie
- rekord zapisuje się lokalnie
- podstawowe pola są walidowane

Pliki kontekstowe:
- 02 Produkt/MVP.md
- 02 Produkt/User flow.md
- 03 Technologia/Model danych implementacyjny.md
```

## Szablon startu sesji w VS Code

W nowej sesji Codexa używaj promptu w tym stylu:

```text
Use $skill-router first. This is Finansowy Copilot.

Read only what is necessary from:
- 00 Założenia startowe.md
- 02 Produkt/MVP.md
- 02 Produkt/User flow.md
- 03 Technologia/Decyzje techniczne.md
- 03 Technologia/Model danych implementacyjny.md

Task:
- [tu wpisz jedno konkretne zadanie]

Constraints:
- [tu wpisz ograniczenia]

Definition of done:
- [tu wpisz kryterium ukończenia]

Work concretely in files, not only in explanation.
At the end, report what changed and what the next step should be.
```

## Zasady dobrej sesji

- jedna sesja = jeden główny problem
- jeden prompt = jeden konkretny cel
- nie każ Codexowi zgadywać kontekstu projektu
- podawaj 1 do 5 plików startowych, nie cały vault
- zapisuj trwałe ustalenia w plikach, nie licz na pamięć czatu
- po każdej większej zmianie aktualizuj backlog albo plan

## Domknięcie sesji

Po każdej istotnej sesji zaktualizuj w Obsidianie przynajmniej jedno z poniższych:

- `04 Plan/Backlog.md`
- `04 Plan/Roadmapa.md`
- odpowiedni plik w `02 Produkt/`
- odpowiedni plik w `03 Technologia/`
- odpowiedni plik w `04 Plan/Updatey wdrożeniowe/`

Jeżeli sesja dała nową decyzję architektoniczną albo produktową, zapisz ją od razu w odpowiednim pliku zamiast trzymać ją tylko w historii rozmowy.

## Zasady Git przy pracy z Codexem

Najważniejsza zasada:

- nie rób commita po każdym pojedynczym promptcie
- rób commit wtedy, gdy zamkniesz jeden logiczny kawałek pracy

Dobra reguła:

- `1 commit = 1 logiczna zmiana`
- najpierw domknij logiczny update w kodzie albo wiki, potem commit
- nie mieszaj w jednym commicie zmian wiki i zmian aplikacji, jeśli da się je rozdzielić

Przykłady dobrych commitów:

- uporządkowanie wiki i linków w dokumentacji
- setup projektu i struktury aplikacji
- wdrożenie lokalnej bazy danych
- wdrożenie ręcznego dodawania wydatku

Kiedy robić commit:

- gdy zmiana jest spójna
- gdy da się ją opisać jednym krótkim komunikatem
- gdy pliki są w stanie, który warto zachować w historii

Kiedy nie robić commitów jeszcze:

- gdy jesteś w połowie zadania
- gdy zmiany są robocze i niespójne
- gdy kilka różnych tematów jest wymieszanych w jednym zestawie zmian

## Prosty workflow Git

1. Otwórz jedną sesję Codexa dla jednego głównego zadania.
2. Pozwól mu doprowadzić zmianę do sensownego stanu.
3. Sprawdź wynik.
4. Jeżeli zadanie jest domknięte, zrób commit.
5. Dopiero potem przejdź do kolejnego większego tematu.

## Kiedy nowa sesja, kiedy ten sam czat

Ten sam czat:

- gdy doprecyzowujesz to samo zadanie
- gdy kończysz ten sam obszar zmian

Nowa sesja:

- gdy zaczynasz inny temat
- gdy przechodzisz z dokumentacji do implementacji
- gdy zmienia się cel pracy i potrzebny jest inny kontekst startowy

## Branching na start

Na obecnym etapie możesz spokojnie pracować na `main`, jeśli:

- pracujesz sam
- zakres jest mały
- zmiany są głównie koncepcyjne albo dokumentacyjne

Dla repo aplikacji obecny stan wygląda tak:

- etapy `00.1-01.3` są już zapisane w historii repo `finanse-app`
- lokalnie wykonane zostały też `02.0 OCR i dodawanie zdjęcia` oraz `02.1 Korekta OCR`
- bieżący następny krok wdrożeniowy to `03.0 Budżety`

Warto przejść na osobne branche, gdy:

- zaczynasz większe wdrożenia techniczne
- kilka tematów będzie rozwijanych równolegle
- chcesz oddzielić eksperyment od stabilnej gałęzi głównej

## Ważna uwaga

- historia czatów Codexa nie jest częścią folderu projektu
- skopiowanie projektu nie przenosi `resume`
- trwały kontekst projektu ma być utrzymywany w plikach i w Git, nie w historii czatu
