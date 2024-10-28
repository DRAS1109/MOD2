#Este programa vai utilizar um ciclo para calcular a soma de todos os nº a começar pelo primeiro inserido até ao segundo inserido

numero_1 = int(input("Introduza o 1º nº: "))
numero_2 = int(input("Introduza o 2º nº: "))

if numero_1 > numero_2:
    t = numero_1
    numero_1 = numero_2 
    numero_2 = t

soma = 0

for i in range (numero_1, numero_2 + 1):
    soma = soma + i
        
print(soma)