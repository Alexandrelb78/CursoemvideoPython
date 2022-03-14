def leiaInt(msg):
    while True:
        try:
            n = int (input(msg))
        except(ValueError, TypeError):
            print ('\033[31mERRO: POR FAVOR, DIGITE UM NUMERO INTEIRO VALIDO.\033[m')
            continue
        except(KeyboardInterrupt):
            print ('\n\033[31mUSUARIO PREFERIU NÃO DIGITAR ESSE NUMERO.\33[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float (input(msg))
        except(ValueError, TypeError):
            print ('\033[31mERRO: POR FAVOR, DIGITE UM NUMERO INTEIRO VALIDO.\033[m')
            continue
        except(KeyboardInterrupt):
            print ('\n\033[31mUSUARIO PREFERIU NÃO DIGITAR ESSE NUMERO.\33[m')
            return 0
        else:
            return n


n1 = leiaInt('DIGITE UM INTEIRO: ')
n2 = leiaFloat('DIGITE UM REAL: ')
print (f'O VALOR INTERIO DIGITADO FOI {n1} E O REAL FOI {n2}')
