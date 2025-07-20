"""
Entendendo Iterators e Iterables

Iterator ->
    - Um objeto que pode ter iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada
"""

nome = 'Geek' # É um iterable, mas não um iterator.
numeros = [1, 2, 3, 4, 5] # É um iterable, mas não um iterator.

# print(next(nome)) # Erro
# Podemos tornar os objetos Iterables:

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# Se continuarmos fazendo a função next() haverá um erro 

print(next(it2))
print(next(it2))
print(next(it2))

print('-'*50)

# Ou seja, quando fazemos:
for letra in nome:
    print(f'{letra}')
# A função next() é feita 'por baixo dos panos' e 'para no momento certo', sem gerar StopIteration
