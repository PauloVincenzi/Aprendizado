"""
Método de Data e Hora

# Com now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana. weekday()

# Os dias da semana do método weekday() começam em 0, sendo esta a segunda feira
# 0 - Segunda feira (Monday)
# 1 - Terça feira (Tuesday)
# 2 - Quarta feira (Wednesday)
# 3 - Quinta feira (Thursday)
# 4 - Sexta feira (Friday)
# 5 - Sábado (Saturday)
# 6 - Domingo (Sunday)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())

aniversario = input('Qual sua data de nascimento? dd/mm/yyyy ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

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

# Formatando datas/horas com strftime() (String Format Time)
# Há várias formatações possíveis
# dd/mm/yyyy

hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')

print(hoje_formatado)

d = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

print(d)

nascimento = input('Qual a sua data de nascimento? dd/mm/yyyy ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# Somente a hora

almoco = datetime.time(12, 30, 0)

print(almoco)

# Marcando tempo de execução do nosso código com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=100000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=100000)
print(tempo)
"""

import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(teste(2))

print()

print(timeit.timeit(functools.partial(teste, 2), number=10000))
