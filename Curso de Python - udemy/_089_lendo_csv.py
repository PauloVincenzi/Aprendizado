"""
Lendo arquivos CSV

CSV - Comma Separated Values - Valores Separados por Vírgula

Podemos ter outros tipos de separadores,não somente vírgula (ponto e vírgula, espaço, ..)

# Possível de se trabalhar, mas não é o ideal (trabalhoso)

with open('Aulas\lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    print(dados)
    dados_lista = dados.split(',')[2:]
    print(dados_lista)

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

"""

print('-'*50)

# Reader

from csv import reader

with open('Aulas\lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')


print('-'*50)


# DictReader

from csv import DictReader

with open('Aulas\lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f'{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centímetros')


print('-'*50)

# Por padrão o método reader e DictReader usa a vírgula como separador,
# Caso tiver que mudar o separador:

# DictReader(arquivo, delimiter=' ')
