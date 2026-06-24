from lector import dataset
import streamlit as st


def PREGUNTA_6(DATOS:list)->list:
    """
    La función recibe la dataset en forma de lista, esta calcula los hospedajes que
    se ubican dentro de un radio de 0.5 km de distancia de la Catedral de Ciudad de México
    Ejemplo:
    PREGUNTA_6([{"name": "Hotel Catedral", "longitude": "-99.13306", "latitude": "19.43444", "price": 500},
                { "name": "Hotel Cercano", "longitude": "-99.13250", "latitude": "19.43400", "price": 800},
                {"name": "Hotel Lejano", "longitude": "-99.12000", "latitude": "19.42000", "price": 1200}]) ==
            
            [{"Nombre": "Hotel Catedral", "Distancia(Km)": 0.0, "Precio": 500, "Ubicación": (-99.13306, 19.43444)},
             {"Nombre": "Hotel Cercano", "Distancia(Km)": 0.1, "Precio": 800, "Ubicación": (-99.13250,19.43400)}]
    """


    # Coordenadas Catedral
    Xc = -99.13306
    Yc = 19.43444


    # Tabla resultante
    tabla = []


    # Lectura del dataset
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
                    "Precio": fila["price"],
                    "Ubicación": (X,Y)
                })


    # Ordena la tabla por orden ASC de las distancias
    tabla.sort(key=lambda x: x["Distancia(Km)"]) 

    # Tabla
    st.dataframe(tabla)

    return tabla



def test_PREGUNTA_6():
    
    datos_test = [{
        "name": "Hotel Catedral",
        "longitude": "-99.13306",
        "latitude": "19.43444",
        "price": 500
    },
    {
        "name": "Hotel Cercano",
        "longitude": "-99.13250",
        "latitude": "19.43400",
        "price": 800
    },
    {
        "name": "Hotel Lejano",
        "longitude": "-99.12000",
        "latitude": "19.42000",
        "price": 1200
    }]
    
    resultado = [{
        "Nombre": "Hotel Catedral",
        "Distancia(Km)": 0.0,
        "Precio": 500,
        "Ubicación": (-99.13306, 19.43444)
    },
    {
        "Nombre": "Hotel Cercano",
        "Distancia(Km)": 0.1,
        "Precio": 800,
        "Ubicación":(-99.13250,19.43400)
    }]

    assert PREGUNTA_6(datos_test) == resultado

