colegio = []
aluno = []
while True:
    aluno.append(str(input('NOME DO ALUNO: ').upper()))
    aluno.append(float(input('NOTA 1: ')))
    aluno.append(float(input('NOTA 2: ')))
    media = (aluno[1]+aluno[2])/2
    aluno.append(media)
    colegio.append(aluno[:])
    aluno.clear()
    resp = str(input('DESEJA CONTINUAR [S/N]: ')).upper()
    if resp == 'N':
        break
print ('=-'*30)
print (f'{"Nº":<4}{"ALUNO":<10}{"MEDIA":>8}')
print ('-'*30)
for p, a in enumerate(colegio):
    print (f'{p:<4}{a[0]:<10}{a[3]:>8.1f}')
while True:
    print ('-='*30)
    opc = int(input('DESEJA MOSTRAR A NOTA DE QUAL ALUNO [999 INTERROMPE]: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(colegio)-1:
        print(f'NOSTAS DE {colegio[opc][0]} SÃO {colegio[opc]}')
print('<<<<<<<<< VOLTE SEMPRE >>>>>>>>>')
