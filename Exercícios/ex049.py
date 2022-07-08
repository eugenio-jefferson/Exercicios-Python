# REFARÇA O DESAFIO NÚMERO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.

print('\033[35m='*16, '\033[33mTABUADA 2.0', '\033[35m=\033[m'*16)
n = int(input('Digite um número para ver sua tabuada: '))
print('\033[35m-\033[m'*13)
for c in range(1, 11):
    print('{} X {:2} = {}'.format(n, c, n * c))
print('\033[35m-\033[m'*13)