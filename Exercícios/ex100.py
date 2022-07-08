# FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIA() E SOMAPAR(). A PRIMEIRA FUNÇÃO
# VAI SORTEIAR 5 NÚMEROS E COLOCÁ-LOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES
# SORTEADOS PELA FUNÇÃO ANTERIOR.

from random import randint
def sorteia(list):
    for c in range(0,5):
        list.append(randint(0,10))
    print(f"Os cinco valores foram sorteados para lista, e são:\n{list};")

def somapar(l):
    s=0
    for v in l:
        if v%2==0:
            s+=v
    print(f"Os valores pares da lista somados deu {s};")

números=[]

sorteia(números)
somapar(números)