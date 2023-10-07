print('------------------------')
print('Digite seu login e senha')
print('------------------------\n')

login = input('Digite seu login:  ')
senha = input('Digite sua senha:  ')
login_permitido = 'flavio'
senha_permitida = '123'

if login == login_permitido and senha == senha_permitida:
    print('Bem vindo ao sistema')
else:
    print('Login ou senha incorreta')