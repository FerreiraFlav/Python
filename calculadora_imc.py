peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / altura**2


if imc <= 18.4:
    print(f'Seu Imc é:',round (imc), '\nVocê esta abaixo do peso.\n')

elif imc >= 18.5 and imc <= 24.9:
   print(f'Seu Imc é:',round (imc), '\nVocê esta com peso normal.\n')

elif imc > 25 and imc <= 29.9:
    print(f'Seu Imc é:',round (imc), '\nVocê esta com sobre peso.\n')
    
elif imc > 30 and imc <= 34.9:
    print(f'Seu Imc é:',round (imc), '\nVocê esta com grau de obesidade I.\n')
    
elif imc > 35 and imc <= 39.9:
    print(f'Seu Imc é:',round (imc), '\nVocê esta com grau de obesidade II.\n')

else:
     print(f'Seu Imc é:',round (imc), '\nVocê esta com grau de obesidade III (mórbida).\n')



