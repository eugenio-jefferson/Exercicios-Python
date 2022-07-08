# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR
# 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL É A SOMA ENTRE ELES (DESCONSIDERANDO
# O FLAG)

print('\033[35m='*10, '\033[33mDIGITE NÚMEROS PARA EU SOMAR', '\033[35m=\033[m'*10)
soma = contador = 0
while True:
    número = int(input('Digite um número [999 para parar]: '))
    if número == 999:
        break
    soma += número
    contador += 1
print(f'Você ditou {contador} números e a soma entre eles é {soma}.')