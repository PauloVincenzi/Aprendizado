"""
Assertions (Afirmações / Checagens / Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, o assert retorna None e caso seja falsa levanta um erro
do tipo AssertionError

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de
erro personalizada

# OBS: A palavra 'asser' pode ser utilizada em qualquer função ou códgo nosso.. não
precisa ser exclusivamente nos testes.

# ALERTA: Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parâmetro -0, nenhum assertion
será validado. Ou seja, todas as suas validações já eram.
"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos'
    return a + b

# print(soma_numeros_positivos(-3, 2)) AssertionError: Ambos os números precisam ser positivos
print(soma_numeros_positivos(2, 4))


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente',
        'lanche'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'

# print(comer_fast_food('arroz')) AssertionError: A comida precisa ser fast food
print(comer_fast_food('lanche'))

# ALERTA: Cuidado ao utilizar 'assert'
