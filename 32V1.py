#Exercicio Nº 50 !!!!!!!!
#Calculadora Avançada

N1 = float(input("Introduza o primeiro numero: "))
N2 = float(input("Introduza o segundo numero: "))
Op = input("Qual operação deseja efetuar? (+, -, /, *) ")

if Op == "+":
    Conta = N1 + N2

elif Op == "-":
    Conta = N1 - N2

elif Op == "/":
    Conta = N1 / N2

elif Op == "*":
    Conta = N1 * N2

else:
    print ("Operação inválida")

print (f" {N1} {Op} {N2} = {Conta}")