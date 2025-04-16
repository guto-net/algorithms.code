"""
Faça um programa em Python que calcula a área em centímetros quadrados de um polígono
regular. Seu programa deve solicitar a digitação da quantidade de lados (Q) do polígono, bem
como da medida em centímetros de sua base (B) e de sua apótema (A), ou seja, a reta imaginária
que une seu centro ao meio de sua base. A relação entre essas grandezas é Area = (Q.B.A)/2.

"""

while True:

    try: # Usar o try no ínico impede qualquer erro de conversão dos inputs, então sempre usar o try no começo para capturar todos os erros possíveis

        Q = float(input("Digite a quantidade de lados (Q)  do poligono: "))

        B = float(input("Digite a medida em centímetros da base (B) do poligono: "))

        A = float(input("Digite a apótema (A) do poligono: "))

        if Q <= 0 or B <= 0 or A <= 0:

            print("Você digitou 0, tente algo mais significativo")

            continue

        Area = (Q * B * A) / 2

        print(f"A medida em centíemtros da area de um poligono é de {Area:.2f}cm")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")