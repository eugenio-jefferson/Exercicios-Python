# FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO
# GERADOS E VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA.

from random import randint
from time  import sleep
jogos=int(input('Quantos jogos serão criados? '))
print('-'*40)
mega=[]
for c in range(1,jogos+1):
    ljogo=[]
    j=0
    while j<6:
        num=randint(1,60)
        if not num in ljogo:
            ljogo.append(num)
            j+=1
    ljogo.sort()
    mega.append(ljogo[:])

for c in range(0,len(mega)):
    print(f'Jogo {c+1:^2}: {mega[c]}')
    sleep(0.5)