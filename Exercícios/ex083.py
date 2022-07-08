# CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO QUALQUER QUE USE PARÊNTESES. SEU PROGRAMA DEVERÁ ANALISAR SE A
# EXPRESSÃO PASSADA ESTÁ COM OS PARÊNTESES ABERTOS E FECHADOS NA ORDEM CORRETA.

exp=str(input('Digite uma expressão com parênteses: '))

esq=exp.count('(')
dir=exp.count(')')
if esq==dir:
    print('A expressão está usando os parênteses corretamente.')
else:
    print('Sua expressão tem um erro no uso dos parênteses.')