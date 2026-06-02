# Inbox zmian

## Powiązane notatki

- [[Backlog]]
- [[Roadmapa]]
- [[Dziennik wdrożeń]]
- [[Feedback testerski 2026-05-25]]
- [[Plan wdrożeń feedbacku testerskiego]]
- [[Inbox - rozpisane updatey/README|Inbox - rozpisane updatey]]

## Cel

To jest miejsce na zapisywanie pomysłów, uwag i zmian, które mają wejść do aplikacji później.

Ten plik nie jest jeszcze planem wdrożenia.
Najpierw zbieramy tutaj surowe uwagi, potem analizujemy je, grupujemy i dopiero na końcu rozbijamy na konkretne paczki dla Codexa.

## Rozpisane update'y

Wybrane pomysły z tego inboxu zostały rozpisane na osobne briefy wykonawcze:

- [[Inbox - rozpisane updatey/01 Historia - filtry i domyślny zakres|01 Historia - filtry i domyślny zakres]]
- [[Inbox - rozpisane updatey/02 Zwijane sekcje UI|02 Zwijane sekcje UI]]
- [[Inbox - rozpisane updatey/03 Budżety - limit 0 jako bez limitu|03 Budżety - limit 0 jako bez limitu]]
- [[Inbox - rozpisane updatey/04 Ustawienia jako centrum aplikacji|04 Ustawienia jako centrum aplikacji]]
- [[Inbox - rozpisane updatey/05 Backup do plików telefonu|05 Backup do plików telefonu]]
- [[Inbox - rozpisane updatey/06 Analiza - wybór okresu|06 Analiza - wybór okresu]]
- [[Inbox - rozpisane updatey/07 Analiza - bilans okresu|07 Analiza - bilans okresu]]

## Zasady pracy

- każda nowa uwaga ma zostać zapisana, nawet jeśli nie jest jeszcze dopracowana
- nie wdrażamy zmian bez wcześniejszego pogrupowania i priorytetu
- nie mieszamy luźnych pomysłów z aktywnym backlogiem wykonawczym
- po analizie pomysł może trafić do `Backlog`, `Roadmapa` albo osobnego planu wdrożenia
- jeżeli pomysł jest od testera, warto dopisać kontekst urządzenia albo ekranu

## Statusy

Używamy prostych statusów:

- `Nowe` - zapisane, jeszcze bez analizy
- `Do omówienia` - wymaga decyzji produktowej albo technicznej
- `Do rozbicia` - wiemy, że chcemy to zrobić, ale trzeba podzielić na paczki
- `Gotowe do planu` - można z tego zrobić prompt albo plan wdrożenia
- `Przeniesione` - trafiło już do backlogu, roadmapy albo planu

## Szablon wpisu

```text
### YYYY-MM-DD - krótki tytuł

Status: Nowe
Źródło: własny pomysł / tester / review / błąd z telefonu
Obszar: dashboard / historia / budżet / ustawienia / OCR / nawigacja / inne

Opis:
- ...

Dlaczego to ważne:
- ...

Notatki do późniejszej analizy:
- ...
```

## Nowe

### 2026-06-02 - Stan pieniędzy za cały okres

Status: Przeniesione do [[Inbox - rozpisane updatey/07 Analiza - bilans okresu|07 Analiza - bilans okresu]]
Źródło: własny pomysł
Obszar: analiza / dashboard / historia / podsumowania

Opis:
- aplikacja powinna mieć opcję pokazania stanu pieniędzy za cały okres
- chodzi o pole / kartę, która liczy:
  - cały przychód
  - minus całe wydatki
  - wynik jako saldo całego okresu
- dokładna forma wymaga jeszcze przemyślenia

Dlaczego to ważne:
- użytkownik może szybko zobaczyć, czy globalnie jest na plusie czy minusie
- to daje szerszy obraz niż tylko aktualny miesiąc
- pasuje do późniejszego wyboru okresu w analizie

Notatki do późniejszej analizy:
- ustalić, czy to ma być osobna karta w analizie, dashboardzie czy historii
- ustalić, czy pole ma działać tylko dla `cały okres`, czy dla dowolnie wybranego zakresu
- rozważyć copy: `Saldo całego okresu`, `Bilans`, `Stan pieniędzy`, `Wynik finansowy`
- doprecyzować, czy wynik ma uwzględniać tylko ręczne transakcje, czy też przyszłe korekty/importy
- sprawdzić, czy użytkownik nie pomyli tego z aktualnym stanem konta bankowego

### 2026-06-02 - Historia: zwijane filtry i domyślnie wszystkie miesiące

Status: Przeniesione do [[Inbox - rozpisane updatey/01 Historia - filtry i domyślny zakres|01 Historia - filtry i domyślny zakres]]
Źródło: własny pomysł
Obszar: historia / filtry / UX / sortowanie

Opis:
- w historii filtry powinny być zdecydowanie zwijane
- na stałe widoczne mogą zostać tylko:
  - `Szukaj`
  - `Typ`
- reszta filtrów ma być schowana pod przyciskiem rozwijania filtrów
- domyślnie historia powinna pokazywać `wszystkie miesiące`
- historia powinna być sortowana tak, żeby najnowsze transakcje były u góry

Dlaczego to ważne:
- ekran historii ma być bardziej czytelny i mniej przeładowany
- większość czasu użytkownik chce szybko znaleźć albo przejrzeć transakcje, a nie od razu konfigurować wszystkie filtry
- `wszystkie miesiące` jako domyślny zakres zmniejsza ryzyko, że użytkownik nie widzi starszych wpisów i myśli, że zniknęły

Notatki do późniejszej analizy:
- sprawdzić, które filtry poza miesiącem powinny trafić pod zwijany panel
- rozważyć tekst przycisku: `Filtry`, `Więcej filtrów` albo ikona z liczbą aktywnych filtrów
- jeżeli użytkownik wybierze inny miesiąc, trzeba ustalić czy aplikacja ma to zapamiętać
- sortowanie `najnowsze na górze` powinno być standardem i nie wymagać ręcznej zmiany

### 2026-06-02 - Zwijane i rozwijane bloczki menu

Status: Przeniesione do [[Inbox - rozpisane updatey/02 Zwijane sekcje UI|02 Zwijane sekcje UI]]
Źródło: własny pomysł
Obszar: UX / nawigacja / porządek ekranu / małe ekrany

Opis:
- bloczki / sekcje, z których składają się ekrany menu, powinny dać się zwijać i rozwijać
- celem jest oszczędzenie miejsca na ekranie i większy porządek wizualny
- użytkownik mógłby rozwinąć tylko ten fragment, który aktualnie go interesuje
- pomysł dotyczy przede wszystkim ekranów z większą liczbą sekcji, np. ustawienia, budżet, analiza albo dashboard

Dlaczego to ważne:
- na telefonie szybko robi się za dużo treści naraz
- zwijane sekcje pozwalają utrzymać ekran czystszy bez usuwania funkcji
- użytkownik może skupić się na jednym obszarze zamiast scrollować przez wszystko

Notatki do późniejszej analizy:
- ustalić, które sekcje mogą być zwijane, a które powinny zawsze zostać widoczne
- nie chować najważniejszych akcji wejściowych, np. szybkiego dodania transakcji
- rozważyć zapamiętywanie stanu rozwinięcia per ekran
- zadbać o czytelny affordance: strzałka, chevron albo nagłówek sekcji jako przycisk
- sprawdzić, czy ten wzorzec ma być wspólnym komponentem UI

### 2026-06-02 - Limit kategorii jako `0 zł = unlimited`

Status: Przeniesione do [[Inbox - rozpisane updatey/03 Budżety - limit 0 jako bez limitu|03 Budżety - limit 0 jako bez limitu]]
Źródło: własny pomysł
Obszar: budżet / kategorie / limity / UX

Opis:
- bazowo wszystkie kategorie mają działać bez limitu
- usuwamy osobny przycisk / przełącznik, który blokuje albo odblokowuje limit
- limit kategorii ma być interpretowany prosto:
  - `0 zł` jako limit oznacza `unlimited` / brak limitu
  - wartość większa niż `0 zł` oznacza aktywny limit
- użytkownik nie powinien musieć osobno włączać limitu dla kategorii, jeśli samo wpisanie kwoty już wystarcza

Dlaczego to ważne:
- mniej przełączników i mniej stanów do zrozumienia
- prostszy model dla użytkownika: brak kwoty = brak limitu
- łatwiejsza lista kategorii, bo nie trzeba osobno tłumaczyć stanu `aktywny bez limitu`
- lepiej pasuje do feedbacku, że nazwa `Aktywne bez limitu` była myląca

Notatki do późniejszej analizy:
- ustalić, czy w UI pokazywać `Bez limitu`, `Unlimited` czy polskie copy
- sprawdzić, czy obecny model danych pozwala na limit `0` bez specjalnego booleana
- jeżeli istnieje osobny stan `limit włączony`, trzeba zdecydować, czy go usuwamy z modelu, czy tylko przestajemy pokazywać w UI
- dopilnować, żeby walidacja nie traktowała `0 zł` jako błędu
- w analizach budżetowych kategoria z limitem `0 zł` nie powinna generować alertów przekroczenia

### 2026-06-02 - Wybór okresu w analizie

Status: Przeniesione do [[Inbox - rozpisane updatey/06 Analiza - wybór okresu|06 Analiza - wybór okresu]]
Źródło: własny pomysł
Obszar: analiza / dashboard / filtrowanie okresu / UX

Opis:
- w analizie powinna być możliwość wybrania okresu danych
- wybór ma działać w podobnej formie jak wybór emoji / wysuwany selektor
- użytkownik powinien móc wybrać m.in.:
  - cały okres
  - pół roku
  - inne zakresy do doprecyzowania
- ten pomysł wymaga jeszcze rozbicia na dokładne planowanie

Dlaczego to ważne:
- analiza bez wyboru zakresu może szybko stać się za mało użyteczna
- użytkownik powinien móc patrzeć zarówno na bieżący okres, jak i dłuższą historię
- `cały okres` i `pół roku` pomagają zobaczyć większy obraz finansów bez ręcznego przełączania miesięcy

Notatki do późniejszej analizy:
- doprecyzować listę predefiniowanych zakresów
- zdecydować, czy zakres ma dotyczyć tylko ekranu analizy, czy też dashboardu
- zaprojektować kompaktowy wysuwany selektor okresu
- sprawdzić, czy obecny model danych i zapytania agregujące są gotowe na zakresy wielomiesięczne
- możliwe zakresy do omówienia: `ten miesiąc`, `3 miesiące`, `6 miesięcy`, `rok`, `cały okres`, `własny zakres`

### 2026-06-02 - Backup i synchronizacja do plików telefonu

Status: Przeniesione do [[Inbox - rozpisane updatey/05 Backup do plików telefonu|05 Backup do plików telefonu]]
Źródło: własny pomysł
Obszar: ustawienia / synchronizacja / backup / dane

Opis:
- synchronizacja albo backup danych powinny dawać możliwość zapisania pliku bezpośrednio do plików telefonu
- nie może być tylko opcji wysłania backupu mailem albo przez inną aplikację
- użytkownik powinien móc świadomie zapisać eksport w lokalnym miejscu, np. w `Pobrane`, `Dokumenty` albo wybranym folderze telefonu
- udostępnianie przez inne aplikacje nadal może zostać jako dodatkowa opcja, ale nie jako jedyna ścieżka

Dlaczego to ważne:
- użytkownik ma większą kontrolę nad swoimi danymi
- backup finansów nie powinien wymuszać użycia maila, komunikatora albo zewnętrznej aplikacji
- lokalny plik jest prostszy do późniejszego importu, przenoszenia i archiwizacji

Notatki do późniejszej analizy:
- sprawdzić możliwości Expo / Android dla zapisu pliku w lokalizacji wybranej przez użytkownika
- rozważyć osobne akcje: `Zapisz do plików` i `Udostępnij`
- najlepiej umieścić to w przyszłym ekranie `Ustawienia -> Dane` albo `Ustawienia -> Backup i synchronizacja`
- import z lokalnego pliku powinien być później spójny z eksportem

### 2026-06-02 - Zmiana ostatniej zakładki na `Ustawienia`

Status: Przeniesione do [[Inbox - rozpisane updatey/04 Ustawienia jako centrum aplikacji|04 Ustawienia jako centrum aplikacji]]
Źródło: własny pomysł
Obszar: nawigacja / ustawienia / bezpieczeństwo / synchronizacja

Opis:
- ostatnia zakładka aplikacji ma zostać zmieniona z `Zabezpieczenia` / `Bezpieczeństwo` na `Ustawienia`
- obecne funkcje związane z PIN-em, biometrią i sesją mają zostać przeniesione do sekcji `Bezpieczeństwo` wewnątrz ustawień
- w ustawieniach powinny znaleźć się wszystkie ważne rzeczy do konfiguracji aplikacji
- przykładowe sekcje:
  - PIN / hasło / biometria
  - synchronizacja
  - backup
  - dane i prywatność
  - informacje o aplikacji

Dlaczego to ważne:
- `Bezpieczeństwo` jako główna zakładka jest za wąskie
- aplikacja będzie potrzebowała jednego centralnego miejsca na konfigurację
- przyszła synchronizacja i backup nie powinny być upychane w przypadkowych ekranach

Notatki do późniejszej analizy:
- dolny tab powinien prawdopodobnie nazywać się `Ustawienia`
- `Bezpieczeństwo` zostaje jako sekcja albo kafel wewnątrz tego ekranu
- onboarding PIN-u powinien prowadzić do `Ustawienia -> Bezpieczeństwo`, a nie do osobnej zakładki `Bezpieczeństwo`
- nie trzeba wdrażać synchronizacji od razu; wystarczy przygotować logiczne miejsce w UI
