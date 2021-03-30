from calculadora import Calculadora

def main():
    print(
        """
        Essa aplicao tem como finalidade demonstrar os valores que serao gastos
        com combustivel durante uma viagem, com base no contador so seu veiculo, e
        com a distancia determinada por voce
        """
    )

    print("Os combustiveis disponiveis para esse calulo sao:")
    print("      Alcool")
    print("      Diesel")
    print("      Gasolina")

    print("    ")

    try:
        distancia = float(input("Distância em Quilômetros a ser percorrida: "))
        consumo = float(input("Consumo de combustivel do veiculo (Km/l): "))
        calculo = Calculadora()
        print(calculo.calcular_gasto(distancia, consumo))
    except ValueError:
        print("O valor recebido nao e valido")

if __name__ == "__main__":
        main()
