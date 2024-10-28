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

while numero_utilizador > numero_secreto or numero_utilizador < numero_secreto or numero_utilizador == numero_secreto:
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

# vz = Quantas vezes o while repetiu
print (f"Precisou de {contador} tentativas para acertar o Número Secreto")