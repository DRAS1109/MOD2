#Todos os exercicios nomeados de 42 pertencem ao ficheiro: PSI-M02-Desafio 02-Repetição.pdf
# Eleições para 3 Listas da Escola

ListaA = 0
ListaB = 0
ListaC = 0
Voto = "D"

while Voto != "O":

    Voto = input("Introduza a letra correspondente à lista: ")
    Voto = Voto.capitalize().strip()

    if Voto in ("A"):
        ListaA = ListaA + 1

    elif Voto in ("B"):
        ListaB = ListaB + 1
    
    elif Voto in ("C"):
        ListaC = ListaC + 1

print (f"Lista A: {ListaA}, Lista B: {ListaB}, Lista C: {ListaC}")