idade = int(input ("Introduza a sua idade: ")) 

if idade < 0 or idade > 120:
    print ("Idade inválida")

elif idade <= 11:
    print ("Está na idade da infância")

elif idade >= 12 and idade <= 20:
    print ("Está na idade da adolscência")

elif idade >= 21 and idade <= 75:
    print ("Está na idade adulta")
    
else:
    print ("Está na idade da velhice")