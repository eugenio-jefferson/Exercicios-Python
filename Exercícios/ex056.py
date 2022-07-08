# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE: -A MÉDIA DE IDADE DO
# GRUPO, -QUAL É O NOME DO HOMEM MAIS VELHO, -QUANTAS MULHERES TÊM MENOS DE 20 ANOS.

print('\033[35m='*15, '\033[33mANALISADOR COMPLETO', '\033[35m=\033[m'*15)
média = 0
hv = 0
velho = str('')
mulh = 0
for g in range(1,5):
    nome = str(input('Nome da {}ª pessoa: '.format(g))).strip().lower().title()
    idade = int(input('Idade da {}ª pessoa: '.format(g)))
    sexo = str(input('Sexo da {}ª pessoa [M/F]: '.format(g))).strip().lower()
    print('\033[35m-\033[m'*40)
    média += idade
    if sexo == 'm':
        if idade > hv:
            hv = idade
            velho = nome
    elif sexo == 'f':
        if idade < 20:
            mulh += 1
print('''A média de idade do grupo lido é de {:.2f} anos.
O homem mais velho tem {} anos e se chama {}.
O grupo tem {} mulheres com menos de 20 anos.'''.format(média / 4, hv, velho, mulh))
