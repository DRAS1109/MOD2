#Calculadora Avançada

S_ou_N = "sim"

while S_ou_N ==  "sim":
    N1 = float(input("Introduza o primeiro numero: "))
    N2 = float(input("Introduza o segundo numero: "))
    Op = str(input("Qual operação deseja efetuar? (+ ou som, - ou sub, / ou div, * ou mul, ou somatorio) "))
    Op = Op.lower().strip()

    if Op in "+som":
        Conta = N1 + N2

    elif Op in "-sub":
        Conta = N1 - N2

    elif Op in "/div":
        Conta = N1 / N2

    elif Op in "*mul":
        Conta = N1 * N2

    elif Op in ("somatorio"):
        if N1 > N2:
            print ("Dados inválidos, o 1º tem de ser menor que o 2º numero.")
            continue
        Conta = 0
        N1 = int(N1)
        N2 = int(N2)
        for i in range (N1, N2 + 1):
            Conta = Conta + i

    else:
        print ("Operação inválida")
        Conta = None

    if Conta is not None:
        print (f"O resultado da operação é: {Conta}")

    S_ou_N = str(input("Deseja fazer mais contas? Sim ou Nao? "))
    S_ou_N = S_ou_N.lower().strip()
