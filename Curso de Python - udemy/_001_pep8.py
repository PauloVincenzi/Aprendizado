"""
PEP8 - Python Enhancements Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica,

Ou, um código mais claro, legível e consistente.

[1] - Utilize Camel Case para nomes de classes (palavras simples com inicial maiúscula);

class Calculadora;
    pass


class CalculadoraCientifica;
    pass


[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação! (a identeção funciona um mais ou menos espaços, porém o padrão visual é 4)
(TAB não é sempre confiável, em alguns computadores, pulam mais de 4 espaços);

[4] - Linhas em branco;

[5] - Imports

Devem ser sempre feitos em linhas separadas

# Import Errado

#import sys, os

# Import Certo

import sys
import os

# Não há problema de utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    TupleType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo deois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções

# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dics ['chave'] = list [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x              = 2
y              = 3
variavel_longa = 6







ESTAS SÃO ALGUMAS REGRAS (NÃO OBRIGATÓRIAS) PARA UM CÓDIGO VISUALMENTE BONITO E ORGANIZADO

"""
