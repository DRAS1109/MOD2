#Todos os exercicios nomeados de 42 pertencem ao ficheiro: PSI-M02-Desafio 02-Repetição.pdf

N = int(input("Introduza um numero: "))
Fatorial = 1

for i in range (1, N + 1):
    Fatorial = Fatorial * i

print(f"O fatorial de {N} é {Fatorial}")