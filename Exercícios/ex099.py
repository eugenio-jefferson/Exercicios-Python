# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS. SEU PROGRAMA
# TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR.

def maior(*v):
    print(f"Analisando os valores: {v}")
    print(f"Foram informados {len(v)} valores;")
    m=v[0]
    for n in v:
        if n> m:
            m=n
    print(f"O maior valor informado foi {m};\n\n")

maior(3,4,6,1,9,6,7,8)
maior(4,2,3,1,0,5)
maior(4,6)
maior(3)
maior()