# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS
# QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR SABENDO QUE O CARRO CUSTA R$ 60 POR DIA E R$ 0,15 POR KM RODADO

print('='*10, 'ALUGUEL DE CARROS','='*10)
dias = int(input('A quantos dias você alugou o carro? '))
km = float(input('Quantos Km você percorreu com o carro? '))
pd = dias * 60
pk = km * 0.15
print('Com o carro alugado a {} dias você vai pagar R$ {:.2f}.'.format(dias, pd))
print('Com {} Km percorridos com o carro você vai pagar R$ {:.2f}. \nTotal a pagar = R$ {:.2f}.'.format(km, pk, pd + pk))