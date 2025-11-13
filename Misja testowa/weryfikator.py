import Kod_uzytkownika

def sukces():
    print("Sukces")

def porazka():
    print("Porazka")

def weryfikator():
    kod_uzytkownika = Kod_uzytkownika.kod_uzytkownika()
    if kod_uzytkownika == "Hello World":
        sukces()
    else:
        porazka()

weryfikator()