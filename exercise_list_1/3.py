"""

Faça um programa em Python que converte temperaturas expressas em graus Celsius para graus
Kelvin. Seu programa deve solicitar a digitação do valor a ser convertido (C). A relação entre
graus Celsius e graus Kelvin é C = K – 273,15.

"""

while True:
    I = input("Digite a temperatura em Celsius a ser convertida para Kelvin: ")
    
    if not I:
        print("Você não digitou nada, tente novamente")
        continue
    
    try:
        
        C = float(I)
        
        K = C + 273.15
        
        print(f"A temperatura em Kelvin é de: {K:.2f}°K")
        
        break
    
    except ValueError:
        print("Erro detectado, digite um valor válido")