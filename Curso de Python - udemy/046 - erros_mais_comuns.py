"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quanto o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que 
o Python não reconhece como parte da linguagem.

Exemplos SyntaxError:

a)
def funcao:
    print('Olá')

b)
None = 1
def = 1

c)
return


2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError:

a)
print()

b)
geek()

c)
a = 18

if a < 10:
    msg = 'É maior que 10'

print(msg)

# Se a for maior que e não 'entrar' no condicional, msg não será definida.


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError:

a)
print(len(5))

b)
print('Geek' + 4)


4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
utilizando um índice inválido.

Exemplos de IndexError:

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][8])


5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo
correto mas valor inapropriado.

Exemplos ValueError:

a)
print(int('Geek')) # O valor esperado seria 'número' ou float ou int


6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError:

a)
dic = {'usuario': 'Paulo', 'Idade': 20}
print(dic['Peso'])

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

Exemplos AttributeError:

a)
tupla = (11, 2, 31, 4)
tupla.sort()


8 - IndentationError -> Ocorre quando não respeitamos a identação do Python (4 espaços)

Exemplos IdentationError:

a)
def saudacoes():
print('Olá')

b)
for i in range(10):
print(i)


EXISTEM MUITOS OUTROS TIPOS DE ERROS. Esses são os mais comuns.

OBS: Exceptions e Erros são sinônimos na programação.
"""



