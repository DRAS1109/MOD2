vz = int(input("Introduza o nº de linhas / colunas do seu tabuleiro: "))

for i in range (vz):
    if i % 2 == 0:
        print("⬜⬛" * 4)
    else:
        print("⬛⬜" * 4)



#Quadrado Preto: https://www.emojiall.com/pt/emoji/%E2%AC%9B
#Quadrado branco: https://www.emojiall.com/pt/emoji/%E2%AC%9C