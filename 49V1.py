#Palavra passe segura
"""
Tem de ter pelo menos um:
-letra maiuscula e minuscula
-numero
-8 caracteres
-caracteres especiais
"""

Palavra_passe = input("Introduza uma palavra passe: ")

Numeros = ("1234567890")
Caracteres_Especiais = ("!#$%&/()=?@£§€{[]}'«»´`~^ºª-_.:,;<>\\|")
alfabeto = ("abcdefghijklmnopqrstuvwxyz")
Tem_Maiusculas = False
Tem_minusculas = False
Tem_Simbolos = False
Tem_Numeros = False

for letra in alfabeto:
    if letra in Palavra_passe: 
        Tem_minusculas = True

for LETRA in alfabeto.upper():
    if LETRA in Palavra_passe: 
        Tem_Maiusculas = True
        
for Caracter in Caracteres_Especiais:
    if Caracter in Palavra_passe:
        Tem_Simbolos = True

for Numero in Numeros:
    if Numero in Palavra_passe:
        Tem_Numeros = True

if Tem_Maiusculas == True and Tem_minusculas == True and Tem_Simbolos == True and Tem_Numeros == True and len(Palavra_passe) >= 8:
    print ("A palavra passe é segura")

else:
    print ("A palavra passe não é segura")

    if Tem_Maiusculas == False:
        print ("Não tem maiusculas")
    
    if Tem_minusculas == False:
        print ("Não tem minusculas")

    if Tem_Numeros == False:
        print ("Não tem numeros")
    
    if Tem_Simbolos == False:
        print ("Não tem caracteres especiais")
    
    if len(Palavra_passe) < 8:
        print ("Tem menos de 8 caracteres")