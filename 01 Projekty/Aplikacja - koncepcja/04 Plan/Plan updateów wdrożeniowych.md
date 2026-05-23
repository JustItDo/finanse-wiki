# Plan updateów wdrożeniowych

## Cel
Rozbić MVP na małe update'y, które można wdrażać krok po kroku bez chaosu.

Założenie:
- każdy update ma dawać konkretny efekt,
- każdy update ma być możliwy do sprawdzenia,
- nie wdrażamy wszystkiego naraz.

## Szybki dostęp
Osobne pliki dla każdego update'u są w folderze [Updatey wdrożeniowe](./Updatey%20wdrożeniowe/README.md).

## Co jest już ustalone
- produkt jest `single-user` na start
- MVP jest `offline-first`
- stack to `Expo + React Native + TypeScript`
- lokalna baza danych to `SQLite`
- OCR ma działać `na urządzeniu`
- web / komputer ma działać z tego samego projektu, ale priorytet wdrożenia to mobile

## Czego brakuje przed wejściem w kod
Te punkty nie blokują rozpoczęcia projektu, ale powinny być domknięte najpóźniej w `Update 0.2`:

- dokładna lista kategorii startowych
- finalny kształt szybkiego formularza ręcznego dodawania wydatku
- format budżetu miesięcznego i relacja `budżet miesiąca` vs `budżety kategorii`
- sposób przechowywania załączników lokalnie
- wybór biblioteki lub podejścia do OCR on-device

## Zasady wdrożeniowe
- zaczynamy od ścieżki ręcznej, bo to ona musi działać najlepiej
- OCR nie może blokować wejścia w MVP, jeśli okaże się zbyt niestabilny
- każda większa funkcja musi kończyć się stanem używalnym, a nie tylko technicznym
- każda warstwa danych powinna być przygotowana tak, żeby później nie utrudnić synchronizacji
- każdy update powinien mieć kryterium `gotowe do codziennego użycia`, a nie tylko `da się kliknąć`

## Przekrojowe decyzje implementacyjne

### Warstwa danych
- potrzebny jest jeden spójny model `transaction`, który obsłuży zarówno wydatek, jak i przychód
- `attachments` powinny być powiązane z transakcją, ale nie mogą być wymagane
- budżety powinny mieć osobną logikę wyliczania, nie zapisujemy tylko surowych sum na ekranie
- trzeba od początku przewidzieć pola techniczne pod późniejsze migracje, np. `id`, `created_at`, `updated_at`, `deleted_at`, `source`

### Architektura aplikacji
- na start warto rozdzielić: `storage`, `domain`, `ui`, `features`
- nawigacja powinna być gotowa pod minimum: dashboard, dodawanie transakcji, historia, budżety, ustawienia
- formularze finansowe i OCR powinny korzystać z tych samych mechanizmów walidacji

### Jakość i bezpieczeństwo
- od początku warto mieć lint, formatowanie i podstawowe testy logiki domenowej
- bezpieczeństwo lokalne trzeba zaprojektować jako osobny etap, ale z uwzględnieniem przechowywania załączników już wcześniej
- trzeba z góry ustalić, które dane są obowiązkowe, a które opcjonalne po OCR

## Definicja gotowości MVP
MVP jest gotowe dopiero wtedy, gdy spełnione są wszystkie warunki:

- ręczne dodawanie wydatku trwa krótko i nie wymaga zbędnych kroków
- dodawanie przychodu i wydatku aktualizuje stan miesiąca i budżety kategorii
- dashboard pokazuje najważniejsze liczby bez przeciążenia
- historia transakcji pozwala zweryfikować zapisane dane
- OCR działa jako wsparcie, ale ręczna korekta jest zawsze szybka
- aplikacja działa wygodnie na telefonie i wystarczająco dobrze na komputerze
- dane lokalne są sensownie chronione

## Kolejność wdrażania
Najbezpieczniejsza kolejność wejścia w projekt:

1. fundament techniczny
2. model danych i logika budżetów
3. ręczne flow dodawania transakcji
4. dashboard i historia
5. OCR jako warstwa przyspieszająca
6. analizy, oszczędności i zabezpieczenia
7. polishing i test realnego użycia

## Update 0.1 - Start projektu

### Cel
Postawić techniczny fundament pod aplikację.

### Zakres
- utworzenie projektu `Expo + React Native + TypeScript`
- przygotowanie podstawowej struktury folderów
- przygotowanie nawigacji
- przygotowanie podstaw wspólnego UI
- konfiguracja `eslint`, `prettier`, aliasów importów i typów wspólnych
- przygotowanie prostego systemu motywu, spacingu i typografii
- przygotowanie środowisk: `dev`, `preview`, lokalny build

### Szczegóły wykonawcze
- ustalić strukturę katalogów np. `app`, `src/features`, `src/shared`, `src/storage`, `src/domain`
- przygotować routing pod podstawowe ekrany nawet jako placeholdery
- od razu przewidzieć web support i sprawdzić, czy aplikacja uruchamia się na mobile i webie
- dodać prosty komponent layoutu, inputów, przycisków i kart, żeby nie budować ekranów od zera za każdym razem

### Kryteria zakończenia
- projekt uruchamia się na telefonie i w przeglądarce
- istnieje spójna struktura katalogów pod dalszą implementację
- działa podstawowa nawigacja między pustymi ekranami
- repo ma bazowe standardy jakości i formatowania

### Efekt
- aplikacja uruchamia się lokalnie
- mamy czysty szkielet pod dalszą pracę

## Update 0.2 - Lokalna baza i modele

### Cel
Przygotować warstwę danych.

### Zakres
- konfiguracja `SQLite`
- implementacja głównych encji:
  - transactions
  - attachments
  - categories
  - category_budgets
  - monthly_budgets
- podstawowy seed danych startowych
- przygotowanie migracji i wersjonowania schematu
- przygotowanie repozytoriów / serwisów do odczytu i zapisu danych

### Szczegóły wykonawcze
- zdefiniować jeden model `transaction` z typem `expense` albo `income`
- określić minimalne pola dla transakcji: kwota, waluta, data, typ, kategoria, opis, metoda płatności, źródło wpisu
- przewidzieć pola techniczne dla OCR: status odczytu, confidence, surowy tekst, źródło załącznika
- zdecydować, czy załączniki są przechowywane jako ścieżki do plików lokalnych czy binarnie
- przygotować warstwę selektorów / zapytań pod dashboard i historię, żeby później nie rozbijać logiki po ekranach

### Kryteria zakończenia
- dane zapisują się i odczytują po restarcie aplikacji
- istnieje seed przykładowych kategorii i jednego miesiąca budżetowego
- baza wspiera zarówno flow ręczne, jak i przyszły OCR
- model danych nie wymaga przebudowy przed rozpoczęciem ekranów produktu

### Efekt
- aplikacja potrafi zapisywać i odczytywać podstawowe dane lokalnie

## Update 0.3 - Kategorie i budżet startowy

### Cel
Przygotować podstawowy system finansowy aplikacji.

### Zakres
- lista kategorii startowych
- możliwość aktywacji i edycji kategorii
- konfiguracja budżetu miesiąca
- konfiguracja budżetów kategorii
- logika wyliczania pozostałego budżetu
- stan pusty dla pierwszej konfiguracji

### Szczegóły wykonawcze
- przygotować rozsądną listę kategorii startowych, ale bez nadmiernego rozdrobnienia
- ustalić, czy budżet miesiąca jest obowiązkowy, czy opcjonalny
- jasno określić relację między limitem miesięcznym całości a limitami kategorii
- zdefiniować zachowanie dla kategorii bez ustawionego limitu

### Kryteria zakończenia
- użytkownik może skonfigurować pierwszy miesiąc budżetowy bez pomocy deweloperskiej
- budżety kategorii przeliczają się spójnie po zapisaniu zmian
- model kategorii jest gotowy pod analizy i historię

### Efekt
- użytkownik ma gotowy szkielet budżetowy do używania aplikacji

## Update 1.0 - Ręczne dodawanie wydatku

### Cel
Zrobić pierwszy naprawdę używalny flow.

### Zakres
- ekran dodawania wydatku
- zapis kwoty, kategorii, daty, opisu i metody płatności
- aktualizacja budżetu po zapisie
- walidacja formularza
- szybkie domyślne wartości, np. dzisiejsza data i ostatnia metoda płatności

### Szczegóły wykonawcze
- formularz powinien być możliwy do obsłużenia jedną ręką na telefonie
- liczba pól widocznych od razu powinna być minimalna, reszta może być opcjonalna
- po zapisie użytkownik musi od razu widzieć wpływ wydatku na budżet kategorii i miesiąca
- trzeba przewidzieć stan edycji istniejącej transakcji, nawet jeśli pełna edycja przyjdzie chwilę później

### Kryteria zakończenia
- użytkownik może dodać wydatek w krótkim flow bez gubienia się
- zapis tworzy poprawną transakcję i aktualizuje dashboard / budżety
- formularz działa poprawnie na telefonie i webie
- błędne dane są blokowane czytelną walidacją

### Efekt
- użytkownik może ręcznie dodać wydatek i zobaczyć jego wpływ na budżet

## Update 1.1 - Ręczne dodawanie przychodu

### Cel
Domknąć podstawy finansów.

### Zakres
- ekran lub tryb dodania przychodu
- zapis przychodu do historii
- aktualizacja stanu miesiąca
- spójna obsługa w tym samym modelu danych co wydatek

### Szczegóły wykonawcze
- najlepiej użyć jednego formularza z przełączeniem typu transakcji
- dla przychodu można uprościć część pól względem wydatku
- logika bilansu miesiąca powinna działać na wspólnych agregacjach, nie na osobnych obejściach

### Kryteria zakończenia
- przychód pojawia się w historii i wpływa na miesięczny bilans
- nie ma duplikacji logiki względem dodawania wydatku

### Efekt
- aplikacja obsługuje pełny podstawowy bilans: przychody i wydatki

## Update 1.2 - Dashboard MVP

### Cel
Pokazać użytkownikowi szybki obraz miesiąca.

### Zakres
- przychody
- wydatki
- bilans
- ile zostało z budżetu
- najważniejsze kategorie budżetowe
- szybki przycisk dodania wydatku
- stany puste i stany z przekroczonym budżetem
- podstawowy przełącznik miesiąca

### Szczegóły wykonawcze
- dashboard ma odpowiadać na trzy pytania: ile wydałem, ile zostało, gdzie przekraczam plan
- nie należy dodawać zbyt wielu wykresów na tym etapie
- sekcje powinny być ułożone pod codzienne wejście, a nie pod pełny raport finansowy

### Kryteria zakończenia
- użytkownik po wejściu do aplikacji rozumie sytuację miesiąca bez przechodzenia do innych ekranów
- dashboard ładuje się szybko i nie wymaga ciężkich zapytań
- ekran zachowuje czytelność na telefonie

### Efekt
- użytkownik po otwarciu aplikacji widzi najważniejsze dane

## Update 1.3 - Historia transakcji

### Cel
Dać kontrolę nad zapisanymi danymi.

### Zakres
- lista transakcji
- filtrowanie
- wyszukiwanie
- szczegóły transakcji
- podstawowa edycja lub usunięcie transakcji

### Szczegóły wykonawcze
- filtrowanie powinno obejmować minimum: typ, miesiąc, kategorię
- trzeba przewidzieć, jak usunięcie lub edycja wpływa na budżety i agregacje
- warto od razu zaprojektować sensowny stan pusty i komunikaty dla braku wyników

### Kryteria zakończenia
- użytkownik może odnaleźć transakcję i sprawdzić jej szczegóły
- edycja lub usunięcie nie psuje budżetów ani dashboardu
- lista działa sprawnie przy rosnącej liczbie wpisów

### Efekt
- użytkownik może przeglądać i kontrolować historię finansów

## Update 2.0 - OCR i dodawanie zdjęcia

### Cel
Uruchomić pierwszy automatyczny flow z paragonami i screenami.

### Zakres
- dodanie zdjęcia paragonu
- dodanie screena płatności
- odczyt OCR na urządzeniu
- podstawowe mapowanie danych do formularza
- lokalne przechowywanie załącznika
- fallback do ręcznego dodania, jeśli OCR nic nie odczyta

### Szczegóły wykonawcze
- przed wdrożeniem trzeba wybrać realnie działające rozwiązanie OCR dla `Expo`
- trzeba rozdzielić przypadki: paragon papierowy i screenshot płatności
- OCR powinien wypełniać formularz, ale nie zapisywać transakcji automatycznie bez potwierdzenia

### Kryteria zakończenia
- użytkownik może dodać obraz z aparatu lub galerii
- wynik OCR potrafi zasilić formularz transakcji
- brak odczytu nie kończy flow błędem bez wyjścia

### Efekt
- aplikacja potrafi wczytać dane z obrazu

## Update 2.1 - Korekta OCR

### Cel
Zrobić OCR używalnym, a nie tylko technicznie działającym.

### Zakres
- ekran korekty OCR
- poprawa kwoty, daty, sklepu i kategorii
- status `do poprawy`
- czytelne oznaczenie pól niepewnych

### Szczegóły wykonawcze
- pola o niskiej pewności odczytu powinny być wyróżnione
- ekran korekty musi być szybszy niż ręczne wpisywanie od zera, inaczej OCR nie daje wartości
- trzeba jasno określić, czy sklep jest polem osobnym, czy częścią opisu / metadanych

### Kryteria zakończenia
- użytkownik rozumie, co OCR odczytał poprawnie, a co wymaga poprawy
- korekta kończy się poprawnym zapisem do tej samej warstwy danych co wpis ręczny

### Efekt
- użytkownik może szybko poprawić błędnie odczytane dane

## Update 2.2 - Dashboard po OCR

### Cel
Domknąć połączenie OCR z codziennym użyciem.

### Zakres
- zapis OCR do historii
- automatyczna aktualizacja budżetu
- pokazanie wpływu wydatku na miesiąc
- spójne oznaczenie źródła wpisu w historii

### Kryteria zakończenia
- transakcje z OCR zachowują się tak samo jak wpisy ręczne
- użytkownik widzi pełny efekt zapisu bez niespójności między ekranami

### Efekt
- flow `zdjęcie -> korekta -> zapis -> aktualizacja budżetu` działa end-to-end

## Update 3.0 - Budżety

### Cel
Rozwinąć kontrolę budżetu.

### Zakres
- ekran budżetów
- lista kategorii z limitem, wydanym i pozostałym budżetem
- procent wykorzystania
- sygnał przekroczenia lub ryzyka przekroczenia

### Szczegóły wykonawcze
- budżety muszą być czytelne nawet przy większej liczbie kategorii
- trzeba zdecydować, czy pokazujemy wszystkie kategorie, czy głównie aktywne
- warto dodać prostą logikę sortowania po wykorzystaniu lub przekroczeniu

### Kryteria zakończenia
- użytkownik łatwo identyfikuje kategorie problemowe
- ekran budżetów jest spójny z dashboardem i historią

### Efekt
- użytkownik widzi dokładnie, jak wyglądają jego budżety

## Update 3.1 - Analizy

### Cel
Dodać pierwszy sensowny poziom analityki.

### Zakres
- wykres wydatków według kategorii
- wykres wydatków w czasie
- największe kategorie kosztów
- przełącznik zakresu czasu minimum dla bieżącego i poprzedniego miesiąca

### Szczegóły wykonawcze
- analizy powinny korzystać z już gotowych agregacji, nie liczyć wszystkiego w komponentach
- na MVP wystarczą 2-3 mocne widoki analityczne
- trzeba pilnować, żeby wykresy nie przykryły podstawowej czytelności liczb

### Kryteria zakończenia
- użytkownik może wskazać główne źródła wydatków i trend w czasie
- analizy działają na realnych danych bez odczuwalnych spowolnień

### Efekt
- użytkownik widzi, na co idą pieniądze

## Update 3.2 - Oszczędności

### Cel
Domknąć finansowy sens aplikacji.

### Zakres
- liczenie oszczędności jako `przychody - wydatki`
- miesięczny cel oszczędności
- postęp celu na dashboardzie
- sygnał, czy użytkownik jest powyżej czy poniżej planu

### Szczegóły wykonawcze
- trzeba jasno określić, czy cel oszczędności jest kwotowy, procentowy, czy oba warianty
- logika celu nie może dublować logiki budżetu całego miesiąca

### Kryteria zakończenia
- cel oszczędności jest zrozumiały i aktualizuje się automatycznie
- użytkownik widzi, czy dany miesiąc idzie zgodnie z planem

### Efekt
- aplikacja pokazuje nie tylko wydatki, ale też postęp finansowy

## Update 4.0 - Bezpieczeństwo

### Cel
Podnieść poziom zaufania do aplikacji.

### Zakres
- PIN albo biometria
- podstawowa ochrona lokalnych danych
- blokada dostępu do aplikacji po wznowieniu

### Szczegóły wykonawcze
- trzeba zdecydować, które dane wymagają dodatkowej ochrony poza samą blokadą wejścia
- zabezpieczenie załączników powinno być spójne z zabezpieczeniem bazy
- jeśli pełne szyfrowanie okaże się zbyt ciężkie na MVP, trzeba przynajmniej jasno ograniczyć zakres ochrony i opisać ryzyko

### Kryteria zakończenia
- użytkownik może zabezpieczyć wejście do aplikacji
- lokalne dane nie są pozostawione całkowicie bez ochrony
- zachowanie po wznowieniu aplikacji jest przewidywalne

### Efekt
- aplikacja jest sensownie zabezpieczona na MVP

## Update 4.1 - Poprawki UX i wydajności

### Cel
Wypolerować najważniejsze flow.

### Zakres
- poprawa szybkości ręcznego dodawania
- poprawa jakości korekty OCR
- uproszczenie newralgicznych ekranów
- poprawa wydajności list i zapytań pod dashboard

### Szczegóły wykonawcze
- ten etap powinien opierać się na realnym używaniu aplikacji, nie na domysłach
- warto spisać 5-10 najczęstszych akcji użytkownika i mierzyć, gdzie flow spowalnia
- poprawki powinny być priorytetyzowane według wpływu na codzienne korzystanie

### Kryteria zakończenia
- najważniejsze flow są zauważalnie szybsze i prostsze
- usunięto największe tarcia wykryte podczas używania aplikacji

### Efekt
- aplikacja jest wygodniejsza w codziennym użyciu

## Update 4.2 - Test MVP

### Cel
Sprawdzić, czy MVP faktycznie działa jak trzeba.

### Zakres
- test codziennego użytkowania
- test użycia na telefonie
- test użycia na komputerze
- sprawdzenie, czy dashboard nie jest przeciążony
- sprawdzenie, czy dodawanie wydatków nie jest zbyt wolne
- sprawdzenie odporności na błędne i niepełne dane OCR

### Sposób oceny
- przejść minimum tydzień realnego używania aplikacji jako głównego rejestru
- zanotować, które dane są pomijane, które ekrany są omijane i gdzie pojawia się frustracja
- porównać ręczne dodawanie i OCR pod kątem realnej oszczędności czasu
- ocenić, czy dashboard pomaga podjąć decyzję finansową w mniej niż minutę

### Kryteria zakończenia
- aplikacja nadaje się do codziennego używania bez wspomagania arkuszem lub innym narzędziem
- najważniejsze błędy i tarcia są znane oraz skatalogowane
- istnieje jasna decyzja: `wdrażamy szerzej`, `zostajemy przy własnym użyciu`, albo `wracamy do poprawek`

### Efekt
- mamy gotową pierwszą wersję MVP do realnego użycia

## Najbliższy plan startowy
Jeśli chcesz wejść w implementację od razu, najlepszy pierwszy ciąg prac to:

1. `Update 0.1` z domknięciem struktury projektu i UI fundamentów
2. `Update 0.2` z realnym modelem `transaction` i migracjami
3. `Update 0.3` z kategoriami startowymi i budżetem miesiąca
4. `Update 1.0` jako pierwszy pełny używalny flow produktu

## Decyzje do podjęcia przed pierwszym commitem
- jaka biblioteka OCR jest realnie wspierana w wybranym stacku
- czy web jest rozwijany równolegle od dnia 1, czy tylko utrzymywany jako zgodność techniczna
- jaki jest minimalny zestaw kategorii startowych
- czy miesięczny cel oszczędności wchodzi od razu do modelu danych, czy dopiero w `Update 3.2`
- czy historia transakcji ma wspierać edycję i usuwanie już w pierwszej wersji
