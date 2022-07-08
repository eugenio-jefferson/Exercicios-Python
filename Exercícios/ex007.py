# DESENVOLVA UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA

print('='*10, 'MÉDIA DE NOTAS', '='*10)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('A média entre {:.1f} e {:.1f}, é: {:.1f}.'.format(n1, n2, (n1 + n2) / 2))