# A CONFIDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA
# CATEGORIA, DE ACORDO COM SUA IDADE: -ATÉ 9 ANOS: MIRIM, -ATÉ 14 ANOS: INFANTIL, -ATÉ 19 ANOS: JÚNIOR, -ATÉ 25 ANOS: SÊNIOR
# -ACIMA: MASTER.

print('\033[35m='*10,'\033[33mCLASSIFICANDO ATLETAS', '\033[35m\033[m'*10)
nasc = int(input('Em qual ano o(a) atleta nasceu? '))
from datetime import date
ida = date.today().year - nasc
print('O(a) atleta nasceu em {} e tem {}.'.format(nasc, ida))
if ida <= 9:
    print('Categoria:\033[1mMIRIM\033[m!')
elif ida <= 14:
    print('Categoria: \033[1mINFANTIL\033[m!')
elif ida <= 19:
    print('Categoria: \033[1mJÚNIOR\033[m!')
elif ida <= 25:
    print('Categoria: \033[1mSÊNIOR\033[m!')
else:
    print('Categoria: \033[1mMASTER')
