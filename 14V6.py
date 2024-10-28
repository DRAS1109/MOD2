#Este programa vai utilizar um ciclo para calcular a soma de todos os nº a começar pelo primeiro inserido até ao segundo inserido

soma = 0
vz = 3

numero_1 = int(input("Introduza o 1º nº: "))
numero_2 = int(input("Introduza o 2º nº: "))

if numero_1 > numero_2:

    for _ in range (1, vz):
        S_ou_N = str(input("Os valores não são válidos, o 1º deve ser inferior ao 2º, deseja inverter os números? Sim ou Nao? "))
        if S_ou_N in "Ss":
            numero_1_copia = numero_1
            numero_1 = numero_2 
            numero_2 = numero_1_copia
            break

        elif S_ou_N in "nN":
            numero_1 = int(input("Introduza o 1º nº: "))
            numero_2 = int(input("Introduza o 2º nº: "))
            if numero_1 < numero_2:
                break

        elif S_ou_N not in "nNsS":
            print (f"A palavra que introduziu ({S_ou_N}) não é valida")

        else: 
            break

for i in range (numero_1, numero_2 + 1):
    soma = soma + i
        
print(soma)