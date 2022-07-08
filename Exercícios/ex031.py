# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM COBRANDO R$ 0,50
# POR KM PARA VIAGENS DE ATÉ 200KM E R$ 0,45 PARA VIAGENS MAIS LONGAS

print('='*10, 'CUSTO DA VIAGEM', '='*10)
km = float(input('Qual a distância da viagem? km '))
'''if km <= 200:
    print('Até 200km, cada km custa R$0,50.')
    preço = km * 0.50
else:
    print('Acima de 200km, cada km custa R$0,45.')
    preço = km * 0.45'''
preço = km * 0.50 if km <= 200 else km * 0.45
print('Como sua viagem é de {:.2f}km, você vai pagar R${:.2f}.'.format(km, preço))