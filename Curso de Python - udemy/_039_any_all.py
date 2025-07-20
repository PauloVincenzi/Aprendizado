"""
Any e All


all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.
"""

# Exemplo all
print('All()')

print(all([0]))

print(all({1, 2, 3, 4}))

print(all((0, 1, 2, 3, 4)))

print(all([]))

print(all('Geek'))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all(nome[0] == 'C' for nome in nomes))

# Exemplo any
print('Any()')

print(any([0, False, {}, {}, []]))

print(any([0, 1, 2, 3, 4]))

print(any([0, 0, 0, 1, 0, 0, 0, 1]))

print(any('Abobrinha'))

print(any([]))
