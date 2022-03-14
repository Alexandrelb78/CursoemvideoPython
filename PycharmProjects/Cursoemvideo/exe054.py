from datetime import date
totmaior = 0
totmenor = 0
for c in range (1 , 8):
    ano = int(input('DIGITE O SEU ANO DE NASCIMENTO: '))
    mid = ((date.today().year) - ano)
    if mid >= 21:
             totmaior = totmaior + 1
    elif mid < 21:
             totmenor = totmenor + 1
print ('{} PESSOAS ATINGIRAM A MAIORIDADE.'.format (totmaior))
print ('{} PESSOAS NÃO ATINGIRAM A MAIORIDADE.'.format (totmenor))
print ('FIM')