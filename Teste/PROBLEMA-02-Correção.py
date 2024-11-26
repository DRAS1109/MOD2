Total_Gasto = 0

Capacidade = int(input("Qual a capacidade do depósito (litros)? "))

if Capacidade >= 100 and Capacidade <= 1000:
    for i in range (1, 10 + 1):
        Valor_Gasto = int(input(f"{i}ª rega: "))

        if Total_Gasto + Valor_Gasto > Capacidade:
            break
        Total_Gasto += Valor_Gasto
    print("Total Gasto: ", Total_Gasto)
    print("Sobra no depósito: ", Capacidade - Total_Gasto)

else:
    print("Capacidade inválida")