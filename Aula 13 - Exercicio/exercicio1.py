num_int = input('Digite um número: ')

if num_int.isdigit():
    num_int = int(num_int)

    if num_int % 2 == 0:
        print(f"{num_int} Número par")
    else:
        print(f"{num_int} Número ímpar")
else:
    print('Não é um número inteiro.')