n = int (input ('DIGITE UM NUMERO PARA O CALCULO DO SEU FATORIAL: '))
c = n
f = 1
while c > 0:
    print ('{} x '.format (c), end = '')
    f = f * c
    c = c - 1
print ('O FATORIAL DE {} É IGUAL A {}'.format (n, f))