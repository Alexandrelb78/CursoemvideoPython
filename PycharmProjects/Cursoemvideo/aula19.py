estado = {} # cria um dicionario
brasil = [] # cria uma lista
for c in range (0,3):
    estado['UF'] = str (input ('UNIDADE FEDERATIVA: ')).upper()
    estado['SIGLA'] = str (input ('SIGLA DO ESTADO: ')).upper()
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print (f'O CAMPO {k} TEM VALOR {v}.')
print (brasil)