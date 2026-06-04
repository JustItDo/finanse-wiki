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
- [[Inbox - rozpisane updatey/08 Ustawienia - reset stanu i komunikatów|08 Ustawienia - reset stanu i komunikatów]]
- [[Inbox - rozpisane updatey/09 Historia - inline szczegóły i edycja transakcji|09 Historia - inline szczegóły i edycja transakcji]]
- [[Inbox - rozpisane updatey/10 Rebranding v2 - nowe logo i żywszy UI|10 Rebranding v2 - nowe logo i żywszy UI]]
- [[Inbox - rozpisane updatey/10A Rebranding v2 - kolory i logo|10A Rebranding v2 - kolory i logo]]
- [[Inbox - rozpisane updatey/10B Rebranding v2 - wdrożenie w kodzie|10B Rebranding v2 - wdrożenie w kodzie]]
- [[Inbox - rozpisane updatey/11 Tryb ciemny i system motywów|11 Tryb ciemny i system motywów]]
- [[Inbox - rozpisane updatey/12 Motywy kolorystyczne - wybór palety|12 Motywy kolorystyczne - wybór palety]]
- [[Inbox - rozpisane updatey/13 Start aplikacji - nazwa i splash|13 Start aplikacji - nazwa i splash]]

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

### 2026-06-04 - Start aplikacji pokazuje starą nazwę albo stare logo

Status: Przeniesione do [[Inbox - rozpisane updatey/13 Start aplikacji - nazwa i splash|13 Start aplikacji - nazwa i splash]]
Źródło: test na telefonie / własna obserwacja
Obszar: branding / splash / app config / Android / Expo

Opis:
- przy ładowaniu aplikacji pojawia się stare pierwsze logo
- pojawia się też nazwa `finanse-app`, mimo że produkt powinien być `Zenifi`
- nowe finalne logo zostanie dostarczone później, więc teraz nie projektujemy logo
- od razu trzeba naprawić niespójności nazwy, splash i konfiguracji startowej

Dlaczego to ważne:
- start aplikacji to pierwszy kontakt z produktem
- stara nazwa wygląda jak niedokończony rebranding
- testerzy mogą pomyśleć, że mają zainstalowany zły build
- jeśli problem wynika ze starego APK/cache, trzeba mieć jasną procedurę czystej reinstalacji

Notatki do późniejszej analizy:
- aktualne `app.json` w repo wskazuje `name: Zenifi`, więc jeśli telefon pokazuje `finanse-app`, trzeba sprawdzić build/cache/native metadata
- sprawdzić assety `icon`, `splash`, `adaptiveIcon`
- nie zmieniać `android.package` bez decyzji, bo może to wpłynąć na instalację i dane
- po dostarczeniu finalnego logo zrobić osobny update assetów

### 2026-06-04 - Motywy jako osobna kategoria ustawień

Status: Dopisane do [[Inbox - rozpisane updatey/04 Ustawienia jako centrum aplikacji|04 Ustawienia jako centrum aplikacji]], [[Inbox - rozpisane updatey/11 Tryb ciemny i system motywów|11 Tryb ciemny i system motywów]] i [[Inbox - rozpisane updatey/12 Motywy kolorystyczne - wybór palety|12 Motywy kolorystyczne - wybór palety]]
Źródło: decyzja produktowa
Obszar: ustawienia / motywy / UX / nawigacja

Opis:
- wybór motywu i kolorystyki nie powinien być schowany w sekcji `Aplikacja`
- w ustawieniach ma powstać osobna kategoria `Motywy`
- sekcja `Aplikacja` powinna zostać informacyjna
- `Motywy` mają zawierać tryb jasny/ciemny/systemowy i wybór palety kolorystycznej

Dlaczego to ważne:
- motywy są realną konfiguracją produktu, a nie informacją o aplikacji
- osobny kafel jest bardziej czytelny dla użytkownika
- łatwiej będzie później rozbudować wybór palet bez przeładowania sekcji `Aplikacja`

Notatki do późniejszej analizy:
- jeśli obecny kod ma blok `Motyw` w sekcji `Aplikacja`, trzeba go przenieść do nowej sekcji `Motywy`
- nie duplikować logiki zapisu preferencji
- sekcja `Aplikacja` ma zawierać nazwę, wersję, tryb danych, platformę i opis offline-first

### 2026-06-04 - Wybór kolorystyki aplikacji poza jasnym i ciemnym trybem

Status: Przeniesione do [[Inbox - rozpisane updatey/12 Motywy kolorystyczne - wybór palety|12 Motywy kolorystyczne - wybór palety]]
Źródło: własny pomysł
Obszar: UI / ustawienia / motywy / personalizacja / branding

Opis:
- aplikacja powinna mieć możliwość wyboru gotowej kolorystyki
- nie chodzi tylko o `Jasny` i `Ciemny`
- użytkownik powinien móc wybrać np. jedną z wcześniej przygotowanych palet: `Neon Mint`, `Electric Pine`, `Signal Finance`
- paleta powinna działać razem z trybem jasnym/ciemnym/systemowym, a nie jako osobny chaotyczny mechanizm

Dlaczego to ważne:
- daje użytkownikowi poczucie personalizacji bez budowania pełnego edytora motywu
- pozwala wykorzystać wcześniej przygotowane palety rebrandingu
- zwiększa atrakcyjność aplikacji bez przebudowy całego UI
- wymusza sensowny system theme tokens zamiast hardcodowanych kolorów

Notatki do późniejszej analizy:
- najlepszy model techniczny to `themeMode + paletteId -> theme`
- domyślna paleta powinna zostać `Neon Mint`
- palety powinny być wybierane w `Ustawienia -> Wygląd`
- nie wdrażać custom HEX ani pełnej personalizacji każdego koloru
- powiązane: [[Inbox - rozpisane updatey/11 Tryb ciemny i system motywów]]
- powiązane: [[../02 Produkt/Zenifi - Palety rebrandingu v2.html]]

### 2026-06-03 - Ustawienia: reset widoku i komunikatów po opuszczeniu ekranu

Status: Przeniesione do [[Inbox - rozpisane updatey/08 Ustawienia - reset stanu i komunikatów|08 Ustawienia - reset stanu i komunikatów]]
Źródło: błąd z telefonu / własny test
Obszar: ustawienia / backup / UX / stan ekranu

Opis:
- po eksporcie backupu w ustawieniach pozostaje powiadomienie / komunikat
- komunikat zostaje widoczny nawet po przejściu do innego okna albo po powrocie do wyboru ustawień
- po wyjściu z ustawień i ponownym wejściu aplikacja powinna pokazać główny wybór ustawień, a nie ostatnio otwarty konkretny podwidok
- stan konkretnego podwidoku ustawień nie powinien zachowywać się jak trwała sesja

Dlaczego to ważne:
- komunikaty po akcji powinny być krótkotrwałe i nie zaśmiecać kolejnych wejść
- użytkownik po powrocie do ustawień oczekuje głównego menu ustawień, a nie starego miejsca w środku flow
- stare powiadomienie o backupie może wyglądać jak aktywny stan albo nowy wynik akcji, mimo że dotyczy poprzedniego wejścia

Notatki do późniejszej analizy:
- po opuszczeniu taba `Ustawienia` wyczyścić feedback / error / backup summary, jeśli nie jest potrzebny
- po ponownym wejściu do ustawień pokazywać główny ekran wyboru sekcji
- rozważyć, czy resetować też formularze PIN-u i importu backupu
- jeżeli nie chcemy pełnego resetu wszystkich formularzy, minimum to reset aktywnej sekcji i komunikatów
- powiązane: [[Inbox - rozpisane updatey/04 Ustawienia jako centrum aplikacji]]
- powiązane: [[Inbox - rozpisane updatey/05 Backup do plików telefonu]]

### 2026-06-03 - Historia: rozwijane szczegóły transakcji inline

Status: Przeniesione do [[Inbox - rozpisane updatey/09 Historia - inline szczegóły i edycja transakcji|09 Historia - inline szczegóły i edycja transakcji]]
Źródło: własny pomysł
Obszar: historia / edycja transakcji / UX / małe ekrany

Opis:
- szczegóły transakcji powinny wyświetlać się po kliknięciu w konkretną transakcję
- kliknięty element na liście powinien się rozwinąć
- w rozwiniętym elemencie użytkownik powinien móc zmienić atrybuty transakcji i zapisać zmiany
- obecne rozwiązanie, gdzie szczegóły pojawiają się na dole historii, jest niewygodne przy dużej liczbie transakcji
- jeśli lista ma np. 100 transakcji, użytkownik nie powinien przewijać na dół, żeby edytować element kliknięty wyżej

Dlaczego to ważne:
- edycja transakcji powinna być bezpośrednio powiązana z elementem, którego dotyczy
- inline expansion skraca flow i zmniejsza scrollowanie
- użytkownik łatwiej rozumie, którą transakcję aktualnie edytuje
- historia będzie bardziej używalna przy dużej liczbie wpisów

Notatki do późniejszej analizy:
- rozważyć tryb: kliknięcie rozwija szczegóły, drugi klik albo `Zwiń` zamyka
- na razie może być rozwinięta tylko jedna transakcja naraz
- edycja inline powinna korzystać z tych samych walidacji co obecny panel szczegółów
- trzeba przemyśleć usuwanie transakcji w tym rozwiniętym stanie
- warto połączyć ten pomysł z update'em historii i zwijanych filtrów
- powiązane: [[Inbox - rozpisane updatey/01 Historia - filtry i domyślny zakres]]

### 2026-06-03 - Tryb ciemny z przełącznikiem w ustawieniach

Status: Przeniesione do [[Inbox - rozpisane updatey/11 Tryb ciemny i system motywów|11 Tryb ciemny i system motywów]]
Źródło: własny pomysł
Obszar: UI / ustawienia / motyw / dostępność / kolorystyka

Opis:
- aplikacja powinna dostać tryb ciemny
- użytkownik powinien mieć możliwość zmiany motywu w `Ustawieniach`
- tryb ciemny powinien być spójny z przyszłą żywszą kolorystyką i brandingiem aplikacji
- ustawienie motywu powinno być zapamiętywane

Dlaczego to ważne:
- część użytkowników będzie korzystać z aplikacji wieczorem albo w słabym świetle
- tryb ciemny zwiększa komfort codziennego używania
- ustawienie motywu w aplikacji daje użytkownikowi kontrolę zamiast wymuszania jednego wyglądu
- przy rebrandingu warto od razu myśleć o dwóch wersjach palety: jasnej i ciemnej

Notatki do późniejszej analizy:
- zdecydować, czy dostępne opcje to `Jasny`, `Ciemny`, `Systemowy`, czy tylko `Jasny` / `Ciemny`
- najlepiej rozważyć opcję `Systemowy` jako domyślną, jeśli implementacja nie będzie zbyt kosztowna
- przygotować tokeny kolorów dla obu motywów
- sprawdzić wszystkie ekrany pod kontrast i czytelność danych finansowych
- tryb ciemny powinien być zmianą systemową w theme, a nie lokalnym hardcodem kolorów w ekranach
- powiązane z pomysłem: `Nowe logo i żywsza kolorystyka aplikacji`

### 2026-06-03 - Nowe logo i żywsza kolorystyka aplikacji

Status: Przeniesione do [[Inbox - rozpisane updatey/10 Rebranding v2 - nowe logo i żywszy UI|10 Rebranding v2 - nowe logo i żywszy UI]]
Źródło: własny pomysł
Obszar: branding / logo / UI / kolorystyka / zaangażowanie

Opis:
- aktualne logo jest do wymiany, bo wygląda zbyt słabo i nie buduje mocnej tożsamości aplikacji
- kolorystyka aplikacji powinna być bardziej żywa, energetyczna i przyjemna do codziennego patrzenia
- aplikacja nie powinna wyglądać zbyt spokojnie, płasko ani nudno
- kierunek ma bardziej przyciągać uwagę użytkownika i dawać więcej wizualnej satysfakcji
- logo i UI powinny być spójne, a nie wyglądać jak dwa osobne style

Dlaczego to ważne:
- aplikacja finansowa będzie używana regularnie, więc ekran musi zachęcać do powrotu
- mocniejszy brand może pomóc odróżnić aplikację od generycznych trackerów wydatków
- żywsze akcenty mogą poprawić odbiór dashboardu, postępu, oszczędności i pozytywnych stanów
- obecne logo nie jest jeszcze wystarczająco mocnym znakiem produktu

Notatki do późniejszej analizy:
- przygotować nowe kierunki logo, bardziej czytelne i atrakcyjne jako ikona aplikacji
- rozważyć bardziej nasyconą paletę, ale z zachowaniem czytelności danych finansowych
- nie świecić całym interfejsem naraz; energia powinna być w akcentach, stanach sukcesu, ikonach, wykresach i mikrointerakcjach
- sprawdzić kontrast tekstu i dostępność po zmianie kolorów
- dopracować system kolorów dla:
  - tła
  - kart
  - przychodów
  - wydatków
  - oszczędności
  - alertów
  - CTA
- możliwy osobny update: `Rebranding v2 - logo i żywszy UI`
- powiązane: [[../02 Produkt/Zenifi - rekomendacja marki]]

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
