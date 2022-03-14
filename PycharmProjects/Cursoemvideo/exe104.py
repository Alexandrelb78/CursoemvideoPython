def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str (input (msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE UM NUMERO INTEIRO VALIDO.\033[m')
        if ok:
            break
    return valor


n = leiaInt ('DIGITE UM NUMERO: ')
print (f'VOCE ACABOU DE DIGITAR O NUMERO {n}')
