from abc import ABC, abstractmethod

from uteis import fatores_comprimento, fatores_massa


def converter(valor, categoria, unidade_origem, unidade_destino):
    try:
        valor = float(valor)
    except ValueError:
        return "Digite um número válido."

    if categoria == "Comprimento":
        conversor = ConversaoComprimento()
    elif categoria == "Temperatura":
        conversor = ConversaoTemperatura()
    elif categoria == "Massa":
        conversor = ConversaoMassa()
    else:
        return "Categoria inválida."

    try:
        return conversor.converter(valor, unidade_origem, unidade_destino)
    except KeyError:
        return "Unidade inválida."


class Metodoconversao(ABC):

    @abstractmethod
    def converter(self, valor, unidade_origem, unidade_destino):
        pass


class ConversaoComprimento(Metodoconversao):

    def converter(self, valor, unidade_origem, unidade_destino):
        fatores = fatores_comprimento()

        valor_base = valor * fatores[unidade_origem]
        valor_final = valor_base / fatores[unidade_destino]

        return valor_final


class ConversaoMassa(Metodoconversao):

    def converter(self, valor, unidade_origem, unidade_destino):
        fatores = fatores_massa()

        valor_base = valor * fatores[unidade_origem]
        valor_final = valor_base / fatores[unidade_destino]

        return valor_final


class ConversaoTemperatura(Metodoconversao):

    def converter(self, valor, unidade_origem, unidade_destino):
        if unidade_origem == "Celsius":
            valor_celsius = valor
        elif unidade_origem == "Fahrenheit":
            valor_celsius = (valor - 32) * 5 / 9
        elif unidade_origem == "Kelvin":
            valor_celsius = valor - 273.15
        else:
            raise KeyError(unidade_origem)

        if unidade_destino == "Celsius":
            valor_final = valor_celsius
        elif unidade_destino == "Fahrenheit":
            valor_final = (valor_celsius * 9 / 5) + 32
        elif unidade_destino == "Kelvin":
            valor_final = valor_celsius + 273.15
        else:
            raise KeyError(unidade_destino)

        return valor_final
