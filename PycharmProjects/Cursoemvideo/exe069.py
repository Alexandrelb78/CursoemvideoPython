cad = H = M = id = sx = 0
while True:
    print ('-='*25)
    print ('PADARIA MONTEIRO')
    print ('-='*25)
    id = int (input ('DIGITE SUA IDADE: '))
    sx = ' '
    while sx not in 'MH':
        sx = str (input ('DIGITE SEU SEXO[H/M]: ')).upper().strip()[0]
    if sx == 'H':
        H = H + 1
    if sx == 'M' and id < 20:
        M = M + 1
    if id > 18:
        cad = cad + 1
    op = ' '
    while op not in 'SN':
        op = str (input ('DESEJA CONTINUAR [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break
print ('*='*25)
print ('FIM DO PROGRAMA DE CADASTRO')
print ('*='*25)
print (f'O CADASTRO POSSUI {cad} PESSOSAS COM MAIS DE 18 ANOS')
print (f'O CADASTRO POSSUI {H} HOMENS CADASTRADOS')
print (f'O CADASTRO POSSUI {M} MULHERES COM MENOS DE 20 ANOS')
