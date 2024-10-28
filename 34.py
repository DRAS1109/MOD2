#Este código le uma frase ao utilizador e mostra uma letra por linha

frase = input("Introduza uma palavra: ")

for i in range (len (frase)-1,-1,-1):
    print(frase [i])
