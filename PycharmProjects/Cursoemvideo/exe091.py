from random import randint
from time import sleep
from operator import itemgetter
dados = {}
ranking = []
for c in range (1, 5):
    num = randint(1, 6)
    dados ['JOGADOR'] = c
    dados ['NUMERO'] = num
    print (f'O JOGADOR {dados["JOGADOR"]} TIROU {dados["NUMERO"]}')
    sleep(1)
print ('*'*30)
ranking = sorted (dados.items(), key= itemgetter(dados['JOGADOR']), reverse=True)
print ('*'*30)
print (' == RANKING DOS JOGADORES ==  ')
for i, v in enumerate (ranking):
    print (f' {i + 1}º LUGAR: {v[0]} COM {dados["NUMERO"]}')
print ('FIM')
