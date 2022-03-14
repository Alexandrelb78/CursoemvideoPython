num = input('DIGITE UM NUMERO INTEIRO: ')
if num.isdigit():
    num = int(num)
    if num %2 == 0:
       print ('ESTE NUMERO É PAR!!')
    else:
        print ('ESTE NUMERO É IMPAR!!')
else:
    print ('VOCê NÃO DIGITOU UM NUMERO INTEIRO, DIGITE NOVAMENTE POR FAVOR!!')
    num = input('DIGITE UM NUMERO INTEIRO: ')
    num = int(num)
    if num %2 == 0:
       print ('ESTE NUMERO É PAR!!')
    else:
        print ('ESTE NUMERO É IMPAR!!')
print('OBRIGADO, BOM DIA!!!')
