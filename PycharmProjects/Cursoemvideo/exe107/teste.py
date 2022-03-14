import moeda
p = float (input ('DIGITE O PREÇO: R$ '))
print (f'A METADE DE R$ {p} É R$ {moeda.metade(p)}')
print (f'O DOBRO DE R$ {p} É R$ {moeda.dobro(p)}')
print (f'AUMENTANDO EM 10%, TEMOS R$ {moeda.aumentar(p,10)}')
print (f'REDUZINDO 13%, TEMOS R$ {moeda.diminuir(p,13)}')
