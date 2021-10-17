"""
len - Faz contagem de caracteres digitados pelo usuário
"""

# usuario = input('Digite seu usuário: ')
# qtd_caracteres = len(usuario)
#
# if qtd_caracteres < 6:
#     print('Você precisa digitar pelo menos 6 caracteres.')
# else:
#    print('VocÊ foi cadastrado no sistema.')
#
#  print(usuario, qtd_caracteres, type(qtd_caracteres))

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(len(string2))
print(string2.__len__())

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')