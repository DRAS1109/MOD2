#Todos os exercicios nomeados de 42 pertencem ao ficheiro: PSI-M02-Desafio 02-Repetição.pdf

numero = int(input("Insira um número inteiro: "))
numero_inicial = numero
paridade = 0

while numero > 0:
    paridade = paridade + numero % 2
    numero = numero // 2

print(f"A paridade de {numero_inicial} é {paridade}")