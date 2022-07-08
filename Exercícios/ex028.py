# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO DE 0 A 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR
# QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR. O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU

from random import randint
from time import sleep
print('\033[36m='*70, '\n',' '*2, '\033[33mESTOU PENSANDO EM UM NÚMERO INTEIRO DE 0 A 5, TENTE ADIVINHAR!\n' + '\033[36m='*70)
escolhido = randint(0, 5)
num = int(input('\033[34mEm qual número estou pensando? '))
print('HUMM, DEIXE-ME VER, VOCÊ...\033[m')
sleep(2)
print('\033[32mVocê acertou, parabéns!' if num == escolhido else '\033[31mVocê errou o núemro era {}, mais sorte na próxima vez!'.format(escolhido))