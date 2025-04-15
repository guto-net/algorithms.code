"""
Lembrando que o perímetro de uma figura é a medida do contorno dela, faça um programa em
Python que calcula o perímetro em centímetros de um polígono regular. Seu programa deve
solicitar a digitação da quantidade de lados (Q) e a medida em centímetros de um dos lados do
polígono.

"""

while True:

    Q = int(input("Digite a quantidade de lados (Q) de um poligno: "))
    
    lado = float(input("Digite a media em centímetros um lado (lado) do poligono: "))

    if Q < 3:

        print("O polígono tem que ter no mínimo 3 lados")

        continue

    if lado < 0:

        print("Você digitou 0, tente algo mais significativo")

        continue

    try:

        media = Q * lado

        print(f"A medida em centímetro de um poligono é de {media:.2f}")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")