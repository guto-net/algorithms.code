"""
Lembrando que uma equação de primeiro grau tem a forma AX+B=0 (por exemplo 3,5X+2,1=0),
sendo A e B coeficientes reais, faça um programa em Python que calcula a raiz de uma equação
de primeiro grau. Seu programa deve solicitar a digitação do valor dos coeficientes A e B da
equação.

"""

while True:

    try:
        A = float(input("Digite o coeficiente de A: "))

        B = float(input("Digite o coeficiente de B: "))

        if A <= 0 or B <= 0:

            print("Você digitou 0, tente algo mais significativo")

            continue

        X = -B / A

        print(f"A raiz da equação de primeiro grau é de {A}X + {B} = 0 é {X:.2f}")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")