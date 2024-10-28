#Este algoritmo diz qual dos 3 numeros inseridos pelo utilizador é o maior
V1= int(input ("Introduza o 1º numero: "))
V2= int(input ("Introduza o 2º numero: "))
V3= int(input ("Introduza o 3º numero: "))


if V1 > V2 and V1 > V3:
    print (f"O maior numero é o: {V1}, o primeiro numero inserido" )
if V1 == V2 and V1 > V3:
    print (f"O 1º e o 2º numero inserido: ({V1}) são maiores do que o 3º numero inserido ({V3})")
if V1 == V3 and V1 > V2:
    print (f"O 1º e o 3º numero inserido: ({V1}) são maiores do que o 2º numero inserido ({V2})")
        
if V2 > V1 and V2 > V3:
    print (f"O maior numero é o: {V2}, o primeiro numero inserido" )
#if V2 == V1 and V2 > V3:
    #print (f"O 1º e o 2º numero inserido: ({V2}) são maiores do que o 3º numero inserido ({V3})")
#if V2 == V3 and V2 > V1:
    #print (f"O 2º e o 3º numero inserido: ({V2}) são maiores do que 2º numero inserido ({V1})")

if V3 > V1 and V3 > V2:
    print (f"O maior numero é o: {V3}, o 3º numero inserido" )
if V3 == V1 and V3 > V2:
    print (f"O 1º e o 3º numero inserido: ({V3}) são maiores do que o 2º numero inserido ({V2})")
if V3 == V2 and V3 > V1:
    print (f"O 2º e o 3º numero inserido: ({V3}) são maiores do que o 1º numero inserido ({V1})")

if V1 == V2 == V3:
    print (f"O 1º, o 2º e o 3º numero inserido ({V1}) são iguais")