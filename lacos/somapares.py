#Somando os números Pares de 1 a 100 utilizando laços de repetição

soma = 0

for numero  in range(1, 101):
    if numero %2  ==0:
        soma += numero

print('A soma dos números de 1 a 100 é :', soma)

