#Este algoritmo calcula a media e diz se é positiva ou negativa (>=10)
N1= int(input ("Introduza a 1º nota: "))
N2= int(input ("Introduza a 2º nota: "))
N3= int(input ("Introduza o 3º nota: "))

Media = (N1 + N2 + N3) / 3
print (f"Média: {Media}")

if Media >= 10:
    print ("É positiva")
else:
    print ("É negativa")