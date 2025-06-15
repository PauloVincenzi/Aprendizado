"""
 Conjuntos

 - Conjuntos em qualquer linguagem de programação, faz referência à Teoria dos Conjuntos
 da Matemática

 - Aqui no Python, os conjuntos são chamados de Sets;

 Dito isto, da mesma forma que na matemática:

 - Sets (conjuntos) não possuem valores duplicados;
 - Sets (conjuntos) não possuem valores ordenados;
 - Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

 Conjuntos são bons para se utilizar quando precisamos armazenar elementos,
 mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
 com chaves, valores e itens duplicados.

 Os conjuntos (sets) são referenciados em Python com chaves {}

 Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;
"""

# Definindo um conjunto:
print('Definindo um conjunto')

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erro e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}

# Podemos verificar se determinado elemento está contido no conjunto (igual as outras coleções estudadas)

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem
print('Importante lembrar que, além de não termos valores duplicados, não temos ordem')

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 12, 1, 44, 5]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 12, 1, 44, 5)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 12, 1, 44, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# OBS: Note que apenas o conjunto não apresenta a ordenação dada a ele.

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.5}

# Usos interessantes com Sets
print('Usos interessantes com Sets')

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(f'Na feira vieram {len(cidades)} pessoas')

# De quantas cidades diferentes?
# Fazer um loop para tirar a repetição?
# Usar um set é mais fácil

print(f'De {len(set(cidades))} cidades diferentes')

# Adicionando elementos em um conjunto
print('Adicionando elementos em um conjunto')

conj = {1, 2, 3}
print(conj)

conj.add(4)
conj.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(conj)

# Remover elementos de um conjunto
print('Remover elementos de um conjunto')
print(conj)

# Forma 1

s.remove(1)  # Não é índice ! Informamos o valor a ser removido.
print(conj)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError

# Forma 2

conj.discard(4)
print(conj)

# OBS: Se o valor não for encontrado, nenhum erro é gerado.

# Copiando um conjunto para outro
print('Copiando um conjunto para outro')

# Forma 1 - Deep Copy - Objetos separados, independentes
print('Deep Copy')

novo1 = conj.copy()
print(novo1)

novo1.add(4)

print(novo1)
print(conj)

# Forma 2 - Shallow Copy - Objetos interligados
print('Shallow Copy')

novo2 = s

novo2.add(1)

print(novo2)
print(s)

# Podemos remover todos elementos de um conjunto usando o clear()

# Métodos Matemáticos de Conjuntos
print('Métodos Matemáticos de Conjuntos')

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
print(f'Conjunto 1: {estudantes_python}')
print(f'Conjunto 2: {estudantes_java}')

# União entre conjuntos:
print('União')

# Forma 1 - Utilizando o union

print(estudantes_python.union(estudantes_java))

# Forma 2 - Utilizando o caractere pipe '|'

print(estudantes_python | estudantes_java)

# Intersecção entre conjuntos:
print('Interseccão')

# Forma 1 - Utilizando o intersection

print(estudantes_python.intersection(estudantes_java))

# Forma 2 - Utilizando o &

print(estudantes_python & estudantes_java)

# Está em um conjunto, mas não está no outro
print('Subtração')

# Forma 1 - Utilizando o difference

print(estudantes_python.difference(estudantes_java))

# Forma 2 - Utilizando o -

print(estudantes_java - estudantes_python)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
print('Soma, Valor Máximo, Valor Mínimo, Tamanho')

# * Se os valores forem todos inteiros ou reais

s = {0, 1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
