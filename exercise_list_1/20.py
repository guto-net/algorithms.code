"""
Faça um programa em Python que calcula a área em centímetros quadrados de um quadrado. Seu
programa deve solicitar a digitação da medida em centímetros do lado (L) do quadrado. A relação
entre essas grandezas é Area = L².

"""

while True:

    L = float(input("Digite a medida em centímetros do lado (L) do quadrado: "))

    if L <= 0:

        print("Você digitou 0, tente algo mais significativo")

        continue

    try:

        Area = L ** 2

        print(f"A medida em centímetros da area do quadrado é de {Area:.2f}cm")

        break

    except ValueError:

        print("Erro detectado, digite algo válido")