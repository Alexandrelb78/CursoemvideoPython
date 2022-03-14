def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str (input(msg)).replace(',','.').strip()
        if entrada.isalpha():
            print (f'ERRO: \"{entrada}" É UM PREÇO INVALIDO!')
        else:
            valido = True
            return float (entrada)
