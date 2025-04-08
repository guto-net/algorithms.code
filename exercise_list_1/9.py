"""

Levando em conta as relações entre unidades de temperatura mostradas nos 6 primeiros
exercícios, faça um programa em Python que converte temperaturas expressas em graus
Fahrenheit para graus Rankine. Seu programa deve solicitar a digitação do valor a ser
convertido (F).

"""

while True:
    
    i = input("Digite a temperatura em Fahrenheit a ser convertido para Rankine: ")
    
    if not i:
        print("Você não digitou nada, tente novamente")
        continue
    
    try:
        
        F = float(i)
        
        R = F + 459.67
        
        print(f"A temperatura em Rankine é de: {R:.2f}")
        
        break
    
    except ValueError:
        print("Erro detectado, digite um valor válido")