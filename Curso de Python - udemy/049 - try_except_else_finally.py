"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DE DADOS DEVE SER TRATADA!

OBS: A função do usuário é destruir seu sistema.
"""

# Nunca fazer:

# num = int(input('Informe um número: '))
# print(f'Você digitou {num}')

# Sempre:

num = None

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# Else -> É executado somente se não ocorrer o erro.

print()

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')

# Tente executar o código, se der erro, execute except e após isso o finally. Se não der erro, execute o else e após isso o finally.
# OBS: O bloco finally é SEMPRE executado.
# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

print()

# Exemplo mais complexo

# Forma 'errada'
"""
def dividir(num, den):
    return num / den

try:
    num1 = int(input('Informe o numerador: '))
    num2 = int(input('Informe o denominador: '))
except ValueError:
    print(f'O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print(dividir(num1, num2))
"""

# O tratamento deve ser ainda na função, sem retornar um valor que possivelmente dá erro.

# Forma 'certa'

def dividir(num, den):
    try:
        return int(num) / int(den)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'
    
num1 = input('Informe o numerador: ')
num2 = input('Informe o denominador: ')

print(dividir(num1, num2))

"""
Ao invés de retornar uma mensagem específica e um except NomeDoErro para cada possivel erro, podemos: 

try:
    execução
except (ValueError, TypeError, ...)
    print('Deu algum problema')
"""
