"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}
"""

receita = {'jan': 100, 'feb': 250, 'mar': 180}

print(receita)

# Iterar sobre dicionários
print('Iterar sobre dicionários')

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} gerou-se R$ {receita[chave]}')

# Acessando as chaves
print('Acessando as chaves')

print(receita.keys())

for chave in receita.keys():
    print(chave)

# Acessando os valores
print('Acessando os valores')

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
print('Desempacotamento de dicionários')

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, Valor Máximo*, Valor mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
