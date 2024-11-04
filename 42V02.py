#Todos os exercicios nomeados de 42 pertencem ao ficheiro: PSI-M02-Desafio 02-Repetição.pdf
#Este programa calcula a expoente de um numero inserido pelo utilizador

Resultado = 1

Base = int(input("Introduza o numero correspondente à base: "))
Expoente = int(input("Introduza o numero correspondente ao expoente: "))

for i in range (Expoente):
    Resultado = Resultado * Base

print (f"{Base} elevado a {Expoente} = {Resultado}")