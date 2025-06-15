"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

"""

# CUIDADO 1: As tuplas são representadas por (), mas veja:
print('CUIDADO 1')

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
print('CUIDADO 2')

tupla3 = (4)   # Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,)   # Isso é uma tupla!
print(tupla4)
print(type(tupla4))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parênteses
# (4) -> Não é tupla
# (4,) -> É tupla
# 4, -> É tupla

# Método para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Concatenação de tuplas
print('Concatenação de tuplas')

tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = 4, 5, 6
print(tupla2)
print(tupla1 + tupla2)
print(tupla1)
print(tupla2)
print('Tuplas são imutáveis, mas podemos sobrescrever seus valores')
tupla3 = tupla1 + tupla2 + tupla1
print(tupla3)

# Copiando uma tupla para outra
print('Copiando uma tupla para outra')

tupla = (1, 2, 3)
print(tupla)

nova = tupla    # Na tupla não temos o problema de Shallow Copy
print(nova)
print(tupla)

# Exemplos de funcionalidades feitas para tuplas semelhantes a maneira que são feitas para listas:
#   Desempacotamento de tupla (x, y,.. = tuple)
#   Podemos gerar uma tupla dinamicamente com range (tupla = tuple(range(x)))
#   Verificar se determinado elemento está contido na tupla (x in tuple)
#    Soma*, Valor Máximo*, Valor Mínimo* e tamanho (sum, max, min, len)
#   Contando elementos detro de uma tupla (count)
#   O acesso a elementos de uma tupla ([])
#   Verificar em qual índice um elemento está na tupla (index)

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção
# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*.

# * Isso porque trabalhar com elementos imutáveis traz segurança para o código
