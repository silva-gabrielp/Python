"""
Operadores Relacionais - Aula 9
== > >= < <= !=

== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor ou igual a
!= diferente

"""
#  num_1 = 2  # int
#  num_2 = 2  # int
#  expressao = num_1 > num_2
#  print(expressao)
#  print(num_1 == num_2)
#  print( 2 == 2 )

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

#  Limite para pegar empréstimo
idade_menor = 20  # Muito Jovem
idade_maior = 30  # Passou da idadeGa

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')