"""
#Numero perfeito, é perfeito se a soma de todos os divisores positivos derem o proprio nº

Contador = 0

N = int(input("Introduza o limite maximo: "))
while Contador != N:
    Soma = 0
    for i in range (1, Contador):
        if Contador % i == 0:
            Soma = Soma + i
    Contador = Contador + 1

    if Soma == Contador:
        print(f"{Contador} é um numero perfeito")

NÃO ESTA A FUNCIONAR

"""
#Numero perfeito, é perfeito se a soma de todos os divisores positivos derem o proprio nº

N = int(input("Introduza o limite maximo: "))
for k in range (1, N + 1):
    Soma = 0
    for i in range (1, k):
        if k % i == 0:
            Soma = Soma + i

    if Soma == k:
        print(f"{k} é um numero perfeito")