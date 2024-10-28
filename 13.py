#Este programa vai utilizar um ciclo para calcular e mostrar a tabuada de um número

numero = int(input("Introduza o nº da tabuada: "))
qnt_vz = int(input("Quantas tabuadas quer fazer? "))

qnt_vz = qnt_vz + 1

for i in range (1, qnt_vz):
    print(i, "x", numero, "=", i * numero)