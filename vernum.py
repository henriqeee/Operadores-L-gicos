#verificando se o número é Positivo, Negativo ou zero.

def verificacao():
    
    num = int(input('Informe seu número: '))
    if num == 0:
        print('O número é Zero!')
    
    elif num > 0:
        print('O número é Positivo!')

    else:
        print('O número é Negativo!')

    
verificacao()