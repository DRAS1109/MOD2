#Jogo Nº Secreto Ciclo
#Importar Biblioteca Random
import random

#Criar Nº Secreto
numero_secreto = random.randint(1,10)

#Pedir ao Utilizador um Nº
numero_utilizador = int(input ("Introduza um numero de 1 a 10: "))

#Contador de Ciclos
contador = 1

#Dizer se o número está correto
if numero_utilizador == numero_secreto:
    print (f"O numero {numero_utilizador} está correto!")

for _ in range (1, 100):
    if numero_utilizador == numero_secreto:
        print (f"O numero {numero_utilizador} está correto!")
        break

    elif numero_utilizador > numero_secreto:
        print (f"O número secreto é menor que {numero_utilizador}, tente denovo :)")
        numero_utilizador = int(input ("Introduza um numero de 1 a 10: "))

    elif numero_utilizador < numero_secreto:
        print (f"O número secreto é maior que {numero_utilizador}, tente denovo :)")
        numero_utilizador = int(input ("Introduza um numero de 1 a 10: "))

    contador = contador + 1
#    if contador == 15:
#        print ("Ecedeu o número limite de tentativas. Seu Noooooob")

print (f"Precisou de {contador} tentativas para acertar o Número Secreto")