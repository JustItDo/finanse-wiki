# Użytkownicy i scenariusze

## Powiązane notatki

- [[../Mapa projektu|Mapa projektu]]
- [[../01 Wizja/Start - brief projektu|Brief projektu]]
- [[User flow]]
- [[Flow OCR i screenów]]
- [[Sukces MVP]]
- [[../04 Plan/Updatey wdrożeniowe/04.2 Test MVP|Update 4.2 - Test MVP]]

## Typy użytkowników
- użytkownik główny: Ty, osoba zarządzająca własnymi finansami
- potencjalny przyszły użytkownik: osoba prywatna, która chce prostego narzędzia do kontroli wydatków i oszczędzania

## Główne scenariusze użycia
- szybkie dodanie wydatku zaraz po zakupie
- zrobienie zdjęcia paragonu albo dodanie screena potwierdzenia płatności
- automatyczne odczytanie kwoty, daty, sklepu i sugerowanej kategorii
- zapisanie transakcji i automatyczne pomniejszenie budżetu w odpowiedniej kategorii
- sprawdzenie, ile pieniędzy poszło w danym miesiącu na konkretne kategorie
- porównanie wydatków pomiędzy okresami
- sprawdzenie, ile udało się odłożyć
- zauważenie kategorii, które najbardziej obciążają budżet

## Najważniejsze ścieżki użytkownika
- użytkownik otwiera aplikację i w kilka sekund dodaje wydatek ręcznie
- użytkownik robi zdjęcie paragonu albo wrzuca screena, aplikacja odczytuje dane, proponuje kategorię, użytkownik potwierdza i zapisuje wpis
- po zapisaniu aplikacja od razu aktualizuje budżet kategorii i pokazuje wpływ na bieżący miesiąc
- użytkownik wchodzi na dashboard i widzi stan miesiąca: wydatki, przychody, bilans i oszczędności
- użytkownik otwiera analizy i sprawdza wykresy oraz kategorie z największym udziałem w kosztach
- użytkownik przegląda historię transakcji i poprawia błędnie przypisaną kategorię

## Docelowy codzienny flow
1. Użytkownik zbiera w ciągu dnia paragony albo screeny wydatków.
2. Wieczorem albo od razu po zakupie wrzuca zdjęcie lub screen do aplikacji.
3. Aplikacja wykrywa podstawowe dane:
   - kwotę,
   - datę,
   - nazwę sklepu lub źródła wydatku,
   - sugerowaną kategorię.
4. Użytkownik szybko potwierdza albo poprawia dane.
5. Po zapisie:
   - transakcja trafia do historii,
   - odpowiedni budżet zostaje pomniejszony,
   - dashboard i wykresy od razu się aktualizują.
6. Użytkownik może potem sprawdzić:
   - ile wydał,
   - na co wydał,
   - w których kategoriach przekracza plan,
   - ile może jeszcze odłożyć w tym miesiącu.

## Problemy i ryzyka po stronie użytkownika
- użytkownik nie będzie regularnie wpisywał danych, jeśli proces będzie zbyt długi
- OCR może błędnie odczytywać paragony, więc potrzebna jest korekta przed zapisem
- screeny z różnych aplikacji płatniczych mogą mieć różny układ, więc parser musi być odporny na różne formaty
- zbyt skomplikowane wykresy lub metryki obniżą użyteczność
- jeśli aplikacja nie będzie szybka na telefonie, codzienne korzystanie spadnie
- użytkownik musi mieć poczucie bezpieczeństwa danych finansowych
