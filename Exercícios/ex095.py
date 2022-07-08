# APRIMORE O DESAFIO 093 PARA QUE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES
# DO APROVEITAMENTO DE CADA JOGADOR.

dic= {}
lista= []
gols=[]
resp='s'
while not resp =='n':
    dic.clear()
    dic['nome'] = str(input('Nome do jogador: '))
    quant=int(input(f'Quantantas partidas {dic["nome"]} jogou? '))
    gols.clear()
    for c in range(0,quant):
        gols.append(int(input(f'  Quantos gols ele fez na {c+1} partida? ')))
    dic['gols']=gols[:]
    dic['total']=sum(gols)
    lista.append(dic.copy())
    while True:
        resp=str(input('Quer continuar? [S | N]: ')).lower()
        if resp in 'sn':
            break
        print('ATENÇÂO! Use apenas "S" ou "N"!')

print('-'*60)
print(f"{'ID':<6}{'NOME':<20}{'GOLS':<25}{'TOTAL':<9}")
print('-'*60)
for i,v in enumerate(lista):
    print(f"{i:^6}{str(v['nome']):<20}{str(v['gols']):<25}{str(v['total']):^9}")
print('-'*60)

num = 0
while not num == 999:
    num = int(input('Informe o ID de um jogador para ver seus detalhes [999 para finalizar]: '))
    c=0
    if 0 <= num <= (len(lista)-1):
        for i, v in enumerate(lista):
            if i==num:
                print(f"O jogador {v['nome']} fez: ")
                for g in v['gols']:
                    c+=1
                    print(f"   - {g} na {c}º partida;")
    else:
        print(f'O ID {num} não existe, tente novamente!')