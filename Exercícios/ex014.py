# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM °C PARA °F

print('='*10, 'CONVERSOR DE TEMPERATURAS', '='*10)
celsius = float(input('Digite a temperatura em graus celsius: °C '))
print('A temperatura {}°C em °F é {:.2f}°F'.format(celsius, celsius * 1.8 + 32))