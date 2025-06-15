"""
Map

Com map, fazemos mapeamento de valores para função.
"""

import math


def area(r):
    """Calcual a área de um círculo com raio 'r'"""
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 4, 2, 44, 16]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(area)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um interável

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.

"""
Para fixar.

Temos dados iteráveis: a1, a2, ... , an

Temos uma função: f(x)

Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar na função

# O Map Object: f(a1), f(a2), ... , f(an)
"""

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

print(cidades)

# F = (9/5 * C) + 32

c_para_f = lambda dado: (dado[0], (9/5 * dado[1]) + 32)

print(list(map(c_para_f, cidades)))
