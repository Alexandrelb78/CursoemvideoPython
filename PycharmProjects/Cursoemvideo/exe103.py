def ficha (nome='<DESCONHECIDO>', gols=0):
    print ('-'*30)
    nome = str (input('NOME DO JOGADOR: '))
    if nome.strip() == '':
        print( 'DESCONHECIDO' )
    gols = str (input('NUMERO DE GOLS: '))
    if gols.isnumeric():
        gols = int(go)
    else:
        gols = 0
    return f'O JOGADOR {nome} FEZ {gols}(S) NO CAMPEONATO'


print (ficha())

