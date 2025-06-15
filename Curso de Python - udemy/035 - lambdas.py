"""
Utilizando lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas.

"""

# Exemplo de função em Python

def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão Lambda?
calc = lambda x: 3 * x + 1

print(calc(4))

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' PAulo    ', 'EDUARDO'))
print(nome_completo(' maicon', '    kruGUer '))

# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradburry', 'Robery Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

# Mais um

# Função quadrática

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a*x**2 + b*x + c"""
    return lambda x: a*x**2 + b*x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

# não é preciso definir a variável teste

print(geradora_funcao_quadratica(2, 5, 3)(2))
