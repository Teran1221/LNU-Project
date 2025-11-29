from math import sqrt
from random import randint
from dystans import dystans as funkcja

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
    x1 = randint(0,10)
    x2 = randint(0,10)
    y1 = randint(0,10)
    y2 = randint(0,10)
    print(str(x1) + str(x2) + str(y1) + str(y2))
    WYNIK = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    kod_uzytkownika = funkcja(x1,x2,y1,y2)
    komunikat = "Twój dystans różni się od prawidłowego o: " + f"{abs(WYNIK - kod_uzytkownika):.4f}".rstrip('0').rstrip('.')
    try:
            if abs(kod_uzytkownika - WYNIK) <=0.01:
                sukces()
            else:
                porazka()
    except:
        return False

def print_komunikat():
    print(komunikat)

weryfikator()
print_komunikat()