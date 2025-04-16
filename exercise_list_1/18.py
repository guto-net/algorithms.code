import math

"""
Lembrando que o perímetro de uma figura é a medida do contorno dela, faça um programa em
Python que calcula o perímetro em centímetros de um círculo. Seu programa deve solicitar a
digitação da medida em centímetros do raio (R) do círculo. A relação entre essas grandezas é
Area = 2 π R, sendo π constante e aproximadamente igual a 3,1415.

"""

while True:

    R = float(input("Digite a medida em centímetros o raio (R) do circulo: "))

    if R <= 0:

        print("Você digitou zero, tente algo mais significativo")

        continue

    try:

        perimeter = 2 * math.pi * R

        print (f"A medida em centímetros do raio do circulo é de {perimeter:.2f}cm")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")