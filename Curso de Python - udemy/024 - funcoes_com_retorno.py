"""
Funções com retorno

EX: pop() é uma função com retorno, enquanto print() é uma função sem retorno

OBS1: Em Python, quando uma função não retorna nenhum valor, o retorno é None

OBS2: Não precisamos necessariamente criar uma variável para receber o retorno
de uma função. Podemos passar a execução da função para outras funções.

OBS3: Sobre a palavra reservada 'return'

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
"""

# Exemplo função que imprime mas não retorna

def quadrado_de_7():
    print(7*7)

ret = quadrado_de_7()

print(f' Retorno: {ret}')

# Vamos refatorar (reescrever / redefinir) esta função para que ela retorne o valor
print('Após refatorar:')

def quadrado_de_7():
    return 7 * 7

# ret = quadrado_de_7()
# print(f' Retorno: {ret}') 

print(f'Retorno: {quadrado_de_7()}')

# Caso desejo printar algo. Por que retornar um valor e printar este retorno, ao invés de printar direto?
# O retorno funciona como se fosse uma variável, de modo que pode ser manipulado;
# Ex: print(funcao_definida_com_retorno + outra_variavel)

# Exemplo (OBS3):

def diz_oi():
    print('Estou sendo executado antes do return..')
    return 'Oi'
    print('Estou sendo executado após o return..')


print(diz_oi())

# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

 