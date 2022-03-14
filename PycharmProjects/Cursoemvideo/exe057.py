F = str
M = str
sexo = str (input('DIGITE SEU SEXO [ M / F]: ')).upper().strip()
while sexo != 'F' and sexo != 'M':
    print ('RESPOSTA ERRADA, TENTE NOVAMENTE!')
    sexo = str (input ('DIGITE SEU SEXO [M / F]: ')).upper().strip()
print ('OBRIGADO!')