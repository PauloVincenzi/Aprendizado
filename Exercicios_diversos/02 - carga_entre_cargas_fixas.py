print('-' * 150)
print("""Na reta horizontal há cargas q1 e q2 separadas por d metros de distância. 
Entre q1 e q2 existe uma carga q3""")
print('-' * 150)
q1 = float(input('Qual o valor (em micro coulomb) da carga q1? '))/1000000
q2 = float(input('Qual o valor (em micro coulomb) da carga q2? '))/1000000
q3 = float(input('Qual o valor (em micro coulomb) da carga q3? '))/1000000
dt = float(input('Qual a distancia (em metros) entre q1 e q2? '))
vd = float(input('Qual a variação da distância (d)? '))
while (10*vd) >= dt:
    vd = float(input('Digite uma variação de d menor ou igual que um décimo da distância entre q1 e q2: '))
print('-' * 150)
t = float()
d = float()
ffant = 0.0
dant = 0.0
ff13 = 0.1
ff32 = 0.0
while (abs(ff13) != abs(ff32)) and (d < dt):
    e = ''
    d += vd
    if (q1 > 0 and q3 > 0) or (q1 < 0 and q3 < 0):
        f13 = (9 * (10 ** 9)) * q1 * q3 / (d ** 2)
    else:
        f13 = -(9 * (10 ** 9)) * q1 * q3 / (d ** 2)
    if (q3 > 0 and q2 > 0) or (q3 < 0 and q2 < 0):
        f32 = -(9 * (10 ** 9)) * q3 * q2 / ((dt - d) ** 2)
    else:
        f32 = (9 * (10 ** 9)) * q3 * q2 / ((dt - d) ** 2)
    sf13 = f'{f13:.6f}'
    ff13 = float(sf13)
    sf32 = f'{f32:.6f}'
    ff32 = float(sf32)
    fr = f13 + f32
    sfr = f'{fr:.7f}'
    ffr = float(sfr)
    if fr < 0:
        print(f'Distância q1-q3: {d:.5f} - F Coulomb q1-q3: {f13:.5f}       Distância q3-q2: {(dt-d):.5f} - F Coulomb q3-q2: {f32:.5f}          Força R para Esquerda: {fr:.5f}')
    else:
        print(f'Distância q1-q3: {d:.5f} - F Coulomb q1-q3: {f13:.5f}       Distância q3-q2: {(dt-d):.5f} - F Coulomb q3-q2: {f32:.5f}          Força R para Direita: {fr:.5f}')
    if ffant > 0 > ffr:
        print(f"""------------------------------------------------------------------------------------------------------------------------------------------------------
A distância q1-q3 para que q3 fique estável corresponde a algum valor próximo ao intervalo [{dant:.6f}, {d:.6f}];
A distância q3-q2 para que q3 fique estável corresponde a algum valor próximo ao intervalo [{(dt-d):.6f}, {(dt-dant):.6f}];
Esse ponto de estabilidade não pode ser encontrado com uma variação de d igual à {vd},""")
        e = str(input('Dessa forma, tornemos a variação de d 2x menor? [S/N] ')).upper()
        print('-' * 150)
        while e not in ['S', 'N']:
            print('Entrada incorreta!')
            e = str(input('Tornar a variação de d 2x menor? [S/N] ')).upper()
            print('-' * 150)
        if e == 'N':
            break
        else:
            d -= vd*1.5
            vd = vd / 2
    sfant = f'{fr:.7f}'
    ffant = float(sfant)
    dant = d
if e not in ['S', 'N']:
    print('-' * 150)
print(f'A carga q3 se mantém estável quando está {d:.6f} metros de distância de q1 e {(dt-d):.6f} metros de distância de q2.')
print('-'*150)
print('FIM'.center(150))
print('-'*150)

