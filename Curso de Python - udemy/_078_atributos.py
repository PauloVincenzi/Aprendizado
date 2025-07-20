"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos
nós conseguímos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utiizado para a construção do objeto.

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demosntrar que determinado atributo deve ser tratado como provado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo underscore no início do seu nome.

Isso é conhecido também como Name Mangling.

"""

# Classes com atributos de instâncias públicos

class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False
    

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
    

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')
print(user.email)
# print(user.__senha) # AttributeError
print(user._Acesso__senha) # Temos acesso, mas não deveríamos fazer este acesso. (Name Mangling)


print('-'*50)


# O que significa atributos de instância?

# Significa, que ao criarmos instâncias/obetos de uma classe, todas as instâncias
# terão estes atributos

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()


print('-'*50)


# Atributos de Classe

# Atributos de classes, são atributos declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos de classe, todas as instâncias
# terão o mesmo valor para este atributo.

# Refatorar a classe Produto

class Produto:

    # Atributo de classe
    imposto = 1.05 # 0.05 % de imposto
    contador = 0 

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('PlayStaton 4', 'Video game', 2300)
p2 = Produto('Xbox S', 'Video game', 4500)

print(p1.imposto) # Acesso possível, mas incorreto de um atributo de classe
print(p2.imposto) # Acesso possível, mas incorreto de um atributo de classe
print(p1.valor)
print(p2.valor)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe.

print(Produto.imposto) # Acesso correto de um atributo de classe.

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de claase aqui em Python,
# são chamados de atributos estáticos.


print('-'*50)


# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p3 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atribudo dinâmico

p3.peso = '5 kg' # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p3.nome}, Descrição: {p3.descricao}, Valor: {p3.valor}, Peso: {p3.peso}')


# Deletando atributos

print(p3.__dict__)

del p3.peso

print(p3.__dict__)

del p3.descricao

print(p3.__dict__)
