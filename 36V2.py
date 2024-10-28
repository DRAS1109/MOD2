#Este programa le x letras do utilizador e no final indicar quantas vogais o utilizador introduziu

vz = 10
Vogais = "aeiou"
Contador_Vogais = 0

for i in range (vz):
    Letra = (input("Introduza uma letra: "))
    Letra = Letra.lower().strip()
    while len(Letra) != 1:
        print("Só pode inserir uma letra")
        Letra = (input("Introduza uma letra: "))

    if Letra in Vogais:
        Contador_Vogais = Contador_Vogais + 1

print(f"Introduziu {Contador_Vogais} vogais.")