from kod_uzytkownika import funkcja

komunikat = "Coś poszło nie tak..."

def sukces():
    global komunikat
    komunikat += "\n Sukces"
    return True

def porazka():
    global komunikat
    komunikat += "\n Porażka"
    return False

def weryfikator():
    global komunikat
    kod_uzytkownika = funkcja()
    WYNIK = "Hello World"
    komunikat = "kod użytkownika: \"" + funkcja() + "\", oczekawana wartość: \"" + WYNIK + "\""
    try:
            if kod_uzytkownika == WYNIK:
                sukces()
            else:
                porazka()
    except:
        return False

def print_komunikat():
    print(komunikat)

weryfikator()
print_komunikat()