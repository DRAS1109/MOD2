#Este programa vai utilizar um ciclo para calcular a soma de todos os nº a começar pelo primeiro inserido até ao segundo inserido

numero_1 = int(input("Introduza o 1º nº: "))
numero_2 = int(input("Introduza o 2º nº: "))

soma = 0

if numero_1 < numero_2:
    incremento = 1
else:
    incremento = -1

for i in range (numero_1, numero_2 + incremento, incremento):
    soma = soma + i
        
print(soma)