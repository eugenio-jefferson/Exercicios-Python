# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(), QUE RECEBE UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE UMA
# MENSAGEM COM TAMANHO ADAPTÁVEL.

def escreva(text):
    print('~'*(len(text)+6))
    print(f'{text:^{len(text)+6}}')
    print('~'*(len(text)+6))

escreva('Olá, mundo!')
escreva('EUGÊNIO JEFFERSON')
escreva('Curso de Python no Youtube')
escreva('CeV')