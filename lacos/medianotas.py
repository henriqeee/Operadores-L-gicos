#Calculando a Média das Notas com Laços de Repetição

#Entrada das notas
notas_str = input("Digite as notas separadas por espaço: ")

# Converter a string de notas em uma lista de floats
notas = [float(nota) for nota in notas_str.split()]

# Calcular a média das notas
media = sum(notas) / len(notas)

# Impressão do resultado
print("A média das notas é:", media)