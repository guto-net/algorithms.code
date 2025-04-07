"""

Faça um programa em Python que converte temperaturas expressas em graus Fahrenheit para
graus Celsius. Seu programa deve solicitar a digitação do valor a ser convertido (F). A relação
entre graus Celsius e graus Fahrenheit é C = 5/9 (F -32).

"""

while True:
    
    I = input("Digite o valor em Fahrenheit a ser convertido para Celsius: ")
    
    # Condição que verifica se o input é vazio
    if not I:
        print("Você não digitou nada, tente novamente")
        continue # volta ou pula pro próximo ciclo de repetição
        
    try:
        
        F = float(I)
        
        C = 5 / 9 * F - 32
        
        print(f"A temperatura em Farenheit é de: {C:.2f}°C")
        
        break
    
    except ValueError:
        print("Erro detectado, digite um valor válido")