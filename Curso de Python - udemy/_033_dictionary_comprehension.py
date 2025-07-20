"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4)

Se quisermos criar um set (conjunto):

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxy

{chave:valor for valor in interável}
"""

# Exemplos

# 1

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave:valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

# 2

numeros = [1, 2, 3, 4]

quadrado = {valor:valor ** 2 for valor in numeros}

print(quadrado)

# 3

chaves = 'abcde'
valores= [1, 2, 3, 4, 5]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}
print(mistura)

# 4

numeros = [1, 2, 3, 4 ,5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
