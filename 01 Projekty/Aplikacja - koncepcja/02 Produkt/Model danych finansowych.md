# Model danych finansowych

## Cel
Ten punkt określa, jakie informacje aplikacja musi przechowywać o wydatkach, przychodach, załącznikach, kategoriach i budżetach.

Dobrze dobrany model danych ma:

- wspierać szybkie codzienne dodawanie wydatków,
- obsługiwać paragony i screenshoty,
- umożliwiać sensowne wykresy i analizy,
- nie komplikować MVP bardziej niż to potrzebne.

## Model 1 - Prosty

### Główna idea
Jedna transakcja przechowuje tylko podstawowe informacje potrzebne do zapisania wydatku lub przychodu.

### Pola transakcji
- `typ` - wydatek albo przychód
- `kwota`
- `data`
- `kategoria`
- `opis`
- `źródło` - ręcznie, paragon, screen

### Cechy modelu
- jedna transakcja ma jedną kategorię
- zdjęcie lub screen jest opcjonalnym dodatkiem
- model jest bardzo lekki

### Zalety
- szybkie wdrożenie
- mała złożoność
- dobre na bardzo małe MVP

### Wady
- słabsze wsparcie dla OCR
- mało miejsca na rozwój
- gorsza jakość analiz i historii źródła danych

## Model 2 - Zbalansowany

### Główna idea
Model przechowuje nie tylko samą transakcję, ale też informacje o źródle, metodzie płatności i danych wykrytych z paragonu lub screena.

### Główne byty
- `transactions`
- `attachments`
- `categories`
- `category_budgets`
- opcjonalnie `monthly_budgets`

### Proponowane pola transakcji
- `id`
- `typ` - wydatek albo przychód
- `kwota`
- `waluta`
- `data_transakcji`
- `kategoria_id`
- `opis`
- `merchant` - sklep lub źródło transakcji
- `metoda_płatności` - gotówka, karta, BLIK, przelew, inne
- `źródło_dodania` - ręcznie, paragon, screen
- `status` - zatwierdzona, do poprawy
- `attachment_id`
- `created_at`
- `updated_at`

### Proponowane pola załącznika
- `id`
- `typ` - paragon albo screen
- `ścieżka_lub_url`
- `ocr_raw_text`
- `ocr_detected_amount`
- `ocr_detected_date`
- `ocr_detected_merchant`
- `ocr_confidence` - opcjonalnie

### Proponowane pola kategorii
- `id`
- `nazwa`
- `typ` - wydatek albo przychód
- `kolor`
- `ikona`
- `aktywna`

### Proponowane pola budżetu kategorii
- `id`
- `kategoria_id`
- `miesiąc`
- `rok`
- `limit`
- `wydano`
- `pozostało`

### Cechy modelu
- jedna transakcja nadal ma jedną kategorię
- OCR i screenshoty są wspierane wprost
- model dobrze nadaje się do dashboardu i analiz
- daje dobrą bazę pod późniejszy rozwój

### Zalety
- bardzo dobry balans między prostotą a rozwojowością
- dobrze pasuje do głównego flow tej aplikacji
- pozwala wygodnie analizować dane i rozwijać OCR

### Wady
- więcej pól i zależności niż w modelu prostym
- wymaga lepszego zaprojektowania już na starcie

## Model 3 - Zaawansowany

### Główna idea
Model danych przygotowany pod dojrzalszy produkt z bardziej rozbudowaną logiką finansową.

### Dodatkowe możliwości
- jedna transakcja może mieć wiele pozycji
- wydatki można rozbijać na kilka kategorii
- można obsługiwać wydatki stałe i subskrypcje
- można rozróżniać potrzeby i zachcianki
- można dodać bardziej zaawansowane insighty i automatyzacje

### Dodatkowe byty
- `transaction_items`
- `subscriptions`
- `saving_goals`
- `accounts`
- `insights`
- `recurring_rules`

### Zalety
- bardzo mocna baza pod rozwój produktu
- najlepsza elastyczność
- dobra pod produkt premium i zaawansowaną analitykę

### Wady
- za duża złożoność na start
- większe ryzyko przeciążenia MVP
- wolniejsze wejście w development

## Wstępna rekomendacja
Na ten moment najbardziej sensowny wydaje się `Model 2: Zbalansowany`.

Powód:

- dobrze wspiera OCR i screenshoty,
- daje sensowną bazę pod budżety i analizy,
- nadal nie jest przesadnie ciężki na MVP,
- pozwala później przejść do bardziej zaawansowanej wersji bez przebudowy wszystkiego od zera.

## Decyzja
Wybrany model danych finansowych dla projektu to `Model 2: Zbalansowany`.

To jest oficjalna decyzja dla MVP.
