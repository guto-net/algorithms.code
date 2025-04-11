# Estrutura condicional

![Estrutura condicional img 1](https://financetrain.sgp1.cdn.digitaloceanspaces.com/27536-if-condition.png)

Uma estrutura condicional é quando você implementa uma espécie de "verificação" para algo, por exemplo: quando você quer que certo resultado seja de tal maneira, você verifica.

```python

name = "guto-net"

if name == "guto-net":

    return True

```
Então se o nome realmente for guto-net ele retorna verdadeiro, mas podemos fazer um outro caso para a verificação ultilizando o else, como visto na imagem.


```python

name = "guto-net"

if name == "guto-net":

    return True

else:
    
    print("Não é o nome desejado")

```

Observe que podemos além de fazer uma "sub verificação" podemos retornar respostas mais amigáveis caso a verificação seja falsa.

![Estrutura condicional img 2](https://pages.cs.wisc.edu/~cs310-1/modules/Programming/_Sequential%20and%20Conditional%20Execution/Conditional%20Execution/if_else_flow.jpg)

A condição é uma das estruturas mais importantes da programação, com ela podemos válidar os dados, gerenciar o fluxo do nosso algoritmo e isso é a base fundamental!