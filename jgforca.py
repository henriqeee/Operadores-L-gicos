import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "openai", "inteligencia"]
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6  # Pode ajustar o número de tentativas conforme necessário

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_palavra_oculta(palavra_secreta, letras_corretas))

    while tentativas > 0:
        letra_usuario = input("Digite uma letra: ").lower()

        if letra_usuario in letras_corretas:
            print("Você já tentou esta letra. Tente outra.")
        elif letra_usuario in palavra_secreta:
            letras_corretas.append(letra_usuario)
            print("Letra correta!")
        else:
            tentativas -= 1
            print("Letra incorreta. Tentativas restantes:", tentativas)

        print(exibir_palavra_oculta(palavra_secreta, letras_corretas))

        if set(letras_corretas) == set(palavra_secreta):
            print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
            break

    if tentativas == 0:
        print("Você esgotou suas tentativas. A palavra correta era:", palavra_secreta)

if __name__ == "__main__":
    jogo_da_forca()
