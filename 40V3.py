#Quantos dias faltam para o fim do ano

Dia = int(input("Introduza o dia do ano: "))
Mes = int(input("Introduza o mes do ano: (1 - Janeiro, 10 - Outubro): "))
Ano = int(input("Introduza o ano: "))
DAno = 0

if Ano % 4 == 0:
    if Ano % 100 != 0:
        DFevereiro = 29

    else:
        DFevereiro = 28

if Mes in (1,3,5,7,8,10,12):
    DMes = 31

elif Mes in (4,6,9,11):
    DMes = 30

elif Mes == 2:
    DMes = DFevereiro

DMesAtual = DMes - Dia
Mes = Mes + 1


while Mes <= 12:

    if Mes in (1,3,5,7,8,10,12):
        DMes = 31

    elif Mes in (4,6,9,11):
        DMes = 30

    elif Mes in (2):
        DMes = DFevereiro

    DAno = DAno + DMes
    Mes = Mes + 1


DAno = DAno + DMesAtual

print (f"Faltam {DAno} dias para o fim do ano")