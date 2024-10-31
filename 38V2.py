#Este programa vai utilizar um ciclo para calcular a soma de todos os nº a partir do que o utilizador inseriu

numero = float(input("Introduza o nº: "))
numero = numero + 0.5

soma = 0
mensagem = ""

for i in range (10):
    if i < 9:
        mensagem = mensagem + str(numero) + ","
    else:
        mensagem = mensagem + str(numero)
    soma = soma + numero
    numero = numero + 0.5
    
    
print(mensagem, "=", soma)