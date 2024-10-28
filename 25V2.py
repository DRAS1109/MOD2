#Este programa avisa quando as 10 mesas cada uma com 5 cadeiras estiverem todas ocupadas

mesas = 10
lugares = mesas * 5

while mesas > 0:
    pessoas = int(input("Introduza o nº de pessoas: "))
    if pessoas > lugares:
        print ("Não há lugares para tantos clientes")
        break

    mesas = mesas - 1
    lugares = lugares - pessoas
    print (f"Mesas vazias: {mesas}")
    print (f"Lugares livres: {lugares}")

    if mesas == 0:
        print ("Não há mais mesas disponiveis")
        break