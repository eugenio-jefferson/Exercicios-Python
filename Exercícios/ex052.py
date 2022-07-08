# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO.

print('\033[35m-=-='*20, '\033[33mANALISADOR DE NÚMEROS PRIMOS', '\033[35m=-=-\033[m'*20)
n = int(input('Digite um número para eu analisar: '))
con = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[36m', end='')
        con += 1
    else:
        print('\033[37m', end='')
    print(c, end='\033[m; ')
print('\nO número {} foi divisivel {} vezes.'.format(n, con))
if con == 2:
    print('Por isso ele \033[32mELE É PRIMO\033[m!')
else:
    print('Por isso ele \033[31mNÃO É PRIMO\033[m!')