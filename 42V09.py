#Todos os exercicios nomeados de 42 pertencem ao ficheiro: PSI-M02-Desafio 02-Repetição.pdf

Capital_Inicial = float(input("Introduza o deposito inicial: "))
Capital_Acumulado = Capital_Inicial
N_Anos = int(input("Introduza o nº de anos de capitalização: "))
#N_Capitalizaçoes_Anuais = float(input("Introduza o nº de capitalizações anuais \nPor exemplo: Semestrais = 2 \n"))
Taxa = float(input("Introduza a taxa de juro: "))

for i in range (N_Anos):
    Capital_Acumulado = Capital_Acumulado * (1 + (Taxa / 100 ))

    print(f"{i}º Ano: {Capital_Acumulado}") 

print (f"Juros ganhos: {round(Capital_Acumulado - Capital_Inicial, 2)}")