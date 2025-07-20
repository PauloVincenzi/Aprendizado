"""
Tipo int (números inteiros)
    obs: é possível colocar '_' para simbolizar três casas em números.

Tipo float (números reais, decimais)
    obs1: separados por ponto e não virgula.
    obs2: pode-se trabalhar com números complexos

Tipo bool (algebra booleana: verdadeiro ou falso)
    obs: True ou False. Sempre com a inicial maiúscula.

Tipo str (string)
    Em Python, string é tudo que estiver entre:
    - Aspas simples
    - Aspas duplas
    - Aspas simples triplas
    - Aspas duplas triplas
"""
# Para facilitar a visualização apenas
num = 1000000
print(num)
num = 1_000_000
print(num)
print(type(num))
print()

# ERRADO, retorna uma tupla
valor = 1, 44
print(valor)
print(type(valor))
print()

# CERTO
valor = 1.44
print(valor)
print(type(valor))
print()

# É possível fazer dupla atribuição
n1, n2 = 12, 25
print(n1 + n2)
print()

# Complexos: O imaginário é representado por 'j'
ncomplex = 5j
print(ncomplex)
print(type(ncomplex))
print(ncomplex.real)
print(ncomplex.imag)
print(ncomplex**2)
print()

"""
Operações básicas (booleano)
"""

at1 = True
print(at1)
print(type(at1))
print()

# Negação (not)
"""
'Para um dado dual, a negação inverte-o' 
"""
print(not at1)
print()

# or e and
"""
Operadores lógicos

True or True -> True
True or False -> True
False or True -> True
False or False -> False

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""

at2 = False
print(at1 or at2)
print(at1 and not at2)
print()

# Duas formas de pular uma linha
print("Gina's \nBar")
print("""Gina's
Bar""")
print()

"""
Tudo maiúsculo
print(nome.upper())

Tudo minúsculo
print(nome.lower())

Inicial de cada palavra maiúsculo
print(nome.title())

Transforma em uma lista de strings. Cada espaço muda o elemento da lista.
print(nome.split())

Exclui os espaços 'a mais'
print(nome.strip())
"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12 ]
# ['P', 'a', 'u', 'l', 'o', ' ', 'E', 'd', 'u', 'a', 'r', 'd', 'o']
nome = 'Paulo Eduardo'
print(nome)
print(nome[7])
print(nome[0:5])
print(nome[6:13])
print()

# Comece do primeiro elemento, vá até o último elemento e inverta
print(nome[::-1])
print(nome[::2])
print()

# Inverter caracteres
print(nome.replace('o', 'a'))
