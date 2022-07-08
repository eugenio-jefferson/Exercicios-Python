# REESCREVA A FUNÇÃO LEIAINT() QUE FIZEMOS NO DESAFIO 104, INCLUINDO AGORA A POSSIBILIDADE DE DIGITAÇÃO DE UM NÚMERO
# DE TIPO INVÁLIDO. APROVEITE E CRIE TAMBÉM A FUNÇÃO LEIAFLOAT() COM A MESMA FUNCIONALIDADE.

def leiaint(text):
    while True:
        try:
            n=int(input(text))
        except:
            print(f'ERRO! Você não digitou um número inteiro!')
        else:
            return n
            break

def leiafloat(text):
    while True:
        try:
            n=float(input(text))
        except:
            print(f'ERRO! Você não digitou um número real!')
        else:
            return n
            break
i=leiaint('Digite um número inteiro: ')

r=leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {i}, e o real foi {r};')