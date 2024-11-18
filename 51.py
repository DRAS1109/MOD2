"""
Um produto de um supermercado está em promoção.
As primeiras 10 unidades custam 10€ cada
Se comprar mais de 10 tem direito a um desconto de 5%, este desconto só aplicado ao número de unidades para além das 10 iniciais
Se comprar mais de 20 tem direito a um desconto de 10% nas unidades que excedem as 20 iniciais
Faça um programa que pergunte quantas unidades o cliente comprou e calcule o preço total a pagar
"""

N_Unidades = int(input("Introduza o Nº de unidades compradas: "))
Preço = 10

if N_Unidades <= 10:
    Preço_Total = N_Unidades * Preço
    print (f"o preço total a pagar é de {Preço_Total}€")

elif N_Unidades > 10:
    Desconto = 0.05
    Preço_Total = (10 * Preço) + ((N_Unidades - 10) * (Preço - (Preço * Desconto)))
    Valor_descontado = ((N_Unidades - 10) * Preço) - (Preço_Total - (10 * Preço))

    if N_Unidades > 20:
        Desconto = 0.10
        Preço_Total = (20 * Preço) + ((N_Unidades - 20) * (Preço - (Preço * Desconto)))
        Valor_descontado = ((N_Unidades - 20) * Preço) - (Preço_Total - (20 * Preço))
    
    print (f"O preço total a pagar é de {Preço_Total}€ e economizou {Valor_descontado}€")
    
else:
    print ("O Nº de unidades nao pode ser negativo")