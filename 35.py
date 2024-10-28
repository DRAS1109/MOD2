#Este programa imprime todos os numeros inferiores a 100, com excecao dos multiplos de 3

vz = 100

for i in range (vz):
    if i % 3 != 0:
        print (i)