rendimento = {}
gols = []
soma = 0
rendimento ['jogador'] = str (input('NOME DO JOGADOR: ')).upper()
partidas = int (input (f'QUANTAS PARTIDAS {rendimento["jogador"]} JOGOU: '))
for g in range (0, partidas):
    gols.append(int(input(f'QUANTAS GOLS NA PARTIDAS {g}?: ')))
    soma = soma + (gols[g])
rendimento ['total'] = soma
rendimento ['gols'] = gols [:]
print ('=-'*30)
print (f'JOGADOR {rendimento["jogador"]} MARCOU {rendimento["gols"]} TOTAL GOLS: {rendimento["total"]}')
print ('=-'*30)
for k, v in rendimento.items():
    print (f'O CAMPO {k} TEM VALOR {v}')
print ('=-'*30)
print (f'O JOGADOR {rendimento["jogador"]} JOGOU {partidas} PARTIDAS.')
for p, g in enumerate (gols):
    print (f'=> NA PARTIDA {p}, FEZ {g} GOLS.')
print (f'FOI UM TOTAL DE {rendimento["total"]}')

