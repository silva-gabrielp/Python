"""
Formatando valores com modificadores - Aula 14

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float) - :.2f
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f) -

> - Esquerda
< - Direita
^ - Centro
"""

#  num_1 = 10
#  num_2 = 3
#  divisao = num_1 / num_2
#  print( '{:.2f}'.format(divisao) )
#  print( f'{divisao:.2f}' )

#  nome = 'Gabriel Silva'
#  print(f'{nome:s}')

#  nome = 'Gabriel Silva'
#  print((50-len(nome)) / 2 )
#  print(f'{nome:#^50}')

#  num_1 = 1
#  print(f'{num_1:0>10}')

#  num_2 = 1150
#  print(f'{num_2:0<10}')
#  print(f'{num_2:.2f}')
#  print(f'{num_2:0>10.2f}')

#  nome = 'Gabriel'
#  sobrenome = 'Silva'
#  nome_formatado = '{:#^50}'.format(nome)
#  nome_formatado = '{n:0<20}'.format(n=nome)
#  nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
#  print(nome_formatado)

#  nome = 'Gabriel Silva'
#  nome = nome.ljust(20, '#')
#  print(nome)

nome = 'Gabriel Silva'
print(nome.lower())  # Tudo meniscus
print(nome.upper())  # Tudo maiúsculas
print(nome.title())  # Primeiras letra maiúculas
