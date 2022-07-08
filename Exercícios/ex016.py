''' CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA SUA PORÇÃO INTEIRA
EXEMPLO: 6,0987 TEM COMO PORÇÃO INTEIRA O 6'''

from math import trunc
print('='*10, 'QUEBRANDO UM NÚMERO', '='*10)
print('A porção inteira é {}.'.format(trunc(float(input('Digite um número: ')))))