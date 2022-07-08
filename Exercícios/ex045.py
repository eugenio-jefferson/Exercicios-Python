# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

print('\033[35m=-='*15, '\n\033[33m{:^45}\n'.format('VAMOS JOGAR JOKENPÔ!') + '\033[35m=-=\033[m'*15)
esc = str(input('Escolha PEDRA, PAPEL ou TESOURA: ')).strip().lower()
jok = ['pedra', 'papel', 'tesoura']
from random import choice
pc = choice(jok)
if esc == 'pedra' or esc == 'papel' or esc == 'tesoura':
    print(end='\033[33m{:^15}{}'.format('','JO'))
    from time import sleep
    sleep(1)
    print(end='KEN')
    sleep(1)
    print('PÔ!!\033[m')
    print('Você colocou {}, e eu coloquei {}.'.format(esc, pc))
    if esc == 'pedra' and pc == 'tesoura':
        print('{:^45}'.format('\033[32mVocê ganhou\033[m!'))
    elif esc == 'tesoura' and pc == 'papel':
        print('{:^45}'.format('\033[32mVocê ganhou\033[m!'))
    elif esc == 'papel' and pc == 'pedra':
        print('{:^45}'.format('\033[32mVocê ganhou\033[m!'))
    elif esc == 'tesoura' and pc == 'pedra':
        print('{:^45}'.format('\033[31mEu ganhei\033[m!'))
    elif esc == 'papel' and pc == 'tesoura':
        print('{:^45}'.format('\033[31mEu ganhei\033[m!'))
    elif esc == 'pedra' and pc == 'papel':
        print('{:^45}'.format('\033[31mEu ganhei\033[m!'))
    else:
        print('{:^45}'.format('\033[1mEmpatamos\033[m!'))
else:
    print('\033[31mVocê não colocou pedra, papel ou tesoura, tente novamente!')
print('''

By: Ge''')
