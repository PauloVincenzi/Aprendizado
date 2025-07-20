import random

print('-' * 60)
numero_respostas = int(input('Quantas pessoas responderão ao questionário? '))
idade = dict(menor17=0, intervalo=0, maior27=0)
estados = dict(ac=0, al=0, ap=0, am=0, ba=0, ce=0, es=0, go=0, ma=0, mt=0, ms=0, mg=0, pa=0, pb=0, pr=0, pe=0, pi=0,
               rj=0, rn=0, rs=0, ro=0, rr=0, sc=0, sp=0, se=0, to=0, df=0)
freq_ru = dict(zero=0, um=0, dois=0, tres=0, quatro=0, cinco=0, seis=0, sete=0)  # 0 à 7 (escalar Ponderada)
satisfacao = dict(nada=0, pouco=0, indiferente=0, satisfeito=0, completamente=0)  # 1 à 5
paladar = dict(nada=0, pouco=0, media=0, agucado=0, muito=0)  # 1 à 7  (escalar Ponderada)
tipo_alimentar = dict(vegano=0, vegetariano=0, carnivoro=0)  # Considerar ou não avaliações (frango, omelete e carne)
s = float()
# Para todos 'gosto_..': Detesto=-2, Não gosto=-1, Indiferente=0, Gosto=1, Adoro=2
gosto_arroz = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
gosto_feijao = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
gosto_macarrao = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
gosto_sopa = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
gosto_polenta = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
gosto_frango = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
gosto_omelete = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
gosto_carne = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
gosto_legumes = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
gosto_verduras = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
gosto_geral = dict(detesto=0, naogosto=0, indiferente=0, gosto=0, adoro=0)
qntt_arroz = int()
media_qntt_arroz = float()
qntt_suco = int()
media_qntt_suco = float()
chave_maior_arroz = None
chave_maior_feijao = None
chave_maior_macarrao = None
chave_maior_sopa = None
chave_maior_polenta = None
chave_maior_frango = None
chave_maior_omelete = None
chave_maior_carne = None
chave_maior_legumes = None
chave_maior_verduras = None
chave_maior_geral = None

# Pergunta 1 - Qual sua idade?
# Fonte:
# https://agenciabrasil.ebc.com.br/educacao/noticia/2020-05/mapa-do-ensino-superior-aponta-para-maioria-feminina-e-branca
# A distribuição baseia-se em dados em que aproximadamente 60% dos universitários estão na faixa de 18 a 26 anos;
# Além disso, 18% dos alunos estão na faixa de 25 a 29 anos.
for c in range(0, numero_respostas):
    s = random.randint(1, 100)
    if s <= 15:
        idade['menor17'] += 1
    elif s <= 75:
        idade['intervalo'] += 1
    else:
        idade['maior27'] += 1

# Pergunta 2 - Você nasceu em qual estado?
# Fonte: Censo Demográfico 2022 - IBGE
# A distribuição por estado segue a risca a porcentagem de distribuição demográfica.
for c in range(0, numero_respostas):
    s = random.randint(1, 10012)
    if 1 <= s < 41:
        estados['ac'] += 1
    elif 41 <= s < 195:
        estados['al'] += 1
    elif 195 <= s < 231:
        estados['ap'] += 1
    elif 231 <= s < 425:
        estados['am'] += 1
    elif 425 <= s < 1121:
        estados['ba'] += 1
    elif 1121 <= s < 1554:
        estados['ce'] += 1
    elif 1554 <= s < 1743:
        estados['es'] += 1
    elif 1743 <= s < 2090:
        estados['go'] += 1
    elif 2090 <= s < 2424:
        estados['ma'] += 1
    elif 2424 <= s < 2604:
        estados['mt'] += 1
    elif 2604 <= s < 2740:
        estados['ms'] += 1
    elif 2740 <= s < 3751:
        estados['mg'] += 1
    elif 3751 <= s < 4161:
        estados['pa'] += 1
    elif 4161 <= s < 4357:
        estados['pb'] += 1
    elif 4357 <= s < 4921:
        estados['pr'] += 1
    elif 4921 <= s < 5367:
        estados['pe'] += 1
    elif 5367 <= s < 5528:
        estados['pi'] += 1
    elif 5528 <= s < 6319:
        estados['rj'] += 1
    elif 6319 <= s < 6482:
        estados['rn'] += 1
    elif 6482 <= s < 7018:
        estados['rs'] += 1
    elif 7018 <= s < 7096:
        estados['ro'] += 1
    elif 7096 <= s < 7127:
        estados['rr'] += 1
    elif 7127 <= s < 7502:
        estados['sc'] += 1
    elif 7502 <= s < 9690:
        estados['sp'] += 1
    elif 9690 <= s < 9799:
        estados['se'] += 1
    elif 9797 <= s < 9873:
        estados['to'] += 1
    else:
        estados['df'] += 1

# Pergunta 3 - O quão satisfeito você está com o que o ru tem a oferecer?
# Teoricamente será 20 % para cada
for c in range(0, numero_respostas):
    s = random.randint(1, 5)
    if s == 1:
        satisfacao['nada'] += 1
    elif s == 2:
        satisfacao['pouco'] += 1
    elif s == 3:
        satisfacao['indiferente'] += 1
    elif s == 4:
        satisfacao['satisfeito'] += 1
    else:
        satisfacao['completamente'] += 1

# Perguntas 4, 5 e 6 influenciam de alguma forma o bloco que avalia as comidas.
# Pesquisa IBOPE 2018 - Vegetariano / Vegano
# Os dados não são precisos
# 4% vegano, 14 % vegetariano, 82 % carnívoro
for c in range(0, numero_respostas):
    sfreq = random.randint(0, 7)
    if sfreq == 0:
        freq_ru['zero'] += 1
    elif sfreq == 1:
        freq_ru['um'] += 1
    elif sfreq == 2:
        freq_ru['dois'] += 1
    elif sfreq == 3:
        freq_ru['tres'] += 1
    elif sfreq == 4:
        freq_ru['quatro'] += 1
    elif sfreq == 5:
        freq_ru['cinco'] += 1
    elif sfreq == 6:
        freq_ru['seis'] += 1
    else:
        freq_ru['sete'] += 1
    spaladar = random.randint(1, 5)
    if spaladar == 1:
        paladar['nada'] += 1
    elif spaladar == 2:
        paladar['pouco'] += 1
    elif spaladar == 3:
        paladar['media'] += 1
    elif spaladar == 4:
        paladar['agucado'] += 1
    else:
        paladar['muito'] += 1
    stipo = random.randint(1, 100)
    if stipo <= 4:
        tipo_alimentar['vegano'] += 1
    elif stipo <= 18:
        tipo_alimentar['vegetariano'] += 1
    else:
        tipo_alimentar['carnivoro'] += 1
    s = random.randint(1, 5)
    if s == 1:
        gosto_arroz['detesto'] += spaladar * sfreq
    elif s == 2:
        gosto_arroz['naogosto'] += spaladar * sfreq
    elif s == 3:
        gosto_arroz['indiferente'] += spaladar * sfreq
    elif s == 4:
        gosto_arroz['gosto'] += spaladar * sfreq
    else:
        gosto_arroz['adoro'] += spaladar * sfreq
    s = random.randint(1, 5)
    if s == 1:
        gosto_feijao['detesto'] += spaladar * sfreq
    elif s == 2:
        gosto_feijao['naogosto'] += spaladar * sfreq
    elif s == 3:
        gosto_feijao['indiferente'] += spaladar * sfreq
    elif s == 4:
        gosto_feijao['gosto'] += spaladar * sfreq
    else:
        gosto_feijao['adoro'] += spaladar * sfreq
    s = random.randint(1, 5)
    if s == 1:
        gosto_macarrao['detesto'] += spaladar * sfreq
    elif s == 2:
        gosto_macarrao['naogosto'] += spaladar * sfreq
    elif s == 3:
        gosto_macarrao['indiferente'] += spaladar * sfreq
    elif s == 4:
        gosto_macarrao['gosto'] += spaladar * sfreq
    else:
        gosto_macarrao['adoro'] += spaladar * sfreq
    s = random.randint(1, 5)
    if s == 1:
        gosto_sopa['detesto'] += spaladar * sfreq
    elif s == 2:
        gosto_sopa['naogosto'] += spaladar * sfreq
    elif s == 3:
        gosto_sopa['indiferente'] += spaladar * sfreq
    elif s == 4:
        gosto_sopa['gosto'] += spaladar * sfreq
    else:
        gosto_sopa['adoro'] += spaladar * sfreq
    s = random.randint(1, 5)
    if s == 1:
        gosto_polenta['detesto'] += spaladar * sfreq
    elif s == 2:
        gosto_polenta['naogosto'] += spaladar * sfreq
    elif s == 3:
        gosto_polenta['indiferente'] += spaladar * sfreq
    elif s == 4:
        gosto_polenta['gosto'] += spaladar * sfreq
    else:
        gosto_polenta['adoro'] += spaladar * sfreq
    if stipo <= 18:
        gosto_frango['indiferente'] += spaladar * sfreq
    else:
        s = random.randint(1, 5)
        if s == 1:
            gosto_frango['detesto'] += spaladar * sfreq
        elif s == 2:
            gosto_frango['naogosto'] += spaladar * sfreq
        elif s == 3:
            gosto_frango['indiferente'] += spaladar * sfreq
        elif s == 4:
            gosto_frango['gosto'] += spaladar * sfreq
        else:
            gosto_frango['adoro'] += spaladar * sfreq
    if stipo <= 4:
        gosto_omelete['indiferente'] += spaladar * sfreq
    else:
        s = random.randint(1, 5)
        if s == 1:
            gosto_omelete['detesto'] += spaladar * sfreq
        elif s == 2:
            gosto_omelete['naogosto'] += spaladar * sfreq
        elif s == 3:
            gosto_omelete['indiferente'] += spaladar * sfreq
        elif s == 4:
            gosto_omelete['gosto'] += spaladar * sfreq
        else:
            gosto_omelete['adoro'] += spaladar * sfreq
    if stipo <= 18:
        gosto_carne['indiferente'] += spaladar * sfreq
    else:
        s = random.randint(1, 5)
        if s == 1:
            gosto_carne['detesto'] += spaladar * sfreq
        elif s == 2:
            gosto_carne['naogosto'] += spaladar * sfreq
        elif s == 3:
            gosto_carne['indiferente'] += spaladar * sfreq
        elif s == 4:
            gosto_carne['gosto'] += spaladar * sfreq
        else:
            gosto_carne['adoro'] += spaladar * sfreq
    s = random.randint(1, 5)
    if s == 1:
        gosto_legumes['detesto'] += spaladar * sfreq
    elif s == 2:
        gosto_legumes['naogosto'] += spaladar * sfreq
    elif s == 3:
        gosto_legumes['indiferente'] += spaladar * sfreq
    elif s == 4:
        gosto_legumes['gosto'] += spaladar * sfreq
    else:
        gosto_legumes['adoro'] += spaladar * sfreq
    s = random.randint(1, 5)
    if s == 1:
        gosto_verduras['detesto'] += spaladar * sfreq
    elif s == 2:
        gosto_verduras['naogosto'] += spaladar * sfreq
    elif s == 3:
        gosto_verduras['indiferente'] += spaladar * sfreq
    elif s == 4:
        gosto_verduras['gosto'] += spaladar * sfreq
    else:
        gosto_verduras['adoro'] += spaladar * sfreq

# Perguntas 7 e 8
for c in range(0, numero_respostas):
    s = (random.random()) * 1000
    qntt_arroz += s
    s = (random.random()) * 1000
    qntt_suco += s
media_qntt_arroz = qntt_arroz / numero_respostas
media_qntt_suco = qntt_suco / numero_respostas

maior_arroz = max(gosto_arroz.values())
maior_feijao = max(gosto_feijao.values())
maior_macarrao = max(gosto_macarrao.values())
maior_sopa = max(gosto_sopa.values())
maior_polenta = max(gosto_polenta.values())
maior_frango = max(gosto_frango.values())
maior_omelete = max(gosto_omelete.values())
maior_carne = max(gosto_carne.values())
maior_legumes = max(gosto_legumes.values())
maior_verduras = max(gosto_verduras.values())

for chave, valor in gosto_arroz.items():
    if valor == maior_arroz:
        chave_maior_arroz = chave
        break
for chave, valor in gosto_feijao.items():
    if valor == maior_feijao:
        chave_maior_feijao = chave
        break
for chave, valor in gosto_macarrao.items():
    if valor == maior_macarrao:
        chave_maior_macarrao = chave
        break
for chave, valor in gosto_sopa.items():
    if valor == maior_sopa:
        chave_maior_sopa = chave
        break
for chave, valor in gosto_polenta.items():
    if valor == maior_polenta:
        chave_maior_polenta = chave
        break
for chave, valor in gosto_frango.items():
    if valor == maior_frango:
        chave_maior_frango = chave
        break
for chave, valor in gosto_omelete.items():
    if valor == maior_omelete:
        chave_maior_omelete = chave
        break
for chave, valor in gosto_carne.items():
    if valor == maior_carne:
        chave_maior_carne = chave
        break
for chave, valor in gosto_legumes.items():
    if valor == maior_legumes:
        chave_maior_legumes = chave
        break
for chave, valor in gosto_verduras.items():
    if valor == maior_verduras:
        chave_maior_verduras = chave
        break

gosto_geral['detesto'] = (gosto_arroz['detesto'] + gosto_feijao['detesto'] + gosto_macarrao['detesto'] +
                          gosto_sopa['detesto'] + gosto_polenta['detesto'] + gosto_frango['detesto'] +
                          gosto_omelete['detesto'] + gosto_carne['detesto'] + gosto_legumes['detesto'] + gosto_verduras[
                              'detesto'])
gosto_geral['naogosto'] = (gosto_arroz['naogosto'] + gosto_feijao['naogosto'] + gosto_macarrao['naogosto'] +
                           gosto_sopa['naogosto'] + gosto_polenta['naogosto'] + gosto_frango['naogosto'] +
                           gosto_omelete['naogosto'] + gosto_carne['naogosto'] + gosto_legumes['naogosto'] +
                           gosto_verduras['naogosto'])
gosto_geral['indiferente'] = (gosto_arroz['indiferente'] + gosto_feijao['indiferente'] + gosto_macarrao['indiferente'] +
                              gosto_sopa['indiferente'] + gosto_polenta['indiferente'] + gosto_frango['indiferente'] +
                              gosto_omelete['indiferente'] + gosto_carne['indiferente'] + gosto_legumes['indiferente'] +
                              gosto_verduras['indiferente'])
gosto_geral['gosto'] = (gosto_arroz['gosto'] + gosto_feijao['gosto'] + gosto_macarrao['gosto'] +
                        gosto_sopa['gosto'] + gosto_polenta['gosto'] + gosto_frango['gosto'] +
                        gosto_omelete['gosto'] + gosto_carne['gosto'] + gosto_legumes['gosto'] + gosto_verduras[
                            'gosto'])
gosto_geral['adoro'] = (gosto_arroz['adoro'] + gosto_feijao['adoro'] + gosto_macarrao['adoro'] +
                        gosto_sopa['adoro'] + gosto_polenta['adoro'] + gosto_frango['adoro'] +
                        gosto_omelete['adoro'] + gosto_carne['adoro'] + gosto_legumes['adoro'] + gosto_verduras[
                            'adoro'])
maior_geral = max(gosto_geral.values())
for chave, valor in gosto_geral.items():
    if valor == maior_geral:
        chave_maior_geral = chave
        break

print('-' * 60)
print(f'{numero_respostas} INDIVÍDUOS ENTREVISTADOS'.center(60))
print('-' * 60)

print(f'DISTRIBUIÇÃO DA POPULAÇÃO POR IDADE'.center(60))
print('-' * 60)
print(f'17 anos ou menos: {(idade["menor17"]) * 100 / numero_respostas} %')
print(f'Entre 18 e 26 anos: {(idade["intervalo"]) * 100 / numero_respostas} %')
print(f'27 anos ou mais: {(idade["maior27"]) * 100 / numero_respostas} %')
print('-' * 60)

print(f'DISTRIBUIÇÃO DA POPULAÇÃO POR ESTADO'.center(60))
print('-' * 60)
print(f'Acre - {(estados['ac']) * 100 / numero_respostas} %')
print(f'Alagoas - {(estados['al']) * 100 / numero_respostas} %')
print(f'Amapá - {(estados['ap']) * 100 / numero_respostas} %')
print(f'Amazonas - {(estados['am']) * 100 / numero_respostas} %')
print(f'Bahia - {(estados['ba']) * 100 / numero_respostas} %')
print(f'Ceará - {(estados['ce']) * 100 / numero_respostas} %')
print(f'Espírito Santo - {(estados['es']) * 100 / numero_respostas} %')
print(f'Goiás - {(estados['go']) * 100 / numero_respostas} %')
print(f'Maranhão - {(estados['ma']) * 100 / numero_respostas} %')
print(f'Mato Grosso - {(estados['mt']) * 100 / numero_respostas} %')
print(f'Mato Grosso do Sul - {(estados['ms']) * 100 / numero_respostas} %')
print(f'Minas Gerais - {(estados['mg']) * 100 / numero_respostas} %')
print(f'Pará - {(estados['pa']) * 100 / numero_respostas} %')
print(f'Paraíba - {(estados['pb']) * 100 / numero_respostas} %')
print(f'Paraná - {(estados['pr']) * 100 / numero_respostas} %')
print(f'Pernambuco - {(estados['pe']) * 100 / numero_respostas} %')
print(f'Piauí - {(estados['pi']) * 100 / numero_respostas} %')
print(f'Rio de Janeiro - {(estados['rj']) * 100 / numero_respostas} %')
print(f'Rio Grande do Norte - {(estados['rn']) * 100 / numero_respostas} %')
print(f'Rio Grande do Sul - {(estados['rs']) * 100 / numero_respostas} %')
print(f'Rondônia - {(estados['ro']) * 100 / numero_respostas} %')
print(f'Roraima - {(estados['rr']) * 100 / numero_respostas} %')
print(f'Santa Catarina - {(estados['sc']) * 100 / numero_respostas} %')
print(f'São Paulo - {(estados['sp']) * 100 / numero_respostas} %')
print(f'Sergipe - {(estados['se']) * 100 / numero_respostas} %')
print(f'Tocantins - {(estados['to']) * 100 / numero_respostas} %')
print(f'Distrito Federal - {(estados['df']) * 100 / numero_respostas} %')
print('-' * 60)

print('DISTRIBUIÇÃO DO NÍVEL DE SATISFAÇÃO DA POPULAÇÃO'.center(60))
print('-' * 60)
print(f'Nada Satisfeito: {(satisfacao["nada"]) * 100 / numero_respostas} %')
print(f'Pouco Satisfeito: {(satisfacao["pouco"]) * 100 / numero_respostas} %')
print(f'Indiferente: {(satisfacao["indiferente"]) * 100 / numero_respostas} %')
print(f'Satisfeito: {(satisfacao["satisfeito"]) * 100 / numero_respostas} %')
print(f'Completamente Satisfeito: {(satisfacao["completamente"]) * 100 / numero_respostas} %')
print('-' * 60)

print('DISTRIBUIÇÃO DE FREQUÊNCIA DO RU'.center(60))
print('-' * 60)
print(f'Nenhum dia na semana: {(freq_ru["zero"]) * 100 / numero_respostas} %')
print(f'Um dia na semana: {(freq_ru["um"]) * 100 / numero_respostas} %')
print(f'Dois dias na semana: {(freq_ru["dois"]) * 100 / numero_respostas} %')
print(f'Três dias na semana: {(freq_ru["tres"]) * 100 / numero_respostas} %')
print(f'Quatro dias na semana: {(freq_ru["quatro"]) * 100 / numero_respostas} %')
print(f'Cinco dias na semana: {(freq_ru["cinco"]) * 100 / numero_respostas} %')
print(f'Seis dias na semana: {(freq_ru["seis"]) * 100 / numero_respostas} %')
print(f'Sete dias na semana: {(freq_ru["sete"]) * 100 / numero_respostas} %')
print('-' * 60)

print('DISTRIBUIÇÃO DO QUÃO AGUÇADO É O PALADAR'.center(60))
print('-' * 60)
print(f'Nada aguçado: {(paladar["nada"]) * 100 / numero_respostas} %')
print(f'Pouco aguçado: {(paladar["pouco"]) * 100 / numero_respostas} %')
print(f'Na média: {(paladar["media"]) * 100 / numero_respostas} %')
print(f'Aguçado: {(paladar["agucado"]) * 100 / numero_respostas} %')
print(f'Muito aguçado: {(paladar["muito"]) * 100 / numero_respostas} %')
print('-' * 60)

print('DISTRIBUIÇÃO DO TIPO ALIMENTAR'.center(60))
print('-' * 60)
print(f'Carnívoros: {(tipo_alimentar["carnivoro"]) * 100 / numero_respostas} %')
print(f'Veganos: {(tipo_alimentar["vegano"]) * 100 / numero_respostas} %')
print(f'Vegetarianos: {(tipo_alimentar["vegetariano"]) * 100 / numero_respostas} %')
print('-' * 60)

print('AVALIAÇÃO DE CADA ALIMENTO'.center(60))
print('-' * 60)
print(f'Arroz: {chave_maior_arroz}  -   {maior_arroz * 100 / (gosto_arroz["detesto"] +
                                                              gosto_arroz["naogosto"] + gosto_arroz["indiferente"] + gosto_arroz["gosto"] + gosto_arroz["adoro"])} % das respostas')
print(f'Feijao: {chave_maior_feijao}  -   {maior_feijao * 100 / (gosto_feijao["detesto"] +
                                                                 gosto_feijao["naogosto"] + gosto_feijao["indiferente"] + gosto_feijao["gosto"] + gosto_feijao["adoro"])} % das respostas')
print(f'Macarrao: {chave_maior_macarrao}  -   {maior_macarrao * 100 / (gosto_macarrao["detesto"] +
                                                                       gosto_macarrao["naogosto"] + gosto_macarrao["indiferente"] + gosto_macarrao["gosto"] + gosto_macarrao["adoro"])} % das respostas')
print(f'Sopa: {chave_maior_sopa}  -   {maior_sopa * 100 / (gosto_sopa["detesto"] +
                                                           gosto_sopa["naogosto"] + gosto_sopa["indiferente"] + gosto_sopa["gosto"] + gosto_sopa["adoro"])} % das respostas')
print(f'Polenta: {chave_maior_polenta}  -   {maior_polenta * 100 / (gosto_polenta["detesto"] +
                                                                    gosto_polenta["naogosto"] + gosto_polenta["indiferente"] + gosto_polenta["gosto"] + gosto_polenta["adoro"])} % das respostas')
print(f'Frango: {chave_maior_frango}  -   {maior_frango * 100 / (gosto_frango["detesto"] +
                                                                 gosto_frango["naogosto"] + gosto_frango["indiferente"] + gosto_frango["gosto"] + gosto_frango["adoro"])} % das respostas')
print(f'Omelete: {chave_maior_omelete}  -   {maior_omelete * 100 / (gosto_omelete["detesto"] +
                                                                    gosto_omelete["naogosto"] + gosto_omelete["indiferente"] + gosto_omelete["gosto"] + gosto_omelete["adoro"])} % das respostas')
print(f'Carne: {chave_maior_carne}  -   {maior_carne * 100 / (gosto_carne["detesto"] +
                                                              gosto_carne["naogosto"] + gosto_carne["indiferente"] + gosto_carne["gosto"] + gosto_carne["adoro"])} % das respostas')
print(f'Legumes: {chave_maior_legumes}  -   {maior_legumes * 100 / (gosto_legumes["detesto"] +
                                                                    gosto_legumes["naogosto"] + gosto_legumes["indiferente"] + gosto_legumes["gosto"] + gosto_legumes["adoro"])} % das respostas')
print(f'Verduras: {chave_maior_verduras}  -   {maior_verduras * 100 / (gosto_verduras["detesto"] +
                                                                       gosto_verduras["naogosto"] + gosto_verduras["indiferente"] + gosto_verduras["gosto"] + gosto_verduras["adoro"])} % das respostas')
print('-' * 60)

print('AVALIAÇÃO FINAL (CONSIDERANDO TODOS ALIMENTOS)'.center(60))
print('-' * 60)
print(f'-> {chave_maior_geral}  -      {maior_geral * 100 / (gosto_geral["detesto"] +
                                                                    gosto_geral["naogosto"] + gosto_geral["indiferente"] + gosto_geral["gosto"] + gosto_geral["adoro"])} % das respostas')
print('-' * 60)

print('QUANTIDADE MÉDIA DE ARROZ E SUCO'.center(60))
print('-' * 60)
print(f'Arroz: {media_qntt_arroz} g')
print(f'Suco: {media_qntt_suco} ml')
print('-' * 60)
print('FIM'.center(60))
print('-' * 60)
