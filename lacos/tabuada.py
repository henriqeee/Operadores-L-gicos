#Calculando Tabuada utilizando Laços de Repetição

#Entrada
numero = int(input('Digite o número para ser calculado a Tabuada: '))

#Executa o loop
for multiplicador in range(0, 11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)

