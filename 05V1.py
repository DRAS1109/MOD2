#Este algoritmo diz qual dos 2 numeros inseridos pelo utilizador é o maior
V1= int(input ("Introduza o 1º numero: "))
V2= int(input ("Introduza o 2º numero: "))

if V1 > V2:
        print (f"O maior numero é o: {V1}" )
else:
    if V2 > V1:
        print (f"O maior numero é o: {V2}" )
    else:
        print ("Ambos os numeros são iguas")