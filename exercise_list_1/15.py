"""
Lembrando que o perímetro de uma figura é a medida do contorno dela, faça um programa em
Python que calcula o perímetro em centímetros de um retângulo/paralelogramo. Seu programa
deve solicitar a digitação da medida em centímetros do lado menor (m) e do lado maior (M) do
retângulo/paralelogramo.

"""

while True:

    m = float(input("Digite a medida do lado menor (m) do retângulo: "))

    M = float(input("Digite a medida do lado maior (M) do retângulo: "))

    if m > M:

        print("Lado menor (m) não pode ser maior que o lado (M)")

        continue

    if m <= 0 or M <= 0:
        
        print("Você digitou 0, tente algo mais significativo")

        continue

    try:

        media = m * 2 + M * 2

        print(f"A medida em centímetros de um retângulo é de {media:.2f}cm")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")