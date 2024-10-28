#Este algoritmo determina se o numeros introduzido pelo utilizados é par ou impar
N1 = int(input("Introduza um numero inteiro: "))
Resto = N1 % 2

if Resto == 0:
    print ("É par")
else:
    print ("É impar")