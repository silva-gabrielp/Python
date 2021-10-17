"""
Operadores Lógicos - Aula 9
and, or, not
in e not in
"""
#  AND
#  (Verdadeiro E Verdadeiro) = Verdadeiro
#  (Verdadeiro E Falso) = Falso

#  OR
#  (Verdadeiro OU Verdadeiro) = Verdadeiro
#  (Verdadeiro E Falso) = Verdadeiro

a = ''
b = 0

if not a:
    print('Por favor, preencha o valor de A.')

nome = 'Gabriel Silva.'
if 'e' in nome:
    print("Existe a letra E no seu nome")
else:
    print("Não existe.")
