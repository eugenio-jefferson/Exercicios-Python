# CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE PUDIM ESTÁ ACESSÍVEL PELO COMPUTADOR USADO.

import urllib.request

try:
    s=urllib.request.urlopen('http://pudim.com.br/')
except:
    print(f'Não conseguir entrar no site Pudim.')
else:
    print('Site Pudim acessado!')