#Este algoritmo diz qual dos 10 numeros inseridos pelo utilizador é o maior

vz = int(input ("Quantos numeros pretende comparar? "))

n_maior = int(input (f"Introduza o 1º numero: "))
pos_maior = 1


for i in range(2, vz + 1):
    n_utilizador = int(input (f"Introduza o {i}º numero: "))
    if n_utilizador > n_maior:
        n_maior = n_utilizador
        if i == 1:
            pos_maior = "primeiro"
        elif i == vz:
            pos_maior = "ultimo"
        else:
            pos_maior = i

print (f"{n_maior} é o maior numero e foi o {pos_maior}º nº inserido")