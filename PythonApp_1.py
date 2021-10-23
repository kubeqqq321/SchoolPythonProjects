# pierwsze zajęcia
#
# print("Witaj szkolo")
# print(1234, "1234")
#
# a = 3.5
# b = 3
# print(a)
# print(a*3)
# print(a//2) # // obciete do całkowitych wartośći
# print(type(a),a)
# print(b)
#
#
#
# a = 'hello'
# print(a)
# print(type(a) ,a)
#
# print(a+a)
# print(a*3)
#
#
# print(round(12.1278) ,2 )
# print("10/5 = {0:.3f}".format(10/5))
#
#
# print("Jan\nKowalski")
#
# print("imie" , "nazwisko")
# print("{0:10} {1:10}".format("imie" , "nazwisko"))
#
# #print("dzien" , "miesiac" , "rok")
# #print("{0:2} {1:2} {2:2}".format("dzien" , "miesiac" , "rok"))
#
# day = 13
# month = 10
# year = 2021
#
# print("{0}/{1}/{2}".format(day,month,year))
#
# print(4>2)
#
# a = 3.5
# print(a,int(a))
#
#
# znaki = "abecadlo"
# print(znaki[3:])
# print(znaki[:4])  #[start:stop:krok]
# print(znaki[-1:]) #odliczanie od końca
#
# we = input("Enter your name: ")
# print(we)
#
# liczba = input("Enter a number: ")
# print(liczba, type(liczba))
# liczba = int(liczba)
# print(liczba, type(liczba))
#
#
# if 3>4:
#     print("tak")
# else:
#     print("nie")

# import math
#
# def Delta_calc(a,b,c):
#
#     delta = (b * b) - (4 * a * c)
#     print("Delta = " + str(round(delta, 2)))
#
#     if delta > 0:
#         x1 = (-1 * b - math.sqrt(delta)) / (2 * a)
#         x2 = (-1 * b + math.sqrt(delta)) / (2 * a)
#         print("x1 = " + str(round(x1, 2)))
#         print("x2 = " + str(round(x2, 2)))
#     elif delta == 0:
#         x0 = (-1 * b) / (2 * a)
#         print("x0 = " + str(round(x0, 2)))
#     else:
#         print("Brak pierwiastkow")
#
#
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))
#
# Delta_calc(a, b, c)

# for i in range(5):
#     print(i)
#
# print("------------------")
#
# for i in range(5,11):
#     print(i)
#
# print("------------------")
#
# for i in range(20,10 , -1):
#     print(i)
#
# print("------------------")
#
# for i in ('a' ,'b' ,'c'):
#     print(i)

print("------------------")

#liczby naturalne podzielne przez pewna wartość (zrobione)

# min = int(input("Enter min:"))
# max = int(input("Enter max:"))
#
# wartosc = int(input("Podaj liczbe przez ktora beda dzielone licizby z podanego zakresu: "))
#
# for i in range(min, max + 1):
#     if (i % wartosc) == 0:
#         print(i)

print("------------------")

#ciąg fibonnaciego (uzytkownik wpisuje numer ciagu który chce zobaczyć)

# n_ciagu = int(input("Podaj numer ciagu który chcesz zobaczyc: "))
# print("numer ciagu = " + str(n_ciagu))
#
# poprzedni , nastepny = 0,1
# if n_ciagu == 0: print("Wartosc iteracyjnie: " + str(n_ciagu))
# elif n_ciagu == 1: print("Wartosc iteracyjnie: " + str(n_ciagu))
# elif n_ciagu > 1:
#     for i in range(n_ciagu-1):
#         poprzedni , nastepny = nastepny , poprzedni+nastepny
#     print("Wartosc iteracyjnie: " + str(nastepny))
#
#
# #obliczanie ciagu fibonacciego za pomoca iteracji
#
# def fib(n_ciagu):
#     if n_ciagu == 0: return 0
#     elif n_ciagu == 1: return 1
#     elif n_ciagu > 1: return (fib(n_ciagu-1) + fib(n_ciagu-2))
#
# print("Wartosc rekurencyjnie = "+ str(fib(n_ciagu)))
#


print("------------------")

#Obliczanie silnii (zrobione)
# an = int(input("Podaj wartosc do silnii: "))
# a0 = 1
# if an >= 1:
#     silnia = 1
#     for i in range(a0, an+1):
#         #silnia = silnia * i
#         silnia *=i
#     print("silnia = " + str(silnia))
# elif an == 0:
#     print("Silnia = " + str(a0))
#




















