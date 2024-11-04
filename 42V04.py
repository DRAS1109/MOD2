#Todos os exercicios nomeados de 42 pertencem ao ficheiro: PSI-M02-Desafio 02-Repetição.pdf
#Este programa avisa quando a carga maxima do avião é excedida

Carga = 0
Dinheiro = 0

while Carga < 1001:
    Peso = int(input("Introduza o peso da mala: "))
    Carga = Carga + Peso
    if Carga <= 1000:
        Dinheiro = Dinheiro + 20
        print(f"Ainda tem disponivel {1000 - Carga} Kg")

print (f"Excedeu o peso maximo suportado e apurou {Dinheiro}€")