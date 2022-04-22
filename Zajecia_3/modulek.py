#nasz modul

def dodaj(liczba1 , liczba2):
    return liczba1 + liczba2

def odejmij(liczba1,liczba2):
    return liczba1 - liczba2

def mnozenie(liczba1 , liczba2):
    return liczba1*liczba2

def dzielenie(liczba1,liczba2):
    if liczba2 == 0:
        print("Dzielenie przez zero")
    else:
        return liczba1/liczba2

def modulo(liczba1, liczba2):
    return liczba1 % liczba2