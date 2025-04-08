"""

Levando em conta as relações entre unidades de temperatura mostradas nos 6 primeiros
exercícios, faça um programa em Python que converte temperaturas expressas em graus Kelvin
para graus Fahrenheit. Seu programa deve solicitar a digitação do valor a ser convertido (K).

"""

while True:
    
    i = input("Digite a temperatura em Kelvin a ser convertida para Fahrenheit: ")
    
    if not i:
        print("Você não digitou nada, tente novamente")
        continue
    
    try:
        
        K = float(i)
        
        F = (K - 273.15) * 9 / 5 + 32
        
        print(f"A temperatura em Fahrenheit é de: {F:.2f}")
        
        break
    
    except ValueError:
        print("Erro detectado, digite um valor válido")
    