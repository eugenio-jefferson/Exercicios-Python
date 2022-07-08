# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA
# CASA, O SALÁRIO DO COMPRADOR E QUANTOS ANOS ELE VAI PAGAR. CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO
# PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRESTIMO SERÁ NEGADO.

print('\033[33m=-'*10, '\033[35mEMPRÉSTIMO HIMOBILIÁRIO', '\033[33m=-\033[m'*10)
casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o valor do seu salário? R$'))
parcela = int(input('Em quantos anos vai parcelar a casa? '))
valor = casa / (parcela * 12)
print('\033[33m=-\033[m'*25)
print('Para pagar uma casa de R${:.2f} em {} anos as parcelas sairam por R${:.2f}.'.format(casa, parcela, valor))
if ((30 / 100) * salário) <= valor:
    print('\033[31mSEU EMPRESTIMO FOI NEGADO!\033[m Por que a parcela é maior que 30% do seu salário.')
else:
    print('\033[32mSEU EMPRESTIMO FOI ACEITO!\033[m')
