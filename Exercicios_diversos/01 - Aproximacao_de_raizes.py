print(""" ------------------------------------------------------------------------------------------------- 
 Este programa irá apresentar aproximações de raízes tal qual: 
 n^(1/2) = (n+q)/2q^(1/2)   e   q é o quadrado perfeito mais próximo de n
 -------------------------------------------------------------------------------------------------
 Para fins de comparar as aproximações, digite um intervalo o qual
 o programa calculará a raiz aproximada (segundo a fórmula apresentada) 
 e a raiz exata (segundo a calculadora) de todos os seus valores inteiros de forma aproximada.
 -------------------------------------------------------------------------------------------------
""")

a = int(input('Início do intervalo: '))
b = int(input('Fim do intervalo: '))
while a > b:
    if a > b:
        print('\nErro. Digite outros valores!\n')
    a = int(input('Início do intervalo: '))
    b = int(input('Fim do intervalo: '))
print('\n-------------------------------------------------------------------------------------------------')
n = a
raizn = float
while n != b+1:
    c_mais = c_menos = q = 0
    while (n + c_mais) / (n + c_mais) ** (1 / 2) != (n + c_mais) // (n + c_mais) ** (1 / 2):
        c_mais += 1
    while (n - c_menos) / (n - c_menos) ** (1 / 2) != (n - c_menos) // (n - c_menos) ** (1 / 2):
        c_menos += 1
    if (n - c_menos) < 0:
        q = (n + c_mais)
    elif c_menos > c_mais:
        q = (n + c_mais)
    else:
        q = (n - c_menos)
    raizn = (n + q)/(2*(q**(1/2)))
    print(f'Raiz de {n}: aproximadamente {raizn:.5f} e exatamente {(n**(1/2)):.5f}')
    n += 1
print('-------------------------------------------------------------------------------------------------')



