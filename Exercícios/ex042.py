# REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO: -EQUILÁTERO:
# TODOS OS LADOS IGUAIS, -ISÓSCELES: DOIS LADOS IGUAIS, -ESCALENOS: TODOS OS LADOS DIFERENTES.

print('\033[35m=-='*15, '\033[33mCRIAÇÃO DE TRIÂNGULOS 2.0', '\033[35m=-=\033[m'*15)
print('Diga o tamanho das três retas para eu verificar se podem formar um triângulo, e, se sim qual será o tipo do triângulo.')
r1 = float(input('Qual a medida da primeira reta? '))
r2 = float(input('Qual a medida da segunda reta? '))
r3 = float(input('Qual a medida da terceira reta? '))
print('\033[35m='*10, '\033[33mANALISANDO...', '\033[35m=\033[m'*10)
from time import sleep
sleep(1)
print('As retas {}, {} e {}:'.format(r1, r2, r3))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mPodem formar\033[m um triângulo!')
    print('Ele é um triângulo',end=' ')
    if r1 == r2 == r3:
        print('\033[1mequilátero\033[m!')
    elif r1 != r2 != r3 != r1:
        print('\033[1mescaleno\033[m!')
    else:
        print('\033[1misósceles\033[m!')
else:
    print('\033[31mNão podem formar\033[m um triângulo!')