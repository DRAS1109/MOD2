#Este programa vai utilizar um ciclo para calcular a soma de todos os nº pares de 1 até ao nº que o utilizador inserir

numero = int(input("Introduza o 2º nº: "))

soma = 0

for i in range (0, numero + 1, 2):
    soma = soma + i
    
print(soma)