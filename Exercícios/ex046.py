# FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFÍCIOS, INDO DE 10 ATÉ 0,
# COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.

print('\033[35m='*10, '\033[33mCONTAGEM REGRECIVA', '\033[35m=\033[m'*10)
from time import sleep
for c in range(10, -1, -1):
    print('\033[36m{:^40}\033[m'.format(c))
    sleep(1)
from emoji import emojize
print(emojize(':fireworks:'*25, use_aliases=True))


