"""
Módulo Collections: Ordered Dict


"""

# Em um dicionário, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b':2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}') 

print()

# Ordered Dict é um dicionário mas a ordem é mantida!

# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b':2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}') 

# Visualizando

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(f'Dict1 = {dict1}')
print(f'Dict2 = {dict2}')

print('Os dicionários são iguais?')
print('A linguagem entede que:')
print(dict1 == dict2)
print('Mas, NÃOOOO! Suas chaves e valores são iguais, mas não são organizados na mesma ordem.')

