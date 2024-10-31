#Este programa vai utilizar um ciclo para calcular a serie de fibonacci

x1 = 0
x2 = 1

vz = int(input("Introduza o nº vz: "))
print(x1)
print(x2)

for _ in range (vz - 2):
    soma = x1 + x2
    print(soma)
    x1 = x2
    x2 = soma
