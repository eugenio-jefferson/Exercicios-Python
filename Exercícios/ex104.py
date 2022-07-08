# CRIE UM PROGRAMA QUE TENHA A FUNÇÃO LEIAINT(), QUE VAI FUNCIONAR DE FORMA SEMELHANTE A FUNÇÃO INPUT() DO PYTHON,
# SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR NUMÉRICO.

def leiaint(text):
    while True:
        n=input(text)
        if n.isnumeric():
            print(f'Você digitou o número {n}.')
            break
        else:
            print(f'ERRO! Você não digitou um número inteiro!')

leiaint('Digite um número: ')