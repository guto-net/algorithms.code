"""

Lembrando que o perímetro de uma figura é a medida do contorno dela, faça um programa em
Python que calcula o perímetro em centímetros de um triângulo. Seu programa deve solicitar a
digitação da medida em centímetros dos lados (A, B e C) do triângulo.

"""

while True:

    A = float(input("Digite o lado A do triangulo: "))

    B = float(input("Digite o lado B do triangulo: "))
   
    C = float(input("Digite o lado C do triangulo: "))

    if A <= 0 or B <= 0 or C <= 0: # or para quando quiser saber se qualquer condição é verdadeira

        print("Você não digitou nada, tente novamente")

        continue

    try:

        perimeter = A + B + C

        print(f"O perimetro do triangulo é de: {perimeter:.2f}cm")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")

