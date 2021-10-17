nome = 'Gabriel'
idade = 24
ano_atual = 2021
altura = 1.70
peso = 98.5

nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{0} tem {1} anos, {2} de altura e pesa {3}kg.'.format(nome, idade, altura, peso))
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'Gabriel nasceu em {nascimento}.')