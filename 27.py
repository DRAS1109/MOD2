#Este programa le varios numeros do utilizador e diz se e negativo ou positivo e se é impar e par, o ciclo acaba quando o utilzador digitar 0

n_utilizador = 1

while n_utilizador != 0:
    n_utilizador = int(input("Introduza um numero: "))

    if n_utilizador > 0:
        if n_utilizador % 2 == 0:
            print (f"{n_utilizador} é positivo e par")

        else:
            print (f"{n_utilizador} é positivo e impar")
    
    if n_utilizador < 0:
        if n_utilizador % 2 == 0:
            print (f"{n_utilizador} é negativo e par")

        else:
            print (f"{n_utilizador} é negativo e impar")