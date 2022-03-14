cadastro = {}
cadsec = []
mulheres = []
soma = 0
while True:
    cadastro ['nome'] = str (input('NOME: ')).upper()
    while True:
        cadastro ['sexo'] = str (input('SEXO [M/F]: ')).upper()[0]
        if cadastro ['sexo'] in 'MF':
            break
        print ('ERRO! POR FAVOR, DIGITE APENAS M OU F')
    cadastro ['idade'] = float (input ('IDADE: '))
    while True:
        resp = str (input ('DESEJA CONTINUAR [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print ('ERRO! RESPONDA APENAS S OU N')
    cadsec.append(cadastro.copy())
    if resp == 'N':
        break
print ('=-'*30)
print (f'O GRUPO TEM {len(cadsec)}.')
for m in range (0, (len(cadsec))):
    soma = soma + (cadsec[m]['idade'])
media = (soma / (len(cadsec)))
print (f'A MÉDIA DE IDADE DO GRUPO É {media:.2f}.')
for s in range (0, (len(cadsec))):
    if (cadsec[s]['sexo']) == 'F':
        mulheres.append(cadsec[s]['nome'])
print (f'AS MULHERES CADASTRADAS FORAM: {mulheres}')
print ('LISTA DAS PESSOAS COM IDADE ACIMA DA MÉDIA:')
for i in range (0, (len(cadsec))):
    if (cadsec[i]['idade']) >= media:
        print (f'NOME:{cadsec[i]["nome"]}   SEXO:{cadsec[i]["sexo"]}   IDADE:{cadsec[i]["idade"]}')
print (('<>'*20), ('ENCERRADO'), ('<>'*20))
