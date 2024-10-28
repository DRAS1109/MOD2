#Este algoritmo conta o nº de vogais de uma frase inserida pelo utilizador
Frase = str(input ("Introduza uma frase: "))
contador = 1
for letra in Frase:
    if letra in "aeiouAEIOU":
        contador = contador +1
    
print (f"A frase indicada tem {contador} vogais")