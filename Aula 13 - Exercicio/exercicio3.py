nome = input("Qual o seu primeiro nome? ")

qtd_cact = len(nome)

if qtd_cact <= 4:
    print("Seu nome é curto")

elif 5 <= qtd_cact <= 6:
    print("Seu nome é normal")

else:
    print("Seu nome é muito grande")