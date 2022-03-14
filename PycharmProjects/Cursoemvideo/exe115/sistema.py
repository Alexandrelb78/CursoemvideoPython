from exe115.lib.interface import*
from exe115.lib.arquivo import*
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu (['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opçao de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str (input ('NOME: ')).upper()
        idade = leiaInt('IDADE: ')
        cadastrar (arq, nome, idade)
    elif resposta == 3:
        cabeçalho ('Saindo do sistema .... Até logo!!!')
        break
    else:
        print ('\033[31mERRO! Digite uma opção válida\033[m')
        sleep(2)
