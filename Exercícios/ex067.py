# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ PARA CADA NÚMERO DIGITADO PELO USUÁRIO. O PROGRAMA
# SERÁ INTEROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.

print('\033[35m='*15, '\033[33mTABUADA 3.0', '\033[35m=\033[m'*15)
while True:
        num = int(input('Quer ver a tabuada de qual valor? '))
        print('\033[35m-\033[m'*43)
        if num < 0:
            print('{:>35}'.format('\033[31mFIM DO PROGRAMA!'))
            break
        for c in range(0, 11):
            print(f'{num:>18} x {c:<2} = {num*c}')
        print('\033[35m-\033[m'*43)