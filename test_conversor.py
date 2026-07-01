from conversor import converter


def test_comprimento_metro_para_centimetro():
    assert converter(1, "Comprimento", "Metro", "Centímetro") == 100


def test_massa_quilograma_para_grama():
    assert converter(1, "Massa", "Quilograma", "Grama") == 1000


def test_temperatura_celsius_para_fahrenheit():
    assert converter(0, "Temperatura", "Celsius", "Fahrenheit") == 32


def test_valor_invalido():
    assert converter("abc", "Comprimento", "Metro", "Centímetro") == "Digite um número válido."


def test_categoria_invalida():
    assert converter(1, "Volume", "Litro", "Mililitro") == "Categoria inválida."


def test_unidade_invalida():
    assert converter(1, "Comprimento", "Metro", "Milha") == "Unidade inválida."
