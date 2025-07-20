"""
Descrição:

Devemos desenvolver uma aplicação onde ao ser inicializada apresente ao usuário um menu onde seja
possível cadastrar, listar e comprar produtos, além de visualizar carrinho de compra ou sair da aplicação.

Ao adicionar um produto no carrinho de compras, deve-se verificar se já existe um mesmo produto no carrinho,
bastando alterar a quantidade. Ao finalizar a compra deve ser apresentado ao usuário o total de acordo
com os produtos e quantidades inseridas no carrinho de compra.
"""

produtos = []
carrinho = []

def menu():
    print('-'*60)
    print('Selecione uma opção abaixo:')
    print('1 - Cadastrar produto')
    print('2 - Listrar produtos')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair da aplicação')
    print()
    selecao = input()
    while selecao not in ['1', '2', '3', '4', '5', '6']:
        print('-'*60)
        print('Entrada inválida!')
        print('-'*60)
        print('Selecione uma opção abaixo:')
        print('1 - Cadastrar produto')
        print('2 - Listrar produtos')
        print('3 - Comprar produto')
        print('4 - Visualizar carrinho')
        print('5 - Fechar pedido')
        print('6 - Sair da aplicação')
        print()
        selecao = input()
    print('-'*60)
    return selecao

def cadastrar_produto():
    print(' CADASTRAR PRODUTO '.center(60, '='))
    print('-'*60)
    nome = input('Qual o nome do produto? ')
    while True:
        try:
            valor = input('Qual o valor? ')
            valor = float(valor)
            break
        except:
            print('Entrada inválida!')
    if [nome, valor] in produtos:
        print('Este produto já está cadastrado no mercado com este preço.')
    else:
        print(f'Produto "{nome}" cadastrado por R$ {valor} com sucesso!')
        produtos.append([nome, valor])

def listar_produtos():
    print(' LISTA DE PRODUTOS '.center(60, '='))
    print('-'*60)
    for produto in produtos:
        print(f'{produto[0]} - R$ {produto[1]}')

def comprar():
    print(' COMPRAR PRODUTO '.center(60, '='))
    print('-'*60)
    for i, produto in enumerate(produtos):
        print(f'[{i+1}] - {produto[0]} - R$ {produto[1]}')
    ind = input('Selecione o número referente ao produto desejado: ')
    while int(ind) not in [x+1 for x in range(len(produtos))]:
        print('Entrada incorreta!')
        ind = input('Selecione o número referente ao produto desejado: ')
    ind = int(ind)

    for item in carrinho:
        if produtos[ind-1][0] == item[0]:
            item[2] += 1
            return
        
    carrinho.append([produtos[ind-1][0], produtos[ind-1][1], 1])

def visualizar_carrinho():
    print(' CARRINHO DE PRODUTOS '.center(60, '='))
    print('-'*60)
    for produto in carrinho:
        print(f'{produto[0]} - R$ {produto[1] * produto[2]} - {produto[2]} unidade(s)')

def fechar_pedido():
    print(' COMPRA FINALIZADA '.center(60, '='))
    print('-'*60)
    print('Você comprou:')
    for item in carrinho:
        print(f'{item[2]} unidade(s) de {item[0]} por R$ {item[1]*item[2]}')

print('-'*60)
print(' BEM-VINDO AO MERCADINHO '.center(60, '='))

selecao = ''
while selecao != '6':
    selecao = menu()
    if selecao == '1':
        cadastrar_produto()
    elif selecao == '2':
        listar_produtos()
    elif selecao == '3':
        comprar()
    elif selecao == '4':
        visualizar_carrinho()
    elif selecao == '5':
        fechar_pedido()
