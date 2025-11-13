from kod_uzytkownika import funkcja

def sukces():
    print("Sukces")

def porazka():
    print("Porazka")

def weryfikator():
    kod_uzytkownika = funkcja()
    if kod_uzytkownika == "Hello World":
        sukces()
    else:
        porazka()

weryfikator()