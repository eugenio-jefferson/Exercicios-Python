# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS: O PRIMEIRO QUE INDICA O NÚMERO A CALCULAR
# E O OUTRO CHAMADO SHOW, QUE SERÁ UM VALOR LÓGICO OPCIONAL INDICANDO SE SERÁ MOSTRADO OU NÃO NA TELA O PROCESSO DE
# CÁLCULO DO FATORIAL.

def fatorial(f,show=False):
    """
    - Calcula o fatorial de um número
    :param f: número a ser calculado
    :param show: mostrar ou não a conta
    :return: retorna o valor
    """
    c=1
    while f>=1:
        c*=f
        if show:
            print(f,end=' x ')
        if f==1 and show:
            print('= ',end='')
        f-=1
    return c

print(fatorial(5,show=True))

help(fatorial)