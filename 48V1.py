#Caixa Multibanco
#1 - Ver Saldo | 2- Depositar Dinheiro (min: 0.01, max: 10000)| 3- Levantar Dinheiro (min: 10, max: 400)| 4 - Terminar

Ação = "O"
Saldo = float(input("Introduza o saldo disponivel: "))

while Ação.upper() != "T":
    print (f"\nTem disponivel {round(Saldo, 2)}€")
    Ação = input("Qual ação pretende efetuar?\nIntroduza as letras correspondentes: D: Depositar | L: Levantar | T: Terminar  ")
    print("")

    if Ação.upper() == "D":
        Valor = float(input("Introduza o valor a depositar: "))
        if Valor - round (Valor, 2) == 0:
            if Valor > 0.01 and Valor < 10000:
                Saldo = Saldo + Valor
            else: 
                print ("Para efetuar essa operação terá de ir ao banco \n" )
        else:
            print("O valor não é valido, só pode ter 2 casas decimais.")


    elif Ação.upper() == "L":
        Valor = float(input("Introduza o valor a levantar: "))
        if Valor - round (Valor, 2) == 0:
            if Valor > 10 and Valor < 400 and Saldo > Saldo - Valor:
                    Saldo = Saldo - Valor
            else: 
                print ("Para efetuar essa operação terá de ir ao banco")
                print ("")
        else:
            print("O valor não é valido, só pode ter 2 casas decimais.")