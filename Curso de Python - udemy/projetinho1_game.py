"""
001 - GAME

Descrição:
Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuário escolher o nível de
dificuldade do jogo e após isso gera e apresenta, de forma aletaória, um cálculo para que possamos informar o resultado.

Iremos limitar as operações em somar, diminuir e multiplicar. Se o usuário acertar a resposta, somará 1 ponto ao seu score.
Acertando ou errando, ele poderá ou não continuar o jogo.
"""

import random

def soma(dif):
    if dif == '1':
        a = random.randint(0, 30)
        b = random.randint(0, 30)
    elif dif =='2':
        a = random.randint(0, 500)
        b = random.randint(0, 500)
    else:
        a = round(random.uniform(0, 1000), 2)
        b = round(random.uniform(0, 1000), 2)
    print(f'Quanto é {a} + {b} ?')
    return a, b, a+b

def subtracao(dif):
    if dif == '1':
        a = random.randint(0, 30)
        b = random.randint(0, 30)
    elif dif =='2':
        a = random.randint(0, 500)
        b = random.randint(0, 500)      
    else:
        a = round(random.uniform(0, 1000), 2)
        b = round(random.uniform(0, 1000), 2)
    print(f'Quanto é {a} - {b} ?')
    return a, b, a-b
    
def multiplicacao(dif):
    if dif == '1':
        a = random.randint(0, 10)
        b = random.randint(0, 10)
    elif dif =='2':
        a = random.randint(0, 50)
        b = random.randint(0, 50)
    else:
        a = random.randint(0, 300)
        b = random.randint(0, 300)
    print(f'Quanto é {a} * {b} ? (com duas casas decimais, se necessário)')
    return a, b, a*b

def divisao(dif):
    if dif == '1':
        a = random.randint(0, 5)
        b = random.randint(1, 5)
    elif dif =='2':
        a = random.randint(0, 50)
        b = random.randint(1, 50)
    else:
        a = random.randint(0, 300)
        b = random.randint(1, 300)
    print(f'Quanto é {a} / {b} ? (com duas casas decimais, se necessário)')
    return a, b, a/b
    
points = 0
operacoes = [soma, subtracao, multiplicacao, divisao]

print('-'*100)

nome = input('Qual o seu nome? ')
print(f'Bem vindo ao jogo matemático {nome}!')

print('-'*100)

dificuldade = input('Informe a dificuldade [1 = fácil; 2 = médio; 3 = difícil]: ')
while dificuldade not in ['1', '2', '3']:
    print('Entrada incorreta!')
    dificuldade = input('Informe a dificuldade [1 = fácil; 2 = médio; 3 = difícil]: ')

continuar = ''
while continuar != 'SAIR':
    print('-'*100)

    operacao_escolhida = random.choice(operacoes)
    a, b, gabarito = operacao_escolhida(dificuldade)

    while True:
        resposta = input('Digite um número: ')
        try:
            resposta = float(resposta)
            break
        except ValueError:
            print('Entrada incorreta!')
    
    print('-'*100)

    if resposta == gabarito:
        print('Você acertou!!')
        print('+ 1 point')
        points += 1
    else:
        print('Você errou :(')
        print(f'A resposta correta para a operação de {str(operacao_escolhida)} entre {a} e {b} é {gabarito}')
    
    print('-'*100)
    continuar = input(f'Você fez {points} ponto(s) até então, se desejar finalizar o jogo digite "sair": ').upper()
print('-'*100)
