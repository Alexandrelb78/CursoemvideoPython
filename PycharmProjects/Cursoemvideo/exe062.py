print ('GERADOR DE PA')
print ('-='*20)
n = int(input ('DIGITE UM NUMERO: '))
p = int(input ('DIGITE A RAZÃO DA PA: '))
c = 1
t = n
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        c = c + 1
        t = t + p
        print ('{} - '.format (t), end = '')
    print ('PAUSA')
    mais = int (input ('QUANTOS TERMOS VOCÊ QUER A MAIS? '))
print ('TOTAL FINALIZADA COM {} TERMOS MOSTRADOS'.format (total))