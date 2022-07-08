# CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS
# PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS FEITA EM CADA PARTIDA. NO FINAL, TUDO ISSO SERÁ GUARDADO EM
# UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO.

dic={'Nome': str(input('Digite o nome do jogador: '))}
quant =int(input(f'Quantas partidas {dic["Nome"]} jogou? '))
gols=[]
for c in range(0,quant):
    gols.append(int(input(f'Quantos gols ele fez na {c+1}º partida? ')))
dic['Gols'] =gols[:]
dic['Total de gols'] = sum(gols)
print('-'*50)
print(dic)
print('-'*50)
for k,v in dic.items():
    print(f'{k} tem o valor {v};')
print('-'*50)
print(f'O jogador {dic["Nome"]} jogou {quant}.')
for i,v in enumerate(dic['Gols']):
    print(f'  - Na {i+1}º partida ele fez {v} gols;')
print(f'Teve um total de {dic["Total de gols"]} gols.')