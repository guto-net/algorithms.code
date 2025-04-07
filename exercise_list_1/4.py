"""

Faça um programa em Python que converte temperaturas expressas em graus Kelvin para graus
Celsius. Seu programa deve solicitar a digitação do valor a ser convertido (K). A relação entre
graus Celsius e graus Kelvin é C = K – 273,15.

"""

while True:
    I = input("Digite a temperatura em Kelvin a ser convertido para Celsius: ")
    
    if not I:
        print("você não digitou nada, tente novamente")
        continue
    
    try:
        
        K = float(I)
        
        C = K - 273.15
        
        print(f"A temperatura em celsius é de: {C:.2f}°")

        break
    
    except ValueError:
        print("Erro detectado, digite um valor válido")
        