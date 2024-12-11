"""calculadora com while"""

while True:
    numero_1 = input('digite um numero')
    numero_2 = input('digite outro numero')
    operador = ('digite o operador:(+-*/)')
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
        
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = None

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('um ou ambos os numeros digitados sao invalidos')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        Print('digite apenas um operador')
        continue

    print('realizando sua conta. cofira o rsultado abaixo:')
    if operador == '+':
        print(num_1_float + num_2_float)

    elif operador == '-':
        print(num_1_float - num_2_float)


    elif operador == '*':
        print(num_1_float * num_2_float)
        

    elif operador == '/':
        print(num_1_float / num_2_float)



    sair = input('quer sair?[s]sim').lower().startswith('s')
    print(sair)
    if sair is true:
        break