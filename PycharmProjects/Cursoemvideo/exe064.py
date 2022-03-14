c = s = n = 0
print ('-*'*15)
print ('TRATANDO VALORES!!!! PARA SAIR DIGITE 999')
print ('-*'*15)
while n != 999:
    c = c + 1
    n = int (input ('DIGITE UM NUMERO QUALQUER: '))
    s = s + n
print ('VOCÊ DIGITOU {} VALORES E O SOMATÓRIO É {}'.format ((c - 1),(s - 999)))
print ('FIM')



