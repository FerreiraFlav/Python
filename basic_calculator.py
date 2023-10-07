



# sourcery skip: remove-unnecessary-cast
while True:
    print('\nCALCULADORA BASICA')    
    
    numero1 = input('Digite primeiro numero: ')
    numero2 = input('Digite o segundo numero: ')
    operador = input('Digite [ + - * / ]  ')
    numero_valido = True
    numero1 = float(numero1)
    numero2 = float(numero2)

    try:
        numero_valido = True
    except:
        numero_valido = None


    if  numero_valido is None:
        print('Ambos os numero digitados são invalidos.\n')
        continue

    operadores_permitidos = ' + - * /'
    if operador not in operadores_permitidos:
        print('operador invalido.\n')
        
    if len(operador) > 1:
        print('Digite apenas um operador.\n')
       
    elif operador =='+':
        resultado = numero1 + numero2
        print(resultado,'\n')
        
    elif operador =='-':
        resultado = numero1 - numero2
        print(resultado,'\n')
        
    elif operador =='*':
        resultado = numero1 * numero2
        print(resultado,'\n')
        
    elif operador =='/':
        resultado = numero1 / numero2
        print(f'Resultado é:',[resultado],'\n') 

    sair = input("[s] para Sair: ").lower().startswith('s')
    print(sair)
    if sair is True:
        print('Saindo...')
        break