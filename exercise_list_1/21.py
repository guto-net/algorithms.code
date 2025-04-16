"""
Faça um programa em Python que calcula a área em centímetros quadrados de um retângulo. Seu
programa deve solicitar a digitação da medida em centímetros do lado menor (m) e do lado maior
(M) do retângulo. A relação entre essas grandezas é Area = m . M

"""

while True:

    m = float(input("Digite a medida em centímetros do lado menor (m) do retângulo: "))
    
    M = float(input("Digite a medida em centímetros do lado maior (M) do retângulo: "))

    if m > M:

        print("Lado menor (m) não pode ser maior que lado maior (M)")

        continue

    if m <= 0 or M <= 0:

        print("Você digitou 0, tente algo mais significativo")

        continue

    try:

        Area = m * M

        print(f"A medida em centíemtros da area do retângulo é de {Area:.2f}cm")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")
