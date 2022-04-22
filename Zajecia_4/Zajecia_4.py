
# import numpy as np

# a = np.arrange(10) #<0,10)
# a = np.arrange(1,9,2) # od 1 do 9 krok 2
# a = np.linspace(0,1,9)
# a = np.ones((3,3))
# a = np.zeros((2,2))
# a = np.eye(3)
# a = np.diag(np.array([1,2,3,4]))
# a = np.random.rand(4)
# a = np.random.random(3)
# a = np.random.randint(0,11,7)

# print(a)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x = np.linspace(0,3,20)
# y = np.linspace(0,4,20)
# plt.plot(x,y ,'o')
# plt.show()


# xy = np.random.rand(20,20)
# # print(xy)
# plt.imshow(xy, cmap=plt.cm.hot)
# plt.colorbar()
# plt.show()

# ax = plt.axes(projection='3d')
# ax.scatter(2,3,4)
# plt.show()



# slicing dla tablic (np wybor 3 kolumny, 2 wiersza , z 1 wiersza elementu od 2 do 5)






#
# # a) element środkowy
# a = np.random.rand(5,5)
# print(a)
# print(a[2,2])
#
# # b) wiersz drugi
# arr = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10]])
# print(arr[1, 0:])
#
# # c) ostatnia kolumna
# arr = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10]])
# print(arr[0:,-1]) # index tablicy 0 = 1,2,3,4,5 a 1  = 6,7,8,9,10
#                     # wtedy arr[0:] są to 2 tablice wierszowe i nasze -1 bierze ostatnia
#                     # z oby dwu tablic

# pliki
# plik = open("dane.txt" , "r")
#
# for linia in plik:
#     print(linia)
#
# plik.close()
#
# plik2 = open("b.txt", "a")
# # plik2.write("ola ma parasol")
# plik2.close()


# while plik2:
#     a = input("podaj kilka napisow: ")
#     if a == '1':
#         plik2.write(a)
#         print(end="\n")
#         break

# plik = open("dane.txt" , "r+")
#
# while plik:
#     a = str(input("podaj napis: "))
#     plik.write(a)
#     if a == '1':
#         plik.close()
#


    



# a = input("podaj kilka napisow: ")
# plik2.write(a , end="\n",)



# bez kporzystania z plik.close()
# with open('dane.txt', 'a') as f:
#     f.write("I love\nPython")
# 
# with open('dane.txt', 'r') as f:
#     for line in f:
#         print(line)



import numpy as np
import matplotlib.pyplot as plt
# Though the following import is not directly being used, it is required
# for 3D projection to work
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(5)

centers = [[1, 1], [-1, -1], [1, -1]]
iris = datasets.load_iris()
X = iris.data
y = iris.target

estimators = [('k_means_iris_8', KMeans(n_clusters=8)),
              ('k_means_iris_3', KMeans(n_clusters=3)),
              ('k_means_iris_bad_init', KMeans(n_clusters=3, n_init=1, init='random'))]

fignum = 1
titles = ['8 clusters', '3 clusters', '3 clusters, bad initialization']

for name, est in estimators:
    fig = plt.figure(fignum, figsize=(4, 3))
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
    est.fit(X)
    labels = est.labels_

    ax.scatter(X[:, 3], X[:, 0], X[:, 2],  c=labels.astype(np.float), edgecolor='k')

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('Petal width')
    ax.set_ylabel('Sepal length')
    ax.set_zlabel('Petal length')
    ax.set_title(titles[fignum - 1])
    ax.dist = 12
    fignum = fignum + 1

# Plot the ground truth
fig = plt.figure(fignum, figsize=(4, 3))
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

for name, label in [('Setosa', 0),
                    ('Versicolor', 1),
                    ('Virginica', 2)]:
    ax.text3D(X[y == label, 3].mean(),
              X[y == label, 0].mean(),
              X[y == label, 2].mean() + 2, name,
              horizontalalignment='center',
              bbox=dict(alpha=.2, edgecolor='w', facecolor='w'))

# Reorder the labels to have colors matching the cluster results
y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=y, edgecolor='k')

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('Petal width')
ax.set_ylabel('Sepal length')
ax.set_zlabel('Petal length')
ax.set_title('Ground Truth')
ax.dist = 12

plt.show()


#
#
#
#
#
#
#


# coding: utf-8

# Implémentation de K-means clustering python
# Code produit par le site https://mrmint.fr

# Chargement des bibliothèques
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# from sklearn import datasets
#
#
# #chargement de jeu des données Iris
# iris = datasets.load_iris()
#
# #importer le jeu de données Iris dataset à l'aide du module pandas
# x = pd.DataFrame(iris.data)
#
# x.columns = ['Sepal_Length','Sepal_width','Petal_Length','Petal_width']
#
#
# y = pd.DataFrame(iris.target)
#
#
# y.columns = ['Targets']
#
#
# #Création d'un objet K-Means avec un regroupement en 3 clusters (groupes)
# model=KMeans(n_clusters=3)
#
#
#
# #application du modèle sur notre jeu de données Iris
# model.fit(x)
#
#
#
# #Visualisation des clusters
# plt.scatter(x.Petal_Length, x.Petal_width)
# plt.show()
#
#
#
#
# colormap=np.array(['Red','green','blue'])
#
#
#
# #Visualisation du jeu de données sans altération de ce dernier (affichage des fleurs selon leur étiquettes)
# plt.scatter(x.Petal_Length, x.Petal_width,c=colormap[y.Targets],s=40)
# plt.title('Classification réelle')
# plt.show()
#
# #Visualisation des clusters formés par K-Means
# plt.scatter(x.Petal_Length, x.Petal_width,c=colormap[model.labels_],s=40)
# plt.title('Classification K-means ')
# plt.show()

