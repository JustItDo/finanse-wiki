# Start Sesji Codex

## Powiązane notatki

- [[Mapa projektu]]
- [[README]]
- [[00 Założenia startowe]]
- [[01 Wizja/Start - brief projektu|Brief projektu]]
- [[02 Produkt/MVP]]
- [[03 Technologia/Decyzje techniczne]]
- [[04 Plan/Roadmapa]]

## Co jest gotowe

- projekt `Finansowy Copilot` ma uporządkowaną dokumentację w vaultcie
- repo Git zostało zainicjalizowane dla tego vaulta
- pierwszy commit został utworzony:
  - `3b089ff` `Initialize project context, planning notes, and Codex skills`
- `.obsidian/` i `99 Robocze/` są wykluczone z Git przez `.gitignore`

## Gdzie jest kontekst projektu

Najważniejsze pliki do czytania tylko wtedy, gdy są potrzebne do zadania:

- `README.md`
- `00 Założenia startowe.md`
- `01 Wizja/Start - brief projektu.md`
- `02 Produkt/MVP.md`
- `03 Technologia/Decyzje techniczne.md`
- `04 Plan/Roadmapa.md`
- `05 Codex Skills/`

## Jakie skille są przygotowane

W projekcie i w aktywnym katalogu `~/.codex/skills` są dostępne:

- `feature-implementation`
- `code-review`
- `behavior-preserving-refactor`
- `service-diagnosis`
- `skill-router`

## Jak zaczynać nową sesję

Domyślny prompt startowy projektu jest zapisany w:

- `01 Projekty/Aplikacja - koncepcja/PROMPT STARTOWY CODEX.txt`

Najwygodniejszy start w VS Code:

- uruchom task `Codex: Finansowy Copilot`
- task odpala lokalny skrypt `scripts/start-codex-finanse.sh`
- ten skrypt uruchamia `codex` z gotowym promptem projektu

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

## Workflow Obsidian <-> VS Code

Podział ról:

- Obsidian = decyzje, zakres, backlog, briefy, notatki z sesji
- VS Code = wykonanie, kod, testy, integracje, praca z Codexem

Zasada:

- nie zaczynaj sesji Codexa od pustego polecenia
- najpierw przygotuj notatkę zadania w Obsidianie
- potem uruchom Codexa w VS Code z odwołaniem do konkretnych plików
- po zakończeniu pracy wróć do Obsidiana i zapisz wynik sesji

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

Jeżeli sesja dała nową decyzję architektoniczną albo produktową, zapisz ją od razu w odpowiednim pliku zamiast trzymać ją tylko w historii rozmowy.

## Ważna uwaga

- historia czatów Codexa nie jest częścią folderu projektu
- skopiowanie projektu nie przenosi `resume`
- trwały kontekst projektu ma być utrzymywany w plikach i w Git, nie w historii czatu
