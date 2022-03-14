print('GERADOR DE PA')
print ('=-'*20)
n = int (input('DIGITE UM NUMERO: '))
p = int (input ('DIGITE A RAZAO DA PA: '))
c = 1
t = n
while c <= 10:
    c = c + 1
    t = t + p
    print ('{} - '.format (t), end ='')
print ('FIM')