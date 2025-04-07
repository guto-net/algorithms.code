"""

Faça um programa em Python que converte temperaturas expressas em graus Celsius para graus
Fahrenheit. Seu programa deve solicitar a digitação do valor a ser convertido (C). A relação entre
graus Celsius e graus Fahrenheit é C = 5/9 (F -32).

"""
while True: # Vai repetir até o break
    
    I = input("Digite sua temperatura em Celsius a ser convertida para Fahrenheit: ")
    
    if not I:
        print("Você não digitou nada, tente novamente")
        continue
        
    try:
        
        C = float(I)
        F = 9 / 5 * C + 32
        print(f"A temperatura em Fahrenheit é de: {F:.2f}°F")
        
        break
    
    except ValueError:
        print("Erro detectado, digite um valor válido")
        