#Este algoritmo pede dois nomes ao utilizador e diz qual é o maior
nome1 = input ("Introduza o 1º nome: ")
nome2 = input ("Introduza o 2º nome: ")

letras1 = len(nome1)
letras2 = len(nome2)

if letras1 > letras2:
    print (f"O maior nome é: {nome1}")

elif letras2 > letras1:
    print (f"O maior nome é: {nome2}")

else: 
    print (f"Ambos os nomes têm o mesmo tamanho, {letras1} letras.")

