#Resolução do Exercicio 01 do Grupo II
#Este algoritmo calcula a velocidade media
p1 = int(input ("Introduza os minutos de passagem no ponto 1: "))
p2 = int(input ("Introduza os minutos de passagem no ponto 2: "))
Distancia = int(input ("Introduza a distancia (metros): "))


Duração_M = p2 - p1
Duração_S = Duração_M * 60
V_Media = Distancia / Duração_S

print (F" {V_Media:.3f} m/s")