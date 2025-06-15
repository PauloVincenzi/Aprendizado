print('-' * 150)
print("""Considere um recipiente com volume conhecido, este recipiente será preenchido com um 
líquido qualquer (exceto a água, pois esta apresenta comportamento anômalo de 0ºC à 4ºC),
conhecendo os coeficientes de dilatação volumétrica do líquido e o do recipiente,
determine qual o volume de líquido adicionado ao recipiente para que o volume vazio
no recipiente seja constante qualquer que seja a temperatura.""")
print('-' * 150)
vt = float(input('Qual o volume do recipiente (em litros)? '))
while vt <= 0:
    vt = float(input('Digite um volume do recipiente positivo: '))
ar = float(input('Qual o valor (em micro ºC^-1) do coeficiente de dilatação volumétrica do recipiente? '))/1000000
while ar <= 0:
    ar = float(input('Digite um valor (em micro ºC^-1) do coeficiente de dilatação volumétrica do recipiente positivo: ')) / 1000000
al = float(input('Qual o valor (em micro ºC^-1) do coeficiente de dilatação volumétrica do líquido? '))/1000000
while al <= 0:
    al = float(input('Digite um valor (em micro ºC^-1) do coeficiente de dilatação volumétrica do líquido positivo: ')) / 1000000
varv = float(input('Qual a variação do volume? '))
while 10*varv >= vt:
    varv = float(input('Digite uma variação do volume menor que um décimo do volume total do recipente: '))
print('-' * 150)
varvreal = 0.1
varvap = 0.0
varvrec = 0.0
vc = 0.0
antvarvreal = 0.1
fvarvreal = 0.1
fvarvrec = 0.0
bo = False
if al > ar:
    while ((abs(fvarvreal) != abs(fvarvrec)) and (vc < vt)) or bo == True:
        bo = False
        vc += varv
        vv = vt - vc
        varvreal = al * vc
        varvap = (al - ar) * vc
        varvrec = ar * vt
        svarvreal = f'{varvreal:.11f}'
        svarvrec = f'{varvrec:.11f}'
        fvarvreal = float(svarvreal)
        fvarvrec = float(svarvrec)
        print(
            f'V.líquido: {vc:.5f} - V.vazio: {vv:.5f} - VarV.liq.real: {varvreal:.10f} - VarV.recipiente: {varvrec:.10f} - VarV.liq.aparente: {varvap:.10f}')
        if varvreal == varvrec:
            print('CEREJA')
            break
        if abs(antvarvreal) < abs(varvrec) < abs(varvreal):
            print(f"""------------------------------------------------------------------------------------------------------------------------------------------------------
Esse ponto de estabilidade não pode ser encontrado com uma variação de do volume igual à {varv},""")
            e = str(input('Dessa forma, tornemos a variação de d 2x menor? [S/N] ')).upper()
            print('-' * 150)
            while e not in ['S', 'N']:
                print('Entrada incorreta!')
                e = str(input('Tornar a variação do volume 2x menor? [S/N] ')).upper()
                print('-' * 150)
            if e == 'N':
                break
            else:
                vc -= varv * 1.5
                varv = varv / 2
                bo = True
        antvarvreal = varvreal
    print('-' * 150)
    print(f"""Com as informações fornecidas, a proporção entre o volume vazio e o volume preenchido com o líquido
permanecerá constante quando o recipiente for preenchido com {vc:.6f} litros do líquido em questão,
de modo que {(vt-vc):6f} litros do recipiente ficarão vazios.""")
else:
    print(f"""Considerando que o coeficiente de dilatação volumétrica do recipiente é maior que o coeficiente
de dilatação do líquido, não existe uma quantidade de líquido menor ou igual a capacidade máxima
do recipiente ({vt} L) tal que a dilatação real do líquido seja igual a dilatação do recipiente.
Assim, é impossível fazer com que a proporção entre o volume de líquido
e o volume vazio do recipiente torne-se constante.""")
print('-' * 150)
print('FIM'.center(150))
print('-' * 150)
