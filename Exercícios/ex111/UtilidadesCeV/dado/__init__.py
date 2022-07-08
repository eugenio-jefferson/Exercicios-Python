def leiadinheiro(text):
    while True:
        v=input(text).strip()
        if v.isalpha() or v=='':
            print(f'O valor digitado não é um número valido!')
        else:
            return float(v.replace(',','.'))
            break