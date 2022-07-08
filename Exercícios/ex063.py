# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO "N" INTEIRO QUALQUER E MOSTRE NA TELA OS PRIMEIROS "N" ELEMENTOS DE UMA SEQUÊNCIA
# DE FIBONACCI. EX: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print('\033[35m='*10, '\033[33mMOSTRANDO OS TERMOS DA SEQUÊNCIA DE FIBONACCI', '\033[35m=\033[m'*10)
n = int(input('Quantos termos você quer mostrar? '))
print('\033[35m-\033[m'*80)
f1 = 0
f2 = 1
cont = 2
print(f1, end=' -▶ ' if cont <= n else '.')
print(f2 if cont <= n else '', '-▶ ' if n > 2 else '', end='')
while not cont >= n:
    cont += 2
    if n > 2:
        f1 += f2
        print(f1, end='.' if (cont - n) == 1 else ' -▶ ')
        if (cont - n) == 1:
            print('')
        else:
            f2 += f1
            print(f2, end='.'if cont == n else ' -▶ ')

    else:
        print('.')
print('\n'+ '\033[35m-'*80)
