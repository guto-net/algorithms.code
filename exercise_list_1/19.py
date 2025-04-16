"""
Faça um programa em Python que calcula a área em centímetros quadrados de um triângulo. Seu
programa deve solicitar a digitação da medida em centímetros da base (B) e da altura (A) do
triângulo. A relação entre essas grandezas é Area = (B * A) / 2.

"""

while True:

    B = float(input("Digite a medida em centímetros da base (B) do triângulo: "))

    A = float(input("Digite a medida em centímetros da altura (A) do triângulo: "))

    if B <= 0 or A <= 0:

        print("Você digitou zero, tente algo mais significativo")

        continue

    try:

        Area = (B * A) / 2

        print(f"A medida em centímetros da area de um triângulo é de {Area:.2f}cm")

        break

    except ValueError:

        print("Erro detectado, digite algo válido")
