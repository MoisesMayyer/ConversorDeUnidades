from abc import ABC, abstractmethod
from uteis import fatores_comprimento, fatores_massa

def converter(valor, categoria, unidadei, unidadef):
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

    return conversor.converter(valor, unidadei, unidadef)



class Metodoconversao(ABC):

    @abstractmethod
    def converter(self, valor, unidadei, unidadef):
        pass


class ConversaoComprimento(Metodoconversao):

    def converter(self, valor, unidadei, unidadef):
        fatores = fatores_comprimento()

        valor_base = valor * fatores[unidadei]
        valor_final = valor_base / fatores[unidadef]

        return valor_final


class ConversaoMassa(Metodoconversao):

    def converter(self, valor, unidadei, unidadef):
        fatores = fatores_massa()

        valor_base = valor * fatores[unidadei]
        valor_final = valor_base / fatores[unidadef]

        return valor_final


class ConversaoTemperatura(Metodoconversao):

    def converter(self, valor, unidadei, unidadef):
        valor_celsius = 0

        if unidadei == "Celsius":
            valor_celsius = valor

        elif unidadei == "Fahrenheit":
            valor_celsius = (valor - 32) * 5 / 9

        elif unidadei == "Kelvin":
            valor_celsius = valor - 273.15


        if unidadef == "Celsius":
            valor_final =  valor_celsius

        elif unidadef == "Fahrenheit":
            valor_final = (valor_celsius * 9 / 5) + 32

        elif unidadef == "Kelvin":
            valor_final = valor_celsius + 273.15

        return valor_final