# CRIE UM PROGRAMA ONDE QUATRO JOGADORES JOGUEM UM DADO  E TENHAM RESULTADOS ALEATÓRIOS. GUARDE ESSE RESULTADO EM UM
# DICIONÁRIO. NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO.

from random import randint
import time
from operator import itemgetter
dic={}
for c in range(1,5):
    dic[f'jogador{c}']= randint(1,6)
    print(f"O jogador {c} tirou {dic[f'jogador{c}']} no dado;")
    time.sleep(0.5)
print('-=-'*10)
rank=[]
rank=sorted(dic.items(), key=itemgetter(1),reverse=True)
for i, v in enumerate(rank):
    print(f'{i+1}º é o {v[0]}, que tirou {v[1]};')
    time.sleep(0.5)
print('-=-'*10)

