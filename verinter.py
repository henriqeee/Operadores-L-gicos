#Faça um programa que verifique se um número está dentro de um intervalo específico (por exemplo, entre 10 e 50).

def verifica(numero):
    inicio = 0
    fim = 100

    if inicio <= numero <= fim:
        print(f'O número {numero} está dentro do intervalo')

    else:
        print(f'O número {numero} não está dentro do intervalo')
    
num_usu = float(input('Informe o número para realizar a verificação: '))

verifica(num_usu)