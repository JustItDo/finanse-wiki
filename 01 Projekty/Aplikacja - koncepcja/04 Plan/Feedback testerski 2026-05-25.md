# Feedback testerski 2026-05-25

## Powiązane notatki

- [[Backlog]]
- [[Roadmapa]]
- [[Dziennik wdrożeń]]
- [[Updatey wdrożeniowe/04.2 Test MVP|04.2 Test MVP]]
- [[../03 Technologia/Workflow developera|Workflow developera]]

## Cel notatki

To jest robocza lista pierwszego realnego feedbacku po wypuszczeniu `.apk` na telefon i do pierwszych testerów.

Lista ma być kompletna i nie gubić żadnej uwagi przed późniejszym rozbiciem na mniejsze paczki wdrożeniowe.

## Zasada pracy z tą listą

- najpierw zrobić porządne review jakości kodu i UX
- potem połączyć findings z review z tą listą
- dopiero potem rozbijać zmiany na mniejsze prompty albo wdrażać jedną sensowną paczkę

## Historia i miesiące

- w historii ma być możliwość wybrania opcji `wszystkie miesiące`

## Kategorie i budżety

- ma być możliwość dodania własnej kategorii
- ma być możliwość usuwania istniejących kategorii
- ma być możliwość dowolnej modyfikacji kategorii
- w zakładce `Budżet` ma być lista kategorii z krótkim opisem
- dopiero po kliknięciu w element kategorii użytkownik powinien ustawiać daną kwotę
- nazwa `Aktywne bez limitu` nie ma sensu i powinna zostać zmieniona
- propozycja:
  - `Kategorie bez limitu`
  - `Aktywne kategorie z limitem`
- w tych najważniejszych kategoriach budżetowych nie jest potrzebny obecny długi tekst
- jeżeli zostaje, to powinien być skrócony do lekkiej, minimalnej informacji

## Dashboard

- w dashboardzie nie da się wejść do miesięcy, których jeszcze nie było
- tekst z pustym stanem i brak `guardrailów budżetowych` jest niepotrzebny
- `cel oszczędności` ma zostać zmieniony na `cel oszczędnościowy`
- `Sytuacja miesiąca` ma zostać zmieniona na `Ten miesiąc`

## Dodawanie transakcji i klawiatura

- przy wpisywaniu wartości z klawiatury pola tekstowe są zasłaniane
- klawiatura zasłania pola, do których użytkownik wpisuje treść

## Logowanie, PIN, biometria i sesja

- przy pierwszym odpaleniu aplikacji użytkownik ma być pytany, czy chce ustawić PIN
- jeśli chce, kierujemy go do zakładki `Bezpieczeństwo`
- jeśli nie chce, zapamiętujemy jego wybór i nie pokazujemy mu więcej tego powiadomienia
- przy odblokowywaniu ma być ładny widok z 4 kreskami / polami na PIN
- zamiast cyfr mają pojawiać się kropki
- nie piszemy `PIN zapasowy`, tylko po prostu `PIN`
- przy chęci usunięcia biometrii trzeba potwierdzić akcję palcem albo PIN-em
- na panelu logowania są niepotrzebne napisy `sesja` i `Face ID / odcisk palca`

## Nawigacja i bezpieczne pole robocze

- na telefonach, na których jest dolny pasek systemowy, nasze dolne menu jest zasłaniane przez UI telefonu

## Sugestie UX do późniejszej oceny

- część z tych rzeczy prawdopodobnie da się naprawić w jednym promptcie, jeśli dotyczą tego samego obszaru
- najbardziej naturalne grupy robocze wyglądają dziś tak:
  - historia i filtrowanie miesięcy
  - kategorie i budżety
  - dashboard i copy UI
  - klawiatura, safe area i małe ekrany
  - logowanie, PIN, biometria i sesja

## Status

- lista zapisana
- nic z tej notatki nie powinno zostać pominięte przy późniejszym rozbijaniu na wdrożenia
