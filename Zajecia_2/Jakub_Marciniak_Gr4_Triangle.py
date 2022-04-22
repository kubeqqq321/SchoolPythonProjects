import numpy as np
import matplotlib.pyplot as plt

# Jakub Marciniak Gr4
# Trojkat

    # wzór na pole trójkąta w układzie współrzędnych
def poleTrojkata(xa, ya, xb, yb, xc, yc):
    return 1 / 2 * abs((xb - xa) * (yc - ya) - (yb - ya) * (xc - xa))


def czyWewnatrz(xa, ya, xb, yb, xc, yc, Px, Py):
    # obliczamy pole naszego trójkata
    pole = poleTrojkata(xa, ya, xb, yb, xc, yc)

    # dzielimy trójkąt na 3 mniejsze trójkąty gdzie dajemy nasz punkt
    # jako jeden z wierzchołków każdego trójkata
    pole1 = poleTrojkata(xa, ya, xb, yb, Px, Py)
    pole2 = poleTrojkata(xa, ya, Px, Py, xc, yc)
    pole3 = poleTrojkata(Px, Py, xb, yb, xc, yc)

    #jeżeli pole całego trójkąta jest równe 3 polą pozostałych trójkątów
    # to punkt lezy wewnatrz trójkąt głównego
    if pole == pole1 + pole2 + pole3: print("punkt lezy wewnatrz trojkata")
    else: print("Punkt lezy na zewnatrz trojkata")


try:
    print("Podaj wspolrzedna A")
    xA = float(input("Ax ="))
    yA = float(input("Ay ="))

    print("Podaj wspolrzedna B")
    xB = float(input("Bx ="))
    yB = float(input("By ="))

    print("Podaj wspolrzedna C")
    xC = float(input("Cx ="))
    yC = float(input("Cy ="))

    print("Podaj wspolrzedne punktu P")
    xP = float(input("Px ="))
    yP = float(input("Py ="))

    #Szybkie sprawdzenie czy działa, i działa :)
    #xA, yA, xB, yB, xC, yC, xP, yP = 1, 1, 3, 4, 6, 1, 3, 3 #punkt lezy wewnatrz
    #xA, yA, xB, yB, xC, yC, xP, yP = 1, 1, 3, 4, 6, 1, 3, 5 #punkt lezy na zewnatrz

    #xA, yA, xB, yB, xC, yC, xP, yP = -2, -1, 0, 1, -2, 4, -1, 2 #punkt lezy wewnatrz
    #xA, yA, xB, yB, xC, yC, xP, yP = -2, -1, 0, 1, -2, 4, -1, 3 #punkt lezy na zewnatrz

    czyWewnatrz(xA, yA, xB, yB, xC, yC, xP, yP)# wywołanie funkcji

    '''Przedstawienie przy pomocy matplotlib'''
    X = np.array([xA,xB,xC,xA])
    Y = np.array([yA,yB,yC,yA])

    plt.plot(X,Y)      #linie trojkata
    plt.scatter(xP,yP) #punkt
    plt.grid()
    plt.show()
    '''--------------'''
except ValueError:
    print("Niestety podana wartosc nie jest liczba, prosze wprowadzaj tylko liczby!")




