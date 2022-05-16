from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectMultipleField, RadioField, FieldList
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    book_title =  StringField("Tytuł", validators=[DataRequired()])
    book_author = StringField("Autor", validators=[DataRequired()])
    book_year = IntegerField("Rok wydania", validators=[DataRequired()])
    book_publishing_house = RadioField("Wydawnictwo", choices= sorted(("Rebis", "Filia", "Marginesy", "Zielona Sowa", "MUZA S.A.", "Helion", "Naukowe PWN", "Albatros", "C.H. Beck",
    "Czarna Owca", "Świat Książki", "Inne")))
    book_number_of_pages = IntegerField("Ilość stron", validators=[DataRequired()])
    book_category = SelectMultipleField("Kategoria", choices= sorted(("biografia","biznes", "ekonomia", "marketing","dla dzieci", "dla młodzieży","fantastyka",
    "science fiction", "horror", "historia","informatyka","komiks","kryminał, sensacja, thriller","książka regionalna","kuchnia i diety","lektury, pomoce szkolne",
    "literatura faktu, reportaż","literatura obyczajowa","literatura piękna obca","literatura piękna polska","nauka języków","nauki społeczne i humanistyczne",
    "nauki ścisłe, medycyna","obcojęzyczne","podręczniki akademickie","podręczniki szkolne, edukacja","poezja, aforyzm, dramat","poradniki","prawo",
    "religie i wyznania","rozwój osobisty","sport i wypoczynek","sztuka","turystyka i podróże","zdrowie, rodzina, związki", "Inne")))
    book_description = TextAreaField("Opis", validators=[DataRequired()])
    book_id = IntegerField("Nr id", validators=[DataRequired()])
