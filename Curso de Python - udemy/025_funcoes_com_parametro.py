"""
Funções com Parâmetro (de entrada)

 - Funções que recebem dados para seerem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
 - Não possuem entrada;
 - Não possuem saída;
 - Possuem entrada mas não possuem saída;
 - Não possuem entrada mas possuem saída;
 - Possuem entrada e saída;

"""

# Refatorando uma função

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado(-2))
print(quadrado(10))

# print(quadrado())
# TypeError -> colocar o parâmetro é obrigatório

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada em uma função
# quantos parâmetros forem necessários. Eles são separados por vírgula.

def soma(a, b, c, n):
    return a+b+c+n

def outra(num1, num2, msg):
    return (num1 * num2) * msg

print(soma(2, -1, 3, 6))
print(soma(0, 0, 2, 1))

print(outra(2, 3, "estudando "))
print(outra(2, -1, "marmelada ")) # A msg não é replicada por um número negativo

# OBS: Se a gente informar um número errado de parâmetros ou argumentos, teremos TypeError

# Nomeie parâmetros com nomes coerentes (legibilidade do código)

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!


# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.

def nome_completo(nome, sobrenome):
    return f'Olá {nome} {sobrenome}'

print(nome_completo('Paulo', 'Eduardo'))
print(nome_completo('Eduardo', 'Paulo'))

print(nome_completo(nome='Paulo', sobrenome='Eduardo'))
print(nome_completo(sobrenome='Eduardo', nome='Paulo'))

# Erro comum na utilização do return (linha com #)

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
#       return total
    return total

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(soma_impares(lista))
