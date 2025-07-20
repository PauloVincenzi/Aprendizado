"""
Generators

Em aulas anteriores nós estudamos:
 - List Comprehension
 - Dictionary Comprehension
 - Set Comprehension

Não vimos:
 - Tuple Comprehension... porque elas se chamam Generators
"""

# Execução com List Comprehension

"""
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))
"""

# Execusão usando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))


# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Opte pelo Generator, pois ele usa menos recurso de memória.

# getsizeof() -> Retorna a quantidade de bytes de memória do elemento passado como parâmetro
from sys import getsizeof

print('EM BYTES:')

print(getsizeof(5))
print(getsizeof(512321412))
print(getsizeof('Geek'))
print(getsizeof(True))

print('Para fazer a mesma tarefa:')

print('List Comprehension: ', end='')
print(getsizeof([x * 10 for x in range(1000)]))

print('Set Comprehension: ', end='')
print(getsizeof({x * 10 for x in range(1000)}))

print('Dictionary Comprehension: ', end='')
print(getsizeof({x: x * 10 for x in range(1000)}))

print('Generator: ', end='')
print(getsizeof(x * 10 for x in range(1000)))

# É possivel iterar no Generator Expression!

gen = (x * 10 for x in range(15))
print(gen)
print(type(gen))

for num in gen:
    print(num)
