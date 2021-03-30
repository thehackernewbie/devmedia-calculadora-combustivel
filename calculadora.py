class Calculadora:
    def __init__(self):
        self.__valor_alcool = 4.999
        self.__valor_diesel = 4.232
        self.__valor_gasolina = 5.290

    def calcular_gasto(self, distancia, consumo):
        if (distancia <= 0 or consumo <= 0):
            raise Exception('O valor recebido nao poder ser menor ou igual a zero')

        gasto_alcool = round((distancia / consumo) * self.__valor_alcool, 2)
        gasto_diesel = round((distancia / consumo) * self.__valor_diesel, 2)
        gasto_gasolina = round((distancia / consumo) * self.__valor_gasolina, 2)

        return """
        O valor total gasto e:

        Alcool: R$ {}
        Diesel: R$ {}
        Gasolina: R$ {}

        """.format(
            gasto_alcool, gasto_diesel, gasto_gasolina
        )
