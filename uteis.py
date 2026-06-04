
def lista_de_unidades():
    return {
        "Comprimento": [
            "Centímetro",
            "Metro",
            "Quilômetro"
        ],

        "Massa": [
            "Grama",
            "Quilograma",
            "Tonelada"
        ],

        "Temperatura": [
            "Celsius",
            "Fahrenheit",
            "Kelvin"
        ]
    }



def fatores_comprimento():
    fatores = {
        "Centímetro": 0.01,
        "Metro": 1,
        "Quilômetro": 1000
    }
    return fatores