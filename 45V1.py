#Numero perfeito, é perfeito se a soma de todos os divisores positivos derem o proprio nº

Soma = 0

N = int(input("Introduza um numero: "))

for i in range (1, N):
    if N % i == 0:
        Soma = Soma + i

if Soma == N:
    print(f"{N} é um numero perfeito")
else:
    print(f"{N} não é um numero perfeito")