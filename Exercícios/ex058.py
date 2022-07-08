# MELHORE O JOGO DO DESAFIO 028 AONDE O COMPUTADOR VAI "PENSAR" NUM NÚMERO ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR VAI TENTAR
# ADVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.

print('\033[36m='*70, '\n', ' '*3, '\033[33mESTOU PENSANDO EM UM NÚMERO DE 0 A 10, TENTE ADIVINHAR! 2.0\n'+ '\033[36m=\033[m'*70)
from random import randint
nov = 0
while not nov == 2:
    escolhido = randint(0, 10)
    num = int(input('\033[34mEm qual número estou pensando? '))
    print('HUMM, DEIXE-ME VER...\033[m')
    from time import sleep
    sleep(1)
    cont = 1
    nov = 0
    while num != escolhido:
        print('{:^70}'.format('\033[31mVOCÊ ERROU!'))
        if num < escolhido:
            d = 'maior...'
        else:
            d = 'menor...'
        num = int(input('\033[34mÉ {} Tente novamente: '.format(d)))
        cont += 1
    if cont == 1:
        f = '\033[32mPARABÉNS!\033[m Você precisou de apenas {} tentativas'.format(cont)
    elif 1 < cont <= 3:
        f = '\033[1;37mQUE LEGAL!\033[m Você só precisou de {} tentativas'.format(cont)
    else:
        f = '\033[31mQUE PENA!\033[m Você precisou de {} tentativas'.format(cont)
    print('''{:^70}
            {} para acertar.'''.format('\033[32mVOCÊ ACERTOU!', f))
    if num == escolhido:
        while nov != 1 and nov != 2:
            nov = int(input('''Quer jogar novamente? 
[ 1 ] Sim
[ 2 ] Não
Opção: '''))
            if nov == 2:
                print('\033[31m---- JOGO FINALIZADO ----')
