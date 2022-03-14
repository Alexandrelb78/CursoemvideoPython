from random import choice
lista = int
cedu = sac = 0
print ('-=-'*30)
print ('{:^30}'.format('BANCO REAL'))
print ('-=-'*30)
lista = [1,10,20,50]
nota = choice(lista)
valor = int (input ('VALOR A SACAR: R$ '))
while True:
    sac = valor / nota
    if sac > 0:
       cedu = cedu + 1
       print(f'TOTAL DE {cedu} CEDULAS DE R$ {nota}')
    if sac == 0:
        break
print(f'TOTAL DE {cedu} CEDULAS DE R$ {nota}')
print ('-=-'*35)
print ('VOLTE SEMPRE AO BANCO REAL. TENHA UM BOM DIA!!')
print ('-=-'*35)
