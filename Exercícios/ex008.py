# ESCREVA UM PROGRAMA QUE LEIA O VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS

print('='*10, 'CONVERTOR DE METROS EM CENTÍMETROS E MILÍMETROS', '='*10)
m = float(input('Digite o tamanho em metros: '))
cm = m * 100
mm = m * 1000
print('{}m em centímetros é: {:.0f}cm. \n{}m em milímetros é: {:.0f}mm.'.format(m, cm, m, mm))
