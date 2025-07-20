"""
**kwargs

Poderíamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs existe que utiizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

Nas nossas funções, podemos ter (NESTA ORDEM):
 - Parâmetros obrigatórios
 - *args
 - Parâmetros default (não obrigatórios)
 - **kwargs
"""

# Exemplo 1

def cores_favoritas(**kwargs):
    print(kwargs)
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

# Exemplo 2

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é ...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Exemplo 3

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)
    print()

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felipe', 4, 5 ,3, solteiro=True)
minha_funcao(34, 'Mateus', eu='Não', voce= 'Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f'{kwargs['nome']} {kwargs['sobrenome']}'

nomes = {'nome': 'Paulo', 'sobrenome': 'Vincenzi'}

print(mostra_nomes(**nomes))

# ----------

def soma_numeros(a, b, c):
    print(a + b + c)

soma_numeros(1, 2, 3)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_numeros(*lista)
soma_numeros(*tupla)
soma_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_numeros(**dicionario)

# OBS! Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função.