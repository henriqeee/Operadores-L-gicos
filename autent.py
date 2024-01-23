import random

# Credenciais básicas
usuario_cadastrado = "usuario123"
senha_cadastrada = "senha123"

# Geração de código de autenticação de dois fatores
codigo_autenticacao = random.randint(1000, 9999)

# Simulação de entrada do usuário
usuario_digitado = input("Digite o nome de usuário: ")
senha_digitada = input("Digite a senha: ")

# Verificação das credenciais básicas
if usuario_digitado == usuario_cadastrado and senha_digitada == senha_cadastrada:
    # Credenciais básicas corretas, agora pedir o código de autenticação de dois fatores
    codigo_digitado = int(input("Digite o código de autenticação de dois fatores enviado para o seu dispositivo: "))

    # Verificar o código de autenticação de dois fatores
    if codigo_digitado == codigo_autenticacao:
        print("Autenticação bem-sucedida! Bem-vindo, {}.".format(usuario_cadastrado))
    else:
        print("Código de autenticação incorreto. Autenticação falhou.")
else:
    print("Credenciais básicas incorretas. Autenticação falhou.")
