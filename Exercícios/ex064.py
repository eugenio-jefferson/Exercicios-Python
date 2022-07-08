# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR
# 999, QUE É A CONDIÇÃO DE PARADA, NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES. (DESCONSI-
# DERANDO O FLAG)

print('\033[35m='*10, '\033[33mDIGITE NÚMEROS PARA EU SOMAR', '\033[35m=\033[m'*10)
num = soma = c = 0
num = int(input('Digite um número [use 999 para parar]: '))
while not num == 999:
    soma += num
    c += 1
    num = int(input('Digite um número [use 999 para parar]: '))
print('\033[35m-\033[m'*40)
print('Você digitou {} números, a soma entre eles é {}.'.format(c, soma))

