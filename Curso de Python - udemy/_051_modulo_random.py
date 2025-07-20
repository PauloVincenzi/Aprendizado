"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatórios.

"""

# OBS: Existem duas formas de se utilizar um módulo

# Forma 1 - Importando todo o módulo (não recomendado)

import random

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis (ficarão em memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a melhor forma de utilização.

print(random.random()) # Gera um número pseudo-aleatório entre 0 e 1

# Veja que para utilizar a função random do pacote random, nós colocamos o nome do pacote e o nome da função, separados por ponto.

print()

# Forma 2 - Importando uma função específica do módulo

from random import random

for i in range(10):
    print(random())

# Aqui não mais é preciso colocar o nome do pacote '.' nome da função.
# Podemos utilizar o nome da função diretamente.

print()


# Outras funções do módulo random

from random import uniform, randint, choice, shuffle

for i in range(5):
    print(uniform(3, 7)) # Número real no intervalo pseudo-aleatório. Não incluí 7

print()

# Gerador de apostas para mega-sena (Pode haver repetição de algum número - na mega-sena real não pode)
for i in range(6):
    print(randint(1, 61), end=' ') # Número inteiro no intervalo pseudo-aleatório. Não incluí 61

print('\n')

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas)) # Mostra um valor pseudo-aleatório entre um iterável

print()

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
shuffle(cartas) # Embaralha os dados
print(cartas)


