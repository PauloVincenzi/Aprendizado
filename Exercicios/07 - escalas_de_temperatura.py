print('-'*100)
print('Relações, termométricas, entre a escala (desconhecida) X e escalas já conhecidas: Celcius, Fahrenheit e Kelvin ')
print('-'*100)
tgx = float(input('Digite a temperatura de gelo, ou solidificação da água, em ºX: '))
tvx = float(input('Digite a temperatura de valor, ou vaporização da água, em ºX '))
tc = tf = tk = tx = 0.0
clist = []
flist = []
klist = []
xlist = []
for c in range(101):
    clist.append('|')
    flist.append('|')
    klist.append('|')
    flist.append('|')
tgc = 0.0
tvc = 100.0
tgf = 32.0
tvf = 212.0
tgk = 273.0
tvk = 373.0
print('-'*100)
esc = str(input("""Deseja inserir uma temperatura em qual escala?
Digite 'C' para celcius, 'F' para fahrenheit, 'K' para kelvin e 'X' para a escala recém construída: """)).upper()
while esc != 'C' and esc != 'F' and esc != 'K' and esc != 'X':
    print('\nEntrada inválida!')
    esc = str(input("Digite 'C' para celcius, 'F' para fahrenheit, 'K' para kelvin e 'X' para a escala recém construída: ")).upper()
print('-'*100)
if esc == 'C':
    tc = float(input('Qual a temperatura em graus Celcius? '))
    tf = (9/5)*(tc)+32
    tk = tc + 273
    tx = (tc/100)*(tvx-tgx) + tgx
elif esc == 'F':
    tf = float(input('Qual a temperatura em graus Fahrenheit? '))
    tc = (5/9)*(tf-32)
    tk = (5/9)*(tf-32)+273
    tx = ((tf-32)*(tvx-tgx)/180) + tgx
elif esc == 'K':
    tk = float(input('Qual a temperatura em graus Kelvin? '))
    tc = tk - 273
    tf = (9/5)*(tk-273)+32
    tx = ((tk-273)*(tvx-tgx)/100) + tgx
else:
    tx = float(input('Qual a temperatura em graus X? '))
    tc = 100*(tx-tgx)/(tvx-tgx)
    tf = (180*(tx-tgx)/(tvx-tgx)) + 32
    tk = (100*(tx-tgx)/(tvx-tgx)) + 273
print('-'*100)
print('ºCelcius     ºFahrenheit     ºKelvin     ºX')
if tc == tvc:
    print(f'{tvc:.1f}'.center(8),f'{tvf:.1f}'.center(20),f'{tvk:.1f}'.center(6),f'{tvx:.1f}'.center(11))
    print('   |              |             |         |')
    print(f'{tgc:.1f}'.center(8), f'{tgf:.1f}'.center(20), f'{tgk:.1f}'.center(6), f'{tgx:.1f}'.center(11))
elif tc > tvc:
    print(f'{tc:.1f}'.center(8), f'{tf:.1f}'.center(20), f'{tk:.1f}'.center(6), f'{tx:.1f}'.center(11))
    print('   |              |             |         |')
    print(f'{tvc:.1f}'.center(8), f'{tvf:.1f}'.center(20), f'{tvk:.1f}'.center(6), f'{tvx:.1f}'.center(11))
    print('   |              |             |         |')
    print(f'{tgc:.1f}'.center(8),f'{tgf:.1f}'.center(20),f'{tgk:.1f}'.center(6),f'{tgx:.1f}'.center(11))
elif tc < tgc:
    print(f'{tvc:.1f}'.center(8), f'{tvf:.1f}'.center(20), f'{tvk:.1f}'.center(6), f'{tvx:.1f}'.center(11))
    print('   |              |             |         |')
    print(f'{tgc:.1f}'.center(8), f'{tgf:.1f}'.center(20), f'{tgk:.1f}'.center(6), f'{tgx:.1f}'.center(11))
    print('   |              |             |         |')
    print(f'{tc:.1f}'.center(8), f'{tf:.1f}'.center(20), f'{tk:.1f}'.center(6), f'{tx:.1f}'.center(11))
else:
    print(f'{tvc:.1f}'.center(8), f'{tvf:.1f}'.center(20), f'{tvk:.1f}'.center(6), f'{tvx:.1f}'.center(11))
    print('   |              |             |         |')
    print(f'{tc:.1f}'.center(8), f'{tf:.1f}'.center(20), f'{tk:.1f}'.center(6), f'{tx:.1f}'.center(11))
    print('   |              |             |         |')
    print(f'{tgc:.1f}'.center(8), f'{tgf:.1f}'.center(20), f'{tgk:.1f}'.center(6), f'{tgx:.1f}'.center(11))
print('-'*100)
etcx = (-100*tgx)/(tvx-tgx-100)
etfx = ((32*tvx)-(212*tgx))/(tvx-tgx-180)
etkx = ((273*tvx)-(373*tgx))/(tvx-tgx-100)
print(f'{etcx:.1f}º Celcius e {etcx:.1f}º X correspondem a mesma temperatura.')
print(f'{etfx:.1f}º Fahrenheit e {etfx:.1f}º X correspondem a mesma temperatura.')
print(f'{etkx:.1f}º Kelvin e {etkx:.1f}º X correspondem a mesma temperatura.')
print('-'*100)
print('FIM'.center(100))
print('-'*100)
