lista = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    num = int (input ('DIGITE UM NÚMERO: '))
    if 0 <= num <= 10:
        break
    print ('TENTE NOVAMENTE. ', end = '')
print (f'VOCE DIGITOU O NUMERO {lista [num]}')