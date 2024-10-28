#Este algoritmo calcula o preço que cada um dos 3 amigos tem a pagar pelo nº de fatias que consumiu
f1 = int(input ("Introduza o nº de fatias que o 1º amigo comeu: "))
f2 = int(input ("Introduza o nº de fatias que o 2º amigo comeu: "))
f3 = int(input ("Introduza o nº de fatias que o 3º amigo comeu: "))
Preco = int(input ("Introduza o preço da pizza: "))

N_Fatias = f1 + f2 + f3
Preco_por_Fatia = Preco / N_Fatias

print (f" Cada fatia custa: {(Preco_por_Fatia):.2f} €")
print (f" O 1º amigo terá de pagar: {(Preco_por_Fatia * f1):.2f} €")
print (f" O 2º amigo terá de pagar: {(Preco_por_Fatia * f2):.2f} €")
print (f" O 3º amigo terá de pagar: {(Preco_por_Fatia * f3):.2f} €")