#Este programa verifica a classe pertencente a um jogador

Idade = int(input("Introduza a Idade: "))

if Idade > 0 and Idade < 10:
    Classe = "Infantis"
    
elif Idade >= 10 and Idade < 14:
    Classe = "Iniciados"

elif Idade >= 14 and Idade < 18:
    Classe = "Juniores"

elif Idade >= 18 and Idade < 151:
    Classe = "Seniores"

else:
    Classe = "Provavelmente so vai jogar na proxima vida"

print (Classe)