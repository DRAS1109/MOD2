#aleatorio
import random

numero_secreto = random.randint(1,10)

numero_utilizador = int(input ("Introduza um numero de 1 a 10: "))

if numero_utilizador == numero_secreto:
    print (f"O numero {numero_utilizador} está correto!")

else: 
    if numero_utilizador > numero_secreto:
        print (f"O número secreto é menor que {numero_utilizador}, tente denovo :)")
    else:
        print (f"O número secreto é maior que {numero_utilizador}, tente denovo :)")


    
    numero_utilizador = int(input ("Introduza um numero de 1 a 10: "))

    if numero_utilizador == numero_secreto:
        print (f"O numero {numero_utilizador} está correto!")

    else: 
        if numero_utilizador > numero_secreto:
            print (f"O número secreto é menor que {numero_utilizador}, tente denovo :)")
        else:
            print (f"O número secreto é maior que {numero_utilizador}, tente denovo :)")


        numero_utilizador = int(input ("Introduza um numero de 1 a 10: "))

        if numero_utilizador == numero_secreto:
            print (f"O numero {numero_utilizador} está correto!")

        else:
            print (f"O numero secreto é {numero_secreto}")