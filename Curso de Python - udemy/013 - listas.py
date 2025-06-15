"""
Listas (list)

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem dinâmicos e também de podermos colocar QUALQUER tipo de dado.

Linguanges C/Java:  Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 vetores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possum tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

Listas são mutáveis: Ou seja, elas podem ser mudadas constantemente.

"""

print(type([]))
print()

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['P', 'a', 'u', 'l', 'o', ' ', 'E', 'd', 'u', 'a', 'r', 'd', 'o']

lista3 = []

lista4 = list(range(11))

lista5 = list('Paulo Eduardo')

# Podemos facilmente chegar se determinado valor está contido na lista
print('Podemos facilmente chegar se determinado valor está contido na lista')
num = 7
if num in lista4:
    print(f'Encontrei o número {num} na lista4')
else:
    print(f'Não encontrei o número {num} na lista4')

# Podemos facilmente ordenar uma lista. (Números crescente ou caractéres em ordem alfabética)
print('Podemos facilmente ordenar uma lista.')
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print('Podemos facilmente contar o número de ocorrências de um valor em uma lista')
print(lista1.count(1))
print(lista5.count('a'))

# Adicionar elementos em listas
print('Adicionar elementos em listas')

"""
Para adicionar elementos em listas, utilizamos a função append
"""
print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append, nós só conseguimos adicionar um elemento por vez
#  lista1.append(8, 3, 1) # Erro

# Coloca a lista como elemento único (sublista)
print('Coloca a lista como elemento único (sublista)')
lista1.append([8, 3, 1])
print(lista1)

if [8, 3,1 ] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

# Coloca cada elemento da lista como valor adicional à lista (serve apenas para iteráveis)
print('Coloca cada elemento da lista como valor adicional à lista')
lista1.extend([65, 31, 9])
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice. (Não substitui, adiciona e desloca o restante da lista)
print('Podemos inserir um novo elemento na lista informando a posição do índice.')
lista1.insert(2, 'Novo valor')
print(lista1)

# Ambos casos dá certo
# lista1 = lista1 + lista2
# lista1.extend(lista2)

# Podemos facilmente inverter uma lista
print('Podemos facilmente inverter uma lista')
# lista5.reverse()
# print(lista5)
# ou
print(lista5[:: -1])

# Copiar uma lista
lista6 = lista2.copy()

# Quantos elementos tem uma lista?
print('Quantos elementos tem uma lista?')
print(len(lista2))

# Podemos facilmente remover o último elemento de uma lista
print('Podemos facilmente remover o último elemento de uma lista')
print(lista1)
retorno = lista1.pop()
print(retorno)
print(lista1)

# OBS: Ao removermos um objeto com o pop, o valor deste objeto é sempre retornado.

# Podemos remover um elemento pelo índice. Os elementos da direita serão deslocados para esquerda.
print('Podemos remover um elemento pelo índice. Os elementos da direita serão deslocados para esquerda.')
lista1.pop(2)
print(lista1)

# Podemos remover todos os elementos
print('Podemos remover todos os elementos')
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
print('Podemos facilmente repetir elementos em uma lista')
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista
print('Podemos facilmente converter uma string para uma lista')

# Exemplo 1

curso = 'Bacharelado em Estátistica - Ufscar'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2

curso = 'Bacharelado,em,Estátistica,-,Ufscar'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
print('Convertendo uma lista em uma string')

lista6 = ['Licenciatura', 'em', 'Biologia', '-', 'Ufscar']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

lista1.pop()
lista1.pop()
lista1.pop()
print(lista1)

# Iterando sobre listas
print('Iterando sobre listas')

# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(f'Soma: {soma}')

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
print('Utilizando variáveis em listas')

n1 = 2
n2 = 0
n3 = 1
n4 = 6
n5 = 3

l = [n1, n2, n3, n4, n5]
print(l)

# Fazemos acesso aos elementos de forma indexada
print('Fazemos acesso aos elementos de forma indexada')

cores = ['verde', 'amarelo', 'azul', 'branco', 'preto']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
print('Fazer acesso aos elementos de forma indexada inversa')

print(cores[-1])
print(cores[-2])

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
print('Gerar indice em um for')

for indice, cor in enumerate(cores):
    print(indice, cor)

# OUTROS MÉTODOS NÃO TÃO IMPORTANTES MAS TAMBÉM ÚTEIS

# Encontrar o índice de um elemento da lista1
print('Encontrar o índice de um elemento da lista1')
print(lista1)

# OBS: Caso não tenha esse elemento na lista, será apresentado erro ValueError

print('Em qual índice esta o valor 99')
print(lista1.index(99))

# OBS: Retorna o indice do primeiro elemento encontrado
print('Em qual índice esta o valor 1')
print(lista1.index(1))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print('Em qual índice está o valor 1 a partir do índice 1')
print(lista1.index(1, 1)) # buscando a partir do índice 1

# Podemos fazer busca dentro de um range, incio/fim
print('Em qual índice está o valor 27, considerando o intervalo [4, 7[ ')
print(lista1.index(27, 4, 7))

# Revisão de slicing
print('Revisão de slicing')

# lista[inicio:fim:passo]
# range(inicio:fim:passo]

# Trabalhando com slice de lista com o parâmetro 'inicio'

print(lista1[2:]) # iniciando no índice 2 e pegando todos os elemento restantes

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista1[:6]) # início padrão (índice zero) e pega todos elemento até o elemento de índice 6

# Trabalhando com slice de lista com parâmetros 'início' e 'fim' (intervalo)

print(lista1[3:7]) # inícia no índice 3 e termina no índice 7

# Trabalhando com slice de lista com parâmetro 'passo'

print(lista1[::2]) # começa em zero e vai até o final, de 2 em 2

print(lista1[::-1]) # começa pelo final e vai até o começo, de 1 em 1

# Invertendo valores em uma lista
print('Invertendo valores em uma lista')

nomes = ['Paulo', 'Eduardo', 'De', 'Vincenzi']
print(nomes)
nomes[0], nomes[1], nomes[2], nomes[3] = nomes[3], nomes[2], nomes[1], nomes[0]
print(nomes)

# Há uma forma melhor de inverter
nomes = ['Paulo', 'Eduardo', 'De', 'Vincenzi']
print(nomes)
nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho (* Se os valores forem todos inteiros ou reais.)

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print('Soma da lista')
print(sum(lista1))
print('Valor máximo da lista')
print(max(lista))
print('Valor mínimo da lista')
print(min(lista))
print('Tamanho da lista')
print(len(lista))

# Transformar uma lista em tupla
print('Transformar uma lista em tupla')

print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
print('Desempacotamento de listas')

n1, n2, n3, n4 = lista

print(n1)
print(n2)
print(n3)
print(n4)

# OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError

# IMPORTANTE - COBRADO ATÉ EM ENTREVISTAS DE EMPREGO

# Copiando uma lista para outra (Deep Copy e Shallow Copy)
print('Copiando uma lista para outra (Shallow Copy e Deep Copy)')

# Forma 1 - Deep Copy
print('Deep Copy')

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy
print('Shallow Copy')

lista = [1, 2, 3]
print(lista)

nova = lista # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificações em uma das listas, essas modificações se refletiram em ambas as listas.
# Isso em Python é chamado de Shallow Copy.
