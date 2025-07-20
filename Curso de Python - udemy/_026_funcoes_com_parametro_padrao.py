"""
Funções com Parâmetro Padrão (Default Paramters)

 - Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')
print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

 - Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções, etc
"""

def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(3, 5))
print(exponencial(3)) # Ao colocar o parâmetro potencia=2, este parâmetro se torna opcional, onde ao não ser
# passado pel usuário, o parâmetro assume o valor padrão definido (2)

# OBS: Em funções Python, os parâmetros com valores default DEVEM sempre estarem ao final da declaração.
# Caso contrário, ERRO!

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(nome='Ozzy'))

# Funções como parâmetros

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confuções...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # Variável global

def diz_oi():
    adjetivo = 'legal'
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor} {adjetivo}'

print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

# Será impresso o instrutor definido pela global (pense que a função não 'rodou' para definir intrutor localmente)
print(instrutor)

# Tentar imprimir / utilizar uma variável local sem que a função a retorne, tornará em erro.
# print(adjetivo)


# Se puder evitar variáveis globais, evite!
# UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada):
"""
total = 0

def incrementa():
    total += 1
    return total
"""

# Forma correta (Avisa que queremos utilziar a variável global):
total = 0

def incrementa():
    global total
    total += 1
    return total 

print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador # Diz que a variável não é global (definida dentro de uma função), mas também não é local (se fosse estaria dentro da função dentro)
        contador += 1
        return contador
    return dentro()

print(fora())
print(fora())
