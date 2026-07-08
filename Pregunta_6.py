import streamlit as st


# La funcion auxiliar ordena de menor a mayor las distancias
# de los hospedajes
def AuxPregunta6(tabla):
    

    # Lista resultante que contiene las distancias
    listaDistancias = []
    
    
    # Lista resultante que contiene los elementos acomodados
    listaOrdenada = []


    # Este ciclo guarda las distancias en la lista
    for i in tabla:
        
        
        if i["Distancia(Km)"] not in listaDistancias:
            
            
            listaDistancias.append(i["Distancia(Km)"])
    

    # Ordena las distancias de menor a mayor
    listaDistancias.sort()


    # Ordena los elementos de tabla en funcion a su distancia
    for j in listaDistancias:
        
        
        for k in tabla:


            if j == k["Distancia(Km)"] and k not in listaOrdenada:
                
                
                listaOrdenada.append(k)


    return listaOrdenada


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
            # 0.5km = 0.0002143 r
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


    # Ordena de menor a mayor las distancias
    tabla = AuxPregunta6(tabla)


    return tabla
        

# Funcion que muestra el grafico en streamlit
def Grafico_Pregunta6(DATASET:list)->None:
    
    
    # Funcion auxiliar
    tabla = PREGUNTA_6(DATASET)
    

    # Tabla en strealit
    st.dataframe(tabla)

