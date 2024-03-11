#Calculando o Fatorial de um número com Laços de Repetição

#Entrada
numero = int(input('Digite um número para ser calculado o seu fatorial: '))

#Inicializando resultado
factorial = 1

#Loop para calcular
for i in range(1, numero + 1) :
    factorial *= i 

#Mostra o resultado
print('O Fatorial de ', numero, "é", factorial)
