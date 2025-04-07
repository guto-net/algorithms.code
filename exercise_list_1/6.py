"""

Faça um programa em Python que converte temperaturas expressas em graus Rankine para graus
Celsius. Seu programa deve solicitar a digitação do valor a ser convertido (C). A relação entre
graus Celsius e graus Rankine é C = (R/1.8) – 491,67.

"""

while True:
    
    I = input("Digite a temperatura em Rankine a ser convertido para Celsius: ")
    
    if not I:
        print("Você não digitou nada, tente novamente")
        continue
    
    try:
        
        R = float(I)
        
        C = (R - 491.67) * 5 / 9
        
        print(f"A temperatura em celcius é de: {C:.2f}°")
        
        break
    
    except ValueError:
        print("Erro detectado, tente novamente")