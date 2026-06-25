from Pregunta_1 import AUX_PREGUNTA_1
from Pregunta_5 import PREGUNTA_5
from Pregunta_6 import PREGUNTA_6
from lector import dataset

# test_pregunta_1.py

def test_devuelve_5_elementos():

    resultado = AUX_PREGUNTA_1()
    assert len(resultado) == 5



def test_PREGUNTA_5():
    resultado = [{"Nombre": "Cómodo y lindo Dpto.", "Precio": 150.0, "Ubicación": (-99.24999814788514, 19.32927732036978)},
                 {"Nombre": "cuarto privado con baño propio", "Precio": 154.0, "Ubicación": (-99.27086530036256, 19.314865453550965)},
                 {"Nombre": "533 Habitación céntrica en remodelación", "Precio": 189.0, "Ubicación": (-99.1956584278164, 19.372925252214305)},
                 {"Nombre": "Habitación no. 9 | Las Almendras", "Precio": 196.0, "Ubicación": (-99.21619, 19.37231)}]
    assert PREGUNTA_5("Álvaro Obregón" , 200.0 , dataset()) == resultado



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