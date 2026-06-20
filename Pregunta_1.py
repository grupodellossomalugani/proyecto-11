import csv 
from lector import DATASET
from Pregunta_3 import lista_de_alcaldias

#Tomas

#Cosas por terminar:
#Falta el diseno de datos + casos de pruebas donde sea posible 

def PREGUNTA_1():

    #lista vacia donde se van a guardar los promedios 
    lista_promedios = []

    #for q rrecorre todas las alcaldias  
    for alcaldia in lista_de_alcaldias:

        #acumuladores 
        suma = 0
        cantidad = 0

        #Reccorre todas las filas del dataset
        for fila in DATASET:

            #si el campo neighbourhood es igual a la alcaldia que se esta buscando:
            if fila["neighbourhood"] == alcaldia:

                #y es distinto de precio vacio 
                if fila["price"] != "":
                    
                    # agrega el precio al acumulador de suma y suma una al acumulador de cantidad 
                    suma += float(fila["price"])
                    cantidad += 1
        #validacion 
        if cantidad > 0:
            
            
            #calculo del promedio
            promedio = suma / cantidad

            #guarda la alcaldia y su promedio 
            lista_promedios.append([alcaldia, promedio])

    #orden de promedio 
    for i in range(len(lista_promedios)):

        for j in range(i + 1, len(lista_promedios)):
            
            if lista_promedios[j][1] > lista_promedios[i][1]:#cambia la posicion si se encuentra uno mayor 

                auxiliar = lista_promedios[i]
                lista_promedios[i] = lista_promedios[j]
                lista_promedios[j] = auxiliar
#devuelve las 5 alcaldias con mayor precio 
    return lista_promedios[:5]
