idade = int(input ("Introduza a sua idade: ")) 

if idade >= 0 and idade <= 11:
    print ("Está na idade da infância")

if idade >= 12 and idade <= 20:
    print ("Está na idade da adolscência")

if idade >= 21 and idade <= 75:
    print ("Está na idade adulta")

if idade >= 76 and idade <= 120:
    print ("Está na idade da velhice")

if idade < 0 or idade > 120:
    print ("Idade inválida")