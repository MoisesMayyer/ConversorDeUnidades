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
    return {
        "Centímetro": 0.01,
        "Metro": 1,
        "Quilômetro": 1000
    }


def fatores_massa():
    return {
        "Grama": 0.001,
        "Quilograma": 1,
        "Tonelada": 1000
    }
