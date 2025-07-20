fr = float()
ar = float()
t = float()
z = 0
print('-'*100)
print("""Um objeto O de carga q1 está verticalmente alinhado com um ponto fixo P de carga q2.
O ponto P está situado em uma posição 'zero'.""")
s0 = float(input('Qual a posição (vertical, em metros e diferente de zero) do objeto O? '))
s = s0
q1 = abs(float(input('Qual a carga q1? (em micro coulomb) '))/1000000)
q2 = abs(float(input('Qual a carga q2? (em micro coulomb) '))/1000000)
m = float(input('Qual o peso (em kg) do objeto O? '))
a = float(input('Deseja analisar a posição do objeto O em quantos segundos? '))
vt = float(input('Qual a variação de t (tempo)? '))
fp = m * 9.8
d = abs(s0)
fe = (9 * (10 ** 9)) * q1 * q2 / (d ** 2)
print('-'*100)
print("""Considere que as cargas q1 e q2 são ambas positivas ou que são ambas negativas.
Isto é, existe uma força elétrica de repulsão entre as cargas.
Além disso, considere que a constante eletrostática no vácuo vale 9*10^9 Nm^2/C^2.""")
print('-'*100)
while t < (a+vt):
    if t == 0:
        print(f'Time: {t:.4f} - Position: {s:.7f} - Ar: {z:.7f} - Fr: {z:.7f} - F Coulomb: {z:.7f} - F Weight: {z:.7f}')
    else:
        fe = (9 * (10 ** 9)) * q1 * q2 / (d ** 2)
        if s < 0:
            fr = - fp - fe
            ar = fr / m
        else:
            fr = - fp + fe
            ar = fr / m
        v = ar * t
        s = s0 + (v * vt) + ((1/2)*ar*(vt**2))
        s0 = s
        d = abs(s - 0)
        if s < 0:
            print(f'Time: {t:.4f} - Position: {s:.8f} - Ar: {ar:.8f} - Fr: {fr:.8f} - F Coulomb: {-fe:.8f} - F Weight: {-fp:.8f}')
        else:
            print(f'Time: {t:.4f} - Position: {s:.8f} - Ar: {ar:.8f} - Fr: {fr:.8f} - F Coulomb: {fe:.8f} - F Weight: {-fp:.8f}')
    sfe = f'{fe:.8f}'
    ffe = float(sfe)
    sfp = f'{fp:.8f}'
    ffp = float(sfp)
    if ffe == ffp:
        print('-'*100)
        print(f"""O loop foi interrompido pois o objeto O entrou em equilíbrio, isto é, a força peso é igual a força de coulomb.
Portanto, o objeto O permanece estável em {s:.7f} metros acima do ponto P.""")
        break
    t += vt
print('-'*100)
print('FIM'.center(100))
print('-'*100)