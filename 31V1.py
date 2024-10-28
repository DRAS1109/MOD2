#Este programa diz qual é a duração de um album de musicas

segundos = 0

vz = int(input("Quantas musicas deseja inserir? "))

for i in range (vz):
    musica = int(input(f"Introduza a duração da {i + 1}º musica (Em segundos): "))
    while musica <= 0 or musica >= 6000:
        print ("Dados inválidos, a musica tem de ter mais de 0 segundos e menos de 100 min")
        musica = int(input(f"Introduza a duração da {i + 1}º musica (Em segundos): "))
    
    segundos = segundos + musica
      
minutos = segundos // 60
segundos = segundos % 60

print (f"O seu album tem: {minutos}:{segundos} min.")

"""
minutos = 0
while segundos > 60:
    segundos = segundos - 60 
    minutos = minutos + 1
"""
