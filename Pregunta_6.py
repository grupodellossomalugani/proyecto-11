from lector import DATASET
import streamlit as st


def PREGUNTA_6():
    DATOS = DATASET


    # Coordenadas Catedral
    Xc = -99.13306
    Yc = 19.43444


    tabla = []


    for fila in DATOS:


        # Evalua que los datos longitud y latitude sean validos
        if fila["longitude"] != "" and fila["latitude"] != "":


            # Coordenadas del hospedaje
            X = float(fila["longitude"])
            Y = float(fila["latitude"])


            # Calculo para saber si se encuentra en el radio
            if (X -  Xc)**2 + (Y - Yc)**2 <= 0.00002143:


                # Conversion de grados a kilometros
                Distancia = ( ( (X-Xc)**2 + (Y-Yc)**2 ) ** 0.5) * 108
                Distancia = round(Distancia,1)


                # Agrega los datos que satisfacen las condiciones
                tabla.append({
                    "Nombre": fila["name"],
                    "Distancia(Km)": Distancia,
                    "Precion": fila["price"],
                    "Direccion": " "
                })


    # Ordena la tabla por orden ASC de las distancias
    tabla.sort(key=lambda x: x["Distancia(Km)"]) 

    # Tabla
    st.dataframe(tabla)



