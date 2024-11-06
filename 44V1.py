#Um programa para testar credenciais
"""
Le o email e password
Se estiverem incorretos -> login falhou
Se falhou 3 vezes cancelar
"""

Email = "a9999@esenviseu.net"
Password = "9999CV*2024"
Tentativas = 1

while Tentativas > 0:
    EmailTentativa = input("Introduza o email: ")
    EmailTentativa = EmailTentativa.strip()
    PasswordTentativa = input("Introduza a password: ")
    PasswordTentativa = PasswordTentativa.strip()

    if EmailTentativa != Email or PasswordTentativa != Password:
        Tentativas = Tentativas + 1
        print("Login falhou, tente denovo")

    else:
        print("Sucesso, login comfirmado")
        break
    
    if Tentativas == 4:
        print("Esgotou 3 tentativas de login, tente mais tarde")
        break