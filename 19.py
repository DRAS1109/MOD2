#Este algoritmo verifica se um número é primo

numero = int(input ("Introduza um número: "))

Primo = True

for D in range (2, numero):
    if numero % D == 0:
        Primo = False
        
if Primo == True:
    print (f"O número introduzido ({numero}) é primo")

else:
    print (f"O número introduzido ({numero}) não é primo")
