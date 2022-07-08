# DESAFIO: CRIE UM ALGORISMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

print('='*10, 'O DOBRO TRIPLO E RAIZ QUADRADA', '='*10)
n = int(input('Digite um número: '))
print('O dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrade de {} é {:.2f}.'.format(n, (n*2), n, (n*3), n, pow(n, (1/2))))
# pow(n, (1/2) ) ou (n ** 1/2)