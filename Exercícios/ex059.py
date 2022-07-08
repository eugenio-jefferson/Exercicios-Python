# CRIE UM PROGRAMA QUE LEIA DOIS VALORESDE MOSTRE UM MENU NA TELA: [1]SOMAR, [2]MULTIPLICAR, [3]MAIOR, [4]NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA, SEU PROGRAMA DEVERAR REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.

print('\033[35m='*10, '\033[33mCALCULADORA', '\033[35m=\033[m'*10)
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
op = 0
while not op == 5:
    print('''\033[35m=-=- \033[33mO que você deseja fazer? \033[35m-=-=\033[m
[ 1 ] Somar;
[ 2 ] Multiplicar;
[ 3 ] Maior;
[ 4 ] Novos números;
[ 5 ] Sair do programa;
{}'''.format('\033[35m=-=\033[m'*10))
    op = int(input('Escolha uma opção: '))
    from time import sleep
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
        sleep(3)
    elif op == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre {} x {} é {}.'.format(n1, n2, multiplicação))
        sleep(3)
    elif op == 3:
        maior = n1 if n1 > n2 else n2
        print('Entre {} e {} o maior número é {}.'.format(n1, n2, maior))
        sleep(3)
    elif op == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
        sleep(3)
    elif op == 5:
        print('\033[33mFinalizando o programa...')
        sleep(1.5)
    else:
        print('\033[31mOPÇÃO INVALIDA, TENTE NOVAMENTE!')
        sleep(1)
