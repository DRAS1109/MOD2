#Sequencia de Collatz, se o numero for par, divide por 2, se for impar, dmultiplica por 3 e soma 1, e faz o mesmo ao numero seguinte

Contar = 0

N = int(input("Introduza um numero: "))

while N != 1:
    if N % 2 == 0:
        N = int(N / 2)
    else:
        N = int((N * 3) + 1)

    print(N)

    Contar = Contar + 1

print(f"Foram necessarios {Contar} passos. ")