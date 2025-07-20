"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime


# print(dir(datetime))

# Suporta o intervalo de ano:
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print('-'*50)


# Retorna data e hora corrente
print(datetime.datetime.now())

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

print('-'*50)


# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()
print(inicio)
# Alterar o horário para 16 horas, 0 minutos, 0 segundos, 0 microsegundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

# Recebendo dados do usuário e convertendo para data

evento = datetime.datetime(2019, 1, 1, 0)
print(evento)

print()

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
print(f'{nascimento}  -  {type(nascimento)}')

nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(f'{nascimento}  -  {type(nascimento)}')

"""

import datetime

evento = datetime.datetime.now()

# Acessa individual dos elementos de data e hora

print(evento.year) # ano
print(evento.month) # mês
print(evento.day) # dia
print(evento.hour) # hora
print(evento.minute) # minuto
print(evento.second) # segundo
print(evento.microsecond) # microsegundo

