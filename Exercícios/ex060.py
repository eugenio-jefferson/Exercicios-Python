# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL. EX: 5! = 5x4x3x2x1 = 120.

print('\033[35m='*10, '\033[33mFATORIANDO', '\033[35m=\033[m'*10)
num = int(input('Digite um número: '))
c = num + 1
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 1:
    f *= c - 1
    c -= 1
    print('{}'.format(c), 'x ' if c > 1 else '= ', end='')
print(f)