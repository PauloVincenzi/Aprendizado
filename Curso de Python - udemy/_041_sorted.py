"""
Sorted

OBS: Não confunda, apenas do nome, com a função sort() que já estudamos em listas.
O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma Lista com os elementos do iterável ordenados.
"""

# Exemplo

numeros = (6, 3, 2, 1, 8)
print(numeros)

print(sorted(numeros))

print(numeros)

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

print()
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)
print()

# print(sorted(usuarios)) # Error

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"])) 
print()

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
print()

# Último exemplo

musicas = [
    {"título": "Thunderstruck", "tocou": 3},
    {"título": "Dead Skin Mask", "tocou": 2},
    {"título": "Back in Black", "tocou": 4},
    {"título": "Too old to rock'in'roll", "tocou": 32}
]

# Ordenada da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
print()

# Ordenada da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
