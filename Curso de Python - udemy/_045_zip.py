"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.
"""

# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# Podemos converter
print(list(zip1))

zip2 = zip(lista1, lista2, 'abc')
print(list(zip2))

print()

# O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver trabalhando
# com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar.

lista3 = [7, 8, 9, 10, 11]
zip3 = zip(lista1, lista2, lista3)
print(list(zip3))

# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

"""
Contextualizando: considere uma tabela com intervalos de valores (idade), cada intervalo de classe é espressa como uma tupla (I, F)
dentro da lista dados.
Ao descompactar dados com o asterisco e fazer zip, duas tuplas são geradas: a primeira apresenta todos os valores de início de intervalo (I)
e fim de intervalo (F).
"""

print()

# Exemplo mais complexo

prova1 = [80, 91, 78, 95]
prova2 = [93, 50, 75, 26]
alunos = ['maria', 'joao', 'mario', 'pedro']

final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print('Maior nota: ',final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
