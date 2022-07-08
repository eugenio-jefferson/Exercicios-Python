# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES
# E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR
# VALORES.

print('\033[35m='*10, '\033[33mDIGITE NÚMEROS PARA EU MOSTRA A MÉDIA E O MAIOR E MENOR', '\033[35m=\033[m'*10)
continua = ''
maior = menor = média = c = 0
while continua != 'não':
    num = int(input('Digite um número: '))
    if maior == 0:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    média += num
    c += 1
    while not (continua == 'sim' or continua == 'não'):
        continua = str(input('Quer continuar [SIM OU NÃO]? ')).lower().strip()
    if continua == 'sim':
        continua = ''
    elif continua == 'não':
        continua = 'não'
print('''A média entre os números é de {}.
O maior número foi {}.
O menor número foi {}.'''.format(média / c, maior, menor))
