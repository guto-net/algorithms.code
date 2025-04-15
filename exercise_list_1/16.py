"""
Lembrando que o perímetro de uma figura é a medida do contorno dela, faça um programa em
Python que calcula o perímetro em centímetros de um trapézio. Seu programa deve solicitar a
digitação da medida em centímetros do lado paralelo menor (m), do lado paralelo maior (M) e de
outro lado (O) do trapézio, lembrando que os dois lados não paralelos de um trapézio têm medidas
iguais.

"""

while True:

    m = float(input("Digite a medida em centímetros do lado menor (m) do trapézio: "))
    
    M = float(input("Digite a medida em centímetros do lado maior (M) do trapézio: "))
   
    O = float(input("Digite a medida em centímetros do outro lado (O) do trapézio: "))

    if m > M:

        print("lado (m) não pode ser maior que (M)")

        continue


    if m <= 0 or M <= 0 or O <= 0:

        print("Você digitou 0, digite algo mais significante")

        continue

    try:

        media = m + M + 2 * O

        print(f"A medida em centímetros de um trapézio é de {media:.2f}cm")

        break

    except ValueError:

        print("Erro detectado, digite um valor válido")