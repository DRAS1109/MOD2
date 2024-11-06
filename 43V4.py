#Todos os exercicios nomeados de 43 pertencem ao Desafio 0
#Um programa para avisar quando a carga do avião chegar a 1000 Kg e diz qual o valor apurado

Carga = 0
V_Apurado = 0

while Carga <= 1000:
    P_Mala = float(input("Introduza o peso da mala: "))
    Carga = Carga + P_Mala
    if Carga <= 1000:
        V_Apurado = V_Apurado + 20
        print(f"Ainda pode trasnportar {1000 - Carga}Kg")

print (f"Conseguiu apurar {V_Apurado}€")