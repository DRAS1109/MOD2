#Este programa diz qual é a duração de um album de musicas
segundos = 0
contador = 0

musica = int(input("Introduza a duração da 1º musica (Em segundos): "))

while musica != 0:
    contador = contador + 1
    musica = int(input(f"Introduza a duração da {contador + 1}º musica (Em segundos): "))
    if musica >= 6000:
        print ("Dados inválidos, a musica tem de ter menos de 100 min")
        musica = int(input(f"Introduza a duração da {contador + 1}º musica (Em segundos): "))

    
    segundos = segundos + musica
      
minutos = segundos // 60
segundos = segundos % 60
print (f"O seu album tem: {minutos}:{segundos} min.")