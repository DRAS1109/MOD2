#Todos os exercicios nomeados de 42 pertencem ao ficheiro: PSI-M02-Desafio 02-Repetição.pdf
#Este programa é para um kartodromo, ele le o tempo de passagem na meta e no fim de 5 voltas mostra na box o tempo total

SegundosT = 0

for i in range (5):
    #Minutos = int(input(f"Introduza os minutos de passagem na {i}ª volta: "))
    Segundos = int(input(f"Introduza os segundos de passagem na {i + 1}ª volta: "))
    print ("") #Para dar um espaço

    SegundosT = SegundosT + Segundos

MinutosT = SegundosT // 60

if MinutosT > 0:
    SegundosT = SegundosT % (MinutosT * 60)

print (f"Demorou {MinutosT} minutos e {SegundosT} segundos")