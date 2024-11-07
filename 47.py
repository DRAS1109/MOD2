#Triangulos

A = float(input("Introduza a medida de um lado: "))
B = float(input("Introduza a medida de outro lado: "))
C = float(input("Introduza a medida de outro lado: "))

#Validação
if A > 0 and B > 0 and C > 0:
    if (A + B) > C or (B + C) > A or (C + A) > B:

        #Tipo de Triagulo:
        if A == B == C:
            print ("É um triangulo equilatero")

        elif A != B != C:
            print ("É um triangulo escaleno")

        else:
            print ("É um triangulo isosceles")

    else:
        print ("Os valores são invalidos")

else:
    print ("Um triangulo não tem lados negativos")