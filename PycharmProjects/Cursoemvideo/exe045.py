from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print ('VAMOS JOGAR JOKENPO')
print ('-=-'*20)
print ('EU SOU O COMPUTADOR E VOU ESCOLHER A MINHA OPÇÃO')
print ('-=-'*20)
jogador = int (input ('''ESCOLHA A SUA OPÇÃO:
[0] PEDRA
[1] PAPEL
[2] TESOURA
QUAL A SUA JOGADA: '''))
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PO!!!')
sleep(1)
comput = randint(0 , 2)
if comput == jogador:
    print ('EMPATE')
elif comput == 0 and jogador == 2:
    print ('EU GANHEI, PEDRA GANHA DE {}.'.format (jogador))
elif comput == 0 and jogador == 1:
     print ('VOCÊ GANHOU, PEDRA PERDE DE {}.'.format (jogador))
elif comput == 1 and jogador == 1:
    print ('EMPATE')
elif comput == 1 and jogador == 0:
    print ('EU GANHEI, PAPEL GANHA DE {}.'.format (jogador))
elif comput == 1 and jogador == 2:
    print ('VOCÊ GANHOU, PAPEL PERDE DE {}.'.format (jogador))
elif comput == 2 and jogador == 2:
    print ('EMPATE')
elif comput == 2 and jogador == 1:
    print ('EU GANHEI, TESOURA GANHA DE {}.'.format (jogador))
elif comput == 2 and jogador == 0:
    print ('VOCÊ GANHOU, TESOURA PERDE DE {}.'.format (jogador))

