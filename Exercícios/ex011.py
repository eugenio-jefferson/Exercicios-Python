# FAÇA UM PROGRAMA QUE LEIA A LARGURA E ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA
# NECESSARIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2m QUADRADO.

print('='*10, 'QUANTILIDADE DE TINTA PARA PINTAR UMA PAREDE', '='*10)
l = float(input('Qual a largura da parede em metros? '))
h = float(input('Qual a altura da parede em metros? '))
a = l * h
t = a / 2
print('Para pintar uma parede de {}m de largura e {}m de altura, com área de {:.2}m².'.format(l,h,a), end='')
print('É necessário {:.2f}l de tintas.'.format(t))
