#Este algoritmo determina se o Joaquim tem acesso autorizado
email = input("Introduza o seu email")
palavra_passe = input ("Introduza a sua palavra passe")

if email == "joaquim@gmail.com" and palavra_passe == "12345":
    print ("Acesso autorizado")
else:
    print ("Erro. Credenciais invalidas.")