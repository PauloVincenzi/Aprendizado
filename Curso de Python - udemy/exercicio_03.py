print('-'*100)

# Aqui o arquivo é aberto para escrita e leitura (w: 'limpa' o arquivo antes de ser aberto)
with open('C:\\Users\\ABREU\\Desktop\\Python\\Geek University\\Exercicios\\arq.txt', 'w+') as arquivo:
    e = ''
    while e != '0':
        arquivo.write(input('Adicione ao arquivo: '))
        arquivo.write('\n')
        e = input('Deseja continuar? (digite 0 caso não): ')
    print('-'*100)
    arquivo.seek(0)
    print(arquivo.read())
