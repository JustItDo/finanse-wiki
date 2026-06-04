# Dziennik wdrożeń

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[README|README]]
- [[Updatey wdrożeniowe/README|Updatey wdrożeniowe]]
- [[../START SESJI CODEX|Start sesji Codex]]
- [[../03 Technologia/Stan repo aplikacji|Stan repo aplikacji]]

## Cel notatki

To jest krótki dziennik wykonanych etapów wdrożeniowych.

Nie zastępuje szczegółowych notatek produktowych ani technicznych.
Ma dawać szybki obraz:

- co zostało realnie wykonane
- w jakim repo znajduje się efekt
- co jest następnym krokiem

## 2026-05-24

### `00.1 Start projektu`

- status: `wykonane w workspace finanse-app`
- wynik:
  - postawiony projekt `Expo + React Native + TypeScript`
  - dodana nawigacja
  - dodane bazowe komponenty UI
  - dodane lint, prettier, aliasy i wsparcie web
- następny krok:
  - `00.2 Lokalna baza i modele`

### `00.2 Lokalna baza i modele`

- status: `wykonane w workspace finanse-app`
- wynik:
  - wdrożone `SQLite`
  - dodane migracje
  - dodane repozytoria i bootstrap storage
  - przygotowane pola pod OCR i przyszły import z wiki
- następny krok:
  - `00.3 Kategorie i budżet startowy`

### `00.3 Kategorie i budżet startowy`

- status: `wykonane w workspace finanse-app`
- wynik:
  - wdrożony ekran i logika konfiguracji kategorii
  - wdrożony opcjonalny budżet miesiąca
  - wdrożone budżety kategorii i liczenie pozostałego budżetu
- następny krok:
  - `01.0 Ręczne dodawanie wydatku`

### `01.0 Ręczne dodawanie wydatku`

- status: `wykonane w repo finanse-app`
- commit:
  - `49fac8f` `01.0-01.1 Add shared manual transaction entry flow`
- wynik:
  - wdrożony szybki formularz ręcznego dodawania transakcji
  - zapis wydatku aktualizuje budżet kategorii i stan miesiąca
  - dodana walidacja formularza i stan sukcesu po zapisie
- następny krok:
  - `01.1 Ręczne dodawanie przychodu`

### `01.1 Ręczne dodawanie przychodu`

- status: `wykonane w repo finanse-app`
- commit:
  - `49fac8f` `01.0-01.1 Add shared manual transaction entry flow`
- wynik:
  - dodany tryb przychodu w tym samym flow formularza
  - przychód zapisuje się do wspólnego modelu `transactions`
  - bilans miesiąca liczy się na wspólnych agregacjach dla przychodów i wydatków
- następny krok:
  - `01.2 Dashboard MVP`

### `01.2 Dashboard MVP`

- status: `wykonane w repo finanse-app`
- commit:
  - `e7dd3a9` `01.2 Add MVP dashboard overview`
- wynik:
  - wdrożony główny ekran szybkiego wglądu w miesiąc z przychodami, wydatkami i bilansem
  - dodany stan „ile zostało z budżetu”, stany puste i komunikat o przekroczeniu planu
  - dodane najważniejsze kategorie budżetowe oraz prosty przełącznik miesiąca
  - logika agregacji dashboardu została wyniesiona poza komponent UI
- następny krok:
  - `01.3 Historia transakcji`

### `01.3 Historia transakcji`

- status: wykonane w repo finanse-app
- commit: `673b39b` `01.3 Add transaction history management flow`
- wynik:
  - wdrożona lista historii transakcji z filtrowaniem po typie, miesiącu i kategorii.
  - dodane wyszukiwanie, edycja inline i usuwanie.
- następny krok:
  - `02.0 OCR i dodawanie zdjęcia`

### `02.0 OCR i dodawanie zdjęcia`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - działa wybór zdjęcia paragonu z aparatu
  - działa wybór screena płatności z galerii
  - dodany został fallback `Wybierz paragon z galerii` do testów na emulatorze
  - obrazy zapisują się lokalnie jako załączniki i trafiają do tego samego flow danych co dalszy import
  - OCR on-device działa przez `@react-native-ml-kit/text-recognition`
  - poprawiono zapis załącznika pod `Expo 56` przez odejście od deprecated `FileSystem.copyAsync` na rzecz `File.copy`
  - flow OCR czeka na zakończone kopiowanie pliku i waliduje istnienie załącznika przed odczytem
- następny krok:
  - `02.1 Korekta OCR`

### `02.1 Korekta OCR`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - działa ekran korekty OCR z poprawą kwoty, daty, sklepu i kategorii
  - pola o niskiej pewności są oznaczane i prowadzą użytkownika do ręcznej poprawy
  - zapis kończy się w tej samej warstwie danych co wpis ręczny
  - heurystyka kwot dla paragonów została dopracowana pod końcowy blok płatności `SUMA PLN`, `DO ZAPŁATY`, `ZAPŁACONO`
  - parser odrzuca teraz linie podatkowe, datoczas i mylące wartości z pozycji towaru
- następny krok:
  - `02.2 Dashboard po OCR`

### `02.2 Dashboard po OCR`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - zapis po OCR używa tej samej ścieżki danych co wpis ręczny
  - po zapisie OCR budżety, bilans miesiąca i dashboard aktualizują się bez osobnych wyjątków
  - ekran zapisu pokazuje wpływ transakcji na miesiąc także dla wpisów z OCR
  - historia i szczegół transakcji pokazują spójne źródło wpisu `Ręcznie`, `OCR paragonu` albo `OCR screena`
  - oznaczenie źródła zostało wyniesione poza UI do wspólnej warstwy domenowej
- następny krok:
  - `03.0 Budżety`

### `03.0 Budżety`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - ekran budżetów został przebudowany z etapu konfiguracji `00.3` do codziennego widoku kontroli budżetu
  - kategorie wydatkowe są teraz porządkowane poza UI według ryzyka, wykorzystania i aktywności
  - dodane zostały sekcje `Wymagają uwagi`, `Aktywne i pod kontrolą`, `Aktywne bez limitu` i `Nieaktywne kategorie`
  - dla budżetu miesiąca i kategorii pokazywane są limit, wydane, pozostało i procent wykorzystania
  - wspólne statusy `w normie`, `blisko limitu` i `przekroczony` korzystają z jednej warstwy danych współdzielonej z dashboardem
- następny krok:
  - `03.1 Analizy`

### `03.1 Analizy`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - dodany został osobny ekran `Analizy` w nawigacji tabowej w miejsce placeholdera ustawień
  - analizy pokazują udział wydatków według kategorii, największe kategorie kosztów i trend dzienny wydatków
  - zakres danych można przełączyć między bieżącym i poprzednim miesiącem
  - logika agregacji została wyniesiona poza UI do wspólnej warstwy danych i korzysta z przygotowanych sum kategorii oraz nowych sum dziennych
- następny krok:
  - `03.2 Oszczędności`

### `03.2 Oszczędności`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - dodany został miesięczny, kwotowy cel oszczędności dla jednego aktywnego miesiąca
  - oszczędności liczą się prosto jako `przychody - wydatki`
  - cel ustawia się w zakładce `Budżety` razem z planem miesiąca
  - dashboard pokazuje aktualny stan oszczędności, cel, brakującą kwotę albo nadwyżkę i prosty postęp celu
  - logika celu korzysta ze wspólnych agregacji miesiąca zamiast dublować logikę budżetu
- następny krok:
  - `04.0 Bezpieczeństwo`

## 2026-05-25

### `04.0 Bezpieczeństwo`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - dodany został centralny moduł bezpieczeństwa z własnym providerem i stanem blokady
  - wejście do aplikacji można zabezpieczyć `PIN-em 4-cyfrowym`
  - biometria działa jako opcjonalne, szybsze odblokowanie nad tym samym PIN-em
  - sekret blokady i ustawienia bezpieczeństwa są trzymane poza `SQLite` w `expo-secure-store`
  - po wznowieniu aplikacji z tła dostęp zostaje ponownie zablokowany pełnoekranowym overlayem
  - dodana została zakładka `Bezpieczeństwo` do konfiguracji PIN-u, biometrii, zmiany PIN-u i wyłączenia blokady
  - pełne szyfrowanie lokalnej bazy i załączników zostało świadomie odłożone poza ten etap MVP
- następny krok:
  - ręczny test na urządzeniu lub emulatorze dla PIN-u, wznowienia i biometrii
  - potem `04.1 Poprawki UX i wydajności`

### `04.1 Poprawki UX i wydajności`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - ekran dodawania został rozdzielony na czytelny tryb ręczny i tryb OCR
  - dodane zostały `Szybkie powtórki` do podstawiania ostatnich podobnych wpisów
  - manualny flow został uproszczony do domyślnej ścieżki `kwota -> kategoria -> zapis`, a szczegóły pozostały rozwijane
  - korekta OCR pokazuje teraz, ile pól wymaga uwagi, i nie pokazuje surowego tekstu, dopóki użytkownik go nie rozwinie
  - historia przestała wykonywać zbędne pełne pobranie danych przy filtrach tylko po to, by rozpoznać pusty stan
  - dodane zostały dodatkowe indeksy pod miesięczne zapytania transakcyjne dla dashboardu, historii, budżetów i analiz
- następny krok:
  - ręczny test codziennego flow po etapach `04.0-04.1`
  - potem `04.2 Test MVP`

### `04.2 Test MVP`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - sprawdzone zostały najważniejsze flow MVP dla dashboardu, wpisu ręcznego, OCR, historii, budżetów, analiz, oszczędności i bezpieczeństwa
  - `typecheck`, `lint` i eksport web przechodzą poprawnie
  - potwierdzono spójność głównych przeliczeń i wspólnej warstwy danych między modułami
  - wykryto blocker UX w bezpieczeństwie: krótkie przejście do aparatu lub galerii zrywało sesję
  - blocker został poprawiony przez timeout sesji przy wznowieniu zamiast natychmiastowej blokady
  - na tej podstawie MVP zostało ocenione jako gotowe do codziennego użycia
- następny krok:
  - zrobić pakiet dopracowań UX i jakości przed testami telefonu
  - potem wejść w kilka dni realnego używania jako głównego rejestru

### Dopracowanie przed testami telefonu

- status: `wykonane w repo finanse-app`
- commit:
  - `c5faecc` `Polish pre-phone-test UX and lock session flow`
- wynik:
  - skrócone zostały zbyt długie opisy na głównych ekranach
  - usunięte zostały techniczne napisy typu `update`
  - ekran dodawania transakcji nie otwiera już od razu klawiatury i lepiej znosi pracę na małym ekranie
  - komunikat po zapisie transakcji został uproszczony do krótkiego `Dodano` i nie zasłania dalszego flow
  - sesja po PIN-ie albo biometrii została wydłużona tak, żeby dodanie paragonu nie wymuszało ponownego odblokowania
  - po anulowaniu albo błędzie biometrii ekran blokady nie zapętla już auto-logowania i pozwala normalnie wejść PIN-em
- następny krok:
  - wypchnąć commit `c5faecc`
  - zrobić pełny ręczny test na telefonie

### `Paczka 3` - klawiatura, safe area i małe ekrany

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - root `SafeAreaProvider` został dopięty z `initialWindowMetrics`
  - dolne menu zaczęło uwzględniać dolny inset systemu na telefonach z gestami i paskiem systemowym
  - ekrany `Dodaj transakcję`, `Budżety`, `Bezpieczeństwo` i `Historia` dostały poprawione zachowanie scrolla oraz insetów przy aktywnej klawiaturze
  - `Dashboard` i `Analizy` dostały dynamiczny dolny padding, żeby końcówka treści nie wpadała pod wyższy tabbar
  - dodany został mały współdzielony helper do liczenia bezpiecznego dolnego paddingu zawartości ekranów
- następny krok:
  - ręczny test telefonu dla klawiatury, focusu pól, dolnego menu i małych ekranów
  - potem `Paczka 4` - logowanie, PIN, biometria i sesja

### `Paczka 4` - logowanie, PIN, biometria i sesja

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - przy pierwszym uruchomieniu bez aktywnego PIN-u pojawia się pytanie o włączenie blokady z przejściem do zakładki `Bezpieczeństwo`
  - odrzucenie pytania jest zapamiętywane lokalnie i prompt nie wraca przy kolejnych uruchomieniach bez zmiany decyzji użytkownika
  - ekran odblokowania dostał 4 pola PIN-u z maskowaniem cyfr kropkami i prostszym copy bez technicznych etykiet
  - wyłączenie biometrii wymaga teraz potwierdzenia biometrią albo PIN-em zamiast prostego toggle
  - logika aktywnej sesji została utrzymana: zwykłe przejście do aparatu lub galerii nie wymusza ponownego PIN-u
- następny krok:
  - pełny ręczny test telefonu dla onboardingu PIN-u, blokady, anulowanej biometrii i powrotu z aparatu lub galerii

### `Podstawowy rebranding Zenifi`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - nazwa aplikacji w konfiguracji Expo została ustawiona na `Zenifi`
  - slug, scheme oraz identyfikatory buildów zostały uporządkowane pod kolejne buildy jako `zenifi`
  - przygotowane zostały nowe assety marki na bazie `zenifi-logo-v3-balance.svg`
  - podmienione zostały:
    - app icon
    - Android adaptive icon
    - monochrome icon
    - splash asset
    - favicon web
  - bazowa paleta aplikacji została zbliżona do kierunku marki `Zenifi`
  - najbardziej oczywiste miejsca widocznej starej marki w UI zostały usunięte lub podmienione
- następny krok:
  - uruchomić kolejny build / preview już pod marką `Zenifi`
  - ocenić, czy potrzebny jest drugi etap rebrandingu UI bez mieszania go z bieżącym utrzymaniem produktu
  - potem tylko selektywne poprawki z realnego użycia

### `Paczka 2` - kategorie i budżety

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - kategorie dostały pełny podstawowy CRUD: tworzenie, edycję i usuwanie
  - zakładka `Budżety` pokazuje teraz listę kategorii z krótkim opisem zamiast ciężkiej edycji inline każdej pozycji
  - limit kategorii ustawia się dopiero po wejściu w konkretny element
  - sekcje zostały uproszczone do bardziej produktowego nazewnictwa `Kategorie z limitem` i `Kategorie bez limitu`
  - opisy najważniejszych sekcji budżetowych zostały skrócone
  - usunięcie kategorii odłącza powiązane stare transakcje od kategorii i czyści jej limit dla bieżącego miesiąca
  - do paczki dopięty został też wybór ikony kategorii, wykorzystywanej potem na dashboardzie
- następny krok:
  - ręczny test telefonu dla dodawania, edycji i usuwania kategorii oraz ustawiania limitu po wejściu w detal
  - potem commit razem z pozostałymi paczkami feedbacku

### `Paczka 1` - historia oraz dashboard copy i filtrowanie miesięcy

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - historia dostała filtr `Wszystkie miesiące`
  - przełącznik miesięcy na dashboardzie został utrzymany jako otwarty także dla pustych miesięcy, co pozostaje najprostszym zachowaniem zgodnym z produktem
  - z dashboardu usunięty został tekst o `guardrailach budżetowych`
  - `Cel oszczędności` został zmieniony na `Cel oszczędnościowy`
  - `Sytuacja miesiąca` została zmieniona na `Ten miesiąc`
  - skrócone zostały puste stany i pomocnicze teksty na dashboardzie
- następny krok:
  - ręczny test telefonu dla historii z filtrem wszystkich miesięcy i dla pustych / przyszłych miesięcy na dashboardzie
  - potem commit razem z pozostałymi paczkami feedbacku

### `03.x Doprecyzowanie OCR po teście ręcznym`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - po wdrożeniu `03.0` ręczny test wykazał regresję heurystyk OCR dla części screenów płatności i części paragonów
  - parser paragonów dostał wyższy priorytet dla wyniku z układu OCR bloków nad surowym fallbackiem tekstowym
  - parser screenów został doprecyzowany o anchory płatności, filtrowanie szumu bankowego i karanie małych opłat/prowizji
  - po tej poprawce ręcznie sprawdzone przykłady zaczęły znowu zwracać poprawne kwoty
- następny krok:
  - `04.0 Bezpieczeństwo`

### Budżety przychodów

- status: `doprecyzowane lokalnie w repo finanse-app`
- wynik:
  - w budżetach przychodów przyjęto uproszczenie MVP: brak osobnych celów i limitów per kategoria, pozostaje podgląd realnych wpływów
- następny krok:
  - utrzymać to uproszczenie do czasu osobnego etapu rozwoju budżetów

## Stan commitów

Na moment tego wpisu:

- `finanse-wiki` ma własną historię commitów dla dokumentacji i struktury vaultu
- `finanse-app` ma w historii repo domknięte wdrożenia `00.1-01.3`
- kolejne lokalne commity aplikacji obejmują:
  - `2dfc98c` `Complete 02.2 OCR dashboard integration`
  - `8f6f4f5` `Finalize 02.0-02.1 OCR receipt flow`
  - `83cd25e` `02.0-02.1 Add OCR import and correction flow`
  - `b4d31c4` `Fix income category budget entry`

Warto dalej dopisywać tu skrócone odniesienia do hashy po każdym kolejnym update.

### `Drobne dopracowania po testach telefonu`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - po wyłączeniu nagłówków tabów ekrany dostały wspólny górny inset oparty o safe area, żeby treść nie wpadała pod status bar
  - `Dodaj transakcję` odświeża teraz kontekst po powrocie na ekran, więc nowo dodane kategorie z `Budżetów` są od razu widoczne
  - sekcja dodawania z obrazu dostała prostszy, mniej techniczny język zamiast cięższego nazewnictwa `OCR`
- następny krok:
  - dalsze poprawki już tylko po realnym użyciu i pojedynczych zgłoszeniach z telefonu

### `Domknięcie dnia`

- status: `zapisane w wiki`
- wynik:
  - podstawowy rebranding do `Zenifi` jest opisany i zapisany
  - poprawki UX po testach telefonu są już ujęte w dokumentacji
  - lokalne APK nie pozostaje w repo jako docelowy artefakt dystrybucyjny, bo ta droga ma iść przez GitHub Releases
- następny krok:
  - przygotować pierwszy release poza repo zamiast trzymać duże binaria w Git
  - kolejne drobne poprawki robić tylko po realnym użyciu

## 2026-06-02

### `04.3 Backup ZIP`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - dodany został ręczny eksport danych do pliku `zenifi-backup-YYYY-MM-DD-HH-mm.zip`
  - dodany został ręczny import backupu ZIP przez picker dokumentów
  - format backupu zawiera `manifest.json`, `data.json` i realne pliki załączników pod `attachments/<attachmentId>/<filename>`
  - `data.json` nie przenosi lokalnych `fileUri`, tylko stabilne metadane załączników i ścieżkę `backupPath`
  - import scala dane po stabilnych `id`, aktualizuje tylko nowsze rekordy i nie kasuje lokalnych danych
  - konflikty kategorii po nazwie są obsługiwane przez mapowanie na lokalną kategorię albo sufiks ` (import)`
  - backup nie przenosi PIN-u, biometrii ani sekretów z `SecureStore`
  - pierwsza wersja ZIP-a nie jest szyfrowana, ale manifest ma pola przygotowane pod przyszłe szyfrowanie i chmurę
  - dodane zależności: `expo-document-picker`, `expo-sharing`, `fflate`
  - `typecheck` i `lint` przechodzą
- ograniczenia:
  - ręczny smoke test na urządzeniu pozostaje do wykonania, bo Expo dev server nie wystartował w środowisku Codexa przez zajęte porty `8081` i `8082`
  - web ma w tej wersji tylko jawny komunikat, że ZIP backup jest funkcją mobilną
- następny krok:
  - ręczny test Androida: eksport, import na czystej instalacji, ponowny import bez duplikatów, import na istniejących danych i sprawdzenie załączników

### `Zmiana zakładki zabezpieczeń na Ustawienia`

- status: `wykonane lokalnie w repo finanse-app`
- wynik:
  - dolna zakładka konfiguracji aplikacji ma teraz etykietę `Ustawienia` zamiast `Bezpieczeństwo`
  - ikona zakładki została zmieniona z tarczy na koło zębate
  - ekran konfiguracji ma nagłówek `Ustawienia`, a sekcje PIN-u, biometrii i kopii danych pozostają częścią tego ekranu
  - prompt pierwszego PIN-u kieruje użytkownika do `Ustawień`
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi

## 2026-06-03

### `01 Historia - filtry i domyślny zakres`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/01 Historia - filtry i domyślny zakres]]
- wynik:
  - historia domyślnie otwiera zakres `Wszystkie miesiące`
  - lista historii pozostaje sortowana od najnowszych transakcji do najstarszych
  - na górze filtrów stale widoczne są `Szukaj` i segment `Typ`
  - filtry `Miesiąc` i `Kategoria` są ukryte pod przyciskiem `Filtry aktywne: X`
  - licznik aktywnych filtrów dotyczy ukrytych filtrów miesiąca i kategorii
  - po edycji transakcji historia nie przełącza się automatycznie z `Wszystkie miesiące` na konkretny miesiąc
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
- do sprawdzenia ręcznie:
  - test telefonu opisany w notatce update'u: historia z transakcjami z różnych miesięcy, wyszukiwanie, segment typu, rozwinięcie filtrów, filtr miesiąca/kategorii i czyszczenie filtrów

### `02 Zwijane sekcje UI`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/02 Zwijane sekcje UI]]
- wynik:
  - dodany został wspólny komponent `CollapsibleSection`
  - stan rozwinięcia jest zapamiętywany per `screenId` i `sectionId`
  - web zapisuje stan w `localStorage`, a aplikacja natywna przez istniejące `expo-secure-store`
  - pilotaż wdrożono na ekranie `Historia` dla sekcji dodatkowych filtrów
  - stale widoczne pozostają krytyczne kontrolki historii: `Szukaj` i segment `Typ`
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
- do sprawdzenia ręcznie:
  - otworzyć historię, zwinąć i rozwinąć `Filtry aktywne: X`, przejść na inny ekran, wrócić i sprawdzić zapamiętany stan sekcji

### `03 Budżety - limit 0 jako bez limitu`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/03 Budżety - limit 0 jako bez limitu]]
- wynik:
  - wariant `3B` został wdrożony bez migracji modelu danych
  - wpisanie `0 zł` w limicie kategorii jest poprawne i zapisuje się jako limit `0`
  - w agregacji budżetów limit kategorii `0` jest interpretowany jak `Bez limitu`
  - kategoria z limitem `0` nie trafia do przekroczeń, ryzyk ani kategorii z limitem
  - szczegół kategorii ma jedno pole limitu bez osobnego przełącznika limitu; puste pole albo `0` oznacza `Bez limitu`
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
- do sprawdzenia ręcznie:
  - wejść w kategorię wydatkową, ustawić limit `0 zł`, wrócić do listy budżetów i potwierdzić stan `Bez limitu`
  - dodać wydatek w tej kategorii i sprawdzić, że nie pojawia się przekroczenie
  - zmienić limit na kwotę większą od zera i ponownie na `0 zł`

### `04 Ustawienia jako centrum aplikacji`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/04 Ustawienia jako centrum aplikacji]]
- wynik:
  - wariant `4B` został wdrożony jako lokalne centrum ustawień bez osobnego stacka nawigacji
  - pierwszy widok `Ustawień` pokazuje kafle `Bezpieczeństwo`, `Backup i dane`, `Synchronizacja` i `Aplikacja`
  - kafel `Bezpieczeństwo` prowadzi do istniejącej konfiguracji PIN-u, biometrii, zmiany PIN-u i wyłączenia blokady
  - kafel `Backup i dane` prowadzi do istniejącego eksportu i importu backupu ZIP oraz informacji o danych lokalnych
  - kafel `Synchronizacja` jasno pokazuje, że sync nie jest dostępny w MVP
  - kafel `Aplikacja` pokazuje podstawowe informacje o aplikacji i trybie offline-first
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
- do sprawdzenia ręcznie:
  - otworzyć `Ustawienia`, wejść w każdy kafel i wrócić do centrum ustawień
  - w `Bezpieczeństwie` sprawdzić dostęp do PIN-u oraz biometrii
  - w `Backup i dane` sprawdzić dostęp do eksportu i importu
  - potwierdzić, że `Synchronizacja` nie sugeruje gotowej funkcji

### `05 Backup do plików telefonu`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/05 Backup do plików telefonu]]
- wynik:
  - wariant `5B` został wdrożony bez zmiany formatu backupu ZIP
  - w `Ustawienia -> Backup i dane` jest jeden przycisk startowy `Utwórz backup`
  - po przygotowaniu ZIP-a w cache pojawiają się akcje `Zapisz do plików` i `Udostępnij`
  - zapis do plików używa systemowego wyboru katalogu Expo FileSystem SDK 56
  - udostępnianie używa dotychczasowego systemowego share sheet
  - import backupu ZIP pozostał bez zmiany
  - nie wdrażano szyfrowania ani synchronizacji
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
- do sprawdzenia ręcznie:
  - na telefonie wejść w `Ustawienia -> Backup i dane`, nacisnąć `Utwórz backup`, potem `Zapisz do plików` i wybrać katalog w systemowym pickerze
  - ponownie utworzyć backup i sprawdzić `Udostępnij`
  - po zapisaniu pliku sprawdzić, że import nadal przyjmuje zapisany ZIP
- poprawka po teście telefonu:
  - zapis do katalogu wybranego przez Android SAF używa teraz `Directory.createFile(...)`, bo `File.create(...)` jest odrzucane dla URI `content://`
  - po poprawce `npm run typecheck` i `npm run lint` przechodzą

### `06 Analiza - wybór okresu`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/06 Analiza - wybór okresu]]
- wynik:
  - wariant `6C` został wdrożony bez zmian w dashboardzie
  - ekran `Analizy` ma kompaktowy przycisk aktualnego okresu
  - po kliknięciu przycisku otwiera się wysuwany selektor zakresu
  - obsługiwane zakresy to `Ten miesiąc`, `Poprzedni miesiąc`, `3 miesiące`, `6 miesięcy`, `Rok` i `Cały okres`
  - agregacje analizy składają dane z wielu miesięcy przez istniejące repozytoria transakcji
  - trend pozostaje dzienny dla pojedynczego miesiąca, a dla zakresów wielomiesięcznych pokazuje słupki miesięczne
  - puste stany i metryka aktywności są dopasowane do wybranego zakresu
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
- do sprawdzenia ręcznie:
  - na telefonie otworzyć `Analizy`, kliknąć kompaktowy przycisk okresu i zamknąć selektor bez wyboru
  - wybrać kolejno każdy zakres i sprawdzić, czy podsumowanie, kategorie i trend się odświeżają
  - porównać wartości dla `Ten miesiąc`, `6 miesięcy` i `Cały okres`
  - sprawdzić pusty stan na zakresie bez wydatków

### `07 Analiza - bilans okresu`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/07 Analiza - bilans okresu]]
  - [[Inbox - rozpisane updatey/06 Analiza - wybór okresu]]
- wynik:
  - wariant `7B` został wdrożony na ekranie `Analizy`
  - karta `Bilans okresu` pokazuje mocny wynik liczony jako `przychody - wydatki`
  - breakdown karty pokazuje `Przychody`, `Wydatki` i `Wynik`
  - wynik reaguje na aktualny zakres z selektora analizy
  - copy karty mówi, że wynik dotyczy transakcji zapisanych w aplikacji i nie jest saldem konta bankowego
  - karta pokazuje też zrozumiały stan zerowy dla zakresu bez danych
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
- do sprawdzenia ręcznie:
  - na telefonie dodać przychód i wydatek w tym samym okresie, wejść w `Analizy` i sprawdzić wynik bilansu
  - sprawdzić wariant dodatni, ujemny i zerowy
  - zmienić zakres analizy i potwierdzić, że karta przelicza `Przychody`, `Wydatki` i `Wynik`
  - sprawdzić copy karty, czy nie sugeruje salda bankowego

### `08 Ustawienia - reset stanu i komunikatów`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/08 Ustawienia - reset stanu i komunikatów]]
  - [[Inbox - rozpisane updatey/04 Ustawienia jako centrum aplikacji]]
  - [[Inbox - rozpisane updatey/05 Backup do plików telefonu]]
- wynik:
  - po opuszczeniu taba `Ustawienia` lokalny widok wraca do `home`, czyli głównego menu kafli
  - po kliknięciu `Wróć do ustawień` z podwidoku lokalny widok także wraca do `home` i czyści stare komunikaty
  - wejście w inny kafel ustawień czyści stare komunikaty z poprzedniej sekcji
  - czyszczone są `feedback`, `errorMessage` i `backupSummary`
  - czyszczone są też tymczasowe potwierdzenie wyłączenia biometrii i jego pole PIN-u
  - asynchroniczne akcje backupu nie ustawiają nowych komunikatów, jeśli użytkownik opuścił już tab `Ustawienia`
  - logika PIN-u, biometrii i repozytorium backupu nie została przebudowana
- celowo zostawione:
  - wartości pól formularzy PIN-u i zmiany PIN-u nie są twardo resetowane przy opuszczeniu taba
  - stan trwały ustawień bezpieczeństwa oraz ustawienia backupu nie są zmieniane
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
- do sprawdzenia ręcznie:
  - wejść w `Ustawienia -> Backup i dane`, utworzyć backup, przełączyć tab i wrócić do `Ustawień`
  - potwierdzić, że widoczne jest główne menu ustawień, bez starego komunikatu i bez podsumowania backupu
  - wejść ponownie w `Backup i dane` i sprawdzić, że stare akcje backupu nie są widoczne bez ponownego utworzenia backupu
  - utworzyć backup, kliknąć `Wróć do ustawień` i potwierdzić, że centrum ustawień nie pokazuje już komunikatu ani podsumowania backupu

### `09 Historia - inline szczegóły i edycja transakcji`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/09 Historia - inline szczegóły i edycja transakcji]]
  - [[Inbox - rozpisane updatey/01 Historia - filtry i domyślny zakres]]
- wynik:
  - kliknięcie transakcji rozwija jej szczegóły bezpośrednio pod rekordem historii
  - edycja, zapis, anulowanie edycji, usuwanie i podgląd załącznika pozostają w tym samym rozwiniętym elemencie
  - jednocześnie może być rozwinięta tylko jedna transakcja
  - ponowne kliknięcie aktywnej transakcji albo przycisk `Zwiń` zamyka szczegóły
  - kliknięcie innej transakcji zamyka poprzedni detal i otwiera nowy
  - walidacja edycji i zapis korzystają z dotychczasowej logiki historii
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
- do sprawdzenia ręcznie:
  - na telefonie wejść w `Historia`, kliknąć transakcję z góry listy i sprawdzić rozwinięcie inline
  - kliknąć inną transakcję i potwierdzić, że poprzednia się zamyka
  - wejść w `Edytuj`, zmienić pole, zapisać i sprawdzić odświeżenie listy
  - wejść ponownie w edycję, nacisnąć `Anuluj` i potwierdzić powrót do podglądu bez zapisu
  - przewinąć dłuższą listę i sprawdzić, czy rozwinięty element nie rozjeżdża layoutu

### `10B Rebranding v2 - wdrożenie w kodzie`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/10A Rebranding v2 - kolory i logo]]
  - [[Inbox - rozpisane updatey/10B Rebranding v2 - wdrożenie w kodzie]]
  - [[Inbox - rozpisane updatey/10 Rebranding v2 - nowe logo i żywszy UI]]
- decyzja wejściowa:
  - paleta: `Neon Mint`
  - kierunek logo: `Logo B - Z + wykres`
- wynik:
  - assety app icon, adaptive icon, monochrome icon, splash i favicon zostały wygenerowane z nowego źródła SVG
  - konfiguracja Expo dostała tło `#F6FFF9` i bazę `#102A2A`
  - `src/shared/theme` ma teraz `lightTheme`, `lightColors` i semantyczne tokeny pod późniejsze `darkTheme`
  - wspólne CTA używa tokenów `cta` i `ctaText`
  - stany ostrzeżeń, danger, sukcesu i miękkich akcentów w głównych ekranach korzystają z tokenów zamiast lokalnych HEX-ów
  - nie wdrażano dark mode, zmian nawigacji ani zmian logiki danych
- świadomie pozostawione hardcody kolorów:
  - `app.json` i SVG assetów jako źródła brandingu Expo
  - `src/shared/theme/index.ts` jako centralne źródło tokenów
  - `src/storage/seedData.ts` jako kolory danych startowych kategorii
  - `src/features/analysis/data/analysis.ts` jako fallback koloru kategorii do osobnej decyzji, jeśli kolory kategorii mają też przejść na tokeny
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
  - asset `assets/icon.png` został obejrzany lokalnie po wygenerowaniu
- do sprawdzenia ręcznie:
  - ikona aplikacji i adaptive icon na Androidzie
  - splash / start aplikacji
  - dashboard, główne CTA i karty metryk
  - dodawanie transakcji z akcentem pól wymagających uwagi
  - historia, budżety i ustawienia pod kątem kontrastu tekstów i stanów

### `11 Tryb ciemny i system motywów`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/11 Tryb ciemny i system motywów]]
  - [[Inbox - rozpisane updatey/10 Rebranding v2 - nowe logo i żywszy UI]]
- wynik:
  - dodano system motywów z preferencjami `Systemowy`, `Jasny` i `Ciemny`
  - preferencja zapisuje się lokalnie przez `expo-secure-store`, a na webie przez `localStorage`
  - tryb `Systemowy` rozwiązuje się przez ustawienie telefonu z `useColorScheme`
  - `StatusBar` przełącza styl ikon zgodnie z aktywnym motywem
  - `NavigationContainer`, tabbar, overlay blokady, prompt PIN-u i wspólne komponenty UI korzystają z bieżących tokenów theme
  - kluczowe ekrany `Dashboard`, `Dodaj`, `Historia`, `Budżety`, `Analizy`, `Ustawienia` i ekran blokady zostały przepięte z jasnych statycznych kolorów na dynamiczne style motywu
  - po update `12` przełącznik motywu jest dostępny w `Ustawienia -> Motywy`
  - nie wdrażano pełnej personalizacji palety ani rozbudowanego edytora motywów
- świadomie pozostawione hardcody kolorów:
  - `src/shared/theme/index.ts` jako centralne źródło tokenów light/dark
  - `src/storage/seedData.ts` jako kolory danych startowych kategorii
  - `src/features/analysis/data/analysis.ts` jako fallback koloru kategorii
  - assety Expo i SVG jako źródła brandingu aplikacji
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
  - `git diff --check` nie zgłasza problemów
- do sprawdzenia ręcznie:
  - na telefonie wejść w `Ustawienia -> Motywy` i przełączyć kolejno `Ciemny`, `Jasny`, `Systemowy`
  - zamknąć i ponownie uruchomić aplikację, sprawdzając, czy wybrany motyw został zapamiętany
  - przejść przez `Dashboard`, `Dodaj`, `Historia`, `Budżety`, `Analizy`, `Ustawienia` i ekran blokady, sprawdzając kontrast tekstów, kart, tabbara, CTA oraz status baru
  - w trybie `Systemowy` zmienić motyw telefonu i sprawdzić, czy aplikacja reaguje po powrocie na ekran

### `12 Motywy kolorystyczne - wybór palety`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/12 Motywy kolorystyczne - wybór palety]]
  - [[Inbox - rozpisane updatey/11 Tryb ciemny i system motywów]]
  - [[Inbox - rozpisane updatey/10B Rebranding v2 - wdrożenie w kodzie]]
  - [[../02 Produkt/Zenifi - Palety rebrandingu v2]]
- wynik:
  - system theme działa teraz jako `themeMode + paletteId -> theme`
  - dostępne są trzy palety: `Neon Mint`, `Electric Pine` i `Signal Finance`
  - domyślną paletą pozostaje `Neon Mint`
  - `themeMode` i `paletteId` zapisują się niezależnie poza SQLite, natywnie w `expo-secure-store`, a na webie w `localStorage`
  - dotychczasowy klucz trybu `zenifi_theme_preference` jest czytany jako fallback dla istniejących instalacji
  - `Ustawienia -> Motywy` zawiera wybór trybu `Systemowy / Jasny / Ciemny` oraz kafelki palet z próbkami kolorów
  - `Ustawienia -> Aplikacja` pozostaje informacyjne i nie zawiera konfiguracji motywu ani palety
  - progresy, trend analizy i pozytywne stany finansowe korzystają z tokenów palety przez `success` i `chartPrimary`
  - nie dodano edytora kolorów, własnych HEX-ów ani personalizacji poszczególnych tokenów przez użytkownika
- świadomie pozostawione hardcody kolorów:
  - `src/shared/theme/index.ts` jako centralne źródło palet i tokenów
  - `src/storage/seedData.ts` jako kolory danych startowych kategorii
  - `src/features/analysis/data/analysis.ts` jako fallback koloru kategorii
  - assety Expo i SVG jako źródła brandingu aplikacji
- weryfikacja:
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
  - `git diff --check` nie zgłasza problemów
- do sprawdzenia ręcznie:
  - na telefonie wejść w `Ustawienia -> Motywy`
  - przełączyć paletę na `Electric Pine`, sprawdzić `Dashboard`, `Historia`, `Budżety`, `Analizy` i `Ustawienia`
  - przełączyć paletę na `Signal Finance` i sprawdzić te same ekrany
  - przełączyć tryb `Jasny`, `Ciemny` i `Systemowy`, potwierdzając niezależność trybu od palety
  - wejść w `Ustawienia -> Aplikacja` i potwierdzić, że nie ma tam konfiguracji motywu ani palety
  - zamknąć i uruchomić aplikację ponownie, sprawdzając zapamiętanie `themeMode` i `paletteId`

### `13 Start aplikacji - nazwa i splash`

- status: `wdrożone lokalnie w repo finanse-app`
- źródło:
  - [[Inbox - rozpisane updatey/13 Start aplikacji - nazwa i splash]]
  - [[Inbox - rozpisane updatey/10B Rebranding v2 - wdrożenie w kodzie]]
- wynik:
  - `app.json` był już ustawiony na `Zenifi`, `zenifi` i `com.justitdo.zenifi`
  - `package.json` ma techniczną nazwę `zenifi-app`
  - aktywne assety `assets/icon.png`, `assets/splash-icon.png`, `assets/android-icon-foreground.png`, `assets/android-icon-background.png`, `assets/android-icon-monochrome.png` i `assets/favicon.png` są spójne z tymczasowym brandem Zenifi
  - lokalnie wygenerowany folder `android/` miał stare wartości `finanse-app`, `com.anonymous.finanseapp` oraz domyślny splash/launcher Expo
  - lokalny `android/` został wyrównany do `Zenifi`, `com.justitdo.zenifi`, tła `#F6FFF9` i koloru bazowego `#102A2A`
  - natywne zasoby `splashscreen_logo.png` i `ic_launcher*.webp` zostały odświeżone z aktualnych assetów w `assets/`
  - po błędzie `package com.anonymous.finanseapp does not exist` pliki `MainActivity.kt` i `MainApplication.kt` zostały przeniesione do ścieżki `android/app/src/main/java/com/justitdo/zenifi/`
  - usunięto lokalny wygenerowany cache autolinkingu Androida, który nadal zawierał stary `project.android.packageName`
  - finalnego logo nadal nie projektowano; używany jest obecny tymczasowy brand
- uwaga:
  - katalog `android/` jest ignorowany przez Git jako wygenerowany folder natywny, ale lokalnie wpływa na APK budowane przez `expo run:android`
  - jeśli po zmianach telefon nadal pokazuje starą nazwę albo ikonę, przyczyną jest najpewniej stara instalacja APK/dev build/cache, a nie `app.json`
- weryfikacja:
  - `npx expo config --json` zwraca `name: Zenifi` i `android.package: com.justitdo.zenifi`
  - `rg` nie znajduje aktywnych tekstowych referencji do `finanse-app`, `finanseapp` ani `com.anonymous.finanseapp` w sprawdzanych plikach aplikacji i Androida
  - `./gradlew app:assembleDebug -x lint -x test --configure-on-demand --build-cache -PreactNativeDevServerPort=8081 -PreactNativeArchitectures=x86_64 --stacktrace` przechodzi po odświeżeniu cache autolinkingu
  - `npm run typecheck` przechodzi
  - `npm run lint` przechodzi
  - natywne assety Androida zostały sprawdzone rozmiarami i podglądem lokalnym
- do sprawdzenia ręcznie:
  - odinstalować z telefonu stare instalacje `com.anonymous.finanseapp` i `com.justitdo.zenifi`, jeśli są widoczne
  - wykonać czysty rebuild/dev install i sprawdzić, że launcher pokazuje nazwę `Zenifi`
  - uruchomić aplikację na telefonie i sprawdzić splash z tymczasowym znakiem Zenifi na jasnym tle
  - sprawdzić ikonę launchera i ekran ostatnich aplikacji po czystej instalacji
