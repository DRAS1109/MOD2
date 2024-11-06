#Todos os exercicios nomeados de 43 pertencem ao Desafio 0
#Um programa que le as notas dos alunos de uma turma e diz qual o alunos com a melhor nota

Melhor_Nota = -1
Melhor_Aluno = 0

NºAlunos = int(input("Introduza o Nº de alunos: "))

for i in range (1, NºAlunos + 1):
    Nota = int(input(f"Introduza a nota do {i}º aluno: "))
    if Nota > Melhor_Nota:
        Melhor_Nota = Nota
        Melhor_Aluno = i

print (f"O melhor aluno é o Nº {Melhor_Aluno}")