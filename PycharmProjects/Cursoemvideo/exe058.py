from random import randint
from time import sleep
n = 0
computador = int
jogador = int
print ('-*'*30)
print ('VAMOS ADIVINHAR O NUMERO DE 0 A 10 QUE ESTOU PENSANDO')
print ('-*'*30)
computador = randint(0,10)
jogador = int (input ('ESCOLHA SEU NÚMERO: '))
print ('COMPUTADOR PENSANDO......')
sleep (1)
while computador != jogador:
    computador = randint(0,10)
    jogador = int (input ('ESCOLHA SEU NÚMERO: '))
    print ('COMPUTADOR PENSANDO......')
    sleep (1)
    n = n + 1
print ('''PARABENS, VOCE ACERTOU O NUMERO {}
          APÓS {} TENTATIVAS!!!
          BOM DIA.'''.format(jogador, n))


