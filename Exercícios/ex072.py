# CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA POR UMA CONTAGEM POR EXTENSO, DE 0 ATÉ VINTE. SEU PROGRAMA
# DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO.

tupla=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze',
       'dezeseis','dezesete','dezoito','dezenove','vinte')

while True:
    num=int(input('Digite um número de 0 à 20, que vou lhe mostrar por extenso: '))
    if 0<= num <=20:
        print('Você digitou o número',tupla[(num)]+".")
        contin=input("Quer continuar? [S]SIM | [N]Não: ")
        if contin=='N' or contin=='n':
            break
    else:
        print('\nVocê não digitou um número de 0 à 20, tente novamente!\n')