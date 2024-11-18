"""
Este programa vai gerir o embarque num aviao
Nº de lugares do aviao
Nº de bilhetes totais
Ler o nome dos passageiros e guardar nua string separados por \n
Se inserir um nome em branco o programa termina e mostra os nomes dos clientes e quantos entraram
O mesmo se o aviao estiver cheio
"""

N_Passageiros = 0
Todos_Nomes = ""

N_Lugares = int(input("Introduza o Nº de lugares do avião: "))
N_Bilhetes = int(input("Introduza o Nº de bilhetes vendidos: "))

for i in range (1, N_Bilhetes + 1):
    if N_Bilhetes > N_Lugares:
        print ("Overbooking é proibido, ligando para as autoridades para alertar...")
        break
    Nome = input(f"Introduza o nome do {i}º cliente: ")
    
    if Nome != "":
        N_Passageiros = N_Passageiros + 1
        Todos_Nomes = Todos_Nomes + Nome + " \n"

    else:
        print (f"Entraram {N_Passageiros} passageiros e os nomes são:")
        break

print (Todos_Nomes)