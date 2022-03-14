nome = 'ALEXANDRE'
idade = 43
altura = 1.71
ano_atual = 2021
ano_nascimento = ano_atual - idade
e_maior = idade > 18
peso = 76
imc = peso / (altura * altura)

print (f'{nome} TEM {idade} ANOS, {altura} DE ALTURA E PESA {peso} Kg.')
print (f'O IMC DE {nome} É {imc:.2f}.')
print (f'{nome} NASCEU EM {ano_nascimento}')
