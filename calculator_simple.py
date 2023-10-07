number1 = int(input("write a number: "))
number2 = int(input("write another number: "))
operadores = input("digite um operador + - * /")
resultado = 0



if operadores == '+':
    resultado = number1 + number2
    print("Soma é: ", resultado)
elif operadores == '-':
    resultado = number1 - number2
    print("Subitração é: ", resultado)
elif operadores == '*':
    resultado = number1 * number2
    print("multiplicação é: ", resultado)
elif operadores == '/':
    if number2 !=0:
        resultado = number1 / number2
        print(resultado)
    else:
        print('erro de divisão')  

else:#operadores != '+' or '-' or '*' or '/':
    print('Você digitou um operador invalido, calculo finalizado')
    operadores = quit()      

    


