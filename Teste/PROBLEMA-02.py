#Dinis Rafael Albuquerque de Sousa, Nº3 10ºT

Deposito = int(input("Qual a capacidade maxima do deposito? "))
Total_Gasto = 0

if Deposito >= 100 and Deposito <= 1000:
    for i in range (1, 10 + 1):
        if Deposito > 0:
            Rega = int(input(f"{i}º Rega: "))
            if Deposito - Rega >= 0:
                Deposito = Deposito - Rega
                Total_Gasto = Total_Gasto + Rega
            else: 
                print ("Ja gastou a água toda. \nResultados da rega anterior:")
                break

    print(f"Total de água gasta: {Total_Gasto}")
    print(f"Sobra do depósito: {Deposito}")


else:
    print("Não é possivel efetuar os calculos neste deposito")