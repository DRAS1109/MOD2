#Quantos dias faltam para o fim do mes

Dia = int(input("Introduza o dia do ano: "))
Mes = input("Introduza o mes do ano: (1 - Janeiro, 10 - Outubro) ")
Ano = int(input("Introduza o ano: "))

if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    Fevereiro = 29

else:
    Fevereiro = 28


if Mes in ("1","3","5","7","8","10","12"):
    DMes = 31

elif Mes in ("4","6","9","11"):
    DMes = 30

elif Mes in ("2"):
    DMes = Fevereiro


if Dia <= DMes and Mes <= 12:
    DDia = DMes - Dia
    print (f"Faltam {DDia} dias para o fim do mes")

else:
    print ("Dados invalidos")