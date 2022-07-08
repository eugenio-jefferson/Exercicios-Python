# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE
# FOI MULTADO. A MULTA VAI CUSTAR R$ 7,00 POR CADA KM A CIMA DO LIMITE

print('='*15, 'RADAR ELETRÔNICO', '='*15)
km = float(input('Digite a velocidade do veículo: km/h '))
if km > 80:
    multa = (km - 80) * 7
    print('\033[4;31mVocê foi multado em R$ {:.2f}, por está {:.1f}km/h acima do limite de 80km/h.\033[m'.format(multa, km - 80))
print('\033[1;36mFique dentro do lime de 80km/h para não ser multado.\033[m')