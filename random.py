import random

numero_secreto = random.randint(1, 100)

tentativa = int(input("Adivinhe o número entre 1 e 100: "))

while tentativa != numero_secreto:
    if tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
    
    tentativa = int(input("Tente novamente: "))

print("Parabéns! Você acertou o número secreto.")
