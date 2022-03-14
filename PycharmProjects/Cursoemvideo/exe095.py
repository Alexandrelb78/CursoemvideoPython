vasco = []
atleta = []
rendimento = {}
gols = []
soma = 0
while True:
    rendimento['jogador'] = str(input('NOME DO JOGADOR: ')).upper()
    partidas = int(input(f'QUANTAS PARTIDAS {rendimento["jogador"]} JOGOU: '))
    gols.clear()
    for g in range(0, partidas):
        gols.append(int(input(f'QUANTAS GOLS NA PARTIDAS {g}?: ')))
    rendimento['total'] = sum (gols)
    rendimento['gols'] = gols[:]
    atleta.append(rendimento.copy())
    vasco.append(atleta[:])
    atleta.clear()
    while True:
        resp = str(input('DESEJA CONTINUAR [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print ('ERRO! RESPONDA SOMENTE S OU N ')
    if resp == 'N':
        break
print (vasco)
print ('FIM')
