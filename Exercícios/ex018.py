# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO

import math
print('='*10, 'SENO COSSENO E TANGENTE', '='*10)
ângulo = float(input('Digite um ângulo: '))
ar = math.radians(ângulo)
sen = math.sin(ar)
cos = math.cos(ar)
tan = math.tan(ar)
print('='*25)
print('O SENO de {0}° é {1:.2f}. \nO COSSENO de {0}° é {2:.2f}. \nA TANGENTE de {0}° é {3:.2f}.'.format(ângulo, sen, cos, tan))
print('='*25)