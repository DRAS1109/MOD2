#Este programa calcula os pontos restantes da carta de condução
Muito_grave = 0
Grave = 0
Leve = 0
Infração = 0

Pontos = (input("Introduza o numero de pontos disponiveis: "))
if Pontos == "":
    Pontos = 12
else:
    Pontos = int(Pontos)

while Infração != "4":
    print(f"Tem {Pontos} pontos.")
    print("Escoha uma opção (O numero correspondente à  infração):")
    Infração = input("1- Muito grave, 2- Grave, 3- Leve, 4- Terminar: ")
    Infração = Infração.strip()

    if Infração == "1":
        Muito_grave = Muito_grave + 1
        Pontos = Pontos - 6

    elif Infração == "2":
        Grave = Grave + 1
        Pontos = Pontos - 4

    elif Infração == "3":
        Leve = Leve + 1
        if Leve != 1:
            Pontos = Pontos - 1

    if (Muito_grave == 1 and Grave == 1) or (Grave == 2) or Pontos <= 0:
        print("Perdeu a sua carta")
