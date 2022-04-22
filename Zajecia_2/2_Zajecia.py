# 2 zajecia

'''pobrać liczby jeśli 0 koniec'''
'''Zrobione'''

# lista = []
#
# while True:
#     liczba = int(input("Podaj liczbe: "))
#     if liczba != 0:
#         lista.append(liczba)
#         print(lista)
#     else:
#         break
#
# print(lista)
#

'''Zrobione'''
'''znalezć najwiekszy wspólny dzilenik   NWD'''

# liczba1=int(input('podaj pierwszą liczbę: '))
# liczba2=int(input('podaj drugą liczbę: '))
# licznik=0
# #  początek pętli
#
# while liczba1!=liczba2:
#     if liczba1>liczba2:
#         liczba1=liczba1-liczba2
#     else:
#         liczba2=liczba2-liczba1
#
# print("NWD to:", liczba1)
#

'''Zrobione'''
'''jak najlpeze przyblizenie liczby pi'''

# def oblicz_pi():
#     pi = 1
#     N = int(input("Podaj stop: "))
#     for i in range(1, N):
#         pi *= (4 * i * i) / (4 * i * i - 1)
#     pi = pi * 2
#     print(pi)
#
# oblicz_pi()


# def oblicz_pi(N):
#     pi = 1
#     #N = int(input("Podaj stop"))
#     for i in range(1, N):
#         pi *= (4 * i * i) / (4 * i * i - 1)
#     #pi = pi * 2
#     print(pi)
#
# oblicz_pi(12)
#
# def oblicz_pi(N):
#     pi = 1
#     #N = int(input("Podaj stop"))
#     for i in range(1, N):
#         pi *= (4 * i * i) / (4 *i * i - 1)
#     pi = pi * 2
#     return pi
#
# print(oblicz_pi(12))
#
#
# def oblicz_pi(N =100):
#     pi = 1
#     #N = int(input("Podaj stop"))
#     for i in range(1, N):
#         pi *= (4 * i * i) / (4 *i * i - 1)
#     pi = pi * 2
#     return pi
#
# print(oblicz_pi())
#
#
#
# NN= 10
# def oblicz_pi(N =NN):
#     pi = 1
#     #N = int(input("Podaj stop"))
#     for i in range(1, N):
#         pi *= (4 * i * i) / (4 *i * i - 1)
#     pi = pi * 2
#     return pi
#
# NN = int(input("podaj stopped"))
# print(oblicz_pi())
# print(oblicz_pi(NN))
#



'''NWW najwiekszy wspolna wielokrtonosci'''
'''Zrobione'''

# def NWD(liczba1, liczba2):
#     while liczba1 != liczba2:
#         if liczba1 > liczba2:
#             liczba1 = liczba1 - liczba2
#         else:
#             liczba2 = liczba2 - liczba1
#     return liczba1
#     # print("NWD to:", liczba1)
#
#
# def NWW(liczba1, liczba2):
#     nww = (liczba1 * liczba2) / NWD(liczba1, liczba2)
#     # print("NWW " , nww)
#     return int(nww)
#
#
# liczba1 = int(input('podaj pierwszą liczbę: '))
# liczba2 = int(input('podaj drugą liczbę: '))
#
# print("NWD(" + str(liczba1) + ", " + str(liczba2) + ") ", NWD(liczba1, liczba2))
# print("NWW(" + str(liczba1) + ", " + str(liczba2) + ") ", NWW(liczba1, liczba2))


'''silnia rekurencyjnie'''
'''Zrobione'''

# def silnia(n):
#     if n> 1:
#         return n*silnia(n-1)
#     elif n == 0 or 1:
#         return 1

'''potęgowanie rekurencyjnie'''
'''Zrobione'''

# def potegowanie(liczba , potega):
#     if potega == 0:
#         return liczba
#     elif potega < 0:
#         return 1/(potegowanie(liczba,-potega-1)*liczba)
#     else:
#         return potegowanie(liczba, potega - 1) * liczba
#
# numer = int(input("Podaj liczbe: "))
# potega = int(input("Podaj potege: "))
#
# print("silnia rekurencyjnie: " , silnia(numer))
# print("Potegowanie: " + str(potegowanie(numer , potega)))


'''Pusty prostokat'''
'''Zrobione'''

# def prostokat (fdlugosc, fwysokosc, fznak ):
#     for j in range(fwysokosc):
#         for i in range(fdlugosc):
#             if (i > 0 and i < fdlugosc - 1) and (j > 0 and j < wysokosc - 1):
#                 print(" ", "", end='')
#             else:
#                 print(fznak, "", end='')
#         print('')
#
#
# dlugosc = int(input("Podaj dlugosci: "))
# wysokosc = int(input("Podaj wyskokosc: "))
# znak = str(input("podaj znak: "))
#
# prostokat(dlugosc , wysokosc , znak)

'''funckcja czy puunkt lezy wewnatrz trójkata
    imie nazwysko grupa
    do jutra do 24'''
'''Zrobione w innym projekcie'''


