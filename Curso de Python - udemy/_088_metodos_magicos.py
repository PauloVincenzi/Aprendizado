"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

dunder init

dunder repr -> Representação do objeto

dunder str -> Representação (tem preferência em relação ao __repr__)

dunder len

dunder del

dunder add

dunder mul
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
    
    def __str__(self):
        return self.titulo
    
    def __len__(self):
        return self.paginas
    
    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'
    
    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'

livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Ingeligência Artificial com Python', 'McDonalds', 350)


# Sem o métodos de representação, os prints abaixo retornariam um objeto <__main__.Livro object at 0x000002125D28D7F0> 
print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 5)

# Ao término do programa, o Python deleta automaticamente os objetos, assim
# __del__ é executado duas vezes (dois objetos criados)

# Todos esses métodos vêm da classe object
