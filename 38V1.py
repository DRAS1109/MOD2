#Este programa vai utilizar um ciclo para calcular a soma de todos os nº a partir do que o utilizador inseriu

numero = float(input("Introduza o nº: "))
numero = numero + 0.5

soma = 0

for i in range (10):
    if i < 9:
        print (numero, end= " + " )
    else:
        print (numero, end= "" )
    soma = soma + numero
    numero = numero + 0.5
    
    
print(f" = {soma}")