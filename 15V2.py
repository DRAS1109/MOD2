#Este algoritmo lê as notas de 10 alunos e calcula a média

alunos = 10
soma = 0
P = 0

for vz in range (1, alunos + 1):
    nota = int(input(f"Introduza a nota do {vz}º aluno: "))
    soma = soma + nota

    if nota >= 10:
        P = P + 1

media = soma / alunos 
N = alunos - P

print (round (media, 2))
print (f"Em {alunos} alunos, {P} tiveram positiva e {N} tiveram negativa.")