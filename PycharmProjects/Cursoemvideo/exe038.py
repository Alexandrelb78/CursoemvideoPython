n1 = int (input ('DIGITE UM NUMERO: '))
n2 = int (input ('DIGITE OUTRO NUMERO: '))
if n1 > n2:
    print ('O PRIMEIRO VALOR {} É MAIOR QUE O SEGUNDO VALOR {}'.format (n1 , n2))
elif n2 > n1:
    print('O SEGUNDO VALOR {} É MAIOR QUE O PRIMEIRO VALOR {}'.format(n2, n1))
else:
    print ('NÃO EXISTE VALOR MAIOR, OS DOIS VALORES SÃO IGUAIS')