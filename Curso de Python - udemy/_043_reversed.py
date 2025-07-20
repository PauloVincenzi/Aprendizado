"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.]

A função reversed() retorna um iterável chamado List Reverse Iterator
"""

lista = [1, 2, 3, 4, 5]
print(lista)

res = reversed(lista)
print(res)
print(type(res))

# Podemos converter
print(list(res))
print(tuple(res))

for letra in reversed('Geek University'):
    print(letra, end='')
