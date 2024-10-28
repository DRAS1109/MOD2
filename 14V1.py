#Este programa vai utilizar um ciclo para calcular a soma de todos os nº de 1 até ao nº que o utilizador inserir

numero = int(input("Introduza o nº: "))

soma = 0

for i in range (1, numero + 1):
    soma = soma + i
    
print(soma)