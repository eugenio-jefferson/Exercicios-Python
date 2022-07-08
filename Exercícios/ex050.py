# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR
# DIGITADO FOR ÍMPAR, DESCONSIDERE-O.

print('\033[35m='*10, '\033[33mSOMA DOS PARES INTEIROS', '\033[35m=\033[m'*10)
soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}° número: '.format(c)))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares é {}'.format(soma))
