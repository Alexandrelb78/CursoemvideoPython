from time import sleep
def contador(a, b, c):
    print('-=' * 40)
    print(f'CONTAGEM DE {a} ATÉ {b} DE {c} A {c}')
    for c in range(a, b, c):
        sleep(0.5)
        print(c, end=' ')
    print ('FIM!')
    print ('-='*40)


contador(1, 10, 1)
contador(10, 0, -2)
print ('AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!')
inicio = int (input('INICIO: '))
fim = int (input('FIM: '))
passo = int (input('PASSO: '))
if passo == 0:
    passo = 1
print('-=' * 40)
contador(inicio, fim, passo)



