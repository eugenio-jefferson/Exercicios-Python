# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.

print('\033[35m='*10, '\033[33mQUAL É O MAIOR E MENOR?', '\033[35m=\033[m'*10)
ma = 0
me = 0
for c in range(1, 6):
    pes = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    if c == 1:
        ma = pes
        me = pes
    else:
        if pes > ma:
            ma = pes
        if pes < me:
            me = pes
print('''O maior peso é {}kg.
O menor peso é {}kg.'''.format(ma, me))