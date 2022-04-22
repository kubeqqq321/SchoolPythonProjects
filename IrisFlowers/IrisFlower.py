import pandas as pd #Pandas to biblioteka Pythona używana do pracy z zestawami danych.
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

try:
    # wczytujemy sobie dane z naszego pliku tekstowego (najlepiej jak plik byłby z nazwanymi kolumnami odpowiednio
    # sepal_length, sepal_width, petal_length, petal_width, species gdy kolumny będą nie nazwane niestety ale nie działa )
    iris = pd.read_csv("IRIS2.csv")

    # Ustawiamy odpowiednio nasze wartości sepal_length, sepal_width, petal_length, petal_width, na których będziemy pracowac
    data = iris.values[:, (0, 1, 2, 3)]

    # przypisanie warości liczbowych do konkretnej klasy
    iris['class-num'] = iris['species'].map({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})


    # Dwuwymiarowa tablica z danymi wejściowymi(x)
    # Tablica jednowymiarowa z wyjściami(y)

    # train_test_split używamy aby podzielić dane na dwie części jedną
    # train - która służy do trenowania modelu
    # test - służy do sprawdzania jak nasz model działa na dane
    # Przekazując 0.25 jako parametr w train_test_split, który podzieli dane, tak że
    # 25% danych będzie w częsci testowej a pozostałe w części 75% będzie w częsci train
    X_train, X_test, y_train, y_test = train_test_split(data, iris['class-num'] , test_size=0.1)

    # służy do przewidywania modelu klasyfikacji i trenowania go na na danych train
    classifier_tree = DecisionTreeClassifier()
    #przewidywanie wyjścia danych testowych
    y_predict = classifier_tree.fit(X_train, y_train).predict(X_test)



    # Implementacja naszego algorytmu kmeans
    kmeans = KMeans(n_clusters = 3)
    # wyswietla true gdy wykryje odpowiednia klase która sie poda y_kmeans == 0
    # znajdzie Iris-setosa i wypisze go jako true
    # Oblicz centra klastrów i prognozuj indeks klastrów dla każdej próbki.
    y_kmeans = kmeans.fit_predict(data)

    target_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    # classification_report - dla 100% zbioru
    # print(classification_report(iris['class-num'], kmeans.labels_, target_names=target_names))
    # classification_report - dla konkretnej test_size gdzie można ustalić konkretną liczebność zbioru
    print("classification_report:\n",classification_report(y_test, y_predict, target_names=target_names))
    print('confusion_matrix\n',confusion_matrix(y_test, y_predict))
    print('accuracy_score\n',accuracy_score(y_predict, y_test))
    print('y_means: \n',y_kmeans)
    print('pd.Categorical(iris["species"])\n ',pd.Categorical(iris["species"]))



    '''histogramy-----------------------------------------------------------------------------------------------------'''
    # wystrzałowe histogramy dla każdej z długości
    sns.histplot(data=iris, x="sepal_length",hue='species', bins=30)
    plt.show()
    sns.histplot(data=iris, x="petal_width",hue='species', bins=30)
    plt.show()
    sns.histplot(data=iris, x="petal_length",hue='species', bins=30)
    plt.show()
    '''histogramy-----------------------------------------------------------------------------------------------------'''


    '''2d----------------------------------------------------------------------------------------------------'''
    """bez kmeans - wizualizuje położenie, które powinny mieć punkty normalnie wczytane z pliku tektowego bądz csv"""
    # (zmieniając cyfry 1, 2, 3, 4 możęmy odpowienio manipulowac danymi które chcemy dostarczyc tak jak w tym przypadku
    #   będzie to sepal_length oraz sepal_width)
    plt.scatter(data[:,0], data[:,1], s=100, c=iris['class-num'], label='Iris-setosa')

    # kmeans.cluster_centers_[:, 0] -> pokazuje się tu centroid o odpowiednim srodku dla koolumny sepal_length
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='red', label='Centroids')
    plt.show()

    """z kmeans - wizualizuje położenie, które mają punkty odpowiednio po sklasteryzowaniu ich do odpowiednich grup"""
    plt.title('Iris Flower 2D')
    plt.xlabel('Sepal Length (cm)')# sepal_length
    plt.ylabel('Sepal Width (cm)') # sepal_width

    # y_kmeans - sprawdza wrtości class i jeżeli jest ona zapisana y_kmeans == 0 jest to wówczas class 'Iris-setosa'
    #            i jeżeli występuje ona w zbiorze y_kmeans zaznacza ją jako wartosc true i liczy dla niej odpowienia kolumne którą to mamy podaną po przecinku
    #            y_kmeans == 0, '0' jest to kolumna dla której chcemy pokazać zbiór i jest to 'sepal_length'
    # y_kmeans == 0 -> 'Iris-setosa'
    # y_kmeans == 1 -> 'Iris-versicolour'
    # y_kmeans == 2 -> 'Iris-virginica'
    plt.scatter(data[y_kmeans == 0, 0], data[y_kmeans == 0, 1], s=100, c='purple', label='Iris-setosa')
    plt.scatter(data[y_kmeans == 1, 0], data[y_kmeans == 1, 1], s=100, c='orange', label='Iris-versicolour')
    plt.scatter(data[y_kmeans == 2, 0], data[y_kmeans == 2, 1], s=100, c='green', label='Iris-virginica')

    # kmeans.cluster_centers_[:, 0] -> pokazuje się tu centroid o odpowiednim srodku dla koolumny sepal_length
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='red', label='Centroids')
    plt.legend()
    plt.show()
    '''2d----------------------------------------------------------------------------------------------------'''



    '''3d------------------------------------------------------------------------------------------------------'''
    """bez kmeans - wizualizuje położenie, które powinny mieć punkty normalnie wczytane z pliku tektowego bądz csv"""
    fig3d = plt.figure(figsize = (10, 10))
    ax = fig3d.add_subplot(111,projection='3d')

    # (zmieniając cyfry 1, 2, 3, 4 możęmy odpowienio manipulowac danymi które chcemy dostarczyc)
    # Wykres 3d
    ax.scatter(xs=data[:, 0],  # Sepal length (cm)
               ys=data[:, 2],  # Petal length (cm)
               zs=data[:, 1],  # Sepal width (cm)
               s=100,
               c=iris['class-num'],
               alpha=0.8) # przezroczystosc

    # kmeans.cluster_centers_[:, 0] -> pokazuje się tu centroid o odpowiednim srodku dla koolumny sepal_length
    ax.scatter(kmeans.cluster_centers_[:, 0],  #środek clastra Sepal length (cm)
               kmeans.cluster_centers_[:, 2],  #środek clastra Petal length (cm)
               kmeans.cluster_centers_[:, 1],  #środek clastra Sepal width (cm)
               s=100, c='red' # wielkosc oraz kolor
               , label='Centroids',alpha=1) # przezroczystosc

    # tworzymy legende oraz wyswietalmy nasz plt
    plt.legend(loc=2, prop={'size': 19})
    plt.show()


    """z kmeans - wizualizuje położenie, które mają punkty odpowiednio po sklasteryzowaniu ich do odpowiednich grup"""
    fig3d = plt.figure(figsize = (10, 10))
    ax = fig3d.add_subplot(111,projection='3d')
    plt.title('Iris Flower 3D' , size= 36)
    ax.set_xlabel("Sepal length (cm)", size = 18)
    ax.set_ylabel("Petal length (cm)", size = 18)
    ax.set_zlabel("Sepal width (cm)", size = 18)

    # Wykres 3d
    # y_kmeans - sprawdza wrtości class i jeżeli jest ona zapisana y_kmeans == 0 jest to wówczas class 'Iris-setosa'
    #            i jeżeli występuje ona w zbiorze y_means zaznacza ją jako wartosc tru i liczy dla niej odpowienia kolumne którą to mamy podaną po przecinku
    #            y_kmeans == 0, '0' jest to kolumna dla której chcemy pokazać zbiór i jest to 'sepal_length'
    # y_kmeans == 0 -> 'Iris-setosa'
    # y_kmeans == 1 -> 'Iris-versicolour'
    # y_kmeans == 2 -> 'Iris-virginica'
    ax.scatter(xs=data[y_kmeans == 0, 0], ys=data[y_kmeans == 0, 2],zs=data[y_kmeans == 0, 1], s=100, c='purple', label='Iris-setosa', alpha=0.8)
    ax.scatter(xs=data[y_kmeans == 1, 0], ys=data[y_kmeans == 1, 2],zs=data[y_kmeans == 1, 1], s=100, c='orange', label='Iris-versicolour',alpha=0.8)
    ax.scatter(xs=data[y_kmeans == 2, 0], ys=data[y_kmeans == 2, 2],zs=data[y_kmeans == 2, 1], s=100, c='green', label='Iris-virginica',alpha=0.8)

    # kmeans.cluster_centers_[:, 0] -> pokazuje się tu centroid o odpowiednim srodku dla koolumny sepal_length
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 2], kmeans.cluster_centers_[:, 1], s=100, c='red', label='Centroids',alpha=1)

    # tworzymy legende oraz wyswietalmy nasz plt
    plt.legend(loc=2, prop={'size': 19})
    plt.show()
    '''3d------------------------------------------------------------------------------------------------------'''

except FileNotFoundError:
    print("Nie znaleziono pliku!")
except KeyError:
    print("prosze odpalic taki plik, ktory posiada nazwy kolumn w jednym wierszu odzielone przecinkami")

