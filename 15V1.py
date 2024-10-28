#Este algoritmo lê as notas de 10 alunos e calcula a média

soma = 0

for vz in range (1, 11):
    nota = int(input(f"Introduza a nota do {vz}º aluno: "))
    soma = soma + nota

media = soma / 10 

print (round (media, 2))