#Este algoritmo diz todos os divisores do numero inserido

n_utilizador = int(input("Introduza um numero: "))

for i in range (n_utilizador + 1, 0, -1):
    if n_utilizador % i == 0:
        print (i) 