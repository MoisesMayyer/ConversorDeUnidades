from abc import ABC, abstractmethod
from uteis import fatores_comprimento

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
        return "em construção"


class ConversaoTemperatura(Metodoconversao):

    def converter(self, valor, unidadei, unidadef):
        return "em construção"