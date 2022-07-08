#CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILHEIRO DE FUTEBOL, NA ORDEM DE
# COLOCAÇÃO. DEPOIS MOSTRE: A) APENAS OS 5 PRIMEIROS COLOCADOS. B) OS ÚLTIMOS 4 COLOCADOS DA TABELA. C) UMA LISTA COM
# OS TIMES EM ORDEM ALFABÉTICA. D) EM QUE POSIÇÃO DA TABELA ESTÁ O TIME DA CHAPECOENSE.

colocação=('PALMEIRAS','CORINTHIANS','ATHLETICO-PR','ATLÉTICO-MG','INTERNACIONAL','FLUMINENSE','BOTAFOGO','SANTOS',
           'SÃO PAULO','RED BULL BRAGANTINO','AVAÍ','ATLÉTICO-GO','CEARÁ','FLAMENGO','CORITIBA','AMÉRICA-MG',
           'GOIÁS','CUIABÁ','FORTALEZA','JUVENTUDE')

print("-----------------------------------------------------------------------------------------------------------------")
print(f"Os primeiros cincos colocados são: {colocação[:5]}")
print("-----------------------------------------------------------------------------------------------------------------")
print(f'Os últimos quatros colocados são: {colocação[-4:]}')
print("-----------------------------------------------------------------------------------------------------------------")
print(f'A lista em ordem alfabética: {sorted(colocação)}')
print("-----------------------------------------------------------------------------------------------------------------")
print(f'O BotaFogo está na {colocação.index("BOTAFOGO")+1}° posição.')