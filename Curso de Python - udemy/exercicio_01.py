def data_extenso(data):
    c = list(data)
    mes_string = c[3] + c[4]
    mes = int(mes_string)
    if mes == 1:
        return (f'{c[0] + c[1]} de janeiro de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 2:
        return (f'{c[0] + c[1]} de fevereiro de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 3:
        return (f'{c[0] + c[1]} de março de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 4:
        return (f'{c[0] + c[1]} de abril de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 5:
        return (f'{c[0] + c[1]} de maio de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 6:
        return (f'{c[0] + c[1]} de junho de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 7:
        return (f'{c[0] + c[1]} de julho de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 8:
        return (f'{c[0] + c[1]} de agosto de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 9:
        return (f'{c[0] + c[1]} de setembro de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 10:
        return (f'{c[0] + c[1]} de outubro de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 11:
        return (f'{c[0] + c[1]} de novembro de {c[6] + c[7] + c[8] + c[9]}')
    elif mes == 12:
        return (f'{c[0] + c[1]} de dezembro de {c[6] + c[7] + c[8] + c[9]}')
    
date = input('Qual a data? [dd/mm/aaaa] ')
print(f'Por extenso: {data_extenso(date)}')

"""
Após ver a resolução do intrutor, seria mais facil usar "split('/')"
"""
