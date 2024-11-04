#Todos os exercicios nomeados de 42 pertencem ao ficheiro: PSI-M02-Desafio 02-Repetição.pdf
#Este exercicio calcula a temperatura minima, maxima e a amplitude termica das 9 as 17

TempM = -99
Tempm = 99

for i in range (9, 18): #18 porque o ciclo nao alcança o ultimo numero
    Temp = int(input(f"Introduza a temperatura ambiente as {i} horas: "))

    if Temp > TempM:
        TempM = Temp

    elif Temp < Tempm:
        Tempm = Temp

AmTer = TempM - Tempm
print (f"Temperatura Mínima: {Tempm}, Temperatura Maxima: {TempM}, Amplitude Termica: {AmTer}")