import math

"""
Faça um programa em Python que calcula a área em centímetros quadrados de um círculo. Seu
programa deve solicitar a digitação da medida em centímetros do raio (R) do círculo. A relação
entre essas grandezas é Area = π R², sendo π constante e aproximadamente igual a 3,1415.

"""

while True:

    try:

        R = float(input("Digite a medida em centímetros do raio (R) do círculo: "))

        if R <= 0:

            print("Você digitou 0, tente algo mais significativo")

            continue

        Area = math.pi * R ** 2

        print(f"A medida em centímetros da area do quadrado de um círculo é de {Area:.2f}cm")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")

