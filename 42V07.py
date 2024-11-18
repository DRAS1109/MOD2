#Todos os exercicios nomeados de 42 pertencem ao ficheiro: PSI-M02-Desafio 02-Repetição.pdf

N = int(input("Introduza um numero: "))
N_Primo = True

for divisor in range(2, N):
    if N % divisor == 0:
        N_Primo = False

if N_Primo == True:
    print(f"O nº {N} é um nº primo")

else:
    print(f"O nº {N} não é um nº primo")