from exe110 import moeda
p = float (input ('DIGITE O PREÇO: R$ '))
print (f'A METADE DE {moeda.moeda(p)} É {moeda.metade(p, True)}')
print (f'O DOBRO DE {moeda.moeda(p)} É {moeda.dobro(p, True)}')
print (f'AUMENTANDO EM 10%, TEMOS {moeda.aumentar(p,10, True)}')

