def voto(ano):
    from datetime import date
    data = date.today().year
    eleicao = data - ano
    if 18 <= eleicao < 70:
        return f'COM {eleicao} VOTO OBRIGATORIO'
    elif 16 <= eleicao < 18 or eleicao > 65:
        return f' COM {eleicao} VOTO OPCIONAL'
    elif eleicao < 16:
        return f' COM {eleicao} VOTO NEGADO'

print ('-'*30)
nasc = int (input ('EM QUE ANO VOCÊ NASCEU:  '))
print (voto(nasc))



