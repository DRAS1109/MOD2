#Ano Bissexto
Ano = int(input("Introduza um ano: "))

if Ano % 4 == 0 and  Ano % 100 != 0 or Ano % 400 == 0:
    print ("É um ano bissexto")

else:
    print ("Não é um ano bissexto")