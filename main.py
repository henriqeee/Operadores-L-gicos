#Verificando login e senha do usuário.

usuario = input("Nome de usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")