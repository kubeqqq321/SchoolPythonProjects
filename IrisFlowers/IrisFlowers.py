import pandas as pd #Pandas to biblioteka Pythona używana do pracy z zestawami danych.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.cluster import KMeans


try:
    # wczytujemy dane z pliku IRIS.csv przy użyciu pandas
    iris = datasets.load_iris()
    data = iris.data
    y = iris.target

    #bierzemy odpowiednio wartosci za pomoca iloc[] podajac kolumny w ktorych mamy nasze potrezbne dane
    #data= iris.iloc[:, [0, 1, 2, 3]].values

    #iris.head()
    sns.set_style("whitegrid")
    iris_setosa = iris.loc[iris["species"] == "Iris-setosa"]
    iris_virginica = iris.loc[iris["species"] == "Iris-virginica"]
    iris_versicolor = iris.loc[iris["species"] == "Iris-versicolor"]

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(data)

    # Visualising the clusters
    plt.scatter(data[y_kmeans == 0, 0], data[y_kmeans == 0, 1], s=100, c='purple', label='Iris-setosa')
    plt.scatter(data[y_kmeans == 1, 0], data[y_kmeans == 1, 1], s=100, c='orange', label='Iris-versicolour')
    plt.scatter(data[y_kmeans == 2, 0], data[y_kmeans == 2, 1], s=100, c='green', label='Iris-virginica')

    # Plotting the centroids of the clusters
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='red', label='Centroids')
    plt.legend()

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(data)

    # Visualising the clusters
    # plt.scatter(data[y_kmeans == 0, 0], data[y_kmeans == 0, 1], s=100, c='red', label='Iris-setosa')
    # plt.scatter(data[y_kmeans == 1, 0], data[y_kmeans == 1, 1], s=100, c='blue', label='Iris-versicolour')
    # plt.scatter(data[y_kmeans == 2, 0], data[y_kmeans == 2, 1], s=100, c='green', label='Iris-virginica')
    #
    # # Plotting the centroids of the clusters
    # plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='yellow', label='Centroids')
    # plt.legend()

    #Plotting the centroids of the clusters
    # plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c ='red', label = 'Centroids')
    #
    # plt.legend()


    # 3d scatterplot using matplotlib

    # plt3d = plt.figure(figsize = (15, 15))
    # ax = plt3d.add_subplot(111, projection='3d', label ="Iris-3d")
    # ax.set_xlabel("Petal width", size = 30)
    # ax.set_ylabel("Sepal length", size = 30)
    # ax.set_zlabel("Petal length", size = 30)
    #
    # # 3d scatterplot using matplotlib

    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111, projection='3d',label ="Iris-3d")
    plt.scatter(data[y_kmeans == 0, 0], data[y_kmeans == 0, 1], s=100, c='purple', label='Iris-setosa')
    plt.scatter(data[y_kmeans == 1, 0], data[y_kmeans == 1, 1], s=100, c='orange', label='Iris-versicolour')
    plt.scatter(data[y_kmeans == 2, 0], data[y_kmeans == 2, 1], s=100, c='green', label='Iris-virginica')

    #Plotting the centroids of the clusters
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 250, c = 'red', label = 'Centroids')
    #plt.show()


    # sns.FacetGrid(irisFlowers, hue="species", size=3).map(sns.distplot, "petal_length").add_legend()
    # sns.FacetGrid(irisFlowers, hue="species", size=3).map(sns.distplot, "petal_width").add_legend()
    # sns.FacetGrid(irisFlowers, hue="species", size=3).map(sns.distplot, "sepal_length").add_legend()
    plt.show()


except FileNotFoundError:
    print("Nie znaleziono pliku!")

#
#
#
#
#
#
#
# # from mpl_toolkits.mplot3d import Axes3D
# #
# # from sklearn.cluster import KMeans
# # from sklearn import datasets
# #
# # np.random.seed(5)
# #
# # iris = datasets.load_iris()
# # X = iris.data
# # y = iris.target
# #
# # estimators = [
# #     #("k_means_iris_8", KMeans(n_clusters=8)),
# #     #("k_means_iris_3", KMeans(n_clusters=3)),
# #     #("k_means_iris_bad_init", KMeans(n_clusters=3, n_init=1, init="random")),
# # ]
# #
# # fignum = 1
# # titles = ["8 clusters", "3 clusters", "3 clusters, bad initialization"]
# # for name, est in estimators:
# #     fig = plt.figure(fignum, figsize=(4, 3))
# #     ax = Axes3D(fig, rect=[0, 0, 0.95, 1], elev=48, azim=134)
# #     est.fit(X)
# #     labels = est.labels_
# #
# #     ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=labels.astype(float), edgecolor="k")
# #
# #     ax.w_xaxis.set_ticklabels([])
# #     ax.w_yaxis.set_ticklabels([])
# #     ax.w_zaxis.set_ticklabels([])
# #     ax.set_xlabel("Petal width")
# #     ax.set_ylabel("Sepal length")
# #     ax.set_zlabel("Petal length")
# #     ax.set_title(titles[fignum - 1])
# #     ax.dist = 12
# #     fignum = fignum + 1
# #
# # # Plot the ground truth
# # fig = plt.figure(fignum, figsize=(4, 3))
# # ax = Axes3D(fig, rect=[0, 0, 0.95, 1], elev=48, azim=134)
# #
# # for name, label in [("Setosa", 0), ("Versicolour", 1), ("Virginica", 2)]:
# #     ax.text3D(
# #         X[y == label, 3].mean(),
# #         X[y == label, 0].mean(),
# #         X[y == label, 2].mean() + 2,
# #         name,
# #         horizontalalignment="center",
# #         bbox=dict(alpha=0.2, edgecolor="w", facecolor="w"),
# #     )
# # # Reorder the labels to have colors matching the cluster results
# # y = np.choose(y, [1, 2, 0]).astype(float)
# # ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=y, edgecolor="k")
# #
# # ax.w_xaxis.set_ticklabels([])
# # ax.w_yaxis.set_ticklabels([])
# # ax.w_zaxis.set_ticklabels([])
# # ax.set_xlabel("Petal width")
# # ax.set_ylabel("Sepal length")
# # ax.set_zlabel("Petal length")
# # ax.set_title("Ground Truth")
# # ax.dist = 12
# #
# # fig.show()

        
