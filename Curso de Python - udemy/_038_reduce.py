"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (buillt-in). Agora temos
que importar e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legível.

Para entender o reduce()]

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ... , an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y


Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o interável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o resultado.
    Passo 3: res3 = f(res2, a4)

    Isso é repetido até o final

    Passo n: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderíamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), ...), an)
"""

# Como funciona na prática?

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista


from functools import reduce

dados = [2, 3, 4, 5, 25, 12, 11, 10, 6, 2, -3, -2, -8, 6.4, 1.03, 12.02]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros
multiplicacao = lambda x, y: x * y

res = reduce(multiplicacao, dados)
print(res)

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)
