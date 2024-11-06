#Todos os exercicios nomeados de 43 pertencem ao Desafio 0
#Um programa para ler 2 nº e indicar se sao iguais ou diferentes

N1 = int(input("Nº: "))
N2 = int(input("Nº: "))

if N1 == N2:
    print ("Iguais")
else:
    print("Diferentes")

diferença = N1 - N2
if diferença < 0:
    diferença = diferença * -1

print (diferença)