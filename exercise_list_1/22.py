"""
Faça um programa em Python que calcula a área em centímetros quadrados de um
losango/paralelogramo. Seu programa deve solicitar a digitação da medida em centímetros da
diagonal menor (d) e da diagonal maior (D) do losango. A relação entre essas grandezas é Area =
(d . D) / 2.

"""

while True:

    d = float(input("Digite a medida em centímetros da diagonal menor (d) do losangulo: "))

    D = float(input("Digite a medida em centímetros da diagonal maior (D) do losangulo: "))

    if d > D:

        print("Medida menor (d) não pode ser maior que a medida maior (D)")

        continue

    if d <= 0 or D <= 0:

        print("Você digitou 0, tente algo mais significativo")

        continue

    try:

        Area = (d * D) / 2

        print(f"A medida em centímetros da area do losangulo é de {Area:.2f}cm")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")