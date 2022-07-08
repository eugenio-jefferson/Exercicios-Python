# DESAFIO: FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS
# INFORMAÇÕES POSSIVEIS SOBRE ELE

t = input('Digite alguma coisa: ')
print('O tipo primitivo do que você digitou é: {}.'.format(type(t)))
print('É imprimivel? {}.'.format(t.isprintable()))
print('Só tem espaços? {}.'.format(t.isspace()))
print('É um número? {}.'.format(t.isnumeric()))
print('É uma letra? {}.'.format(t.isalpha()))
print('É um digito? {}.'.format(t.isdigit()))
print('É um decimal? {}.'.format(t.isdecimal()))
print('É alfanúmerico? {}.'.format(t.isalnum()))
print('Está capitalizada? {}.'.format(t.istitle()))
print('Está em letras minuscúlas? {}.'.format(t.islower()))
print('Está em letras maiúsculas? {}.'.format(t.isupper()))
