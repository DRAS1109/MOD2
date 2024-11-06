#Todos os exercicios nomeados de 43 pertencem ao Desafio 0
#Um programa que le uma hora e indica a parte do dia

Hora = int(input("Introduza uma hora: "))

if Hora >= 0 and Hora <= 24:
    if Hora >= 5 and Hora <= 7:
        print ("Madrugada")

    elif Hora >= 8 and Hora <= 12:
        print ("Manha")

    elif Hora >= 13 and Hora <= 19:
        print ("Tarde")

    else:
        print ("Noite")