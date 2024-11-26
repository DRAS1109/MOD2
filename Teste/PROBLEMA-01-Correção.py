Saldo_I = float(input("Saldo Inicial: "))
N_Conta = int(input("Nº da Conta: "))
Operação = input("Qual a operação: \n Levantamento: L \n Deposito: D \n")
Valor = float(input("Valor da Operação: "))

if Valor <= 0:
    print ("O valor da operação é invalido")

else:
    if Operação.upper() == "L":
        Saldo_F = Saldo_I - Valor

    elif Operação.upper() == "D":
        Saldo_F = Saldo_I + Valor
    
    else: 
        print("Operação inválida")
    print("Numero da Conta: ", N_Conta)

    if Saldo_F < 0:
        print ("O seu saldo não permite esta ação")

    else:
        print("Saldo Inicial: ", round(Saldo_I, 2))
        print("Saldo Final: ", round(Saldo_F, 2))