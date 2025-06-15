"""
X: capacidade de produção instalada (ton.)
Y: potência instalada (1000 kW)
Z: Área construída (100 m²)

Com base num critério estatístico, qual das variáveis você escolheria para
estimar a capacidade de produção instalada?
"""
X = [4, 5, 3, 5, 8, 9, 10, 11, 12, 12]
Y = [1, 2, 1, 3, 3, 5, 5 ,7, 6, 7]
Z = [6, 7, 10, 11, 11, 9, 12, 12, 11, 14]


def media(A):
    return sum(A)/len(A)


def correlacao(A, B):
    numerador = sum((A[i] - media(A)) * (B[i] - media(B)) for i in range(len(A)))
    denominador = ((sum((A[i] - media(A))**2 for i in range(len(A))))**(1/2)) * ((sum((B[i] - media(B))**2 for i in range(len(A))))**(1/2))
    return numerador / denominador


print(f'Correlação entre X e Y: {correlacao(X, Y):.3f}')
print(f'Correlação entre X e Z: {correlacao(X, Z):.3f}')
print("""\nConclui-se que existe uma correlação de crescimento proporcional muito maior em XY que em XZ.
Assim, a variável Y é mais adequada para estimar a capidacidade de produção instalada.""")
