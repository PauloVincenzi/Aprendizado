"""
Entendendo o *args

 - O *args é um parâmetro, como outro qualquer. Isso significa que você poderá 
chamar de quaquer coisa, desde que começe com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?

O parâmetros *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
Então desde já, lembre-se que tuplas são imutáveis.
"""

# Exemplo 1

def soma_todos_numeros(n1, n2, n3):
    return n1 + n2 + n3

print(soma_todos_numeros(2, 6, 4))

# Se a entrada possui 4 valores, deveríamos adicionar um outro parâmetro, se possuir 5 valores, adicionar dois outros parâmetros..
# Isso se estende ao infinito, então

def soma_todos_numeros(*args):
    return f'Soma dos valores de {args} é {sum(args)}'

print(soma_todos_numeros())
print(soma_todos_numeros(1,3))
print(soma_todos_numeros(2, 5, 9, 4, 5, 7, 6))

# Exemplo 2

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek!'
    return 'Eu não tenho certeza de quem você é..'

print(verifica_info())
print(verifica_info(1, 2, True, 'Geek', 4, 'University'))
print(verifica_info(3, 'Geek'))

# Exemplo 3

def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 5, 7, 9, 2]

# Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma, ele saberá que precisará desempacotar estes dados.
