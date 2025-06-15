s01 = float(input('Qual a posição inicial do carro 1? (em metros) '))
s02 = float(input('Qual a posição inicial do carro 2? (em metros) '))
v01 = float(input('Qual a velocidade inicial do carro 1? (em metros por segundo) '))
v02 = float(input('Qual a velocidade inicial do carro 2? (em metros por segundo) '))
a1 = float(input('Qual a aceleração do carro 1? '))
a2 = float(input('Qual a aceleração do carro 2? '))
vart = float(input('Exibir posições com uma variação de tempo de: '))
t = s1 = s2 = 0.0
print(type(s1))
print('Tempo  -  Posição do carro 1  -  Posição do carro 2')
if s01 > s02:
    s1 = s01 + v01*t + ((a1*(t**2))/2)
    s2 = s02 + v02*t + ((a2*(t**2))/2)
    while s2 < s1:
        s1 = s01 + v01*t + ((a1*(t**2))/2)
        s2 = s02 + v02*t + ((a2*(t**2))/2)
        print(f'Tempo: {t:.3f}      Position 1: {s1:.3f}        Position 2: {s2:.3f}')
        t += vart
    print(f'Portanto o veículo 2 ultrapassou o veículo 1 no instante de tempo t = {t:.2f} segundos na posição aproximada de {((s1+s2)/2):.2f} metros com uma velocidade de {(v02+a2*t):.2f} m/s')
else:
    s1 = s01 + v01*t + ((a1*(t**2))/2)
    s2 = s02 + v02*t + ((a2*(t**2))/2)
    while s1 < s2:
        s1 = s01 + v01*t + ((a1*(t**2))/2)
        s2 = s02 + v02*t + ((a2*(t**2))/2)
        print(f'Tempo: {t:.3f}      Position 1: {s1:.3f}        Position 2: {s2:.3f}')
        t += vart
    print(f'Portanto o veículo 1 ultrapassou o veículo 2 no instante de tempo t = {t:.2f} segundos na posição aproximada de {((s1+s2)/2):.2f} metros com uma velocidade de {(v01+a1*t):.2f} m/s')