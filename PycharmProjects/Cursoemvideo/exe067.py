t = c = n = 0
print ('VAMOS FAZER TABUADA!!! PARA SAIR DIGITE UM VALOR NEGATIVO')
print ('-=-'*35)
while True:
    n = int (input ('DIGITE UM NUMERO PARA VER SUA TABUADA: '))
    if n < 0:
        break
    while c <= 9:
        c = c + 1
        t = n * c
        print (f'{n} x {c} = {t}')
print ('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!!!')