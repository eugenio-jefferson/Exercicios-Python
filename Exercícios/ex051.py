# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PROGRESSÃO ARITIMÉTICA. NO FINAL, MOSTRE OS 10 PRIMEIROS
# TERMOS DESSA PROGREÇÃO.

print('\033[35m='*10, '\033[33mADIVINHANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO ARITIMÉTICA', '\033[35m=\033[m'*10)
a1 = int(input('Qual o primeiro termo da P.A.? '))
r = int(input('Qual a razão da P.A.? '))
print('Os deiz primeiros termos da P.A. com o primeiro termo {} e a razão {}, são:'.format(a1, r))
print('\033[35m-\033[m'*82)
for c in range(1,11):
    print('{}'.format(a1 + (c - 1) * r), end=' -▶ ')
print(end=' Fim da P.A.\n')
print('\033[35m-\033[m'*82)
