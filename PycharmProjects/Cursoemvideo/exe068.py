s = paim = n = 0
from random import randint
print ('-=-'*25)
print ('VAMOS JOGAR PAR OU IMPAR')
print ('-=-'*25)
while True:
    n = int(input('DIGITE UM  VALOR: '))
    pi = str(input('PAR OU IMPAR? [P/I]: ')).upper().strip()
    pc = randint(0 , 10)
    s = n + pc
    paim = s % 2
    if pi == 'I':
        if paim == 1:
            print ('VOCE VENCEU!!')
        else:
            print ('VOCE PERDEU!!')
            break
    print ('VAMOS JOGAR NOVAMENTE...')
    if pi == 'P':
        if paim == 0:
            print ('VOCE VENCEU!!!!!')
        else:
            print ('VOCE PERDEU!')
            break
 print ('-*-'*25)
print (f'VOCE JOGOU {n}E O COMPUTADOR {pc}. TOTAL DE {s}')
