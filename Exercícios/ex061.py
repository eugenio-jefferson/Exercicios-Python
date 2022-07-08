# REFARÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGREÇÃO USANDO
# A ESTRUTURA WHILE.

print('\033[35m='*10, '\033[33mADIVINHANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO ARITIMÉTICA 2.0', '\033[35m=\033[m'*10)
a1 = int(input('Qual o primeiro termo da P.A.? '))
r = int(input('Qual a razão? '))
c = 0
print('Os dez primeiros termos da P.A. com o primeiro termo {} e a razão {}, são: '.format(a1, r))
while c != 10:
    c += 1
    print('{}'.format(a1 + (c -1) * r), end=' -▶ ' if c < 10 else '')
