#Este programa lê 20 números do utilizador e faz a média dos números que estão apenas entre 20 e 50

soma = 0
contador = 0

for X in range (3):
    numero_u = int(input("Introduza um número: "))
    if numero_u >= 20 and numero_u <= 50:
        soma = soma + numero_u
        contador = contador + 1
        media = soma // contador

print (f"A média de todos os números inseridos entre 20 e 50 é: {media}")