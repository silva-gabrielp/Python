nome = 'Gabriel Silva'
idade = 32  # int
altura = 1.80  # float
e_maior = idade > 18  # bool
peso = 80  # int
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))