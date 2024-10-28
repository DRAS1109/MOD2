#Este algoritmo diz todos os divisores do numero inserido

n_utilizador = int(input("Introduza um numero: "))
divisor = n_utilizador

while divisor > 0:
    if n_utilizador % divisor == 0:
        print (divisor) 

    divisor = divisor - 1