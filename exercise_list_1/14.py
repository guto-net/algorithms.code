"""
Lembrando que o perímetro de uma figura é a medida do contorno dela, faça um programa em
Python que calcula o perímetro em centímetros de um quadrado/losango. Seu programa deve
solicitar a digitação da medida em centímetros do lado (L) do quadrado/losango.

"""

while True:

    L = float(input("Digite a medida em cm do lado (L) do quadrado/losangulo: "))

    if L <= 0:
        
        print("Você digitou 0, selecione um valor mais significativo")

        continue

    try:

        media = L * 4

        print(f"A medida em cm do lado (L) do quadrado/losangulo é de {media:.2f}cm")
        
        break

    except ValueError:

        print("Erro detectado, digite um valor válido")