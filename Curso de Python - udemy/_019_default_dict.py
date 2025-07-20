"""
Módulo Collections - Default Dict

# Recap Dicionários

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

# print(dicionario['outro']) # ??? KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criar e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores.

"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro']) # KeyError no dicinário comum, mas aqui não

print(dicionario)

# Todas as funções aprendidas em um dicionário, podem ser usadas aqui



