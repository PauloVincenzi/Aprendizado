"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor.

Nas listas e tuplas o índice corresponde a chave de cada valor (de forma implícita).

Dicionários são representados por chaves {}.

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;
"""

# Criação de dicionários
print('Criação de dicionários')

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai', 'pe': 'Peru'}

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai', pe='Peru')

print(paises)
print(type(paises))

# Acessando elementos
print('Acessando elementos')

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))

# Caso encontre 'py' no dicionário paises, a variável pais será True.
# Caso contrário, a variável será None, ou seja, False.
pais = paises.get('py')
if pais:        # Lembre-se que escrever desta forma pressupõe: 'if pais == True:'
    print('Encontrei o país')
else:
    print('Não encontrei o país')

# Ao invés de usar o if, podemos fazer o seguinte:
# É possível definir um valor padrão.
# Caso a chave dada não seja encontrada, país receberá o valor dado (após a vírgula)
pais = paises.get('py', 'Não encontrado')
print(f'Encontrei o país {pais}')

# Podemos verificar se determinada se encontra em um dicionário
print('Podemos verificar se determinada se encontra em um dicionário')

print('py' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive listas, tuplas e dicionários,
# como chaves de dicionários.
print('Podemos utilizar qualquer tipo de dado, inclusive listas, tuplas e dicionários como chaves em dicts')

# Tuplas são bastante interessantes de serem utilizadas como chave de dicionários (pois as mesmas são imutáveis)
localidades = {
    (35.2945, 39.6719): 'Escritório em Tókio',
    (40.5961, 74.9623): 'Escritório em Tókio',
    (37.2348, 12.4190): 'Escritório em Tókio'
}
print(localidades)

# Adicionar elementos em um dicionário
print('Adicionar elementos em um dicionário')

receita = {'jan': 100, 'feb': 120, 'mar': 300}
print(receita)

# Forma 1

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário
print('Atualizando dados em um dicionário')

# Forma 1

receita['jan'] = 90

print(receita)

# Forma 2

receita.update({'abr': 20})

print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário
print('Remover dados de um dicionário')

receita = {'jan': 100, 'feb': 120, 'mar': 300}
print(receita)

# Forma 1 - Mais comum

retorno = receita.pop('mar')
print(retorno)
print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['feb']
print(receita)

# Caso a chave não existir, será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.

# Métodos de dicionários
print('Métodos de dicionários')

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# A cópia de dicionários (Shallow Copy e Deep Copy) é semelhante à maneira que da cópia de listas

# Forma não usual de criação de dicionários
print('Forma não usual de criação de dicionários')

outro = {}.fromkeys('a', 1)
print(outro)
print(type(outro))

logradouros = {}.fromkeys(['rua', 'avenida', 'marginal', 'viaduto'], 'desconhecido')
print(logradouros)
print(type(logradouros))

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado
# Veja que interessante:

veja1 = {}.fromkeys('teste', 'valor')
print(veja1)

# As lestras 't' e 'e' da palavra teste não foram repetidas, pois em dicionários as chaves não se repetem

# Outro exemplo:

veja2 = {}.fromkeys(range(1, 11), 'novo')
print(veja2)
