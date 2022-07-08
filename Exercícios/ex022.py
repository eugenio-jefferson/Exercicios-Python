# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE: O NOME COM TODAS AS LETRAS EM MAIÚSCULAS E MENÚSCULAS.
# QUANTAS LETRAS TEM NO TOTAL (SEM CONSIDERAR OS ESPAÇÕS). QUANTAS LETRAS TEM O PRIMEIRO NOME

print('='*20, 'ANALISADOR DE NOMES', '='*20)
nome = str(input('Digite seu nome completo: ')).strip()
print('Nome com letras em maiúsculas: {}.'.format(nome.upper()))
print('Nome com letras em menúsculas: {}.'.format(nome.lower()))
print('Seu nome no total tem {} letras.'.format(len(nome.replace(' ',''))))
# print('Seu nome no total tem {} letras'.format(len(nome) - nome.count(' ')))
lista = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(lista[0], len(lista[0])))
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))