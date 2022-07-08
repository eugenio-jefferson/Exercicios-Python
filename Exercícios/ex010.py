# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR
# CONSIDERE US$ 1,00 = R$ 3,27

print('='*10, 'CONVERSOR DE REAIS EM DÓLARES', '='*10)
r = float(input('Quantos reais você tem na carteira? R$ '))
d = r / 5.22
print('Com R$ {:.2f} e com o Dólar á R$ 3,27, você pode comprar US$ {:.2f}.'.format(r,d))