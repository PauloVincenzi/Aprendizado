"""
Você sabe em qual dia da semana você nasceu? (segunda, terça, quarta, ... , domingo)

Além disso, você sabe em quais anos o seu aniversário cairá novamente neste dia?

# Chamemos isto de superaniversário: a data de seu aniversário cujo dia da semana coincide com o dia da semana de seu nascimento
"""

superaniversarios = []

from datetime import datetime, date

aniversario0 = input('Quando você nasceu? dd/mm/yyyy ')
aniversario0 = aniversario0.split('/')
aniversario = datetime(year=int(aniversario0[2]), month=int(aniversario0[1]), day=int(aniversario0[0]))

print('Encontrar superaniversarios em qual periodo?')
inicio = int(input('Início: '))
fim = int(input('Até: '))

for n in range(fim - inicio + 1):
    data_teste = datetime(year=inicio+n, month=int(aniversario0[1]), day=int(aniversario0[0]))
    if data_teste.weekday() == aniversario.weekday():
        superaniversarios.append(inicio + n)

print('-'*100)

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma sexta feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em um sábado')
else:
    print('Você nasceu em um domingo')


print('Anos de superaniversários:')

print(superaniversarios)

print('-'*100)
