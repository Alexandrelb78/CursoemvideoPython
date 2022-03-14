cadastro = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('DIGITE SEU NOME: ')))
    dados.append(float(input('DIGITE SEU PESO: ')))
    if len(cadastro) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    resp = str (input('DESEJA CONTINUAR [S/N]: ')).upper()
    if resp == 'N':
        break
print (f'FORAM CADASTRADAS {len(cadastro)} PESSOAS')
print (f'A MAIOR PESO FOI {maior} KG. PESO DE ', end='')
for p in cadastro:
    if p[1] == maior:
        print (f'{p[0]} ', end='')
print ()
print (f'O MENOR PESO FOI  {menor} KG. PESO DE ', end='')
for p in cadastro:
    if p[1] == menor:
        print (f'{p[0]} ', end='')
print()
