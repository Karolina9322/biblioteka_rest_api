Aplikacja stworzona w oparciu o FLASK i formularze WTF-FORMS
Aplikacja przechowuje listę książek wraz z ich danymi: tytuł, autor, rok wydania, liczba stron, wydawnictwo, kategoria, nr id, opis.
Użytkownik może wyświetlić listę książek, edytować zapisane pozycje oraz dodawać nowe. 

Na aplikację składają się:

app.py - importuje z models.py i forms.py, wyświetla listę książek, opcję utworzenia nowej pozycji oraz edycji już istniejących przy pomocy formularzy z books.html i book.html

forms.py -> zaimportowane z wtfforms formularze dla każdej pozycji: tytuł, autor itd. W przypadku  pola "Wydawnictwo" korzystamy z gotowej listy RadioFIeld z opcją wyboru jednej           pozycji. W przypadku pola "Katogoria" użytkownik może wybrać wiele pozycji(SelectMultipleField).

models.py -> plik zawierający metody określające sposób zapisu zmian: zapis nowej pozycji, edycja pozycji, wyświetlanie pozycji o danym id.

books.html, book.html -> szablony aplikacji

book.json -> dane(lista książek) zapisane w formacie json

RESTowe API: 
api.py -> importuje metody z modelsapi.py, zwraca dane w formacie json, obsługuje zapytania typu GET, POST, DELETE, PATCH

modelsapi.py -> plik zawierający metody określające sposób obsługi zapytań API: pobranie listy, zapis nowej pozycji, edycja pozycji, wyświetlanie pozycji o danym id, usunięcie pozycji. 

