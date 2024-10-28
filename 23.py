#Este programa verifica se uma palavra é um palindrome (O mesmo de tras para a frente)

palavra = input("Introduza uma palavra toda em maiusculas ou toda em minusculas: ")

palavra_inversa = ""

for i in range (len (palavra)-1,-1,-1):
    palavra_inversa = palavra_inversa + palavra [i]

if palavra == palavra_inversa:
    print (f'A palavra "{palavra}" é um palindrome')

else:
    print (f'A palavra "{palavra}" não é um palindrome')
