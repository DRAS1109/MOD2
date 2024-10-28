#Este algoritmo calcula o desconto dependendo da quantidade de produtos
N_Produtos = int(input ("Introduza o numero de produtos: "))
Preco = N_Produtos * 1000
if N_Produtos < 500:
    print (f"Terá de pagar: {Preco}")

elif N_Produtos >= 500 and N_Produtos < 1000:
                Preco_F = (Preco) - (Preco * 0.05)
                print (f"Terá de pagar: {Preco_F}")

else:
        Preco_F = (Preco) - (Preco * 0.08)
        print (f"Terá de pagar: {Preco_F}")
    