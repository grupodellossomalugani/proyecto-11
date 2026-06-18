import csv 
from lector import DATASET
import streamlit as st


#FUNCION DE LA PREGUNTA 4
# Cuál es el precio promedio si deseo hospedarme en la alcaldía Xochimilco?
#  Luca 


def PREGUNTA_4():
     
        # Acumuladores
        cantidad = 0
        suma = 0


        # Iteracion para calcular el promedio
        for fila in DATASET:
            
            # Busca las filas tal que coinciden con "Xochimilco"
            if fila["neighbourhood"] == "Xochimilco":
                
                # Evalua que el precio no sea un espacio en blanco
                if fila["price"] != "":
                    
                    # Definicion 
                    suma += float(fila["price"])
                    cantidad += 1
                
                else:
                    pass


        # Caso si hay registros de Xochimilco
        if cantidad > 0:

            # Operacion
            promedio = round(suma / cantidad, 2)
            print(f"El promedio de precio en Xochimilco es: {promedio}")
        
        # Caso si no hay registros de Xochimilco
        else:
            print("No se encontraron registros para Xochimilco.")

PREGUNTA_4()