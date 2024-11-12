Escola: Emideo Navarro
Nome: Dinis Sousa
Nº e Turma: Nº3 10ºT
Curso: GPSI
Módulo: 2





# Aleatorio
#Importar Biblioteca Random
import random

#Criar Nº Secreto
x = 1
y = 100
numero_secreto = random.randint(x, y)
print (numero_secreto)
N_R = random.randint(1, 99)
print (N_R)





# Arredondamentos
import math #importar a biblioteca de funções math

X = 11.5

print(int(X)) #Converte para o numero inteiro sem arredondar
print(round(X)) #Arredonda para o número par mais proximo

print(math.ceil(X)) # arredonda sempre para o inteiro seguinte (para cima)
print(math.floor(X)) # arredonda sempre para o inteiro anterior (para baixo)

#Arredondar para cima se a parte decimal >= 0.5
parte_decimal = X - (int(X))
if parte_decimal >= 0.5:
    X = int(X) + 1
else:
    X = int(X)
print(X)





# Strings
nome = "          ola mundo"
marca = 'ford'
varias_linhas = """
com varias linhas 
"""

#tamanho da string
print(len(nome))

#converter para maiusculas
print(marca.upper)
print(marca)
marca = marca.upper()
print(marca)

#converter para minusculas
print(marca.lower)
print(marca)

#colocar a primeira letra em maiuscula
marca = marca.capitalize()
print(marca)

#remove os espaços em branco no inicio e no final
print(nome.strip())





# Range
range (5) = (0, 1, 2, 3, 4)
range (1, 5) = (1, 2, 3, 4)
range (5, 1) = (5, 4, 3, 2)
range (1, 10, 2) = (1, 3, 5, 7, 9)
range (10, 1, 2) = (10, 8, 6, 4, 2)





# Match
dia = (int(input("Insira um número inteiro de 1 a 7: ")))
match dia:
    case 1:
        print ("É segunda-feira")
    case 2:
        print ("É terça-feira")
    case 3:
        print ("É quarta-feira")
    case 4:
        print ("É quinta-feira")
    case 5:
        print ("É sexta-feira")
    case 6:
        print ("É sábado")
    case 7:
        print ("É domingo")
    case _:
        print ("O valor indicado não é valido")