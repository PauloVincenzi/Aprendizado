"""
Debuggando com PDB

PDB -> Python Debugger

Debugar significa 'remover os erros/problemas' do código
"""

# OBS: A utilização do print() para debugar código é uma prática ruim.
"""
def dividir(num, den):
    print(f'numerador={num}, denominador={den}')
    try:
        return int(num) / int(den)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))
"""

# Existem formas mais profissionais de se fazer esse 'debug', utilizando debugger
# Em Pyhon, podemos fazer isso em diferentes IDEs, como o VSCode ou utilizando o PDB - Python Debugger

# Exemplo com VSCode: 
# adicione os breakpoints nas linhas em que deseja-se analisar seu comportamento (se o erro está ali ou não)
# clique para debuggar e avance etapas, analisando o que ocorre.

# Teste aqui:

def dividir(num, den):
    try:
        return int(num) / int(den)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
    
print(dividir(4, 3))

print()

# Exemplo 1 com o PDB - Python Debugger

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# * A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando debug foi
# incorporado como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB:
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Angeline'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + sobrenome
curso = 'Progamação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos pdb
