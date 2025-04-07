"""

Faça um programa em Python que converte temperaturas expressas em graus Celsius para graus
Rankine. Seu programa deve solicitar a digitação do valor a ser convertido (C). A relação entre
graus Celsius e graus Rankine é C = (R/1.8) – 491,67.

"""

while True:
    
    I = input("Digite a temperatura em Celsius a ser convertido para Rankine: ")
    
    if not I:
        print("Você não digitou nada, tente novamente")
        continue
    
    try:
        
        C = float(I)
        
        R = C * 9 / 5 + 491.67
        
        print(f"A temperatura em Rankine é de: {R:.2f}°")
        
        break
    
    except ValueError:
        print("Erro detectado, digite um número válido") 