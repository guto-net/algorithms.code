"""
Faça um programa em Python que calcula a área em centímetros quadrados de um trapézio. Seu
programa deve solicitar a digitação da medida em centímetros da base menor (b), da base
maior (B) e da altura (A) do trapézio. A relação entre essas grandezas é Area = ((b+B) . A) / 2.

"""

while True:

    b = float(input("Digite a medida em centímetros da base menor (b) do trapézio: "))

    B = float(input("Digite a medida em centímetros da base maior (B) do trapézio: "))

    A = float(input("Digite a medida em centímetros da altura (A) do trapézio: "))

    if b > B:

        print("A medida menor (b) não pode ser maior que a maior (B)")

        continue

    if b <= 0 or B <= 0 or A <= 0:

        print("Você digitou 0, tente algo mais significativo")

        continue


    try:

        Area = ((b + B) * A) / 2

        print(f"A medida em centímetros da area do trapézio é de {Area:.2f}cm")

        break

    except ValueError:

        print("Erro detectado")