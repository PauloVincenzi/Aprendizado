"""
Definindo Funções

 - Funções são pequenas partes de código que realizam tarefas específicas;
 - Pode ou não receber entras de dados e retornar uma saída de dados;
 - Muitas úteis para executar procedimentos similares por repetidas vezes;

 OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
 é bom fazer uma verificação para que a função seja simplificada.

 Já utilizamos várias funções deste que iniciamos este curso:
 - print()
 - len()
 - max()
 - min()
 - count()
 - e muitas outras;

Definir novas funções facilita e muito a codificação
DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.
Este 'DRY' é uma ideia fortemente vinculada a programação.
"""

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letra minúsculas, e se for nome composto, separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retordo da função.

OBS1: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimor o bloco de código com o já conhecido dois pontos : que é utilizado em Python 
para definir bloco.

OBS2: Não esqueça do parênteses () para executar a função definida
"""

# Definindo funções

# Exemplo 1


def diz_oi():
    print('oi!')

diz_oi()

"""
OBS:

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Exemplo 2

def cantar_parabens():
    print("""
        Parabéns para você
        Nesta data querida
        Muitas felicidades
        Muitos anos de vida
        Viva o aniversariante""")


for n in range(5):
    cantar_parabens()

# Em Python, podemos criar variáveis do tipo de uma função e executar esta função através da variável

saudacoes = diz_oi

saudacoes()
