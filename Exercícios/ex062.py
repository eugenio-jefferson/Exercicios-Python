# MELHORE O DESAFIO 061, PERGUNTANDO AO USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA ENCERRA QUANDO ELE DISSER
# QUE QUER MOSTRAR 0 TERMOS.

print('\033[35m='*10, '\033[33mADIVINHANDO OS TERMOS DA PROGRESSÃO ARITIMÉTICA 3.0', '\033[35m=\033[m'*10)
primeiro = int(input('Qual o primeiro termo da P.A.? '))
razão = int(input('Qual a razão da P.A.? '))
termo = primeiro
c = 1
outro = 10
total = 0
while outro != 0:
    total += outro
    while c <= total:
        c += 1
        print('{}'.format(termo), end=' -▶ ' if c <= total else '')
        termo += razão
    outro = int(input('\nQuer ver mais quantos termos? '))
c -= 1
print('''\n\033[31mPrograma finalizado.
\033[mAo todo foram mostrando {} termos da P.A..'''.format(c))