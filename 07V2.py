#Este algoritmo determina se o Joaquim consegue se registar
email = input("Introduza o seu email")
palavra_passe = input ("Introduza a sua palavra passe")
palavra_passe2 = input ("Introduza novamente a sua palavra passe")


if palavra_passe == palavra_passe2:
    print ("Sucesso! Está registado")
else:
    print ("As a primeira palavra passe nao corresponde com a segunda")