#Dinis Rafael Albuquerque de Sousa, Nº3 10ºT

N_Conta = int(input("Introduza o Nº da conta: "))
Saldo = float(input("Introduza o saldo disponivel: "))
Ação = input("Qual ação pretende efetuar?\nIntroduza as letras correspondentes: D: Depositar | L: Levantar \n")
Saldo_I = Saldo

Valor = float(input("Valor: "))
if Valor > 0: 
    if Ação.upper() == "D":
        Saldo = Saldo + Valor
        print (f"Nº da conta: {N_Conta}")
        print (f"Saldo Inicial: {round (Saldo_I,2)}€")
        print (f"Saldo Final: {round (Saldo,2)}€")
        
    elif Ação.upper() == "L":
        if Valor <= Saldo:
            Saldo = Saldo - Valor
            print (f"Nº da conta: {N_Conta}")
            print (f"Saldo Inicial: {round (Saldo_I,2)}€")
            print (f"Saldo Final: {round (Saldo,2)}€")
            
        else:
            print("O seu saldo não permite efetuar a operação")
            print (f"Nº da conta: {N_Conta}")

    else:
        print ("Não existe nenhuma operação com essa abreviatura")

else: 
    print ("Não é possivel realizar esta operação")