#Este algoritmo diz se o usuario é adulto ou não
Ano_de_NAscimento = int(input ("Introduza o ano do seu nascimento: "))

Ano_Atual = 2024
Idade = Ano_Atual - Ano_de_NAscimento
Adulto = Idade >= 18

if Adulto == True:
    print ("És adulto")
    print ("Já podes votar e tirar a carta de carro")
else:
    print ("Não és adulto")
    print ("Ainda nao podes votar e tirar a carta de carro")