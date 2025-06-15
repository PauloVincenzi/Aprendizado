"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável]
"""

# Exemplo

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

"""
Para entender melhor o que está acontencendo devemos dividir a expressão em duas partes:

 - A primeira parte: for numero in numeros
 - A segunda parte: numero * 10
"""

res = [numero / 2 for numero in numeros]

print(res)


def quadrado(valor):
    return valor ** 2


res = [quadrado(numero) for numero in numeros]

print(res)

# Outros exemplos

# 1

nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# 3

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# obs: python considera '0', lista vazia e string vazia como False

# 4

print([str(numero) for numero in [1, 2, 3, 4, 5]])
