ano =  int (input("Ex: (1995) Digite um ano, conforme o exemplo: "))

if (ano % 4 == 0 and ano % 100 != 0)  or (ano % 400 == 0):
    print('Ano', ano , 'é bissexto')
else:
    print('Ano', ano , 'não é bissexto')
