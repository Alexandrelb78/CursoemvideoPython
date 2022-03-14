menu = str
while menu != '5':
    pn = int (input ('DIGITE O PRIMEIRO NUMERO: '))
    sn = int (input ('DIGITE O SEGUNDO NUMERO: '))
    print ('-='*15)
    print ('ESCOLHA AS OPÇÕES ABAIXO!!!')
    print ('[1] SOMAR')
    print ('[2] MULTIPLICAR')
    print ('[3] MAIOR')
    print ('[4] NOVOS NÚMEROS')
    print ('[5] SAIR DO PROGRAMA')
    print ('-='*15)
    menu = input ('QUAL A SUA OPÇÃO: ')
    if menu == '1':
        soma = pn + sn
        print ('A SOMA ENTRE {} E {} É IGUAL A {}.'.format (pn, sn, soma))
    if menu == '2':
        mult = pn * sn
        print ('A MULTIPLICAÇÃO ENTRE {} E {} É IGUAL A {}.'.format (pn, sn, mult))
    if menu == '3':
        if pn > sn:
            print ('ENTRE OS NÚMEROS {} E {}, O MAIOR É {}.'.format (pn, sn, pn ))
        elif sn > pn:
            print('ENTRE OS NÚMEROS {} E {}, O MAIOR É {}.'.format (pn, sn, sn))
    if menu == '4':
        pn = int(input('DIGITE O PRIMEIRO NUMERO: '))
        sn = int(input('DIGITE O SEGUNDO NUMERO: '))
print ('FIM DO PROGRAMA! OBRIGADO!!!')
