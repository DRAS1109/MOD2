#Criar palavra passe segura
"""
Tem de ter pelo menos um:
-letra maiuscula e minuscula
-numero
-8 caracteres
-caracteres especiais
"""
import random
Palavra_Passe = ""

Numeros = ("1234567890")
Caracteres_Especiais = ("!#$%&/()=?@£§€{[]}'«»´`~^ºª-_.:,;<>\\|")
alfabeto = ("abcdefghijklmnopqrstuvwxyz")

N_Caracteres = random.randint (8, 20)

for _ in range (0, N_Caracteres):
    Ação = random.randint (1, 4)

    if Ação == 1:
        N = random.randint (0, 9)
        Palavra_Passe = Palavra_Passe + str(N)

    if Ação == 2:
        L = random.randint (0, len(alfabeto.upper()))
        Palavra_Passe = Palavra_Passe + alfabeto.upper()[L]

    if Ação == 3:
        l = random.randint (0, len(alfabeto))
        Palavra_Passe = Palavra_Passe + alfabeto[l]
    
    if Ação == 4:
        C = random.randint (0, len(Caracteres_Especiais))
        Palavra_Passe = Palavra_Passe + Caracteres_Especiais[C]

print (f"Uma dica de palavra passe é: {Palavra_Passe}")