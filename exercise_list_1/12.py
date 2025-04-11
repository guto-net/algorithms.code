"""

Levando em conta as relações entre unidades de temperatura mostradas nos 6 primeiros
exercícios, faça um programa em Python que converte temperaturas expressas em graus Rankine
para graus Kelvin. Seu programa deve solicitar a digitação do valor a ser convertido (R).

"""

while True:

    i = input("Digite a temperatura em Rankine a ser convertida para Kelvin: ")

    if not i:

        print("Você não digitou nada, tente novamente")

        continue

    try:

        R = float(i)

        K = R * 5 / 9

        print(f"A temperatura em Kelvin é de {K:2f}")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")