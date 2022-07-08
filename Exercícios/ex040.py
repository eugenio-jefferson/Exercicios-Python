# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL DE ACORDO COM A
# MÉDIA ATINGIDA: -MÉDIA ABIXO DE 5.0: REPROVADO, -MÉDIA ENTRE 5,0 E 6,9: RECUPERAÇÃO, -MÉDIA 7,0 OU SUPERIOR: APROVADO.

print('\033[35m='*10, '\033[33mCALCULADOR DE MÉDIA 2.0', '\033[35m=\033[m'*10)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Com as notas {:.1f} e {:.1f}.\nA média do aluno é de {:.1f}'.format(n1, n2, m))
if m < 5:
    print('O aluno(a) foi \033[31mREPROVADO\033[m!')
elif 5 <= m <= 6.9:
    print('O aluno(a) está em \033[31mRECUPERAÇÃO\033[m!')
else:
    print('O aluno(a) foi \033[32mAPROVADO(A)\033[m!')