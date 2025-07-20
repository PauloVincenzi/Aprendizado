"""
Listas Aninhadas (Nested Lists)

 - Algumas linguagens de programação possuem uma estrutura de dados chamada de arrays
    - Unidimensionais (Arrays / Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as Listas

numeros = [1, 2, 3, 4, 5]
"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

print(listas)

# Como fazemos para acessar os dados?

print(listas[0][1])

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num, end=' ')
    print()

print()

[[print(valor, end=' ') for valor in lista] for lista in listas]

print()

# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])
