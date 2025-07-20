"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos.
"""

# Exemplos

lista = [1, 8, 4, 99, 34, 128]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 128)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 128}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'f': 34, 'g': 128}
print(min(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'f': 34, 'g': 128}
print(max(dicionario.values()))

print(max(3.14, 34, 20))

print(max('a', 'ab', 'abc'))

print(min('a', 'ab', 'abc'))

print(max('Paulo Vincenzi'))

print(min('Paulo Vincenzi'))

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes)) # Tim

print(min(nomes)) # Arya

print(max(nomes, key=lambda nome: len(nome))) # Ollivander

print(min(nomes, key=lambda nome: len(nome))) # Tim

musicas = [
    {"título": "Thunderstruck", "tocou": 3},
    {"título": "Dead Skin Mask", "tocou": 2},
    {"título": "Back in Black", "tocou": 4},
    {"título": "Too old to rock'in'roll", "tocou": 32}
]

# Imprima o nº de vezes que da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Imprima somente o título da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['título'])
print(min(musicas, key=lambda musica: musica['tocou'])['título'])

print(max(musica['título'] for musica in musicas))
print(min(musica['título'] for musica in musicas))
 
# Imprimir somento o título da música mais tocada sem usar max(), min() e lambda
"""
max = 0
for musica in musicas:
    if musica['tocou'] > max
        max = musica['tocou']
    
for musica in musicas:
    if musica['tocou'] == max:
        print(musica['tocou'])
"""
