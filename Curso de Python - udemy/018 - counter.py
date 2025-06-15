"""
Módulo Collection - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade 
de ocorrências desse elemento.

"""

# Utilizando o Counter

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 0, 1, 1, 1, 1, 2, 2, 3, 3, 1, 3, 5, 5, 5, 3, 2, 2, 2, 6, 92, 0]
print(f'Lista: {lista}')

# Utilizando o Counter
res = Counter(lista)

print(f'Counter: {res}')
print(type(res))

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2

nome = str(input('Diga seu nome: '))
print(Counter(nome))

# Exemplo 3

print('Ocorrências de cada palavra de um texto: ')
texto = """ O nome Wikipedia foi criado pelo filósofo norte-americano
Larry Sanger, e é uma combinação do termo havaiano "wikiwiki"
que significa "rápido" ou "rapidamente" com o sufixo da palavra
"enciclopédia".
"""

palavras = texto.split()
print(palavras)
res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print('Encontrando as 5 palavras com mais ocorrências no texto')
print(res.most_common(5))



