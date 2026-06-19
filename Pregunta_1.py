import csv 
from lector import DATASET
from Pregunta_3 import lista_de_alcaldias


def PREGUNTA_1():

    lista_promedios = []

    for alcaldia in lista_de_alcaldias:

        suma = 0
        cantidad = 0

        for fila in DATASET:

            if fila["neighbourhood"] == alcaldia:

                if fila["price"] != "":

                    suma += float(fila["price"])
                    cantidad += 1

        if cantidad > 0:

            promedio = suma / cantidad

            lista_promedios.append([alcaldia, promedio])

    for i in range(len(lista_promedios)):

        for j in range(i + 1, len(lista_promedios)):

            if lista_promedios[j][1] > lista_promedios[i][1]:

                auxiliar = lista_promedios[i]
                lista_promedios[i] = lista_promedios[j]
                lista_promedios[j] = auxiliar

    return lista_promedios[:5]
