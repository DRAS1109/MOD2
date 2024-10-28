#Este algoritmo indica quando acabar o dinheiro ou quando nao puder carregar com esse peso

orçamento_i = float (input ("Introduza o orçamento inicial: "))
peso_i = float (input ("Introduza o peso maximo que pode carregar (Em Kg): "))

orçamento = 1
peso = 1


while orçamento > 0 and peso > 0:

    orçamento = float (input ("Introduza o preço do novo produto: "))
    orçamento = orçamento_i - orçamento
    orçamento_i = orçamento

    if orçamento <= 0:
        print ("Não sobra mais dinheiro")
        break

    peso = float (input ("Introduza o peso do novo produto (Em Kg): "))
    peso = peso_i - peso
    peso_i = peso

    if peso <= 0:
        print ("O produto é muito pesado")
        break

    else: 
        print(f"Ainda tem {orçamento} € e pode carregar mais {peso} Kg")
