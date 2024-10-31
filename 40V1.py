#Ano Bissexto
Ano = int(input("Introduza um ano: "))

if Ano % 4 == 0:
    if Ano % 100 != 0:
        print ("É um ano bissexto")

    else:
        print ("Não é um ano bissexto")