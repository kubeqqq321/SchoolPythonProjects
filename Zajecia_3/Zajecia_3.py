# lista

lista = [1,2,3,4,5,6,7,8]

print(len(lista)) # wyświetla długość listy
print(lista+lista)
#print(lista*lista) wrong!!!
print(lista * 2)

lista2 = lista +lista
print(lista2)

if 5 in lista:
    print('jest')


for item in lista:
    print(item)

print(lista[4])

print(lista.index(5))



# lista = [1,2,3,4,5,6,7,8,3,4,5,2,2]

# print(lista.count(2))
# 
# lista.remove(7)
# print(lista)

# lista.append(13)
# print(lista)

# lista.extend([16,21])
# lista2 = [16,21]
# lista.extend(lista2)
# print(lista)

# print(lista.pop())
# print(lista)


# zadanie tworzymy liste posiadająca co 2 element listy wyjsciowej
# lista = [1,2,3,4,5,6,7,8,3,4,5,2,2]
#
# for i in lista[0::2]:
#     print(i)

# zadanie 2
# lista = [1,2,3,4,5,6,7,8,3,4,5,2,2]
# print(lista[-3])

#zadanie 3
# lista x- elementowa liczb pseudolosowych z pewnego przedziału [a,b]
import random

# lista = []
# for zmienna in range(1,100):
#     lista.append(random.randint(0, 10))
# print(lista)

# zadanie 4 czym są polindromy

# lista = [1, 2, 3, 4, 5]
# lista2 = [5, 4, 3, 2, 1]
#
# lista.reverse()
# print(lista)
#
# # lista = [1, 2, 3, 4, 5]
# # lista2 = lista
# #
# # lista2.reverse()
# # print(lista2)
#
#
# # for i in a[0:] and b[:-1]:
# #     print(i)
#
# # cos = set(a) & set(b)
# # print(cos)
# #
# # print(list(set(a).intersection(set(b))))
#
# # def isPalindrome(x, y):
# #     if len(x) == len(y):
# #         palindrome = True
# #         for i in range(0, len(x)):
# #             if (x[i] != y[len(y) - i - 1]):
# #                 palindrome = False
# #     return palindrome
#
# def palindrome(arr1, arr2):
#    return arr1 == arr2[::-1]
#
# print(palindrome(lista,lista2))

# Zadanie 5 sortowanie elemengtów w liscie

# lista  = [2,4,1,2,6]
# # lista.sort()
# print(lista)
#
# lista2 = sorted(lista)
# print(lista2)

# zadanie 6 Zrobione samemu


def anagrams(string1 , string2):
    if len(string1) != len(string2):
        print("nie sa")
    else:
        sortst1 = sorted(string1) 
        sortst2 = sorted(string2)
        if sortst1 == sortst2:
            print("sa to anagramy")
        else:
            print("nie sa")
    print(string1)

anagrams("jak" , "ka")

# def fun(arr1, arr2):
#     return sorted(arr1) == sorted(arr2)
#
# print(fun("jaki", "kaij"))

# def test(slowo,slowo2):
#     sslowo = sorted(slowo)
#     sslowo2 = sorted(slowo2)
#     if(sslowo == sslow'o2):
#         return True
#     else:
#         return False

# def anagramy(s1,s2):
#     if(sorted(s1)==sorted(s2)):
#         print("anagramy")
#     else:
#         print("no chyba nie")
#
#
# anagramy("jaki", "ikaj")



# zadanie 7 obietosc walca
# import math

# def obWalca(promien ,wysokosc):
#     walec = math.pi *pow(promien,2) * wysokosc
#     print("obietosc walca =",walec)

# obWalca(5,6)
# a=7
# b =4
# obWalca(a,b)

# import modulek   # korzystamy z całej zawarosci

# print(modulek.dodaj(1,2))
# print(modulek.odejmij(1,2))
# print(modulek.mnozenie(1,2))
# print(modulek.dzielenie(1,2))
# print(modulek.modulo(1,2))

# from modulek import odejmij
# print(odejmij(1,2))

# array

# import numpy as np

# a = np.array([2,3,1,6,3]) # rzad
# print(a)

# b = np.array([[3],[6],[8],[1]]) #kolumna
# print(b)

# print(a.ndim)
# print(b.ndim)

# print(a.shape)
# print(b.shape)

# c = np.array([[1, 2, 3], [4, 5, 6]])
# print(c)
# print(c.ndim)
# print(c.shape)