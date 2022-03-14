from exe108 import moeda
p = float (input ('DIGITE O PREÇO: R$ '))
print (f'A METADE DE {moeda.moeda(p)} É {moeda.moeda(moeda.metade(p))}')
print (f'O DOBRO DE {moeda.moeda(p)} É {moeda.moeda(moeda.dobro(p))}')
print (f'AUMENTANDO EM 10%, TEMOS {moeda.moeda(moeda.aumentar(p,10))}')

