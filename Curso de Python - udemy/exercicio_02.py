def maior_valor(lista):
    rol = sorted(lista)
    print(f'O maior valor digitado foi {rol[len(rol)-1]}')

resp = ''
numeros = list()
while resp != 'N':
    numeros.append(int(input('Digite um valor: ')))
    resp = input('Deseja digitar outro valor? ').upper()
    while resp != 'S' and resp != 'N':
        print('Entrada inválida!')
        resp = input('Deseja digitar outro valor? ').upper()

maior_valor(numeros)

"""
Após ver a resolução do intrutor, seria mais facil usar max()
"""
