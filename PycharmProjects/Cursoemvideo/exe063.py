print ('SEQUÊNCIA DE FIBONACCI')
print ('-'*30)
n =  int (input ('QUANTOS VALORES INICIAIS VOCÊ QUER EXIBIR DA SEQUENCIA DE FIBONACCI: '))
t1 = 0
t2 = 1
c = 3
while c <= n:
    t3 = t1 + t2
    print('{} - '.format(t3), end='')
    t1 = t2
    t2 = t3
    c = c + 1
print ('FIM')
