# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATIGIRAM A
# MAIORIDADE E QUANTOS JÁ SÃO MAIORES. MAIORIDADE = 21 ANOS.

print('\033[35m='*10, '\033[33mGRUPO DA MAIORIDADE', '\033[35m=\033[m'*10)
qua = 0
from datetime import date
for a in range(1, 8):
    ano = int(input('Em que ano a {}ª nasceu? '.format(a)))
    if date.today().year - ano >= 21:
        qua += 1
print('''No total \033[32m{}\033[m pessoas são de \033[32mmaiores\033[m.
E \033[31m{}\033[m pessoas são \033[31mmenores\033[m.'''.format(qua, 7 - qua))

