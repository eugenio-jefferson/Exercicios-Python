# FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR, O JOGO SÓ SERÁ INTEROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO
# O TOTAL DE VÍTORIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL.

from random import randint

jogador = computador = ' '
vítorias = 0

print('{:^50}'.format('VAMOS JOGAR PAR OU ÍMPAR!'))
while True:
    while jogador not in 'pi':
        jogador = input('Escolha [ P ] PAR ou [ I ] ÍMPAR: ').strip().lower()[0]

    print('-'*50)

    if jogador == 'p':
        computador = 'ÍMPAR'
        jogador = 'PAR'
    elif jogador == 'i':
        computador = 'PAR'
        jogador = 'ÍMPAR'

    print(f'Você escolheu {jogador} e o computador escolheu {computador}.\n')
    número_jogador = int(input('Agora escolha um número de 0 a 10: '))
    número_computador = randint(0, 10)
    soma = número_computador + número_jogador

    if soma % 2 == 0:
        resposta = 'PAR'
    elif soma % 2 != 0:
        resposta = 'ÍMPAR'

    if jogador == 'PAR' and resposta == 'PAR':
        ganhador = 'VOCÊ'
        vítorias += 1
    elif jogador == 'ÍMPAR' and resposta == 'ÍMPAR':
        ganhador = 'VOCÊ'
        vítorias += 1
    else:
        ganhador = 'o COMPUTADOR'

    print(f'''\nVocê colocou {número_jogador} e o computador colocou {número_computador}, 
A soma entre eles é {soma}, que é um número {resposta}.
\nComo você escolheu {jogador}, {ganhador} ganhou!
\n{"Vamos jogar novamente...":^50}''')
    print('-'*50)
    if ganhador == 'o COMPUTADOR':
        print(f'''\n{"VOCÊ PERDEU E O JOGO FOI FINALIZADO!":^50}
\nVOCÊ GANHOU {vítorias} {"VEZ." if vítorias == 1 else "VEZES."} TENTE NOVAMENTE.''')
        break