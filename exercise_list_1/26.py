"""
Faça um programa em Python que calcula o Índice de Massa Corporal (ou BMI, Body Mass
Index) de uma pessoa. Seu programa deve solicitar a digitação do peso em kilogramas (P) da
pessoa, bem como de sua altura em metros (A). O BMI é dado pelo peso dividido pelo quadrado
da altura.

"""

while True:

    try:

        P = float(input("Digite seu peso: "))

        A = float(input("Digite sua altura em metros: "))

        if P <= 0 or A <= 0:

            print("Você digitou 0, tente algo mais significativo")

            continue

        BMI =  P / A ** 2

        print(f"Seu BMI é de {BMI:.2f}")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")