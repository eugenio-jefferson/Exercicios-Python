# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE

print('='*20, 'SEPARADOR DE NOME', '='*20)
nome = str(input('Qual seu nome completo? ')).strip().title()
lista = nome.split()
print('Seu primeiro nome é {}.\nSeu último nome é {}.'.format(lista[0], lista[-1]))