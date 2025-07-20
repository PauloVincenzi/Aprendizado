"""
Descrição:
Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuário escolher oque deseja fazer no banco,
como criar uma conta, logar em uma conta, efetuar saque, efetuar depósito, efetuar transferência, listar contas. 
"""

logado = False
contas = {}

def menu():
    print('-'*60)
    if logado:
        print('Escolha uma opção:')
        print('[1] - visualizar saldo')
        print('[2] - efetuar saque')
        print('[3] - efetuar depósito')
        print('[4] - efetuar transferência')
        print('[5] - deslogar-se')
    else:
        print('Escolha uma opção:')
        print('[1] - cadatrar-se')
        print('[2] - logar-se')
        print('[3] - listar contas')
        print('[4] - sair do sistema')
    print()

def cadastrar():
    print('-'*60)
    print(' CADASTRAR-SE '.center(60, '='))
    print('-'*60)
    username = input('Digite o nome de usuário: ')
    password = input('Digite a senha: ')
    confirmar_senha = input('Confirme a senha: ')
    while password != confirmar_senha:
        print('Senhas diferentes!')
        password = input('Digite a senha: ')
        confirmar_senha = input('Confirme a senha: ')
    if len(contas) == 0:
        contas[username] = [password, 0]
        print('Conta cadastrada com sucesso!')
    else:
        for conta in contas:
            if conta[0] == username:
                print('Username já cadastrado!')
            else:
                contas[username] = [password, 0]
                print('Conta cadastrada com sucesso!')
                break

def logar():
    print('-'*60)
    print(' LOGAR-SE '.center(60, '='))
    print('-'*60)
    username = input('Digite o nome de usuário: ')
    password = input('Digite a senha: ')
    if username in contas.keys() and password in contas[username] :
        print(f'Bem vindo a sua conta {username}!')
        return username, True
    else:
        print('Usuário e/ou senha incorretos!')

def listar_contas():
    print('-'*60)
    print(' CONTAS CADASTRADAS '.center(60, '='))
    print('-'*60)
    if len(contas) == 0:
        print('Não há contas cadastradas!')
    else:
        for user, dados in contas.items():
            print(f'Username: {user} - Senha: {len(dados[0]) * '*'} - Saldo: {len(str(int(dados[1]))) * '*'}')

def saque(username):
    print('-'*60)
    print(' EFETUAR SAQUE '.center(60, '='))
    print('-'*60)
    while True:
        try:
            valor = input('Qual valor deseja sacar? ')
            valor = float(valor)
            break
        except ValueError:
            print('Digite um número!')
    for user, dados in contas.items():
        if user == username:
            if valor > dados[1]:
                print('ERRO! O valor de saque é superior ao saldo da conta.')
            else:
                print('Saque feito com sucesso!')
                dados[1] -= valor

def deposito(username):
    print('-'*60)
    print(' EFETUAR DEPÓSITO '.center(60, '='))
    print('-'*60)
    while True:
        try:
            valor = input('Qual valor deseja depositar? ')
            valor = float(valor)
            break
        except ValueError:
            print('Digite um número!')
    for user, dados in contas.items():
        if user == username:
            print('Depósito feito com sucesso!')
            dados[1] += valor

def transferir(username):
    print('-'*60)
    print(' EFETUAR TRANSFERÊNCIA '.center(60, '='))
    print('-'*60)
    ok = False
    recebedor = input('Digite o username da conta que irá receber a transferência: ')
    if recebedor not in contas.keys():
        print(f'O username "{recebedor}" não é cadastrado no banco.')
        return
    while True:
        try:
            valor = input('Qual valor deseja transferir? ')
            valor = float(valor)
            break
        except ValueError:
            print('Digite um número!')
    for user, dados in contas.items():
        if user == username:
            if valor > dados[1]:
                print('ERRO! O valor a ser transferido é superior ao saldo da conta.')
            else:
                print('Transferência feita com sucesso!')
                dados[1] -= valor
                contas[recebedor][1] += valor

print('-'*60)
print(' BEM VINDO AO BANCO '.center(60, '='))

while True:
    menu()
    selecao = input()
    if logado:
        if selecao == '1':
            print(f'{username} tem R$ {contas[username][1]} em conta.')
        elif selecao == '2':
            saque(username)
        elif selecao == '3':
            deposito(username)
        elif selecao == '4':
            transferir(username)
        elif selecao == '5':
            print(f'Você deslogou-se {username}!')
            logado = False
        else:
            print('Entrada inválida!')
    else:
        if selecao == '1':
            cadastrar()
        elif selecao == '2':
            username, logado = logar()
        elif selecao == '3':
            listar_contas()
        elif selecao == '4':
            break
        else:
            print('Entrada inválida!')

print('-'*60)