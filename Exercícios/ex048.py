# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO
# INTERVALO DE 1 ATÉ 500.

print('\033[35m='*10, '\033[33mSOMA ÍMPARES DE 1 ATÉ 500 MÚLTIPLOS DE TRÊS', '\033[35m=\033[m'*10)
s = 0
con = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        con += 1
        s += c
print('A soma dos {} números solicidados é {}.'.format(con, s))
