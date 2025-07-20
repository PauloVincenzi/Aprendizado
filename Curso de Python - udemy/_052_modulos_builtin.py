"""
Trabalhando com módulos Builtin (módulos integrados, que há vem instalados no Python)

Embora estes módulos já vêm instalados no Python, eles não são carregados, 
a menos que você coloque-os na memória com o import.

# Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random())

# Podemos importar todas as função de um módulo utilizando o *

from random import *
# corresponde a: import random

# vantagem: não precisa escrever random.'funcao'() e sim apenas 'funcao'()

# Utilizando alias (apelidos) para funções

from random import randint as rdi

print(rdi(1, 10))

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo

from random import (
    random, 
    randint, 
    choice, 
    shuffle
)
"""
