"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Prevenindo que o programa pare de funcionar e o usuário receba mensagens de erro.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em casa de problema
"""

# Exemplos 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema\n')

# Tente executar: 'geek()' caso você encontre erros, execute o print.


# OBS: Tratar erro de forma genérica não é a melhor forma de tratamentos de erros. O ideal
# é SEMPRE tratar de forma específica.


# Exemplo 2 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente\n')

# Exemplo 3 - Tratando um erro específico

try:
    len(5)
except TypeError:
    print('Você está aplicando a função/operação a um tipo inadequado\n')

# Exemplo 4 - Tratando um erro específico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}\n')

# Exemplo 5 - Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    len(5)
    # Testar com outros tipos de erros
except NameError as erra:
    print(f'Deu NameError: {erra}\n')
except TypeError as errb:
    print(f'Deu TypeError: {errb}\n')
except:
    print('Deu um erro diferente\n')

# Exemplo 6

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    
    
dic = {'nome': 'Paulo'}
print(pega_valor(dic, 'idade'))
