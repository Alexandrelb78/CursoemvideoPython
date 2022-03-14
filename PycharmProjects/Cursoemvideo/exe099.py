from time import sleep
def maior(*inteiro):
    cont = maior = 0
    print ('-='*40)
    print ('ANALISANDO OS VALORES PASSADOS...')
    for valor in inteiro:
        print (f'{valor}', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1
    print ((inteiro), end='')
    print (f'FORAM INFORMADOS {cont} VALORES AO TODO')
    print (f'O MAIOR VALOR INFORMADO FOI {maior}')
    print ('-=*'*40)


maior (2, 9, 4, 5, 7, 1)
maior (4, 7, 0)
maior (1, 2)
maior (6)
maior ()
