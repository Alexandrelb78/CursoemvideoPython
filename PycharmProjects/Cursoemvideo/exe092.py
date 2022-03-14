from datetime import date
empresa = {}
while True:
    print ('=-'*30)
    print ('CADASTRO DE PESSOAL DA EMPRESA')
    print ('=-'*30)
    empresa ['nome'] = str(input('NOME: ')).upper()
    empresa ['anonasci'] = int (input ('ANO DE NASCIMENTO: '))
    empresa ['carteira'] = int (input ('CARTEIRA DE TRABALHO [0 não tem]: '))
    empresa ['anocontrata'] = int (input ('ANO DE CONTRATAÇÃO: '))
    empresa ['salario'] = float (input ('SALÁRIO: R$ '))
    print ('#'*30)
    resp = str (input ('DESEJA FAZER OUTRO CADASTRO [S/N]: ')).upper()
    if resp == 'N':
        break
print (f'FUNCIONÁRIO: {empresa ["nome"]}')
print (f'IDADE: {((date.today().year) - empresa ["anonasci"])}')
if empresa['carteira'] != 0:
    print (f'CARTEIRA: {empresa ["carteira"]}')
    print (f'ANO DE CONTRATAÇÃO: {empresa ["anocontrata"]}')
    print (f'SALÁRIO: {empresa ["salario"]}')
    print (f'APOSENTADORIA EM {(((date.today().year) - empresa ["anonasci"]) - ((date.today().year) - empresa ["anocontrata"]) + 35)}')
else:
    print(f'CARTEIRA: {empresa["carteira"]}')
print ('FIM CADASTRO')
