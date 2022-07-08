# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE
# PAGAMENTO: -À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO, -À VISTA NO CARTÃO: 5% DE DESCONTO, -EM ATÉ 2X NO CARTÃO: PREÇO
# NORMAL, -3X OU MAIS NO CARTÃO: 20% DE JUROS.

print('\033[35m-='*10, '\033[33mCALCULADORA DE PAGAMENTOS', '\033[35m-=\033[m'*10)
val = float(input('Qual o preço do produto? R$'))
print('\033[36m-='*10, 'FORMAS DE PAGAMENTOS', '=-'*10, '''\033[m
[ 1 ] À vista dinheiro/cheque, com 10% de desconto;
[ 2 ] À vista no cartão, com 5% de desconto;
[ 3 ] Em até 2x no cartão, sem juros;
[ 4 ] Em 3x ou mais no cartão, com 20% de juros;''')
print('\033[36m-=\033[m'*31)
pag = int(input('Qual a opção de pagamento? '))
if 1 <= pag <= 4:
    if pag == 1:
        vf = val * 0.90
    elif pag == 2:
        vf = val * 0.95
    elif pag == 3:
        vf = val
        par = vf / 2
        print('Parcelando a compra em \033[1m2x\033[m de R${:.2f}, \033[1msem juros\033[m!.'.format(par))
    elif pag == 4:
        vf = val * 1.20
        div = int(input('Vai ser em quantas parcelas? '))
        par = vf / div
        print('Parecelando a compra em \033[1m{}x\033[m de R${:.2f}, com \033[1m20% de juros\033[m!'.format(div, par))
    print('Sua compra de R${:.2f} \033[4mvai custar R${:.2f} no valor final\033[m.'.format(val, vf))
else:
    print('\033[31mOpção de pagamento não encontrada, por favor tente novamente!')


